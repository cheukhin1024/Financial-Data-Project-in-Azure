# Databricks notebook source
import datetime
import time
import requests
import json
from lxml import html
from ib_insync import *

# COMMAND ----------

#util.startLoop()  # uncomment this line when in a notebook

# COMMAND ----------

ib = IB()
ib.connect('10.0.0.4', 7496, clientId=1)

# COMMAND ----------

session = requests.session()

Symbol_arr = []
Company_arr = []
ShortActivist_arr = []
ReleaseDate_arr = []

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9', 'Connection': 'keep-alive', 'Referer': 'https://breakoutpoint.com/',
    'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"', }


def login():
    response = session.get('https://breakoutpoint.com/accounts/login/', headers=headers)
    csrftoken = response.cookies.get_dict()['csrftoken']

    data = {'csrfmiddlewaretoken': csrftoken, 'login': 'cheukhin1024@gmail.com', 'password': 'Christophe24!', }

    response = session.post('https://breakoutpoint.com/accounts/login/', headers=headers, data=data)

    global csrfmiddlewaretoken

    doc = html.fromstring(response.text)
    csrfmiddlewaretoken = doc.xpath('//*[@name="csrfmiddlewaretoken"]/@value')[0].strip()


def get_data():
    global Symbol_arr
    global Company_arr
    global ShortActivist_arr
    global ReleaseDate_arr

    tmp_symbol_lst = []
    tmp_company_lst = []
    tmp_shortactivist_lst = []
    tmp_relase_date_lst = []
    tmp_dict_data = []

    page = 0
    while True:
        data = {'columns[0][data]': '13', 'columns[0][name]': 'symbol', 'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'true', 'columns[0][search][value]': '', 'columns[0][search][regex]': 'false',
            'columns[1][data]': '1', 'columns[1][name]': 'issuer', 'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true', 'columns[1][search][value]': '', 'columns[1][search][regex]': 'false',
            'columns[2][data]': '0', 'columns[2][name]': 'activist', 'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true', 'columns[2][search][value]': '', 'columns[2][search][regex]': 'false',
            'columns[3][data]': '3', 'columns[3][name]': 'release_date', 'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true', 'columns[3][search][value]': '', 'columns[3][search][regex]': 'false',
            'columns[4][data]': '10', 'columns[4][name]': 'campaign_return', 'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true', 'columns[4][search][value]': '', 'columns[4][search][regex]': 'false',
            'columns[5][data]': '16', 'columns[5][name]': 'percent_change_daily ', 'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true', 'columns[5][search][value]': '', 'columns[5][search][regex]': 'false',
            'columns[6][data]': '21', 'columns[6][name]': 'country', 'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'true', 'columns[6][search][value]': '', 'columns[6][search][regex]': 'false',
            'columns[7][data]': '24', 'columns[7][name]': 'region', 'columns[7][searchable]': 'true',
            'columns[7][orderable]': 'true', 'columns[7][search][value]': '', 'columns[7][search][regex]': 'false',
            'columns[8][data]': '25', 'columns[8][name]': 'marketcapinitial', 'columns[8][searchable]': 'true',
            'columns[8][orderable]': 'true', 'columns[8][search][value]': '', 'columns[8][search][regex]': 'false',
            'order[0][column]': '3', 'order[0][dir]': 'desc', 'start': f'{page}', 'length': '20', 'search[value]': '',
            'search[regex]': 'false', 'active_closed': 'L', 'csrfmiddlewaretoken': csrfmiddlewaretoken, }
        response = session.post('https://breakoutpoint.com/activists-shorts/assc/', headers=headers, data=data)
        content = json.loads(response.text)
        try:
            content_data = content['data']
        except:
            content_data = []
        if content_data:
            for data_ in content_data:
                try:
                    symbol_ = data_[13].strip()
                except:
                    symbol_ = ''
                try:
                    Release_date = data_[3].strip()
                except:
                    Release_date = ''
                try:
                    company = data_[1].strip()
                except:
                    company = ''
                try:
                    shortactivist = data_[0].strip()
                except:
                    shortactivist = ''
                if symbol_ == '' and company == '' and shortactivist == '' and Release_date == '':
                    continue

                data = {'symbol_': symbol_, 'Release_date': Release_date, 'company': company,
                        'shortactivist': shortactivist}
                if data not in tmp_dict_data:
                    tmp_dict_data.append(data)
                    tmp_symbol_lst.append(symbol_)
                    tmp_company_lst.append(company)
                    tmp_shortactivist_lst.append(shortactivist)
                    tmp_relase_date_lst.append(Release_date)
            page += 20
        else:
            break

    Symbol_arr = tmp_symbol_lst + Symbol_arr
    Company_arr = tmp_company_lst + Company_arr
    ShortActivist_arr = tmp_shortactivist_lst + ShortActivist_arr
    ReleaseDate_arr = tmp_relase_date_lst + ReleaseDate_arr

placeOrder_Symbol_arr = []
placeOrder_Company_arr = []
placeOrder_ShortActivist_arr = []
placeOrder_ReleaseDate_arr = []

# COMMAND ----------

if __name__ == '__main__':
    login()
    while True:
        print(f'Start: {datetime.datetime.now()}')

        get_data()
        print(placeOrder_Symbol_arr)
        #print(f'Symbol_arr = \n{Symbol_arr}')
        #print(f'Company_arr = \n{Company_arr}')
        #print(f'ShortActivist_arr = \n{ShortActivist_arr}')
        #print(f'ReleaseDate_arr = \n{ReleaseDate_arr}') 
        if Symbol_arr[0] not in placeOrder_Symbol_arr:
            contract = Stock(Symbol_arr[0], 'SMART', 'USD')
            
            ib.qualifyContracts(contract)
            mktSellOrder = Order(action="SELL", totalQuantity=100, orderType="MKT",tif="DAY",outsideRth=False)
            mktSellOrder_trade = ib.placeOrder(contract, mktSellOrder)
            print(mktSellOrder_trade.log)
            print(mktSellOrder_trade.orderStatus.status)
            placeOrder_Symbol_arr.append(Symbol_arr[0])

            ib.qualifyContracts(contract)
            mocBuyOrder = Order(action="BUY", totalQuantity=100, orderType="MOC",tif="DAY",outsideRth=False)
            mocBuyOrder_trade = ib.placeOrder(contract, mocBuyOrder)
            print(mocBuyOrder_trade.log)
            print(mocBuyOrder_trade.orderStatus.status)

        print(f'End: {datetime.datetime.now()}')
        time.sleep(60)