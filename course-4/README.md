# Building a Calculator Agent with Amazon Bedrock AgentCore

Deploy production-ready AI agents in minutes with Amazon Bedrock AgentCore Runtime.

## What is AgentCore?

Amazon Bedrock AgentCore is a suite of services that simplifies deploying AI agents to production. Instead of weeks configuring infrastructure, you get production-ready agents with just 2 commands.

### Amazon Bedrock AgentCore Services

- **Amazon Bedrock AgentCore Runtime** ⭐ - Serverless execution with auto-scaling and session management
- **Amazon Bedrock AgentCore Identity** - Secure credential management for API keys and tokens  
- **Amazon Bedrock AgentCore Memory** - State persistence and conversation history
- **Amazon Bedrock AgentCore Code Interpreter** - Secure code execution sandbox
- **Amazon Bedrock AgentCore Browser** - Cloud browser automation
- **Amazon Bedrock AgentCore Gateway** - API management and tool discovery
- **Amazon BedrockAgentCore Observability** - Monitoring, tracing, and debugging

## Calculator Agent with AgentCore Runtime

This project demonstrates **AgentCore Runtime** by building a calculator agent that handles mathematical computations using the Strands Agents framework with automatic scaling and session isolation.

## Key Benefits

- **10 minutes** from code to production endpoint
- **Serverless** - no infrastructure management
- **Auto-scaling** - handles traffic spikes automatically
- **Session-aware** - maintains conversation context across invocations
- **Built-in security** - AWS security best practices included


## Core Components

1. **Amazon Bedrock AgentCore Runtime**: Provides a secure serverless runtime for deploying and scaling dynamic agents using any framework with any model provider.

2. **Strands Agents**: An agent framework that build production-ready, multi-agent AI systems in a few lines of code. 

## Prerequisites

Before you begin, verify that you have:

