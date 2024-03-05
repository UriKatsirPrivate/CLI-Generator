import requests
# from langchain.llms import VertexAI
from langchain_google_vertexai import VertexAI

# Get the project ID from the metadata server
def get_project_id():
    metadata_server_url = "http://metadata.google.internal/computeMetadata/v1/"
    metadata_flavor = {'Metadata-Flavor': 'Google'}
    try:
        response = requests.get(metadata_server_url + "project/project-id", headers=metadata_flavor)
        if response.status_code == 200:
            project_id = response.text
            return project_id
        else:
            # print(f"Failed to retrieve project ID. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        # print(f"Error: {e}")
        return None
    
def initialize_llm(project_id,region,model_name,max_output_tokens,temperature,top_p,top_k):
    
    # Initialize VertexAI and set up the LLM
    return VertexAI(
        project=project_id,
        location=region,
        model_name=model_name,
        max_output_tokens=max_output_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        verbose=True,
    )