import requests
import datetime as dt
from datetime import timedelta
# import re

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "a_random_token"  # add 1 and delete _ for 2nd user
USER_NAME = "d4v1d"  # add 1 for 2nd user

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Post requesst to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "hours",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Post request to establish the graph

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

pixel_drop = f"{graph_endpoint}/{graph_config['id']}"
# print(pixel_drop)
# Post request to establish a pixel
# CLEANR = re.compile('-')

# My solution:
# string_drop = str(dt.datetime.now()).split(" ")[0]

# Fancy pants:
string_drop = dt.datetime.now().strftime("%Y%m%d")
string_drop2 = (dt.datetime.now()-timedelta(1)).strftime("%Y%m%d")

pixel_params = {
    # "date": re.sub(CLEANR, "", string_drop),
    "date": string_drop,
    "quantity": "1"
}

# response = requests.post(url=pixel_drop, headers=headers, json=pixel_params)

pixel_put_params = {
    "quantity": "1"
}

temp = f"{pixel_drop}/{string_drop2}"

print(temp)

# response = requests.put(url=temp, headers=headers, json=pixel_put_params)

response = requests.delete(url=temp, headers=headers)

print(response.text)
