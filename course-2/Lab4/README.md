# Lab 4: Tools and MCP Integration

**Duration:** 18:55 | **Files:** `mcp_integration.py`, `self_extending_example.py`, `tools/`

## What You'll Learn
- Extend agent capabilities with built-in and custom tools
- Integrate MCP servers for AWS Documentation and Pricing
- Build self-extending agents that create their own tools
- Implement proper error handling and security measures

## Quick Start
```bash
# MCP integration with AWS services (requires AWS credentials)
python mcp_integration.py

# Self-extending agent example
python self_extending_example.py
```

## Key Concepts
- **Built-in Tools**: File operations, HTTP requests from strands-tools
- **Custom Tools**: Create tools with @tool decorator
- **MCP Integration**: Connect to external services via Model Context Protocol
- **Self-Extension**: Agents that create and register their own tools

## Examples
- **AWS Solutions Architect**: Agent with AWS docs and pricing tools
- **Meta Tooling**: Agents that build tools for other agents
- **Tool Composition**: Combining multiple tools for complex workflows

## Requirements
- `ANTHROPIC_API_KEY` in `.env` file
- AWS credentials (for MCP integration)
- `uvx` installed (for MCP servers)