#!/usr/bin/python

class _AlphaVantage:
    def __init__(self):
        self.url="http://www.alphavantage.co/query?"
        self.apikey=""


class IntradayEquity(_AlphaVantage):
    def __init__(self, symbol, interval):
        _AlphaVantage.__init__(self)
        self.symbol = symbol
        self.output = "Use query function"
        if interval == "1min" or interval == "5min" or \
            interval == "15min" or interval == "30min" or \
            interval == "60min":
            self.interval = interval
        else:
            self.interval = "60min"
            print("Invalid interval entry. Interval set at 60min")

    def query(self):
        self.output = self.url + "function=TIME_SERIES_INTRADAY&symbol=" + \
                      self.symbol + "&interval=" + self.interval + \
                      "&apikey=" + self.apikey
        return self.output


class NormEquity(_AlphaVantage):
    def __init__(self, symbol, timeSeries):
        _AlphaVantage.__init__(self)
        self.symbol = symbol
        self.output = "Use query function"
        if timeSeries == "d":
            self.function = "TIME_SERIES_DAILY"
        elif timeSeries == "w":
            self.function = "TIME_SERIES_WEEKLY"
        elif timeSeries == "m":
            self.function = "TIME_SERIES_MONTHLY"
        else:
            self.function = "TIME_SERIES_MONTHLY"
            print("Invalid timeSeries entry. Time set to monthly")

    def query(self):
        self.output = self.url + "function=" + self.function + "&symbol=" + \
                      self.symbol + "&apikey=" + self.apikey
        return self.output


class IndiciesType1(_AlphaVantage):
    def __init__(self, indicator, symbol, interval, time_period, series_type):
        _AlphaVantage.__init__(self)
        self.symbol = symbol
        self.output = "Use query function"
        self.function = indicator
        if time_period > 0:
            self.time_period = time_period
        else:
            self.time_period = "60"
            print("Invalid time period entry. Time period set to 60")

        if interval == "1min" or interval == "5min" or \
            interval == "15min" or interval == "30min" or \
            interval == "60min" or interval == "daily" or \
            interval == "weekly" or interval == "monthly":
            self.interval = interval
        else:
            self.interval = "60min"
            print("Invalid interval entry. Interval set at 60min")

        if series_type == "close" or series_type == "open" or \
            series_type == "high" or series_type == "low":
            self.series_type = series_type
        else:
            self.series_type = "close"
            print("Invalid series type entry. Series type set to close")

    def indicator(self):
        return self.function

    def query(self):
        self.output = self.url + "function=" + self.function + "&symbol=" + \
                      self.symbol + "&interval=" + self.interval + "&time_period=" + \
                      str(self.time_period) + "&series_type=" + self.series_type + \
                      "&apikey=" + self.apikey
        return self.output
