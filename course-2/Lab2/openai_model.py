"""
Lab 02: Model Providers and Configuration
Configuring agents with different LLM providers
"""
# ============================================================
# OpenAI Model
# ============================================================
import os
from pydantic import BaseModel, Field

from strands import Agent
from strands.models.openai import OpenAIModel

from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5")


class PersonInfo(BaseModel):
    """Extract person information from text."""
    name: str = Field(description="Full name of the person")
    age: int = Field(description="Age in years")
    occupation: str = Field(description="Job or profession")

# Configure OpenAI model
# Note: Requires OPENAI_API_KEY environment variable
openai_model = OpenAIModel(
    model_id=OPENAI_MODEL,
    temperature=0.8,
    max_tokens=150
)

# Create agent with OpenAI
agent = Agent(model=openai_model)

# Create agent with GPT-5
result = agent.structured_output(
    PersonInfo,
    "John Smith is a 30-year-old software engineer working at a tech startup."
)

# print the result message
print("\n")
print(f"Name: {result.name}")      # "John Smith"
print(f"Age: {result.age}")        # 30
print(f"Job: {result.occupation}") # "software engineer"

# Prints the metrics
print(f"Metrics: {result.metrics}")
print("-" * 100)
print("\n")
