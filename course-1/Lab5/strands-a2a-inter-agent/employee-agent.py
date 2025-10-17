import os
from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from strands.multiagent.a2a import A2AServer
from urllib.parse import urlparse
from strands.models.anthropic import AnthropicModel


# Define URLs correctly - do not use os.environ.get() for literal values
EMPLOYEE_INFO_URL = "http://localhost:8002/mcp/"
EMPLOYEE_AGENT_URL = "http://localhost:8001/"

# Create the MCP client
employee_mcp_client = MCPClient(lambda: streamablehttp_client(EMPLOYEE_INFO_URL))

model = AnthropicModel(
    client_args={
        "api_key": os.getenv("api_key"),  # Get API key from environment variables
    },
    # **model_config
    max_tokens=1028,
    model_id="claude-3-7-sonnet-20250219",
    params={
        "temperature": 0.3,
    }
)

# Using the MCP client within a context
with employee_mcp_client:
    tools = employee_mcp_client.list_tools_sync()
    
    # Create a Strands agent
    employee_agent = Agent(
        model=model,
        name="Employee Agent",
        description="Answers questions about employees",
        tools=tools,
        system_prompt="you must abbreviate employee first names and list all their skills"
    )
    
    # Create A2A server
    a2a_server = A2AServer(
        agent=employee_agent, 
        host=urlparse(EMPLOYEE_AGENT_URL).hostname, 
        port=int(urlparse(EMPLOYEE_AGENT_URL).port)
    )
    
    # Start the server
    if __name__ == "__main__":
        a2a_server.serve(host="0.0.0.0", port=8001)