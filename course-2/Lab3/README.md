# Lab 3: Advanced Response Processing with Hooks

**Duration:** 13:30 | **Files:** `async_example.py`, `hook_example_1.py`, `hook_example_2.py`

## What You'll Learn
- Implement custom logic at specific agent lifecycle points
- Create event-driven hooks for logging and monitoring
- Process responses with async iterators and callbacks
- Build retry logic and precision parameter modifications

## Quick Start
```bash
# Basic logging hooks
python hook_example_1.py

# Advanced hook modifications
python hook_example_2.py

# Async processing example
python async_example.py
```

## Key Concepts
- **Hook Lifecycle**: BeforeInvocationEvent, AfterInvocationEvent
- **Event Interception**: Modify agent behavior in real-time
- **Async Processing**: Stream responses and handle callbacks
- **Hook Composition**: Combine multiple hooks for complex workflows

## Examples
- **Logging Hook**: Track request start/end times
- **Parameter Hook**: Modify model parameters dynamically
- **Streaming Hook**: Process responses as they arrive

## Requirements
- `ANTHROPIC_API_KEY` in `.env` file