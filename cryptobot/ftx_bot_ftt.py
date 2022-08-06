import logging
import datetime
import os

import ccxt


logging.basicConfig(filename='ftx_bot_ftt.log', encoding='utf-8', level=logging.INFO)
today = datetime.date.today()
logging.info(f'{today} : bot starting')

API_KEY = os.getenv('FTX_API_KEY')
API_SECRET = os.getenv('FTX_API_SECRET')
ftx = ccxt.ftx({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

# get last trading price
ticker = ftx.fetch_ticker(symbol='FTT/JPY')
ltp = ticker['last']
logging.info(f'ltp is {ltp}')

# calculate order price (99% of ltp)
UNIT = 1
order_price = ltp * 0.97
logging.info(f'size is {UNIT}')
logging.info(f'order_pric is {order_price}')

# send BUY order
logging.info(f'send order')
res = ftx.create_order(symbol='FTT/JPY', type='limit', side='buy', amount=UNIT, price=order_price, params={'postOnly': True})
logging.info(f'order id is {res["id"]}')