# Databricks notebook source
import mlflow
import numpy as np
import pandas as pd
import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection
import sklearn.ensemble
from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql import functions
import pyspark.sql.functions #import avg, col, udf
from pyspark.sql import SQLContext
from pyspark.sql import DataFrame
from pyspark.sql.types import *

import json
import urllib3
import chardet

#import urllib.request
#import chardet
#from urllib.parse import unquote
import requests


# COMMAND ----------

sc = spark.sparkContext

# COMMAND ----------

"""

#Tiingo SPY
urlfile_spy = requests.get("https://api.tiingo.com/tiingo/daily/spy/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily")

csv_rdd = sc.parallelize(urlfile_spy)

df_spy_csv_rdd = spark.read.csv(csv_rdd)

display(df_spy_csv_rdd)

"""

# COMMAND ----------

#Tiingo SPY
spy_url ="https://api.tiingo.com/tiingo/daily/spy/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_spy = spark.createDataFrame(pd.read_csv(spy_url))

#Tiingo XLB
xlb_url ="https://api.tiingo.com/tiingo/daily/xlb/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xlb = spark.createDataFrame(pd.read_csv(xlb_url))

#Tiingo XLV
xlv_url ="https://api.tiingo.com/tiingo/daily/xlv/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xlv = spark.createDataFrame(pd.read_csv(xlv_url))

#Tiingo XLC
xlc_url ="https://api.tiingo.com/tiingo/daily/xlc/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xlc = spark.createDataFrame(pd.read_csv(xlc_url))

#Tiingo XLK
xlk_url ="https://api.tiingo.com/tiingo/daily/xlk/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xlk = spark.createDataFrame(pd.read_csv(xlk_url))

#Tiingo XLF
xlf_url ="https://api.tiingo.com/tiingo/daily/xlf/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xlf = spark.createDataFrame(pd.read_csv(xlf_url))

#Tiingo XLP
xlp_url ="https://api.tiingo.com/tiingo/daily/xlp/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xlp = spark.createDataFrame(pd.read_csv(xlp_url))

#Tiingo XLI
xli_url ="https://api.tiingo.com/tiingo/daily/xli/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xli = spark.createDataFrame(pd.read_csv(xli_url))

#Tiingo XLU
xlu_url ="https://api.tiingo.com/tiingo/daily/xlu/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xlu = spark.createDataFrame(pd.read_csv(xlu_url))

#Tiingo XLY
xly_url ="https://api.tiingo.com/tiingo/daily/xly/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xly = spark.createDataFrame(pd.read_csv(xly_url))

#Tiingo XLRE
xlre_url ="https://api.tiingo.com/tiingo/daily/xlre/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xlre = spark.createDataFrame(pd.read_csv(xlre_url))
display(df_xlre)

#Tiingo XLE
xle_url ="https://api.tiingo.com/tiingo/daily/xle/prices?startDate=2005-1-1&endDate=2021-12-31&token=ff008f598182931d7eb1f0b03600aebb4feeb732&format=csv&resampleFreq=daily"

df_xle = spark.createDataFrame(pd.read_csv(xle_url))

#CBOE VIX
vix_url ="https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"

df_vix = spark.createDataFrame(pd.read_csv(vix_url))

#US Daily News Index
#Reference: https://www.policyuncertainty.com/us_monthly.html
all_daily_policy_data_url ="https://www.policyuncertainty.com/media/All_Daily_Policy_Data.csv"

df_all_daily_policy_data = spark.createDataFrame(pd.read_csv(all_daily_policy_data_url))

# COMMAND ----------


#Detect encoding type
"""

ads_url = "https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/ads/ads_index_most_current_vintage.xlsx?la=en&hash=6DF4E54DFAE3EDC347F80A80142338E7"

rawdata = urllib.request.urlopen(ads_url).read()

chardet.detect(rawdata)

"""

# COMMAND ----------

#Create Dataframe for .xlsx URL data

#Aruoba-Diebold-Scotti Business Conditions Index (ADS)
ads_url = "https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/ads/ads_index_most_current_vintage.xlsx?la=en&hash=6DF4E54DFAE3EDC347F80A80142338E7"

