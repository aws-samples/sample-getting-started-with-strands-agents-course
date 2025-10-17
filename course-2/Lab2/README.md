# Lab 2: Model Providers and Configuration

**Duration:** 11:59 | **Files:** `anthropic_model.py`, `bedrock_model.py`, `ollama_model.py`, `openai_model.py`

## What You'll Learn
- Configure agents with multiple LLM providers (Anthropic, Bedrock, OpenAI, Ollama)
- Understand model-specific parameters and capabilities
- Compare structured output and thinking mode features
- Analyze metrics and performance across providers

## Quick Start
```bash
# Anthropic Claude (requires ANTHROPIC_API_KEY)
python anthropic_model.py

# Amazon Bedrock (requires AWS credentials)
python bedrock_model.py

# OpenAI (requires OPENAI_API_KEY)
python openai_model.py

# Local Ollama (requires Ollama installation)
python ollama_model.py
```

## Key Concepts
- **Provider Flexibility**: Switch between cloud and local models
- **Model Parameters**: Temperature, max tokens, thinking mode
- **Structured Output**: JSON response formatting
- **Cost Optimization**: Choose models based on use case

## Requirements
- `ANTHROPIC_API_KEY` (primary)
- AWS credentials (for Bedrock)
- `OPENAI_API_KEY` (optional)
- Ollama installation (for local models)