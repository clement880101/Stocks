#!/usr/bin/python

import alpaca_trade_api as tradeapi

id = 'PKC1DA6WJU5YXE2855E9'
skey = 'JdaVsFcOGT/2zpPwebIkWxGtFKpJzJvY7NQTmYvf'

api = tradeapi.REST(key_id=id,
                    secret_key=skey,
                    base_url='https://paper-api.alpaca.markets',
                    api_version='v2')
account = api.get_account()
if account.trading_blocked:
    print('Account is currently restricted from trading.')
print(account.buying_power)