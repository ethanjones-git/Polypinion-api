import requests

BASE = 'http://127.0.0.1:8000/'

response = requests.get(BASE+'get-news-stream')
print(response.json())