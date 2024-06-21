import requests

Token = '******'
url = 'https://api.nobitex.ir/market/orders/add'

srcCurrency = input('origin currency: ').upper()
dstCurrency = input('destination currency: ').upper()
Amount = input('enter your amount: ')
Price = input('Choose your price to buy currency: ')
StopPrice = input('Determine the selling price: ')
stopLimitPrice = input('Enter the breakeven price')


def SellCoin():
    payload = {
        'type': 'buy',
        'srcCurrency': srcCurrency,
        'dstCurrency': dstCurrency,
        'amount': float(Amount),
        'price': float(Price),
        'stopPrice': float(StopPrice),
        'stopLimitPrice': float(stopLimitPrice)
    }
    headers = {
        'Authorization': f'Token {Token}'
    }
    files = [

    ]
    request = requests.request('POST', url, headers=headers, data=payload, files=files)
    print(request.text)


SellCoin()