ads_url_r = requests.get(ads_url)
open('ads_index_most_current_vintage.xlsx?la=en&hash=6DF4E54DFAE3EDC347F80A80142338E7', 'wb').write(ads_url_r.content)

df_ads = spark.createDataFrame(pd.read_excel('ads_index_most_current_vintage.xlsx?la=en&hash=6DF4E54DFAE3EDC347F80A80142338E7'))
display(df_ads)

# COMMAND ----------

#Reference: https://sparkbyexamples.com/spark/rename-a-column-on-spark-dataframes/


#Rename SPY columns
df_spy_new = df_spy.withColumnRenamed("close", "spy_close").withColumnRenamed("high", "spy_high").withColumnRenamed("low", "spy_low").withColumnRenamed("open", "spy_open").withColumnRenamed("volume", "spy_volume").withColumnRenamed("adjClose", "spy_adjClose").withColumnRenamed("adjHigh", "spy_adjHigh").withColumnRenamed("adjLow", "spy_adjLow").withColumnRenamed("adjOpen", "spy_adjOpen").withColumnRenamed("adjVolume", "spy_adjVolume").withColumnRenamed("divCash", "spy_divCash").withColumnRenamed("splitFactor", "spy_splitFactor")

df_spy_new.show()

#Rename XLB columns
df_xlb_new = df_xlb.withColumnRenamed("close", "xlb_close").withColumnRenamed("high", "xlb_high").withColumnRenamed("low", "xlb_low").withColumnRenamed("open", "xlb_open").withColumnRenamed("volume", "xlb_volume").withColumnRenamed("adjClose", "xlb_adjClose").withColumnRenamed("adjHigh", "xlb_adjHigh").withColumnRenamed("adjLow", "xlb_adjLow").withColumnRenamed("adjOpen", "xlb_adjOpen").withColumnRenamed("adjVolume", "xlb_adjVolume").withColumnRenamed("divCash", "xlb_divCash").withColumnRenamed("splitFactor", "xlb_splitFactor")

#Rename XLV columns
df_xlv_new = df_xlv.withColumnRenamed("close", "xlv_close").withColumnRenamed("high", "xlv_high").withColumnRenamed("low", "xlv_low").withColumnRenamed("open", "xlv_open").withColumnRenamed("volume", "xlv_volume").withColumnRenamed("adjClose", "xlv_adjClose").withColumnRenamed("adjHigh", "xlv_adjHigh").withColumnRenamed("adjLow", "xlv_adjLow").withColumnRenamed("adjOpen", "xlv_adjOpen").withColumnRenamed("adjVolume", "xlv_adjVolume").withColumnRenamed("divCash", "xlv_divCash").withColumnRenamed("splitFactor", "xlv_splitFactor")

#Rename XLC columns
df_xlc_new = df_xlc.withColumnRenamed("close", "xlc_close").withColumnRenamed("high", "xlc_high").withColumnRenamed("low", "xlc_low").withColumnRenamed("open", "xlc_open").withColumnRenamed("volume", "xlc_volume").withColumnRenamed("adjClose", "xlc_adjClose").withColumnRenamed("adjHigh", "xlc_adjHigh").withColumnRenamed("adjLow", "xlc_adjLow").withColumnRenamed("adjOpen", "xlc_adjOpen").withColumnRenamed("adjVolume", "xlc_adjVolume").withColumnRenamed("divCash", "xlc_divCash").withColumnRenamed("splitFactor", "xlc_splitFactor")

#Rename XLK columns
df_xlk_new = df_xlk.withColumnRenamed("close", "xlk_close").withColumnRenamed("high", "xlk_high").withColumnRenamed("low", "xlk_low").withColumnRenamed("open", "xlk_open").withColumnRenamed("volume", "xlk_volume").withColumnRenamed("adjClose", "xlk_adjClose").withColumnRenamed("adjHigh", "xlk_adjHigh").withColumnRenamed("adjLow", "xlk_adjLow").withColumnRenamed("adjOpen", "xlk_adjOpen").withColumnRenamed("adjVolume", "xlk_adjVolume").withColumnRenamed("divCash", "xlk_divCash").withColumnRenamed("splitFactor", "xlk_splitFactor")

