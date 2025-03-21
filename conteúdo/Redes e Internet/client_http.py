import requests
response = requests.get('https://localhost:8000')
print(response.text)