import requests
from datetime import datetime

USER_NAME = "venkat67"
TOKEN = "venkat_secret_tqqoken_123"
GRAPH_ID = "graph1"

pixele_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixele_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "meditation graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}

headers = {"X-USER-TOKEN": TOKEN}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_creation_endpoint = f"{pixele_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you meditate today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
