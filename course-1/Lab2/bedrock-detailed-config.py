from strands import Agent
from strands.models import BedrockModel

# Configure specific Bedrock model
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-premier-v1:0",  # Specify the model
    temperature=0.3,                         # Control randomness
    top_p=0.8,                              # Control token selection
    streaming=True                           # Enable response streaming
)

agent = Agent(model=bedrock_model)