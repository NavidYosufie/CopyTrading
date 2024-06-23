import requests
Token = '*******'

url = 'https://api.nobitex.ir/users/wallets/balance'
payload = {'currency': 'ltc'}
headers = {
    'Authorization': 'Token ec5945d5268534c9088ad23ce6cd546513ca6f4b',
}
request = requests.request('POST', url, headers=headers, data=payload)

print(request.text)