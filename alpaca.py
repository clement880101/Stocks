#!/usr/bin/python

import alpaca_trade_api as tradeapi

class Alpaca:
    def __init__(self):
        self.api = tradeapi.REST(key_id='PKC1DA6WJU5YXE2855E9',
                    secret_key='JdaVsFcOGT/2zpPwebIkWxGtFKpJzJvY7NQTmYvf',
                    base_url='https://paper-api.alpaca.markets',
                    api_version='v2')
        self.account = self.api.get_account()
        if self.account.trading_blocked:
            print('Account is currently restricted from trading.')

    def marketOrder(self, symbol, qty, side, tif):
        self.api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force=tif,
        )

    def limitOrder(self, symbol, qty, side, tif, price):
        self.api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='limit',
            time_in_force=tif,
            limit_price=price
        )

    def exsistingOrder(self):
        orders = self.api.list_orders(
            status='closed',
            limit=100
        )
        print(orders)

