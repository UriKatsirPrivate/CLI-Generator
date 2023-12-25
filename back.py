import requests

def get_project_id():
    metadata_server_url = "http://metadata.google.internal/computeMetadata/v1/"
    metadata_flavor = {'Metadata-Flavor': 'Google'}
    try:
        response = requests.get(metadata_server_url + "project/project-id", headers=metadata_flavor)
        if response.status_code == 200:
            project_id = response.text
            return project_id
        else:
            print(f"Failed to retrieve project ID. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None