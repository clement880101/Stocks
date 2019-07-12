#!/usr/bin/python


from database import *


db = Database()
db.pull(IndiciesType1("DEMA", "AAPL", "monthly", 60, "close"))
db.commit()

# q1 = NormEquity("AAPL", "w")
# IndiciesType1("SMA", "AAPL", "monthly", 60, "close")
# IntradayEquity("AAPL", "60min")