#Rename XLF columns
df_xlf_new = df_xlf.withColumnRenamed("close", "xlf_close").withColumnRenamed("high", "xlf_high").withColumnRenamed("low", "xlf_low").withColumnRenamed("open", "xlf_open").withColumnRenamed("volume", "xlf_volume").withColumnRenamed("adjClose", "xlf_adjClose").withColumnRenamed("adjHigh", "xlf_adjHigh").withColumnRenamed("adjLow", "xlf_adjLow").withColumnRenamed("adjOpen", "xlf_adjOpen").withColumnRenamed("adjVolume", "xlf_adjVolume").withColumnRenamed("divCash", "xlf_divCash").withColumnRenamed("splitFactor", "xlf_splitFactor")

#Rename XLP columns
df_xlp_new = df_xlp.withColumnRenamed("close", "xlp_close").withColumnRenamed("high", "xlp_high").withColumnRenamed("low", "xlp_low").withColumnRenamed("open", "xlp_open").withColumnRenamed("volume", "xlp_volume").withColumnRenamed("adjClose", "xlp_adjClose").withColumnRenamed("adjHigh", "xlp_adjHigh").withColumnRenamed("adjLow", "xlp_adjLow").withColumnRenamed("adjOpen", "xlp_adjOpen").withColumnRenamed("adjVolume", "xlp_adjVolume").withColumnRenamed("divCash", "xlp_divCash").withColumnRenamed("splitFactor", "xlp_splitFactor")

#Rename XLI columns
df_xli_new = df_xli.withColumnRenamed("close", "xli_close").withColumnRenamed("high", "xli_high").withColumnRenamed("low", "xli_low").withColumnRenamed("open", "xli_open").withColumnRenamed("volume", "xli_volume").withColumnRenamed("adjClose", "xli_adjClose").withColumnRenamed("adjHigh", "xli_adjHigh").withColumnRenamed("adjLow", "xli_adjLow").withColumnRenamed("adjOpen", "xli_adjOpen").withColumnRenamed("adjVolume", "xli_adjVolume").withColumnRenamed("divCash", "xli_divCash").withColumnRenamed("splitFactor", "xli_splitFactor")

#Rename XLU columns
df_xlu_new = df_xlu.withColumnRenamed("close", "xlu_close").withColumnRenamed("high", "xlu_high").withColumnRenamed("low", "xlu_low").withColumnRenamed("open", "xlu_open").withColumnRenamed("volume", "xlu_volume").withColumnRenamed("adjClose", "xlu_adjClose").withColumnRenamed("adjHigh", "xlu_adjHigh").withColumnRenamed("adjLow", "xlu_adjLow").withColumnRenamed("adjOpen", "xlu_adjOpen").withColumnRenamed("adjVolume", "xlu_adjVolume").withColumnRenamed("divCash", "xlu_divCash").withColumnRenamed("splitFactor", "xlu_splitFactor")

#Rename XLY columns
df_xly_new = df_xly.withColumnRenamed("close", "xly_close").withColumnRenamed("high", "xly_high").withColumnRenamed("low", "xly_low").withColumnRenamed("open", "xly_open").withColumnRenamed("volume", "xly_volume").withColumnRenamed("adjClose", "xly_adjClose").withColumnRenamed("adjHigh", "xly_adjHigh").withColumnRenamed("adjLow", "xly_adjLow").withColumnRenamed("adjOpen", "xly_adjOpen").withColumnRenamed("adjVolume", "xly_adjVolume").withColumnRenamed("divCash", "xly_divCash").withColumnRenamed("splitFactor", "xly_splitFactor")

