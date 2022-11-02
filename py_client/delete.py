import requests


endpoint = f"http://localhost:8000/4/delete/"

get_response = requests.delete(endpoint)

print(get_response.status_code, get_response.status_code == 204)