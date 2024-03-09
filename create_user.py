import requests
import os

# Creating a user in pixela
pixela_endpoint = "https://pixe.la/v1/users"


# Replace token with your password and username with you desired username
user_parameters ={
    "token": os.environ.get("PW"),
    "username": os.environ.get("USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Should print success if your token and username input in correct
response = requests.post(url=pixela_endpoint, json=user_parameters)
print(response.text)