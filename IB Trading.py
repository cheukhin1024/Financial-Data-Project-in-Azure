from ib_insync import *
import pandas as pd

# util.startLoop()  # uncomment this line when in a notebook
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)


Symbol_arr = ['S92','METC', 'DRCT', 'BXMT', 'NN', 'MOND', 'ISPR','0020']

while True:
    for con in Symbol_arr:
        contract = Stock(con, 'SMART', 'USD')

        bars = ib.reqHistoricalData(
            contract, endDateTime='', durationStr='30 D',
            barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

        df = util.df(bars)
        print(df)
