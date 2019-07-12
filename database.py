#!/usr/bin/python

import urllib.request
import json
import sqlite3
from alphavantage import *


class Database:
    def __init__(self, ):
        self.connect = sqlite3.connect("Stocks.db")
        self.db = self.connect.cursor()
        print("Stocks.db connected")

    def pull(self, obj):
        data = json.load(urllib.request.urlopen(obj.query()))

        if type(obj) is IntradayEquity:
            tablename = "Intraday" + "_" +\
                        data[list(data)[0]]["2. Symbol"] + "_" +\
                        data[list(data)[0]]["4. Interval"]
            self.db.execute('DROP TABLE IF EXISTS ' + tablename)
            self.db.execute('CREATE TABLE ' + tablename + ' (\
                                                            Time Text PRIMARY KEY, \
                                                            Open REAL, \
                                                            High REAL, \
                                                            Low REAL, \
                                                            Close REAL, \
                                                            Volume REAL)')
            date = list(data[list(data)[1]])
            open = []
            high = []
            low = []
            close = []
            volume = []
            for i in date:
                open.append(float(data[list(data)[1]][i]["1. open"]))
                high.append(float(data[list(data)[1]][i]["2. high"]))
                low.append(float(data[list(data)[1]][i]["3. low"]))
                close.append(float(data[list(data)[1]][i]["4. close"]))
                volume.append(float(data[list(data)[1]][i]["5. volume"]))

            for i in list(zip(date, open, high, low, close, volume)):
                self.db.execute("INSERT INTO " + tablename + " VALUES (?,?, ?, ?, ?, ?)", i)

        elif type(obj) is NormEquity:
            tablename = data[list(data)[0]]["2. Symbol"] + "_" +\
                        data[list(data)[0]]["1. Information"].partition(' ')[0]
            self.db.execute('DROP TABLE IF EXISTS ' + tablename)
            self.db.execute('CREATE TABLE ' + tablename + ' (\
                                                            Time Text PRIMARY KEY, \
                                                            Open REAL, \
                                                            High REAL, \
                                                            Low REAL, \
                                                            Close REAL, \
                                                            Volume REAL)')
            date = list(data[list(data)[1]])
            open = []
            high = []
            low = []
            close = []
            volume = []
            for i in date:
                open.append(float(data[list(data)[1]][i]["1. open"]))
                high.append(float(data[list(data)[1]][i]["2. high"]))
                low.append(float(data[list(data)[1]][i]["3. low"]))
                close.append(float(data[list(data)[1]][i]["4. close"]))
                volume.append(float(data[list(data)[1]][i]["5. volume"]))

            for i in list(zip(date, open, high, low, close, volume)):
                self.db.execute("INSERT INTO " + tablename + " VALUES (?,?, ?, ?, ?, ?)", i)

        elif type(obj) is IndiciesType1:
            tablename = data[list(data)[0]]["1: Symbol"] + "_" + \
                        data[list(data)[0]]["2: Indicator"].partition('(')[2].rpartition(')')[0] + "_" +\
                        data[list(data)[0]]["4: Interval"]
            self.db.execute('DROP TABLE IF EXISTS ' + tablename)
            self.db.execute('CREATE TABLE ' + tablename + ' (\
                                                               Time Text PRIMARY KEY, \
                                                               Value REAL)')
            date = list(data[list(data)[1]])
            value = []
            for i in date:
                value.append(float(data[list(data)[1]][i][obj.indicator()]))

            for i in list(zip(date, value)):
                self.db.execute("INSERT INTO " + tablename + " VALUES (?,?)", i)
        print("Table added/updated")

    def commit(self):
        self.connect.commit()

    def close(self):
        self.connect.close()