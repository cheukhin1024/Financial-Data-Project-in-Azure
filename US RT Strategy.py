from ib_insync import *
from pytz import timezone
import datetime
import time
import pandas as pd

#util.startLoop()  # uncomment this line when in a notebook

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1, timeout=30)  
#ib.connect('127.0.0.1', 4002, clientId=4, timeout=30)  

hashmap_historical_data_ADJUSTED_LAST = {}
hashmap_count = {}
hashmap_etf_rank = {}

spy_contract = Stock(symbol="SPY", exchange='SMART', currency='USD')

spy_bars = ib.reqHistoricalData(contract=spy_contract, 
                                endDateTime="", 
                                barSizeSetting='1 day', 
                                durationStr='1 Y', 
                                whatToShow='ADJUSTED_LAST', 
                                useRTH=True)

hashmap_historical_data_ADJUSTED_LAST['SPY'] = util.df(spy_bars)

symbols = ['XLB','XLV','XLC','XLK','XLF','XLP','XLI','XLU','XLY','XLE','XLRE']
for symbol_name in symbols:
    contract = Stock(symbol=symbol_name, exchange='SMART', currency='USD')

    bars = ib.reqHistoricalData(contract=contract, 
                                endDateTime="", 
                                barSizeSetting='1 day', 
                                durationStr='1 Y', 
                                whatToShow='ADJUSTED_LAST', 
                                useRTH=True,
                                formatDate=1,
                                keepUpToDate=False, 
                                chartOptions=[], 
                                timeout=60)
    
    hashmap_historical_data_ADJUSTED_LAST[symbol_name] = util.df(bars)
    
    #print(symbol_name)
    #print(hashmap_historical_data_ADJUSTED_LAST[symbol_name])

    highest_etf_occurance = 0
    hashmap_count[symbol_name] = (hashmap_historical_data_ADJUSTED_LAST[symbol_name]['close'].pct_change(1) > hashmap_historical_data_ADJUSTED_LAST['SPY']['close'].pct_change(1)).sum()
    highest_etf_occurance = max(highest_etf_occurance, hashmap_count[symbol_name])
    print(f'hashmap_count {symbol_name}:', hashmap_count[symbol_name])

for key,val in hashmap_count.items():
    if val == highest_etf_occurance:
        highest_etf_occurance_symbol = key

highest_etf_occurance_symbol_contract = Stock(symbol=highest_etf_occurance_symbol, exchange='SMART', currency='USD')
ib.qualifyContracts(highest_etf_occurance_symbol_contract)

while True:
    tz = timezone('EST')
    current_time_str = datetime.datetime.now(tz).strftime('%H:%M:%S')
    current_time_datetime = datetime.datetime.strptime(current_time_str, '%H:%M:%S')
    placeOrder_time_datetime = datetime.datetime.strptime('15:59:00', '%H:%M:%S')

    if current_time_datetime >= placeOrder_time_datetime:
        live_data = ib.reqHistoricalData(contract,
                                        endDateTime='',
                                        durationStr='1 D',
                                        barSizeSetting='5 secs',
                                        whatToShow='TRADES',
                                        useRTH=True,
                                        formatDate=1,
                                        keepUpToDate=True, 
                                        chartOptions=[], 
                                        timeout=60)
        
        nlv = float([v.value for v in ib.accountValues() if v.tag == 'NetLiquidationByCurrency' and v.currency == 'BASE'][0])
        qty = nlv//live_data[-1].open

        if live_data[-1].close <= -0.018:
            mktBuyOrder = Order(action="BUY", totalQuantity=qty, orderType="MKT",tif="DAY",outsideRth=False)
            mktBuyOrder_trade = ib.placeOrder(contract, mktBuyOrder)
            print(mktBuyOrder_trade.log)
            print(mktBuyOrder_trade.orderStatus.status)
        elif live_data[-1].close >= 0.018:
            mktSellOrder = Order(action="Sell", totalQuantity=qty, orderType="MKT",tif="DAY",outsideRth=False)
            mktSellOrder_trade = ib.placeOrder(contract, mktSellOrder)
            print(mktSellOrder_trade.log)
            print(mktSellOrder_trade.orderStatus.status)
