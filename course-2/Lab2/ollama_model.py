"""
Lab 02: Model Providers and Configuration
Configuring agents with different LLM providers
"""
# ============================================================
# Ollama Model
# ============================================================
import os

from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator

from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL_ID = os.getenv("OLLAMA_MODEL_ID", "llama3.2:3b")

# Create an Ollama model instance
# Ollama models list: https://ollama.com/docs/models
ollama_model = OllamaModel(
    host=OLLAMA_HOST,   # Ollama server address
    model_id=OLLAMA_MODEL_ID,               # Specify which model to use
    temperature=0.7,
    keep_alive="10m",
    stop_sequences=["###", "END"],
    options={"top_k": 40}
)

# Create an agent using the Ollama model
agent = Agent(
    system_prompt="You are a helpful assistant.",
    model=ollama_model,
    tools=[calculator]
)

result = agent("What are the 7 layers of the OSI model? Only return the names of the layers. And what is 7 * 7?")

# print the result message
print("\n")
print("-" * 100)
print("\n")
print(f"Result: {result}")
print("-" * 100)
print("\n")

# Prints the metrics
print(f"Metrics: {result.metrics}")
print("-" * 100)
print("\n")
