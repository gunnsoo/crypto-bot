import logging
import datetime
import os

import ccxt


logging.basicConfig(filename='bf_bot.log', encoding='utf-8', level=logging.INFO)
today = datetime.date.today()
logging.info(f'{today} : bot starting')

API_KEY = os.getenv('BF_API_KEY')
API_SECRET = os.getenv('BF_API_SECRET')
BASE_JP_PRICE = 2000
bf = ccxt.bitflyer({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

# get last trading price
ticker = bf.fetch_ticker(symbol='BTC/JPY')
ltp = ticker['info']['ltp']
logging.info(f'ltp is {ltp}')

# calculate size
MINIMUM = 0.001
base_size = round(BASE_JP_PRICE / float(ltp), 7)
size = base_size if base_size >= MINIMUM else MINIMUM
logging.info(f'size is {size}')

# send BUY order
logging.info(f'send order')
res = bf.create_order(symbol='BTC/JPY', type='LIMIT', side='BUY', amount=size, price=ltp)
logging.info(f'order id is {res["id"]}')