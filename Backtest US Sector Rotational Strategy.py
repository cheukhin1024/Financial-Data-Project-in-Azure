import pandas as pd
import requests

symbol_list = ['XLB','XLV','XLC','XLK','XLF','XLP','XLI','XLU','XLY','XLRE','XLE']

dict_url = {}
dict_response={}
dict_data ={}

df={}

for symbol in symbol_list:
    dict_url[symbol]  = "https://api.tiingo.com/tiingo/daily/"+symbol+"/prices?startDate=2005-01-03&token=ff008f598182931d7eb1f0b03600aebb4feeb732"

    dict_response[symbol] = requests.get(dict_url[symbol])
    dict_data[symbol] = dict_response[symbol].json()

    dict_date={}
    dict_date[symbol]=[]
    dict_close={}
    dict_close[symbol]=[]
    dict_high={}
    dict_high[symbol]=[]
    dict_low={}
    dict_low[symbol]=[]
    dict_open={}
    dict_open[symbol]=[]
    dict_volume={}
    dict_volume[symbol]=[]
    dict_adjClose={}
    dict_adjClose[symbol]=[]
    dict_adjHigh={}
    dict_adjHigh[symbol]=[]
    dict_adjLow={}
    dict_adjLow[symbol]=[]
    dict_adjOpen={}
    dict_adjOpen[symbol]=[]
    dict_adjVolume={}
    dict_adjVolume[symbol]=[]
    dict_divCash={}
    dict_divCash[symbol]=[]
    dict_splitFactor={}
    dict_splitFactor[symbol]=[]

    # Iterate through each data point
    for item in dict_data[symbol]:
        dict_date[symbol].append(item['date'])
        dict_close[symbol].append(item['close'])
        dict_high[symbol].append(item['high'])
        dict_low[symbol].append(item['low'])
        dict_open[symbol].append(item['open'])
        dict_volume[symbol].append(item['volume'])
        dict_adjClose[symbol].append(item['adjClose'])
        dict_adjHigh[symbol].append(item['adjHigh'])
        dict_adjLow[symbol].append(item['adjLow'])
        dict_adjOpen[symbol].append(item['adjOpen'])
        dict_adjVolume[symbol].append(item['adjVolume'])
        dict_divCash[symbol].append(item['divCash'])
        dict_splitFactor[symbol].append(item['splitFactor'])

    # Create the DataFrame
        df[symbol] = pd.DataFrame({
                            'date': dict_date[symbol],
                            'close': dict_close[symbol],
                            'high': dict_high[symbol],
                            'low': dict_low[symbol],
                            'open': dict_open[symbol],
                            'volume': dict_volume[symbol],
                            'adjClose': dict_adjClose[symbol],
                            'adjHigh': dict_adjHigh[symbol],
                            'adjLow': dict_adjLow[symbol],
                            'adjOpen': dict_adjOpen[symbol],
                            'adjVolume': dict_adjVolume[symbol],
                            'divCash': dict_divCash[symbol],
                            'splitFactor': dict_splitFactor[symbol]
                                    })

    # Display the first few rows of the DataFrame
    print(df[symbol].head())
    print(df[symbol].tail())
