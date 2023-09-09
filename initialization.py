import os
import json
import vertexai
from langchain.llms import VertexAI
# from google.cloud import secretmanager

def initialize_llm(project_id,region,model_name,max_output_tokens,temperature,top_p,top_k):
   
    # Initialize VertexAI and set up the LLM
    init_vertexai(project_id=project_id,region=region)
    return set_up_llm(model_name=model_name,max_output_tokens=max_output_tokens,temperature=temperature,top_p=top_p,top_k=top_k)

def init_vertexai(project_id,region):
    # Initialize VertexAI with the proper settings
    vertexai.init(project=project_id, location=region)

def set_up_llm(model_name,max_output_tokens,temperature,top_p,top_k):
    # Set up the VertexAI with the specified parameters
    return VertexAI(
        model_name=model_name,
        max_output_tokens=max_output_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        verbose=True,
    )