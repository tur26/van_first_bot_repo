import requests

api_url = 'http://numbersapi.com/43'
head = {'Content-Type': 'application/json'}

response = requests.get(api_url)


if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)