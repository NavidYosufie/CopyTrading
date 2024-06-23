from dotenv import load_dotenv
import requests
import os

load_dotenv()

Token = {
    'Authorization': f'Token {os.getenv("TOKEN_NobitexAPI")}',
}
BaseUrl = 'https://api.nobitex.ir/'


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
    def get_order(self):
        execution = input('If you want the transaction to be done at the market price, enter the word (market), otherwise, the transaction will be done at the price you specified: ')
        srcCurrency = input('Select the source currency: ')
        dstCurrency = input('Select the destination currency: ')
        amount = input('enter your amount: ')
        price = input('enter your price: ')
        stopPrice = input('If you want to sell your currency at a certain price, enter the price, otherwise, press enter: ')
        stopLimitPrice = input('If you want to determine the loss limit, enter the amount, otherwise press enter: ')

        url = f'{self.base_url}market/orders/add'
        payload = {
            'type': 'buy',
            'execution': 'limit',
            'srcCurrency': 'btc',
            'dstCurrency': 'usdt',
            'amount': f'{amount}',
            'price': f'{price}',
            'stopPrice': '',
            'stopLimitPrice': ''
        }
        if execution:
            payload.update({'execution': execution})
        if srcCurrency:
            payload.update({'srcCurrency': srcCurrency})
        if dstCurrency:
            payload.update({'dstCurrency': dstCurrency})
        if stopPrice:
            payload.update({'stopPrice': stopPrice})
        if stopLimitPrice:
            payload.update({'stopLimitPrice': stopLimitPrice})
        response = requests.request('POST', url, headers=self.token, data=payload)
        status = response.json()
        return status



api = NobitexAPI(BaseUrl, Token)

print(api.get_wallet_balance())
print(api.get_user_order())
print(api.get_order())
