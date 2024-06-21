import requests
Token = '*******'

url = 'https://api.nobitex.ir/users/wallets/balance'
payload = {'currency': 'ltc'}
headers = {
    'Authorization': 'Token *******',
}
request = requests.request('POST', url, headers=headers, data=payload)

print(request.text)