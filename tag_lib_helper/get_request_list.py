# import pandas as pd
# import requests

# file_url = "https://hyperlounge.sharepoint.com/:x:/r/sites/company/Shared%20Documents/General/%E2%98%80%EF%B8%8E%20%ED%8C%80%20%ED%9A%8C%EC%9D%98%20%EC%9E%90%EB%A3%8C/DE_%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%8C%80/400.%20Tag%20Library/NEW_Tag%20Library%20%EC%B6%94%EA%B0%80%EC%9A%94%EC%B2%AD%20%EB%A6%AC%EC%8A%A4%ED%8A%B8.xlsx?d=wae9da4cf635f4f728d5c6ea7da183292&csf=1&web=1&e=rMEGsJ"

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
sharepoint_site_url = "https://hyperlounge.sharepoint.com/"

# Define your client ID and client secret

# Define your SharePoint resource URL (e.g., a file or endpoint you want to access)
sharepoint_resource_url = "https://hyperlounge.sharepoint.com/:x:/r/sites/company/Shared%20Documents/General/%E2%98%80%EF%B8%8E%20%ED%8C%80%20%ED%9A%8C%EC%9D%98%20%EC%9E%90%EB%A3%8C/DE_%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%8C%80/400.%20Tag%20Library/NEW_Tag%20Library%20%EC%B6%94%EA%B0%80%EC%9A%94%EC%B2%AD%20%EB%A6%AC%EC%8A%A4%ED%8A%B8.xlsx?d=wae9da4cf635f4f728d5c6ea7da183292&csf=1&web=1&e=rMEGsJ"

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
