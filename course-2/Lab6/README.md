# Lab 6: Memory Persistent Agents

**Duration:** 15:19 | **File:** `memory_example.py`

## What You'll Learn
- Build agents with long-term memory capabilities across conversations
- Integrate Mem0 for persistent memory storage and retrieval
- Combine memory with web search for enhanced knowledge
- Implement user-specific memory isolation and relevance scoring

## Quick Start
```bash
# Memory agent with web search (requires MEM0_API_KEY)
python memory_example.py
```

## Key Concepts
- **Memory Backends**: FAISS, OpenSearch, Mem0 integration
- **Memory Operations**: Store, retrieve, and list user memories
- **Relevance Scoring**: Semantic similarity for memory retrieval
- **Knowledge Augmentation**: Combine memory with external data sources

## Examples
- **Personal Assistant**: Agent that remembers user preferences
- **Web Search Integration**: Combine memory with DuckDuckGo search
- **User Isolation**: Separate memory spaces per user
- **Conversation Continuity**: Maintain context across sessions

## Requirements
- `ANTHROPIC_API_KEY` in `.env` file
- `MEM0_API_KEY` for memory persistence
- Internet connection (for web search)