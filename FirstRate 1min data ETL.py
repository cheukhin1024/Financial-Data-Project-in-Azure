# Databricks notebook source
#Mount an Azure Blob storage container
dbutils.fs.mount(
  source = "wasbs://finance@finstorage6ef5xpkr7mo3s.blob.core.windows.net",
  mount_point = "/mnt/finance",  
  extra_configs = {"fs.azure.account.key.finstorage6ef5xpkr7mo3s.blob.core.windows.net":"n1cT5j8fFP+qHHI6ve/K2rWAIT/xf/yrTA19WmMZSneFYKYvHt3ux2KRcvIfqZ365meXDXzAOqMX+AStJdrpEA=="})

# COMMAND ----------

#Unmount a mount point
#dbutils.fs.unmount("/mnt/finance")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS deltabase

# COMMAND ----------

# MAGIC %sql
# MAGIC Use deltabase

# COMMAND ----------

# MAGIC %sql
# MAGIC --Enable Auto Optimization
# MAGIC set spark.databricks.delta.properties.defaults.autoOptimize.optimizeWrite = true;
# MAGIC set spark.databricks.delta.properties.defaults.autoOptimize.autoCompact = true;

# COMMAND ----------

import os
import numpy as np
import pandas as pd

from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions
from pyspark.sql.functions import * #import avg, col, udf
from pyspark.sql import SQLContext
from pyspark.sql import DataFrame
from pyspark.sql.types import *
import json

#LIST, RENAME, AND SAVE ALL FILES AS DELTA LAKE AUTOMATICALLY
path_1min = '/dbfs/mnt/finance/FirstRate1min'
filename_lists_1min = os.listdir(path_1min)

df_1min_ = {}
delta_1min ={}

for filename_1min in os.listdir(path_1min):
    
    #split file name
    rawname_1min = filename_1min.split('_')[0]
    name_1min = rawname_1min.split('-')[0]
    
    #create clolumn header names
    temp_1min = StructType([StructField(name_1min+"_dateTime", StringType(), True),StructField(name_1min+"_adjOpen", FloatType(), True),StructField(name_1min+"_adjHigh", FloatType(), True),StructField(name_1min+"_adjLow", FloatType(), True),StructField(name_1min+"_adjClose", FloatType(), True),StructField(name_1min+"_adjVolume", IntegerType(), True)])
    
    #list and create csv dataframes
    temp_df_1min = spark.read.format("csv").option("header", "false").schema(temp_1min).load("/mnt/finance/FirstRate1min/"+filename_1min).withColumn("Ticker", lit(name_1min))
    
    #name each dataframes
    df_1min_[name_1min] = temp_df_1min
    
    #name each table
    table_name_1min = name_1min+'_1min_delta'
    
    print(table_name_1min)
    
    #create delta lake for each dataframes
    df_1min_[name_1min].write.format("delta").mode("overwrite").option("overwriteSchema","True").saveAsTable(table_name_1min)