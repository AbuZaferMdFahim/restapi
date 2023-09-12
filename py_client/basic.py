import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint,json={"query": "Hello World"}) # API --> method HTTP Request
print(get_response.text) # print source code
print(get_response.status_code)
# HTTP Request --> Text
# REST API HTTP Request --> JSON
# JavaScript Object Nototion --> Python Dict
print(get_response.json()['message'])
print(get_response.status_code)