- **AWS Account** 
- **Python 3.10+** environment
- **AWS CLI configured** with `aws configure`
- **AWS Permissions**: Attach the [BedrockAgentCoreFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.html) AWS managed policy and the [starter toolkit policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html#use-the-starter-toolkit)
- **Model Access**: Anthropic Claude 3.5 Haiku (or the model of your preference) [enabled in the Amazon Bedrock console](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)

> **New AWS customers receive up to $200 in credits**  
> Get started at no cost with the [AWS Free Tier](https://aws.amazon.com/free/).

## Step 1: AWS Account Setup

### Create AWS Account and Configure Permissions

If you're using admin access, you can skip the detailed permissions setup. Otherwise, follow [these steps to create an AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) and attach the [BedrockAgentCoreFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.html) AWS managed policy.

### Configure the AWS CLI

Run the following command in your terminal:

```bash
aws configure
```

Enter your credentials:
- `AWS Access Key ID [None]`: (from your downloaded CSV file)
- `AWS Secret Access Key [None]`: (from your downloaded CSV file)
- `Default region name [None]`:  (your AWS Region)
- `Default output format [None]`: `json`

## Step 2: Set Up Project and Install Dependencies

Create a project folder and install the required packages:

```bash
mkdir agentcore-calculator-agent
cd agentcore-calculator-agent
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install the necessary dependencies:

```bash
pip install --upgrade pip
pip install bedrock-agentcore strands-agents bedrock-agentcore-starter-toolkit strands-agents-tools
```

**Required packages:**
- `bedrock-agentcore` - Amazon Bedrock AgentCore SDK
- `strands-agents` - Strands Agents SDK
- `bedrock-agentcore-starter-toolkit` - Amazon Bedrock AgentCore starter toolkit
- `strands-agents-tools` - Tools for Strands Agents including calculator functionality

Verify installation:
```bash
agentcore --help
```

## Step 3: Create Your Agent

Create a deployment folder to keep your agent code organized:

```bash
mkdir deployment
cd deployment
```

Create `my_agent.py`:

```python
from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent
import os
from strands_tools import calculator

# System prompt for the agent
SYSTEM_PROMPT = "You are a helpful assistant that can perform calculations. Use the calculate tool for any math problems."

# Model configuration from environment variable
MODEL_ID = os.getenv("MODEL_ID", "us.anthropic.claude-3-5-haiku-20241022-v1:0")

# Global agent instance for reuse across invocations
agent = None

def create_agent(tools):
    """Create agent with lazy loading pattern for performance"""
    global agent
    if agent is None:
        agent = Agent(
            model=MODEL_ID,
            tools=[tools],
            system_prompt=SYSTEM_PROMPT
        )
    return agent

# Initialize the Bedrock Agent Core application
app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    """AgentCore Runtime entry point"""
    agent = create_agent(calculator)
    prompt = payload.get("prompt", "Hello!")
    result = agent(prompt)
    
    return {
        "response": result.message.get('content', [{}])[0].get('text', str(result))
    }

if __name__ == "__main__":
    app.run()
```

Create `requirements.txt`:

```
bedrock-agentcore
bedrock-agentcore-starter-toolkit
strands-agents
strands-agents-tools
```

## Step 4: Understanding the Calculator Agent Code

The agent implements several key components:

### AgentCore Runtime Entry Point

The `@app.entrypoint` decorator makes your agent deployable to AgentCore Runtime. This is the only difference between a local script and a cloud-deployed agent.

### Agent Initialization with Lazy Loading

The agent is initialized once per session to preserve state and avoid performance costs. Amazon Bedrock AgentCore Runtime provides dedicated containers with up to 8 hours lifetime or 15 minutes of inactivity timeout.

### Calculator Tool

The agent includes a calculator tool from `strands-tools` for performing mathematical operations.

## Step 5: Test the agent code locally 

```bash
python my_agent.py
```

Test

```bash
# In another terminal, test with curl
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Hello world!"
  }'
```

## Step 6: Configure and Deploy to AgentCore Runtime

The AgentCore starter toolkit will automatically create all necessary AWS resources for you, including IAM roles with least-privilege permissions, following AWS security best practices. This is much safer than creating overly permissive roles manually.

### Configure the Agent

```bash
agentcore configure -e my_agent.py
```

When prompted:
- **Execution Role**: Press Enter to auto-create a role with minimal required permissions
- **ECR Repository**: Press Enter to auto-create
- **Requirements File**: Confirm the detected requirements.txt
- **OAuth Configuration**: Type `no`
- **Request Header Allowlist**: Type `no`

### Deploy the Agent

```bash
agentcore launch
```

This command:
- Creates an IAM execution role with minimal required permissions
- Builds your container using AWS CodeBuild (no Docker required locally)
- Creates [Amazon ECR](https://aws.amazon.com/ecr/) repository
- Deploys your agent to Amazon Bedrock AgentCore Runtime
- Configures CloudWatch logging

Note the Agent ARN from the output - you'll need it for programmatic invocation.

### Check Deployment Status

```bash
agentcore status
```

### Find Your Resources

View your resources in the AWS Console:

| Resource | Location |
|----------|----------|
| Agent Logs | CloudWatch → Log groups → `/aws/bedrock-agentcore/runtimes/{agent-id}-DEFAULT` |
| Container Images | ECR → Repositories → `bedrock-agentcore-{agent-name}` |
| Build Logs | CodeBuild → Build history |
| IAM Role | IAM → Roles → Search for "BedrockAgentCore" |

## Step 7: Test Your Deployed Agent

### Simple Invocation

Test your deployed agent with the simplest possible command:

```bash
agentcore invoke '{"prompt": "What is 50 plus 30?"}'
```

### Test Conversation Memory

Test that the agent maintains context within a session:

```bash
agentcore invoke '{"prompt": "Now multiply that result by 2"}'
```

> AgentCore Runtime automatically provides session isolation and memory management.

## Step 8: Invoke from Production Applications

For production applications, use the [InvokeAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html) operation from [AWS SDK](https://aws.amazon.com/what-is/sdk/). 

```python
    # Invoke the agent
    response = client.invoke_agent_runtime(
        agentRuntimeArn=agent_arn,
        runtimeSessionId=session_id, #Must be 33+ characters
        payload=payload,
        qualifier="DEFAULT"
    )
```

Use [invoke_agent.py](invoke_agent.py) application to test the agent.

Run the script to test both calculation capabilities and memory:

```bash
# Set your agent ARN (get from agentcore status)
export AGENT_ARN="YOUR-ARN"

# Run the test script
python invoke_agent.py
```

The script will test:
- Basic calculations
- Memory persistence within a session
- Mathematical operations
- Conversation context retention

**Key Points for Production Use:**
- **Agent ARN**: Get this from `agentcore status` output
- **Session IDs**: Must be 33+ characters for session persistence
- **Authentication**: Uses your AWS credentials (IAM roles, access keys, etc.)


For more troubleshooting information, see [Troubleshoot Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/troubleshoot-runtime.html).

## Step 9: Clean Up

When you're done experimenting, clean up all resources:

```bash
agentcore destroy
```

This removes:
- AgentCore Runtime deployment
- ECR repository and images
- Auto-created IAM roles
- CloudWatch log groups

## Resources

### Documentation
- [What is Amazon Bedrock AgentCore?](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [AgentCore Runtime How It Works](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html)
- [AgentCore Memory Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [AgentCore Gateway Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Programmatic Agent Invocation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-toolkit.html#invoke-programmatically)


### Code Examples
- [AWS Labs AgentCore Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/)

