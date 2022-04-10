import requests

pixela_endpoint ="https://pixe.la/v1/users"

user_params = {
    "token": "a random token",
    "username": "random_user",
    "agreeTermsOfService": "maybe",
    "notMinor": "maybe"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
