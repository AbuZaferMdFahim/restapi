import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title":"abc123","content": 'Hello World',"price":"sss"}) # API --> method HTTP Request
#print(get_response.headers)
#print(get_response.text) # print source code
#print(get_response.status_code)
# HTTP Request --> Text
# REST API HTTP Request --> JSON
# JavaScript Object Nototion --> Python Dict
print(get_response.json())
#print(get_response.status_code)




