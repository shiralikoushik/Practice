import json

import requests

# payload = {"username": "Koushik", "Password": "Testing"}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# r = requests.get("https://github.com/shiralikoushik")
# print(r.text)

r = requests.get("http://httpbin.org//basic-auth/shirali/test", auth=("shirali","test"))

print(r.text)