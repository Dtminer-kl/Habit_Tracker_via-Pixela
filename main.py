import os
import requests
from datetime import datetime

# Pixela endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# Pixela graph
graph_endpoint = f"{pixela_endpoint}/{os.environ.get("USERNAME")}/graphs"

headers = {
    "X-USER-TOKEN": os.environ.get("PW")
}
print(headers)

graph_config = {
    "id": "graph1",
    "name": "Coding",
    "unit": "Mins",
    "type": "float",
    "color": "shibafu"
    # green
}

# Making the graph

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Adding a Pixel to graph
pixel_endpoint = f"{pixela_endpoint}/{os.environ.get("USERNAME")}/graphs/graph1"

# Getting today's date
today = datetime(year=2024, month=3, day=8)
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "100",
}
# response_pixel = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response_pixel.text)

# Updating an pixel
update_endpoint = f"{pixela_endpoint}/{os.environ.get("USERNAME")}/graphs/graph1/{today.strftime("%Y%m%d")}"
update_pixel = {
    "quantity": "10"
}
# response_update = requests.put(url=update_endpoint, json=update_pixel, headers=headers)
# print(response_update.text)

# Delete pixel
delete_endpoint = f"{pixela_endpoint}/{os.environ.get("USERNAME")}/graphs/graph1/{today.strftime("%Y%m%d")}"

# response_delete = requests.delete(url=delete_endpoint,headers=headers)
# print(response_delete.text)


# You can check your graph using the following:
print(pixel_endpoint)