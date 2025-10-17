# Agent-to-Agent (A2A) Communication Example

This directory contains examples of Agent-to-Agent (A2A) communication using the MCP (Model Context Protocol) framework.

## Components

The system consists of three main components:

1. **MCP Server** (`server.py`): Provides employee data and skills information
2. **Employee Agent** (`employee-agent.py`): An agent that can answer questions about employees
3. **HR Agent** (`hr-agent.py`): An agent that can answer HR-related questions by communicating with the Employee Agent

## Setup and Running

### A2A System Runner: Runs the MCP Server, Employee Agent, and HR Agent in parallel

### 1. Set your API key:
 ```bash
   export api_key='your-anthropic-api-key-here'
```

### 2. Start the system:
  ```bash
   python run_a2a_system.py
```


### 4. Make Requests to the HR Agent

Once all three components are running, you can make requests to the HR Agent:

```bash
curl -X POST --location "http://0.0.0.0:8000/inquire" \
-H "Content-Type: application/json" \
-d '{"question": "list employees that have skills related to AI programming"}'
```

## Direct MCP Server Interaction

If you want to interact directly with the MCP server (bypassing the agents), you can use the provided MCP client examples:

### Using the Python Script

```bash
# Navigate to the notebooks directory
cd ..

# Run the script in interactive mode
python mcp_client_example.py --interactive

# List all skills
python mcp_client_example.py --list-skills

# Find employees with a specific skill
python mcp_client_example.py --find-skill "Python"

# Find employees with AI-related skills
python mcp_client_example.py --find-ai-skills
```

### Using the Jupyter Notebook

Open and run the `mcp_client_tutorial.ipynb` notebook in Jupyter to see a step-by-step guide on interacting with the MCP server.

## Architecture

```
+-------------+         +----------------+         +------------+
|  HR Agent   |  <--->  | Employee Agent |  <--->  | MCP Server |
| (Port 8000) |         |  (Port 8001)   |         | (Port 8002)|
+-------------+         +----------------+         +------------+
       ^
       |
    User Requests
```

The HR Agent receives questions from users, communicates with the Employee Agent to get information, and the Employee Agent in turn communicates with the MCP Server to retrieve the actual data.

## Notes

- The MCP Server uses the FastMCP framework to expose tools (functions) that can be called remotely
- The Employee Agent uses the Strands framework to create an AI agent that can use these tools
- The HR Agent provides a REST API endpoint for users to ask questions
