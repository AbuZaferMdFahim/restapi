import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/restapi/"

# get_response = requests.get(endpoint, params={"abc":123}, data={"query": "Hello world"})
get_response = requests.post(endpoint,json={"title":None, "content":"Hello World"})
# print(get_response.headers)
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)

