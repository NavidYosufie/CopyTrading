import requests

Token = '******'

srcCurrency = input('origin currency: ')
dstCurrency = input('destination currency: ')
Amount = input('enter your amount: ')
Price = input('Choose your price to buy currency: ')
StopPrice = input('Set your price for the stop loss: ')

url = 'https://api.nobitex.ir/market/orders/add'

def SellCoin():
    payload  = {
        'type': 'sell',
        'srcCurrency': srcCurrency,
        'dstCurrency': dstCurrency,
        'amount': float(Amount),
        'price': float(Price),
        'stopPrice': float(StopPrice)
    }
    headers = {
        'Authorization': f'Token {Token}'
    }
    files = [

    ]
    request = requests.request('POST', url, headers=headers, data=payload, files=files)
    print(request.text)


SellCoin()



