import requests

endpoint = "http://localhost:8000/restapi/products/"


get_response = requests.get(endpoint)

print(get_response.json())



