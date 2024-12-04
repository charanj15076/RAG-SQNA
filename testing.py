import boto3
from langchain_community.embeddings import BedrockEmbeddings



bedrock_client = boto3.client(service_name="bedrock-runtime")
bedrock_embedding = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock_client)

# mistral.mistral-7b-instruct-v0:2



