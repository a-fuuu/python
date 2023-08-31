# import pandas as pd
# import requests



# local_file_path = "/home/junpyo/file.xlsx"

# response = requests.get(file_url)

# if response.status_code == 200:
#     with open(local_file_path, 'wb') as file:
#         file.write(response.content)
#     print(f"File downloaded successfully to {local_file_path}")
# else:
#     print(f"Failed to download the file. Status code: {response.status_code}")


import requests
from requests.auth import HTTPBasicAuth

# Define your SharePoint site URL


# Define your client ID and client secret

# Define your SharePoint resource URL (e.g., a file or endpoint you want to access)


# Acquire an OAuth2 token using the client ID and client secret
token_url = f"{sharepoint_site_url}/_layouts/15/appstsserver.aspx?SecurityTokenServiceMachine=your-sts-server"
token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "resource": sharepoint_resource_url
}
token_response = requests.post(token_url, data=token_data)
print(token_response.text)
if token_response.status_code == 200:
    access_token = token_response.json().get("access_token")

    # Include the access token in the request headers
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Make a request to access the SharePoint resource
    response = requests.get(sharepoint_resource_url, headers=headers)

    if response.status_code == 200:
        # Process the SharePoint resource here
        print("Request successful")
    else:
        print(f"Failed to access the SharePoint resource. Status code: {response.status_code}")
else:
    print(f"Failed to acquire the OAuth2 token. Status code: {token_response.status_code}")
