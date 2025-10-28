import json
import uuid
import boto3
import os
import sys

def invoke_agent(agent_arn, prompt, region=None, session_id=None):
    """Invoke AgentCore Runtime agent programmatically"""
    
    # Extract region from ARN if not provided
    if not region:
        region = agent_arn.split(':')[3]
    
    # Initialize the Amazon Bedrock AgentCore client
    client = boto3.client('bedrock-agentcore', region_name=region)
    
    # Use provided session_id or generate new one
    if not session_id:
        session_id = str(uuid.uuid4())
    
    # Prepare the payload
    payload = json.dumps({"prompt": prompt}).encode()
    
    try:
        # Invoke the agent
        response = client.invoke_agent_runtime(
            agentRuntimeArn=agent_arn,
            runtimeSessionId=session_id,
            payload=payload,
            qualifier="DEFAULT"
        )
        
        # Process response
        content = []
        for chunk in response.get("response", []):
            content.append(chunk.decode('utf-8'))
        
        result = json.loads(''.join(content))
        return result, session_id
        
    except Exception as e:
        print(f"Error invoking agent: {e}")
        return None, session_id

def main():
    # Get variables from environment or command line
    agent_arn = os.getenv('AGENT_ARN')
    region = os.getenv('AWS_REGION')
    
    # Override with command line arguments if provided
    if len(sys.argv) > 1:
        agent_arn = sys.argv[1]
    if len(sys.argv) > 2:
        region = sys.argv[2]
    
    if not agent_arn:
        print("Usage: python invoke_agent.py <AGENT_ARN> [REGION]")
        print("Or set AGENT_ARN environment variable")
        sys.exit(1)
    
    # Extract region from ARN if not provided
    if not region:
        region = agent_arn.split(':')[3]
    
    print(f"Invoking agent: {agent_arn}")
    print(f"Region: {region}")
    print("-" * 50)
    
    # Test prompts for calculator functionality and memory
    test_prompts = [
        "What is 25 + 30?",
        "Now multiply that result by 2",
        "What was the first calculation I asked you to do?",
        "Calculate the square root of 144",
        "Add 10 to the previous result",
        "What is 15 * 8 + 7?",
        "Divide the previous result by 3"
    ]
    
    # Use the same session ID for all prompts to test memory
    session_id = str(uuid.uuid4())
    print(f"Using session ID: {session_id}")
    print("=" * 60)
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n{i}. Testing: {prompt}")
        print("=" * 60)
        
        result, _ = invoke_agent(agent_arn, prompt, region, session_id)
        
        if result:
            print("Response:")
            if isinstance(result, dict) and 'response' in result:
                print(result['response'])
            else:
                print(json.dumps(result, indent=2))
        else:
            print("Failed to get response from agent")
        
        print("-" * 60)

if __name__ == "__main__":
    main()
