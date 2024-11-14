import requests

token = ''
# api_url = 'https://api.telegram.org/bot6337746585:AAGbmoOQnYOS1UZhH7ncs8R7DAi51DXrvMc/getUpdates'
# ок api_url = f'https://api.telegram.org/bot{token}/getMe'
# ne api_url = f'https://api.telegram.org/bot{token}/sendMessage?chat=393607933&text=Hello!'
# ок api_url = f'https://api.telegram.org/bot{token}/getUpdates?offset=-1'
# ne api_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=393607933&message=Hello world!'
# ne api_url = f'https://api.telegram.org/bot{token}/getUpdate'
# api_url = 'https://api.telegram.org/bot6337746585:AAGbmoOQnYOS1UZhH7ncs8R7DAi51DXrvMc/sendMessage?chat_id=393607933&text=Привет, \u0410\u0440\u0442\u0443\u0440!'
head = {'Content-Type': 'application/json'}

response = requests.get(api_url)


if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)
