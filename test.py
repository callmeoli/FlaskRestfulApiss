import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/19", {"likes": 10, "name": "Tim", "views" : 10000 })
input()
response = requests.get(BASE + "video/19")
print(response.json())
