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
# MAGIC 
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
#Data written to mount point paths ( /mnt ) is stored outside of the DBFS root
path_30min = '/dbfs/mnt/finance/FirstRate30min'
filename_lists_30min = os.listdir(path_30min)

df_30min_ = {}
delta_30min = {}

for filename_30min in os.listdir(path_30min):
    
    #split file name
    rawname_30min = filename_30min.split('_')[0]
    name_30min = rawname_30min.split('-')[0]
    
    #create clolumn header names
    temp_30min = StructType([StructField(name_30min+"_dateTime", StringType(), True),StructField(name_30min+"_adjOpen", FloatType(), True),StructField(name_30min+"_adjHigh", FloatType(), True),StructField(name_30min+"_adjLow", FloatType(), True),StructField(name_30min+"_adjClose", FloatType(), True),StructField(name_30min+"_adjVolume", IntegerType(), True)])
    
    #list and create csv dataframes
    temp_df_30min = spark.read.format("csv").option("header", "false").schema(temp_30min).load("/mnt/finance/FirstRate30min/"+filename_30min).withColumn("Ticker", lit(name_30min))
    
    #name each dataframes
    df_30min_[name_30min] = temp_df_30min
    
    #name each table
    table_name_30min = name_30min+'_30min_delta'
    
    print(table_name_30min)
    
    #create delta lake for each dataframes
    df_30min_[name_30min].write.format("delta").mode("overwrite").option("overwriteSchema","True").saveAsTable(table_name_30min)