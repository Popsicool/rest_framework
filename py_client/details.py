import requests

endpoint = "http://localhost:8000/4/"


get_response = requests.get(endpoint)

print(get_response.json())