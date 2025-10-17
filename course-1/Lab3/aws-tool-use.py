# Import necessary libraries
import os                                     # For accessing environment variables
from strands import Agent                    # Import the Agent class from strands library
from strands.models.anthropic import AnthropicModel  # Import Anthropic's language model
from strands_tools import use_aws           # Import the AWS tool for interacting with AWS services
from dotenv import load_dotenv               # For loading environment variables from .env file

load_dotenv()

# Configure the Anthropic language model (Claude)
model = AnthropicModel(
    # Set up authentication using API key from environment variables
    client_args={
        "api_key": os.getenv("api_key"),  # Get API key from environment variables
    },
    # **model_config
    max_tokens=1028,                    # Set maximum response length to 1028 tokens
    model_id="claude-sonnet-4-20250514",  # Specify which Claude model version to use
    params={
        "temperature": 0.3,              # Set temperature to 0.3 (lower values make output more deterministic)
    }
)

# Create an AI agent with AWS capabilities
agent = Agent(
    model=model,                      # Use the Anthropic model configured above
    tools=[use_aws]                   # Give the agent access to AWS tools for interacting with AWS services
)

# Example queries (toggle line comments to enable)

query= "List the S3 buckets in my account"  # Simple query to list S3 buckets in the configured AWS account

#query="Query the DynamoDB table called 'UserProfiles' in the us-west-2 region. Get all items for userId 'user123' and show me the results in a readable format."  # Query for a specific user in DynamoDB

#query="Find all users in the 'UserProfiles' table in the us-west-2 region who have an attribute 'status' of 'Active', show me their names and email addresses."

# Send the query to the agent and store the response
# The agent will use the use_aws tool to interact with DynamoDB and S3  and filter the results
response = agent(query)