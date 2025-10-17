"""
Lab 02: Model Providers and Configuration
Configuring agents with different LLM providers
"""
# ============================================================
# Amazon Bedrock Model
# ============================================================
from pydantic import BaseModel, Field
from strands import Agent
from strands.models import BedrockModel


# Create book analysis model
class BookAnalysis(BaseModel):
    """Analyze a book's key information."""
    title: str = Field(description="The book's title")
    author: str = Field(description="The book's author")
    genre: str = Field(description="Primary genre or category")
    summary: str = Field(description="Brief summary of the book")
    rating: int = Field(description="Rating from 1-10", ge=1, le=10)


# Configure Bedrock model
# Note: Requires AWS credentials configured
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    max_tokens=4096,
    region="us-east-1",
    temperature=0.5,
    cache_prompt="default"
)

# Create agent with Bedrock
agent = Agent(
    system_prompt="You are a helpful assistant.",
    model=bedrock_model
)

# Verify the model configuration
agent.model.config

# Structured output with Pydantic model
result = agent.structured_output(
    BookAnalysis,
    """
    Analyze this book: "The Hitchhiker's Guide to the Galaxy" by Douglas Adams.
    It's a science fiction comedy about Arthur Dent's adventures through space
    after Earth is destroyed. It's widely considered a classic of humorous sci-fi.
    """
)

# print the result message
print("\n")
print("-" * 100)
print("\n")
print(f"Result: {result}")
print("-" * 100)
print("\n")

# Print each result field
print(f"Title: {result.title}")
print(f"Author: {result.author}")
print(f"Genre: {result.genre}")
print(f"Rating: {result.rating}")
