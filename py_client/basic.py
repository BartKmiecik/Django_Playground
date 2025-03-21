import requests

home = "http://www.httpbin.org"
endpoint = 'http://www.httpbin.org/anything'
endpoint2 = 'http://www.httpbin.org/status/200'
myEndpoint = 'http://127.0.0.1:8000/api/'

get_request = requests.get(myEndpoint, json={"product_id": 123})
# print(get_request.headers)
# print(get_request.text)
print(get_request.json())
# print(get_request.status_code)
