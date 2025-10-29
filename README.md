# Getting Started with Strands Agents - Complete Learning Path

🎯 **Learning Journey**: Course 1 (Fundamentals) → Course 2 (Advanced MCP, Hooks, Session Management) → Course 3 (Multi-Agent Systems) → Course 4 (Production Deployment)

A comprehensive hands-on learning path for AI agent development using the [Strands Agents framework](https://strandsagents.com/). Build intelligent, multi-agent systems from basic concepts to production-ready implementations with advanced capabilities. All of these courses have free video courses to follow along available at Analytics Vidhya. 

---

## 📚 Learning Path Overview

This repository contains four progressive courses that take you from fundamentals to advanced production-ready implementations:

### **Course 1: Getting Started with Strands Agents**
Foundation course covering basic agent creation, model providers, AWS integration, MCP basics, agent-to-agent communication, and observability fundamentals.

Video Series available [here](https://www.analyticsvidhya.com/courses/getting-started-with-strands-agents-build-your-first-ai-agent/?utm_source=new_course_home_page) for free enrollment.

### **Course 2: Advanced Strands Agents with MCP**
Advanced course focusing on production-ready implementations, advanced tool integration, persistent memory systems, hooks, session management, and enterprise features.

Video Series available [here](https://www.analyticsvidhya.com/courses/advanced-strands-agents-mcp/) for free enrollment.

### **Course 3: Building Multi-Agent Systems with Strands Agents**
Develop intelligent multi-agent systems that coordinate, communicate, and solve complex problems using swarm, graph-based and agents as tools patterns with Strands Agents.

Video Series available [here](https://www.analyticsvidhya.com/courses/building-multi-agent-systems-with-strands-agents/) for free enrollment.

### **Course 4: Production Deployment with Amazon Bedrock AgentCore**
Production deployment course covering best practices for running agents in production environments using Amazon Bedrock AgentCore Runtime for serverless scaling and management.

**Total Learning Time**: ~5-6 hours across all courses

---

## 🎓 Course 1: Getting Started with Strands Agents

**Location**: `course-1/` directory

Learn the complete journey of AI agent development, from basic usage to advanced topics like [agent-to-agent (A2A)](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/agent-to-agent/) communication and [observability](https://strandsagents.com/latest/documentation/docs/user-guide/observability-evaluation/observability/).

### What You'll Learn
- Strands Agents Framework - Build intelligent AI agents
- Model Context Protocol (MCP) - Enable tool integration
- Agent-to-Agent Communication - Create multi-agent systems
- Observability & Evaluation - Monitor and improve agent performance

### Course 1 Structure

| 🧪 Lab | 📝 What You'll Learn | ⏱️ Time | 📊 Level |
|--------|---------------------|---------|----------|
| [Lab 1: Strands Agent Basics](course-1/Lab1/) | Agent initialization, system prompts, HTTP tools | 15 min | ![Beginner](https://img.shields.io/badge/-Beginner-brightgreen) |
| [Lab 2: Model Providers](course-1/Lab2/) | Anthropic & Amazon Bedrock integration | 18 min | ![Beginner](https://img.shields.io/badge/-Beginner-brightgreen) |
| [Lab 3: AWS Service Integration](course-1/Lab3/) | AWS service tool usage (S3, DynamoDB) | 15 min | ![Intermediate](https://img.shields.io/badge/-Intermediate-yellow) |
| [Lab 4: MCP & Tools](course-1/Lab4/) | Model Context Protocol, tool creation | 14 min | ![Intermediate](https://img.shields.io/badge/-Intermediate-yellow) |
| [Lab 5: A2A Communication](course-1/Lab5/) | Multi-agent systems & communication | 11 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |
| [Lab 6: Observability](course-1/Lab6/) | LangFuse, RAGAS, performance monitoring | 21 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |

### Course 1 Lab Details

#### Lab 1: Strands Agent Basics
**Files**: `basic-use.py`, `http-tool-use.py`, `system-prompt-use.py`

Learn the fundamentals of creating and using Strands agents:
- Basic agent initialization and usage
- System prompt customization
- HTTP tool integration

#### Lab 2: Model Providers
**Files**: `anthropic-model-provider.py`, `anthropic-pet-breed-agent.py`, `bedrock-default-config.py`, `bedrock-detailed-config.py`

Explore different model providers and configuration options:
- Anthropic Claude model integration
- Amazon Bedrock model configuration

> **Note**: Some portions of this lab require a pre-existing AWS account for the 'generate_image' tool.

#### Lab 3: AWS Service Integration
**Files**: `aws-tool-use.py`

Learn to integrate AWS services with your Strands agents:
- Using the [`use_aws`](https://github.com/strands-agents/tools/blob/main/src/strands_tools/use_aws.py) tool
- Examples with Amazon S3 and Amazon DynamoDB

> **Note**: The code in this lab requires a pre-existing AWS account to properly utilize the 'use_aws' tool. An example Amazon DynamoDB Table is used to generate results when querying a table.

#### Lab 4: Model Context Protocol (MCP)
**Files**: `mcp-and-tools.ipynb`, `mcp_calulator.py`

Deep dive into the Model Context Protocol:
- MCP server creation
- Tool definition and usage
- Calculator and Weather agents examples
- Interactive Jupyter notebook tutorial

#### Lab 5: Agent-to-Agent Communication
**Files**: `a2a-communication.ipynb`, `run_a2a_system.py`, `employee_data.py`, `employee-agent.py`, `hr-agent.py`

Build multi-agent systems with inter-agent communication:
- A2A communication patterns
- Employee/HR agent system example
- MCP server for data sharing
- REST API integration

#### Lab 6: Observability & Evaluation
**Files**: `observability-with-langfuse-and-evaluation-with-ragas.ipynb`, `restaurant-data/`

Monitor and evaluate agent performance:
- Restaurant recommendation agent example
- LangFuse integration for observability
- RAGAS evaluation framework
- Performance metrics and tracing

---

## 🚀 Course 2: Advanced Strands Agents with MCP

**Location**: `course-2/` directory

A comprehensive advanced course for building production-ready AI agents using the Strands Agents SDK. This repository contains 6 progressive labs that teach advanced capabilities including tool integration, memory persistence, Model Context Protocol (MCP), and comprehensive observability.

### What You'll Learn
- **Strands Agents SDK** - Advanced agent architecture and lifecycle management
- **Model Context Protocol (MCP)** - Standardized tool and service integration  
- **Multi-Provider Configuration** - Amazon Bedrock, Anthropic, OpenAI, and Ollama
- **Advanced Processing** - Hooks, session management, and conversation strategies
- **Memory Systems** - Long-term persistent memory with FAISS, OpenSearch, and Mem0
- **Enterprise Features** - Observability, metrics analysis, and performance optimization

### Course 2 Structure

| 🧪 Lab | 📝 What You'll Learn | ⏱️ Time | 📊 Level |
|--------|---------------------|---------|----------|
| [Lab 1: Overview of Strands Agents](course-2/Lab1/) | Fundamental agentic AI concepts, agent lifecycle | 13 min | ![Intermediate](https://img.shields.io/badge/-Intermediate-yellow) |
| [Lab 2: Model Providers](course-2/Lab2/) | Multi-provider configuration, metrics analysis | 12 min | ![Intermediate](https://img.shields.io/badge/-Intermediate-yellow) |
| [Lab 3: Advanced Response Processing](course-2/Lab3/) | Hooks, lifecycle management, async patterns | 14 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |
| [Lab 4: Tools & MCP Integration](course-2/Lab4/) | Custom tools, MCP servers, self-extending agents | 19 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |
| [Lab 5: Session Management](course-2/Lab5/) | Conversation strategies, state persistence | 11 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |
| [Lab 6: Memory Persistent Agents](course-2/Lab6/) | Long-term memory, FAISS, OpenSearch, Mem0 | 15 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |

### Course 2 Lab Details

#### Lab 1: Overview of Strands Agents (12:52)
**Files**: `first_agent.py`

Learn fundamental agentic AI concepts and build your first Strands agent:
- Basic agent creation with default configuration (no API keys required)
- Core agent components and execution flow
- Agent result examination (message, metrics, state, stop reasons)
- Dynamic model configuration and system prompt modification
- Conversation history management and message clearing

#### Lab 2: Model Providers and Configuration (11:59)
**Files**: `anthropic_model.py`, `bedrock_model.py`, `ollama_model.py`, `openai_model.py`

Configure agents across multiple LLM providers for flexibility and cost optimization:
- Model architecture overview and provider-specific parameters
- Bedrock model setup with structured output capabilities
- Anthropic model configuration with thinking mode
- Ollama local deployment and OpenAI integration
- Metrics analysis and performance monitoring

#### Lab 3: Advanced Response Processing with Hooks (13:30)
**Files**: `async_example.py`, `hook_example_1.py`, `hook_example_2.py`

Implement custom logic to intercept and modify agent behavior at lifecycle points:
- Event-driven hook system and lifecycle management
- Before/after event handling and agent modifications
- Async iterators, callback handlers, and retry logic
- Tool hook examples and precision parameter setup

#### Lab 4: Tools and MCP Integration (18:55)
**Files**: `mcp_integration.py`, `self_extending_example.py`, `tools/`

Extend agent capabilities with custom tools and external service integration:
- Built-in tools from strands-agents-tools library
- Custom tool creation using @tool decorator
- MCP server configuration for AWS Documentation and Pricing
- Self-extending agents and meta tooling capabilities
- Proper error handling and security implementation

#### Lab 5: Conversation and Session Management (11:26)
**Files**: `session_example.py`, `verify_session.py`

Manage conversation state and context effectively across interactions:
- Context window challenges and management strategies
- Three conversation manager approaches (Null, SlidingWindow, Summarizing)
- Session state persistence and user isolation
- File-based and Amazon S3 session storage options

#### Lab 6: Memory Persistent Agents (15:19)
**Files**: `memory_example.py`

Build agents with long-term memory capabilities across conversations:
- Memory backends integration (FAISS, OpenSearch, Mem0)
- Web search integration with DuckDuckGo
- Memory storage, retrieval, and relevance scoring
- Amazon Bedrock Knowledge Bases integration
- Retention policies and privacy controls

---

### **Course 3: Building Multi-Agent Systems with Strands Agents**

**Location**: [Strands Samples](https://github.com/strands-agents/samples/tree/main/01-tutorials/02-multi-agent-systems) 

Develop intelligent multi-agent systems that coordinate, communicate, and solve complex problems using swarm, graph-based and agents as tools patterns with Strands Agents.

### Course 3 Structure

| 🧪 Lab | 📝 What You'll Learn | ⏱️ Time | 📊 Level |
|--------|---------------------|---------|----------|
| [Lab 2: Multi-Agent Systems with Swarm Intelligence](https://github.com/strands-agents/samples/blob/main/01-tutorials/02-multi-agent-systems/02-swarm-agent/swarm.ipynb) | Deep dive for Swarm multi-agent pattern | 30 min | ![Intermediate](https://img.shields.io/badge/-Intermediate-yellow) |
| [Lab 3: Multi-Agent Systems with Agent Graph](https://github.com/strands-agents/samples/blob/main/01-tutorials/02-multi-agent-systems/03-graph-agent/graph.ipynb) | Deep dive for Graph multi-agent pattern | 25 min | ![Intermediate](https://img.shields.io/badge/-Intermediate-yellow) |
| [Lab 4: Multi-Agent System with Agents as a Tools](https://github.com/strands-agents/samples/blob/main/01-tutorials/02-multi-agent-systems/01-agent-as-tool/agent-as-tools.ipynb) | Deep dive for Agents as Tools multi-agent pattern | 20 min | ![Intermediate](https://img.shields.io/badge/-Intermediate-yellow) |

---

## 🚀 Course 4: Production Deployment with Amazon Bedrock AgentCore

**Location**: `course-4/` directory

Learn to deploy production-ready AI agents using Amazon Bedrock AgentCore Runtime. This course focuses on serverless deployment, scaling, and management of agents in production environments.

### What You'll Learn
- **Production Best Practices** - Understand differences between development and production agent deployment
- **Amazon Bedrock AgentCore** - Comprehensive overview of AgentCore services and components
- **Serverless Deployment** - Deploy agents with auto-scaling and session management
- **Production Operations** - Monitor, troubleshoot, and maintain production agent systems

### Course 4 Structure

| 🧪 Lab | 📝 What You'll Learn | ⏱️ Time | 📊 Level |
|--------|---------------------|---------|----------|
| [Lab 1: Operating Agents in Production](course-4/) | Production best practices, development vs production differences | 9 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |
| [Lab 2: Introduction to Amazon Bedrock AgentCore](course-4/) | Amazon Bedrock AgentCore fundamentals, service components overview | 12 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |
| [Lab 3: Building agents with Amazon Bedrock AgentCore](course-4/) | Hands-on deployment with AgentCore Runtime | 20 min | ![Advanced](https://img.shields.io/badge/-Advanced-red) |

### Course 4 Lab Details

#### Lab 1: Operating Agents in Production (9:00)
Understand the best practices for running agents in a production setting and how that differs from local development.

#### Lab 2: Introduction to Amazon Bedrock AgentCore (12:00)
Understand the fundamentals of Amazon Bedrock AgentCore and its components.

#### Lab 3: Building a Calculator Agent (20:00)
**Files**: `my_agent.py`, `invoke_agent.py`, `requirements.txt`

Hands-on deployment of a production-ready calculator agent:
- Agent creation with Strands Agents framework
- AgentCore Runtime deployment and configuration
- Testing deployed agents with session management
- Production invocation patterns and best practices

> **Note**: This lab requires an AWS account with appropriate permissions and model access enabled in Amazon Bedrock console.

---

## 🛠️ Technologies & Services

| 🔧 Technology | 🎯 Purpose | 📖 Documentation |
|--------------|-----------|-----------------|
| **Strands Agents** | AI agent framework | [Docs](https://strandsagents.com/) |
| **Anthropic Claude** | Alternative LLM provider | [Docs](https://docs.anthropic.com/) |
| **Amazon Bedrock** | AWS managed LLM service | [Docs](https://docs.aws.amazon.com/bedrock/) |
| **OpenAI** | Alternative LLM provider | [Docs](https://platform.openai.com/docs) |
| **Ollama** | Local model deployment | [Docs](https://ollama.ai/) |
| **Model Context Protocol** | Tool integration standard | [Docs](https://modelcontextprotocol.io/) |
| **LangFuse** | Observability & tracing | [Docs](https://langfuse.com/docs) |
| **RAGAS** | Agent evaluation | [Docs](https://docs.ragas.io/) |
| **Mem0** | Memory persistence | [Docs](https://docs.mem0.ai/) |
| **FAISS** | Vector similarity search | [Docs](https://github.com/facebookresearch/faiss) |
| **OpenSearch** | Search and analytics | [Docs](https://opensearch.org/docs/) |

---

## 📋 Prerequisites

### Course 1 Requirements
- **Python 3.10+**
- **Virtual environment** (recommended)
- **API keys for at least one of:**
  - Anthropic Claude 
  - Amazon Bedrock
- **For Lab 6:** LangFuse account and API key
- **For Labs 3, 5:** AWS account with appropriate CLI configuration

### Course 2 Requirements
- **Completion of Course 1** (Labs 1-6) or equivalent knowledge
- **Python 3.10+**
- **Virtual environment** (recommended)
- **Anthropic Claude API key** (primary requirement) - Get from [Anthropic Console](https://console.anthropic.com/)
- **Additional API keys for specific labs:**
  - Amazon Bedrock (for AWS integration labs)
  - OpenAI (optional alternative)
  - Mem0 (for Lab 6 memory persistence)

### Course 3 Requirements
- **Completion of Course 1-2** (Labs 1-6) or equivalent knowledge
- **Python 3.10+**
- **Virtual environment** (recommended)
- **AWS account with Anthropic Claude 3.7 enabled on Amazon Bedrock**
- **AWS IAM role with permissions to use Amazon Bedrock**

### Course 4 Requirements
- **Completion of Course 1-3** or equivalent knowledge
- **AWS Account** with appropriate permissions
- **Python 3.10+**
- **AWS CLI configured** with `aws configure`
- **AWS Permissions**: [BedrockAgentCoreFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.html) policy
- **Model Access**: Anthropic Claude 3.5 Haiku enabled in Amazon Bedrock console

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aws-samples/sample-getting-started-with-strands-agents-course.git
cd sample-getting-started-with-strands-agents-course
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate (Linux/Mac)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# For Course 1
pip install -r requirements.txt

# For Course 2
cd course-2
pip install -r requirements.txt

# For Course 4
cd course-4
pip install -r requirements.txt
```

### 4. Configure Environment Variables

#### For Course 1:
Create a `.env` file in the root directory:

```bash
# Anthropic (recommended)
ANTHROPIC_API_KEY=your_anthropic_api_key

# AWS Bedrock (optional)
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=us-east-1

# LangFuse (for Lab 6)
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

#### For Course 2:
Copy `.env.example` to `.env` in the `course-2/` directory:

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

---

## 💻 Running the Labs

### Course 1 Examples

**Labs 1-3: Python Scripts**
```bash
cd Lab1
python basic-use.py
```

**Lab 4: Interactive Notebook**
```bash
cd Lab4
jupyter notebook mcp-and-tools.ipynb
```

**Lab 5: Multi-Agent System**
```bash
cd Lab5
jupyter notebook a2a-communication.ipynb
```

**Lab 6: Observability**
```bash
cd Lab6
jupyter notebook observability-with-langfuse-and-evaluation-with-ragas.ipynb
```

### Course 2 Examples

**Lab 1: Agent Fundamentals (No API key required)**
```bash
cd course-2/Lab1
python first_agent.py
```

**Lab 2: Model Providers**
```bash
cd course-2/Lab2
python anthropic_model.py
python bedrock_model.py
```

**Lab 3: Hooks**
```bash
cd course-2/Lab3
python hook_example_1.py
python async_example.py
```

**Lab 4: MCP Integration**
```bash
cd course-2/Lab4
python mcp_integration.py
```

**Lab 5: Session Management**
```bash
cd course-2/Lab5
python session_example.py
```

**Lab 6: Memory Agents**
```bash
cd course-2/Lab6
python memory_example.py
```

### Course 4 Examples

**Lab 3: Production Deployment**
```bash
cd course-4
python my_agent.py
```

**Deploy to AgentCore Runtime**
```bash
cd course-4
agentcore configure -e my_agent.py
agentcore launch
agentcore invoke '{"prompt": "What is 50 plus 30?"}'
```

---

## 🐛 Troubleshooting

### Course 1 Issues

| Issue | Solution |
|-------|----------|
| **API Key Issues** | Ensure all required API keys are set in your `.env` file or environment |
| **Port Conflicts** | Labs use ports 8000-8002, ensure they're available |
| **Import Errors** | Run `pip install -r requirements.txt` to install all dependencies |
| **MCP Server Issues** | Allow time for MCP servers to start before connecting clients |
| **AWS Permissions** | Verify your AWS credentials have necessary permissions for S3/DynamoDB |

### Course 2 Issues

| Issue | Solution |
|-------|----------|
| **API Key Issues** | Ensure `ANTHROPIC_API_KEY` is set correctly (should start with `sk-ant-`) |
| **Import Errors** | Run `pip install -r requirements.txt` in course-2 directory |
| **AWS Credentials** | Only needed for Lab 4 MCP integration - configure AWS CLI or environment |
| **MCP Servers** | Allow time for MCP servers to initialize before agent connections in Lab 4 |
| **Memory Backends** | Mem0 API key only required for Lab 6 memory persistence |

### Course 3 Issues

| Issue | Solution |
|-------|----------|
| **AWS Permissions** | Ensure BedrockAgentCoreFullAccess policy is attached to your user/role |
| **Model Access** | Enable Anthropic Claude 3.7 Sonnet in Amazon Bedrock console |

### Course 4 Issues

| Issue | Solution |
|-------|----------|
| **AWS Permissions** | Ensure BedrockAgentCoreFullAccess policy is attached to your user/role |
| **Model Access** | Enable Anthropic Claude 3.5 Haiku in Amazon Bedrock console |
| **AgentCore CLI** | Run `pip install bedrock-agentcore-starter-toolkit` if `agentcore` command not found |
| **Deployment Failures** | Check CloudWatch logs at `/aws/bedrock-agentcore/runtimes/{agent-id}-DEFAULT` |
| **Session Issues** | Ensure session IDs are 33+ characters for proper session management |

---

## 📚 Additional Resources

### Official Documentation
- [Strands Agents Documentation](https://strandsagents.com/latest/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/)
- [What is Amazon Bedrock AgentCore?](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [AgentCore Runtime How It Works](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html)
- [AgentCore Memory Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [AgentCore Gateway Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Programmatic Agent Invocation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-toolkit.html#invoke-programmatically)

### Related Courses & Tutorials
- [Building with Amazon Bedrock Workshop](https://catalog.workshops.aws/building-with-amazon-bedrock/en-US)
- [LangChain Embeddings with Bedrock](https://github.com/build-on-aws/langchain-embeddings)
- [Strands Agents Samples Repository](https://github.com/strands-agents/samples)

### Blog Posts & Articles
- [Introducing Strands Agents](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/)
- [Open Protocols for Agent Interoperability - Part 3](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-3-strands-agents-mcp/)
- [Strands Agents SDK Technical Deep Dive](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/)

---

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

---