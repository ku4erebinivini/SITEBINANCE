from binance.client import Client

# Замініть 'YOUR_API_KEY' та 'YOUR_SECRET_KEY' на ваші власні ключі Binance API
client = Client('4ivGWIppdKkER2YrRmNwrBmiBz8P5ATLu1SOrOHDmW5NV2fyl3iUxRAI9OgLXJ2G',
                'Vei8iDoVghrur014hInzsyr8m0wpqwB1QO1cdn92nD12OuRpgm0PL87OIcTPYefm')


def get_ethereum_price():
    ticker = client.get_ticker(symbol='ETHUSDT')
    price = ticker['lastPrice']
    return price


def get_bitcoin_price():
    ticker = client.get_ticker(symbol='BTCUSDT')
    price = ticker['lastPrice']
    return price


def get_tron_price():
    ticker = client.get_ticker(symbol='TRXUSDT')
    price = ticker['lastPrice']
    return price
