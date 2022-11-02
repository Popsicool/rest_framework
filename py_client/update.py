import requests

endpoint = "http://localhost:8000/3/update/"

data = {
    "title": "Buga",
}
get_response = requests.patch(endpoint, json=data)

print(get_response.json())
# print(get_response.status_code)
