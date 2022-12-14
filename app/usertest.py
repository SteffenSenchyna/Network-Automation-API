import requests
import json
from flask import Response
from pprint import pprint
import csv
import io
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ipList = ["10.0.10.1"]
# Set the base URL for the RESTCONF API
for ip in ipList:
    url = f"https://{ip}/restconf/data/Cisco-IOS-XE-native:native"
    headers = {
        "Accept" : "application/yang-data+json", 
        "Content-Type" : "application/yang-data+json", 
    }
# Set the credentials for authenticating with the RESTCONF API
auth = ("admin", "cisco")

# Set the username and password for the new user
username = "Steffen"
password = "cisco"

# Create the payload for the POST request
user_data = {
    "Cisco-IOS-XE-native:username":[
            {'name': 'ciscotest',
            'privilege': 15,
            'secret': {'encryption': '0',
                        'secret': 'cisco'}
                        }
                        ]
    }


# Send the POST request to the /restconf/data/Cisco-IOS-XE-native:native/username endpoint
response = requests.post(url, headers=headers,data=json.dumps(user_data), auth=("admin", "cisco"), verify=False)
# print(response.text)
#response = requests.get(url, headers=headers,json=user_data, auth=("admin", "cisco"), verify=False).json()
pprint(response.status_code)
# Check the response status code to ensure the request was successful
# if response.status_code == 201:
#     print(f"Successfully added user {username} to the Cisco switch")
# else:
#     print(f"Failed to add user {username} to the Cisco switch. Status code: {response.status_code}")
