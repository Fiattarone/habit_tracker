import requests

pixela_endpoint ="https://pixe.la/v1/users"
TOKEN = "a_random_token"
USER_NAME = "d4v1d"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graph"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "days",
    "type": "integer",
    "color": "kuro"
}


response = requests.post(url=graph_endpoint, json=graph_config)

print(response.text)
