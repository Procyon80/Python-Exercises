import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print(json)