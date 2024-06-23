import requests


class NobitexAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_wallet_balance(self):
        url = f'{self.base_url}users/wallets/balance'
        payload = {'currency': 'ltc'}
        response = requests.request('POST', url, headers=self.token, data=payload)
        if response.status_code == 200:
            return response.json()
        return response.status_code

    def get_user_order(self):
        url = f'{self.base_url}market/orders/list'
        response = requests.request('GET', url, headers=self.token)
        if response.status_code == 200:
            return response.json()
        return response.status_code

    def set_order(self, type, execution, srcCurrency, dstCurrency, amount, price, stopPrice, stopLimitPrice):
        url = f'{self.base_url}market/orders/add'
        payload = {
            'type': type,
            'execution': execution,
            'srcCurrency': srcCurrency,
            'dstCurrency': dstCurrency,
            'amount': amount,
            'price': price,
            'stopPrice': stopPrice,
            'stopLimitPrice': stopLimitPrice
        }
        response = requests.request('POST', url, headers=self.token, data=payload)
        status = response.json()
        return status


api = NobitexAPI('https://api.nobitex.ir/', {'Authorization': 'Token ******'})

balance = api.get_wallet_balance()
print(balance)
orders = api.get_user_order()
print(orders)
new_order = api.set_order()
print(new_order)