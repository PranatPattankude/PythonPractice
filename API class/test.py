import requests

res = requests.get('http://127.0.0.1:5000/home/3')
print(res.status_code)
print(res.text)