#Rename XLRE columns
df_xlre_new = df_xlre.withColumnRenamed("close", "xlre_close").withColumnRenamed("high", "xlre_high").withColumnRenamed("low", "xlre_low").withColumnRenamed("open", "xlre_open").withColumnRenamed("volume", "xlre_volume").withColumnRenamed("adjClose", "xlre_adjClose").withColumnRenamed("adjHigh", "xlre_adjHigh").withColumnRenamed("adjLow", "xlre_adjLow").withColumnRenamed("adjOpen", "xlre_adjOpen").withColumnRenamed("adjVolume", "xlre_adjVolume").withColumnRenamed("divCash", "xlre_divCash").withColumnRenamed("splitFactor", "xlre_splitFactor")

display(df_xlre_new)
print(df_xlre_new.select("date").dtypes)

#Rename XLE columns
df_xle_new = df_xle.withColumnRenamed("close", "xle_close").withColumnRenamed("high", "xle_high").withColumnRenamed("low", "xle_low").withColumnRenamed("open", "xle_open").withColumnRenamed("volume", "xle_volume").withColumnRenamed("adjClose", "xle_adjClose").withColumnRenamed("adjHigh", "xle_adjHigh").withColumnRenamed("adjLow", "xle_adjLow").withColumnRenamed("adjOpen", "xle_adjOpen").withColumnRenamed("adjVolume", "xle_adjVolume").withColumnRenamed("divCash", "xle_divCash").withColumnRenamed("splitFactor", "xle_splitFactor")

#Rename CBOE VIX columns
df_vix_new = df_vix.withColumnRenamed("DATE", "date").withColumnRenamed("CLOSE", "vix_close").withColumnRenamed("HIGH", "vix_high").withColumnRenamed("LOW", "vix_low").withColumnRenamed("OPEN", "vix_open")

#Rename Aruoba-Diebold-Scotti Business Conditions Index (ADS) columns
df_ads_new = df_ads.withColumnRenamed("Unnamed: 0", "date").withColumnRenamed("ADS_Index", "ads_close")
display(df_ads_new)

print(df_ads_new.select("date").dtypes)

# COMMAND ----------

#Combine ETFs Columns
#Reference: https://sparkbyexamples.com/pyspark/pyspark-join-explained-with-examples/

df_combine_etf_columns = df_spy_new.join(df_xlb_new, ['date'], "full").join(df_xlv_new, ['date'], "full").join(df_xlc_new, ['date'], "full").join(df_xlk_new, ['date'], "full").join(df_xlf_new, ['date'], "full").join(df_xlp_new, ['date'], "full").join(df_xli_new, ['date'], "full").join(df_xlu_new, ['date'], "full").join(df_xly_new, ['date'], "full").join(df_xlre_new, ['date'], "full").join(df_xle_new, ['date'], "full")

df_combine_etf_columns_new = df_combine_etf_columns.sort("date")

display(df_combine_etf_columns_new.tail(100))

# COMMAND ----------

df_spy_new.write.format("delta").mode("overwrite").saveAsTable("spy_delta")
df_xlb_new.write.format("delta").mode("overwrite").saveAsTable("xlb_delta")
df_xlv_new.write.format("delta").mode("overwrite").saveAsTable("xlv_delta")
df_xlc_new.write.format("delta").mode("overwrite").saveAsTable("xlc_delta")
df_xlk_new.write.format("delta").mode("overwrite").saveAsTable("xlk_delta")
df_xlf_new.write.format("delta").mode("overwrite").saveAsTable("xlf_delta")
df_xlp_new.write.format("delta").mode("overwrite").saveAsTable("xlp_delta")
df_xli_new.write.format("delta").mode("overwrite").saveAsTable("xli_delta")
df_xlu_new.write.format("delta").mode("overwrite").saveAsTable("xlu_delta")
df_xly_new.write.format("delta").mode("overwrite").saveAsTable("xly_delta")
df_xlre_new.write.format("delta").mode("overwrite").saveAsTable("xlre_delta")
df_xle_new.write.format("delta").mode("overwrite").saveAsTable("xle_delta")
df_xle_new.write.format("delta").mode("overwrite").saveAsTable("xle_delta")

df_vix_new.write.format("delta").mode("overwrite").saveAsTable("vix_delta")
df_ads_new.write.format("delta").mode("overwrite").saveAsTable("ads_delta")

#spark.sql("select * from xle_delta").show()
display(spark.sql('DESCRIBE ads_delta'))