# Databricks notebook source
#Mount an Azure Blob storage container
dbutils.fs.mount(
  source = "wasbs://finance@finstorage6ef5xpkr7mo3s.blob.core.windows.net",
  mount_point = "/mnt/finance",  
  extra_configs = {"fs.azure.account.key.finstorage6ef5xpkr7mo3s.blob.core.windows.net":dbutils.secrets.get(scope = "finstorage6ef5xpkr7mo3skey", key = "finstorage6ef5xpkr7mo3skey")})

# COMMAND ----------

#Unmount a mount point
#dbutils.fs.unmount("/mnt/finance")

# COMMAND ----------

# MAGIC %sql
# MAGIC USE DATABASE deltabase
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

# COMMAND ----------

df_30min_[name_30min].write.format("delta").mode("overwrite").option("overwriteSchema","True").saveAsTable(table_name_30min)

# COMMAND ----------

import os
#import glob 
import numpy as np
import pandas as pd

from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql import functions
import pyspark.sql.functions #import avg, col, udf
from pyspark.sql import SQLContext
from pyspark.sql import DataFrame
from pyspark.sql.types import *
import json

#LIST, RENAME, AND SAVE ALL FILES AS DELTA LAKE AUTOMATICALLY

df_30mins_delisted_ = {}
_delisted_delta ={}

path_delisted = "/dbfs/FileStore/tables/FirstRate30mins_Delisted"

for filename_delisted in os.listdir(path_delisted):
    
    name_delisted = filename_delisted.split('_')[0]
    
    temp_delisted = StructType([StructField(name_delisted+"_date/time", StringType(), True),StructField(name_delisted+"_adjOpen", FloatType(), True),StructField(name_delisted+"_adjHigh", FloatType(), True),StructField(name_delisted+"_adjLow", FloatType(), True),StructField(name_delisted+"_adjClose", FloatType(), True),StructField(name_delisted+"_adjVolume", IntegerType(), True)])
    
    temp_df_delisted = spark.read.format("csv").option("header", "false").schema(temp_delisted).load("/FileStore/tables/FirstRate30mins_Delisted/"+filename_delisted)
    
    #name each dataframes
    df_30mins_delisted_[name_delisted] = temp_df_delisted
    
    print(df_30mins_delisted_[name_delisted])
    
    #name each table
    table_name_delisted = name_delisted+'_30mins_delisted_delta'
    
    #create delta lake for each dataframes
    df_30mins_delisted_[name_delisted].write.format("delta").mode("overwrite").saveAsTable(table_name_delisted)

display(df_30mins_delisted_['AABA'])
display(spark.sql('SELECT * FROM aaba_30mins_delisted_delta'))