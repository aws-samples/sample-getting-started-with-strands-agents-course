# Advanced Strands Agents with MCP

A comprehensive advanced course for building production-ready AI agents using the Strands Agents SDK. This repository contains 6 progressive labs that teach advanced capabilities including tool integration, memory persistence, Model Context Protocol (MCP), and comprehensive observability.

## 🎯 Course Overview

This advanced course provides foundational and advanced expertise in building production-ready AI agents, focusing on the agent class, agentic loop, and the complete ecosystem of components that power intelligent autonomous systems. You'll master core principles of agentic AI, understanding how agents combine large language models, tools, and memory to create systems that can understand, plan, and execute actions autonomously.

**Course Topics:**
- **Strands Agents SDK** - Advanced agent architecture and lifecycle management
- **Model Context Protocol (MCP)** - Standardized tool and service integration  
- **Multi-Provider Configuration** - Amazon Bedrock, Anthropic, OpenAI, and Ollama
- **Advanced Processing** - Hooks, session management, and conversation strategies
- **Memory Systems** - Long-term persistent memory with FAISS, OpenSearch, and Mem0
- **Enterprise Features** - Observability, metrics analysis, and performance optimization

**Prerequisites:** Basic understanding of AI/ML concepts. For beginners, we recommend starting with [Getting Started with Strands Agents](https://github.com/aws-samples/sample-getting-started-with-strands-agents-course) (Course 1).

## 📚 Lab Structure

### Lab 1: Overview of Strands Agents (12:52)
**Files:** `first_agent.py`

Learn fundamental agentic AI concepts and build your first Strands agent:
- Basic agent creation with default configuration (no API keys required)
- Core agent components and execution flow
- Agent result examination (message, metrics, state, stop reasons)
- Dynamic model configuration and system prompt modification
- Conversation history management and message clearing

### Lab 2: Model Providers and Configuration (11:59) 
**Files:** `anthropic_model.py`, `bedrock_model.py`, `ollama_model.py`, `openai_model.py`

Configure agents across multiple LLM providers for flexibility and cost optimization:
- Model architecture overview and provider-specific parameters
- Bedrock model setup with structured output capabilities
- Anthropic model configuration with thinking mode
- Ollama local deployment and OpenAI integration
- Metrics analysis and performance monitoring

### Lab 3: Advanced Response Processing with Hooks (13:30)
**Files:** `async_example.py`, `hook_example_1.py`, `hook_example_2.py`

Implement custom logic to intercept and modify agent behavior at lifecycle points:
- Event-driven hook system and lifecycle management
- Before/after event handling and agent modifications
- Async iterators, callback handlers, and retry logic
- Tool hook examples and precision parameter setup

### Lab 4: Tools and MCP Integration (18:55)
**Files:** `mcp_integration.py`, `self_extending_example.py`, `tools/`

Extend agent capabilities with custom tools and external service integration:
- Built-in tools from strands-agents-tools library
- Custom tool creation using @tool decorator
- MCP server configuration for AWS Documentation and Pricing
- Self-extending agents and meta tooling capabilities
- Proper error handling and security implementation

### Lab 5: Conversation and Session Management (11:26)
**Files:** `session_example.py`, `verify_session.py`

Manage conversation state and context effectively across interactions:
- Context window challenges and management strategies
- Three conversation manager approaches (Null, SlidingWindow, Summarizing)
- Session state persistence and user isolation
- File-based and Amazon S3 session storage options

### Lab 6: Memory Persistent Agents (15:19)
**Files:** `memory_example.py`

Build agents with long-term memory capabilities across conversations:
- Memory backends integration (FAISS, OpenSearch, Mem0)
- Web search integration with DuckDuckGo
- Memory storage, retrieval, and relevance scoring
- Amazon Bedrock Knowledge Bases integration
- Retention policies and privacy controls

## 📖 Learning Path

1. **Start with Lab 1** - Learn agent fundamentals with no setup required
2. **Progress through Labs 2-3** - Configure multiple providers and implement hooks
3. **Master Lab 4** - Integrate tools and MCP servers for external capabilities  
4. **Build with Lab 5** - Implement sophisticated conversation management
5. **Advanced Lab 6** - Create agents with persistent memory systems

## 🔧 Model Provider Support

This course **primarily uses the Anthropic Claude API**, but all examples can be configured to work with:
- **Amazon Bedrock** (Claude, Llama, Titan, and other models)
- **OpenAI** (GPT-4, GPT-3.5-turbo)
- **Ollama** (Local model deployment)
- **Other providers** supported by Strands SDK

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- **Anthropic Claude API key** (primary requirement)
- Additional API keys for specific labs:
  - Amazon Bedrock (for AWS integration labs)
  - OpenAI (optional alternative)
  - Mem0 (for memory persistence Lab 6)

### Getting Your Anthropic API Key
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign up for an account or log in
3. Navigate to **API Keys** section
4. Click **Create Key** and give it a name
5. Copy your API key (starts with `sk-ant-`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd sample-Advanced-Strands-Agents-with-MCP
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Copy `.env.example` to `.env` and set your API key:
   ```bash
   # Required - Get from https://console.anthropic.com/
   ANTHROPIC_API_KEY=sk-ant-your_key_here
   
   # Optional - for specific labs only
   AWS_ACCESS_KEY_ID=your_aws_key        # For Lab 4 MCP integration
   AWS_SECRET_ACCESS_KEY=your_aws_secret # For Lab 4 MCP integration  
   AWS_SESSION_TOKEN=your_aws_token      # For Lab 4 MCP integration
   OPENAI_API_KEY=your_openai_key        # For Lab 2 model alternatives
   MEM0_API_KEY=your_mem0_key            # For Lab 6 memory persistence
   ```

### Running the Labs

Each lab can be run independently. Start with Lab 1 for advanced fundamentals:

**Lab 1 - Agent Fundamentals (No API key required):**
```bash
cd Lab1
python first_agent.py
```

**Lab 2 - Model Providers:**
```bash
cd Lab2
python anthropic_model.py
python bedrock_model.py
```

**Lab 4 - MCP Integration:**
```bash
cd Lab4
python mcp_integration.py
```

**Lab 6 - Memory Agents:**
```bash
cd Lab6  
python memory_example.py
```

## 📝 Additional Resources

- [Strands Agents Documentation](https://strandsagents.com/latest/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Getting Started with Strands Agents (Course 1)](https://github.com/aws-samples/sample-getting-started-with-strands-agents-course)

## 🐛 Troubleshooting

**Common issues and solutions:**
- **API Key Issues** - Ensure `ANTHROPIC_API_KEY` is set correctly in your `.env` file
  - Key should start with `sk-ant-`
  - Get your key from [Anthropic Console](https://console.anthropic.com/)
- **Import Errors** - Run `pip install -r requirements.txt` if you encounter missing dependencies
- **AWS Credentials** - Only needed for Lab 4 MCP integration (configure AWS CLI or environment variables)
- **MCP Servers** - Allow time for MCP servers to initialize before agent connections in Lab 4
- **Memory Backends** - Mem0 API key only required for Lab 6 memory persistence

## 🔒 Security

See CONTRIBUTING for more information.

## 📄 License

This library is licensed under the MIT-0 License. See the LICENSE file. 
