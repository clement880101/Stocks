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
            exit()
        self.clock = self.api.get_clock()

    def buyingPower(self):
        return self.account.buying_power

    def marketOpen(self):
        return self.clock.is_open

    def getTime(self):
        return self.clock.timestamp

    def showPosition(self):
        portfolio = self.api.list_positions()
        for position in portfolio:
            print("{} shares of {}".format(position.qty, position.symbol))

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

    def cancelOrder(self, id):
        self.api.cancel_order(id)

    def exsistingOrder(self):
        orders = self.api.list_orders(
            status='new',
            limit=100
        )
        print(orders)