"""
Lab 04: Integrating MCP Tools into a Strands Agent
Demonstrates how to connect to an MCP server and use its tools within a Strands agent
"""
import os

from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands.tools.mcp import MCPClient

from strands_tools import file_read, file_write
from mcp import stdio_client, StdioServerParameters
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the Anthropic API key from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set.")

ANTHROPIC_MODEL_ID = "claude-3-7-sonnet-20250219"

# Require AWS credentials to access pricing data
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY]):
    raise ValueError("AWS credentials are required to access pricing data.")
# Define the system prompt to guide the agent's behavior
SYSTEM_PROMPT = """
You are an AWS Solutions Architect with expertise in AWS services and solutions.

  You have access to the following tools:
  - file read: Read the contents of a file
  - file write: Write content to a file
  - AWS Documentation tools:
    * search_documentation: Find relevant AWS docs
    * read_documentation: Get full content of specific docs
    * recommend: Get related documentation

  - AWS Pricing tools:
    * get_pricing_service_codes: List all available AWS service codes
    * get_pricing_service_attributes: Find filterable attributes for a service
    * get_pricing_attribute_values: Get valid values for attributes
    * get_pricing: Get actual pricing data using the service code, region, and filters
    * get_bedrock_patterns: Get architecture patterns for Bedrock
    * generate_cost_report: Generate detailed cost analysis reports

  IMPORTANT PRICING WORKFLOW - FOLLOW EXACTLY:
  1. Use get_pricing_service_codes() to get service codes "AmazonS3" and "AmazonCloudFront"
  2. For each service (S3 and CloudFront), use get_pricing_service_attributes() to find attributes
  3. Use get_pricing("AmazonS3", "us-east-1") for S3 pricing
  4. Use get_pricing("AmazonCloudFront", "us-east-1") for CloudFront pricing
  5. Include all pricing details in your summary

When answering questions, always use the available tools to gather accurate information. Cite
documentation URLs when providing information.
"""

# Configure Anthropic model
# Note: Requires ANTHROPIC_API_KEY environment variable
anthropic_model = AnthropicModel(
    client_args={
        "api_key": ANTHROPIC_API_KEY
    },
    # **model_config
    # Max tokens is set to 8000
    max_tokens=8000,
    model_id=ANTHROPIC_MODEL_ID,
    params={
        "temperature": 0
    }
)

# MCP Servers
aws_docs_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            args=["awslabs.aws-documentation-mcp-server@latest"]
        ),
    )
)

# NOTE: Requires AWS credentials to access pricing data
aws_pricing_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            args=["awslabs.aws-pricing-mcp-server@latest"],
            env={
                "AWS_ACCESS_KEY_ID": AWS_ACCESS_KEY_ID,
                "AWS_SECRET_ACCESS_KEY": AWS_SECRET_ACCESS_KEY,
                "AWS_SESSION_TOKEN": AWS_SESSION_TOKEN,
                "AWS_REGION": AWS_REGION,
            }
        ),
    )
)


prompt = """
Create a summary of hosting a static website on AWS using S3 and CloudFront.
  Include:
  1. Direct links to the official AWS documentation for S3 static website hosting and CloudFront
  distribution setup
  2. Pricing for S3 storage (first 50GB) and CloudFront data transfer (first 10TB)
Save the summary to static_website_aws.md
"""

# Connect to MCP server, list tools, invoke agent with MCP tools, and disconnect
with aws_docs_mcp_client, aws_pricing_mcp_client:
    # Combine tools from both MCP clients
    tools = aws_docs_mcp_client.list_tools_sync() + aws_pricing_mcp_client.list_tools_sync()

    print(f"Available tools from MCP servers ({len(tools)}):")
    for tool in tools:
        print(f"- {tool.tool_name}")

    # Create an agent with default settings
    aws_agent = Agent(
        model=anthropic_model,
        system_prompt=SYSTEM_PROMPT,
        tools=[file_read, file_write, tools],
    )

    aws_agent(prompt)

# Get the event loop metrics summary
metrics_summary = aws_agent.event_loop_metrics.get_summary()

# Print token usage
print("Token Usage:")
print(f"  Input tokens:  {metrics_summary['accumulated_usage']['inputTokens']:,}")
print(f"  Output tokens: {metrics_summary['accumulated_usage']['outputTokens']:,}")
print(f"  Total tokens:  {metrics_summary['accumulated_usage']['totalTokens']:,}")

# Print tool metrics
print("\nTool Usage:")

for tool_name, tool_data in metrics_summary['tool_usage'].items():
    stats = tool_data['execution_stats']
    print(f"  {tool_name}:")
    print(f"    Calls: {stats['call_count']} (Success: {stats['success_count']}, Error: {stats['error_count']})")
    print(f"    Success rate: {stats['success_rate'] * 100:.1f}%")
