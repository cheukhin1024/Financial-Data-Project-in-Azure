# Databricks notebook source
import requests

# COMMAND ----------

from websocket import create_connection
import simplejson as json
ws = create_connection("wss://api.tiingo.com/iex")

subscribe = {
        'eventName':'subscribe',
        'authorization':'ff008f598182931d7eb1f0b03600aebb4feeb732',
        'eventData': {
            'thresholdLevel': 5,
            'tickers': ['SPY', 'AAPL']
    }
}

ws.send(json.dumps(subscribe))
while True:
    print(ws.recv())

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.formatCheck.enabled=false