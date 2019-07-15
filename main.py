#!/usr/bin/python

import time
from alpaca import *
from database import *

# def main():
#     db = Database()
#     ap = Alpaca()
#     done = None
#     print("Start Running")
#     while True:
#         if ap.marketOpen() and done != ap.getTime().strftime('%m-%d-%Y %H:%M'):
#
#
#             done = ap.getTime().strftime('%m-%d-%Y %H:%M')
#         time.sleep(1)


ap = Alpaca()
ap.exsistingOrder()



# db = Database()
# db.pull(NormEquity("ZNGA", "d"))
# db.commit()

# q1 = NormEquity("AAPL", "w")
# IndiciesType1("SMA", "AAPL", "monthly", 60, "close")
# IntradayEquity("AAPL", "60min")