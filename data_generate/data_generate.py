import requests
import json
from typing import List


URL_INFO = "https://api.bittrex.com/v3/currencies"
URL_COIN_PRICE = "https://api.bittrex.com/v3/markets/name_coin-currency/ticker"
COIN_NAMES = {"BTC": "USDT",
              "ETH": "USDT",
              "DOGE": "USDT",
              "TON": "USD",
              "LTC": "USDT",
              "UNI": "USD",
              "USDT": "USD",
              "USDC": "USD"}


def data_generate() -> List[dict]:
    coin_info = []
    response = requests.get(URL_INFO)
    data = json.loads(response.text)
    for i in data:
        if i['symbol'] in COIN_NAMES:
            coin_data = {
                "names": i['symbol'],
                "status": i['status'],
                "coin_type": i["coinType"],
                "tx_fee": i["txFee"],
                "img": i["logoUrl"],
                "price": get_coin_price(i['symbol'], COIN_NAMES[i['symbol']])
            }
            coin_info.append(coin_data)
    return coin_info


def get_coin_price(name_coin, currency) -> int:
    response = requests.get(URL_COIN_PRICE.replace('name_coin', name_coin).replace('currency', currency))
    data = json.loads(response.text)
    return data['lastTradeRate']


print(data_generate())
