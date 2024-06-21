import requests
Token = '45540171a527624374de26ad61945b5f6cc6b001'

url = 'https://api.nobitex.ir/users/wallets/list'
payload = {}
headers = {
    'Authorization': 'Token 45540171a527624374de26ad61945b5f6cc6b001'
}
request = requests.request('GET', url, headers=headers, data=payload)


print(request.text)