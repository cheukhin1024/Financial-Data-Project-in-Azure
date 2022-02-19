# Databricks notebook source
import os
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
path = '/dbfs/FileStore/tables/FirstRate30mins'
filename_lists = os.listdir(path)

df_30mins_ = {}
_delta ={}

for filename in os.listdir(path):
    #split file name
    name = filename.split('_')[0]
    #create clolumn header names
    temp = StructType([StructField(name+"_date/time", StringType(), True),StructField(name+"_adjOpen", FloatType(), True),StructField(name+"_adjHigh", FloatType(), True),StructField(name+"_adjLow", FloatType(), True),StructField(name+"_adjClose", FloatType(), True),StructField(name+"_adjVolume", IntegerType(), True)])
    
    #list and create csv dataframes
    temp_df = spark.read.format("csv").option("header", "false").schema(temp).load("/FileStore/tables/FirstRate30mins/"+filename)
    
    #name each dataframes
    df_30mins_[name] = temp_df
    
    #name each table
    table_name = name+'_30mins_delta'
    
    #create delta lake for each dataframes
    df_30mins_[name].write.format("delta").mode("overwrite").saveAsTable(table_name)
    
display(df_30mins_['AAL'])
display(df_30mins_['AAPL'])
display(df_30mins_['AA'])
display(df_30mins_['A'])

display(spark.sql('SELECT * FROM aal_30mins_delta'))
display(spark.sql('SELECT * FROM aa_30mins_delta'))
display(spark.sql('SELECT * FROM aapl_30mins_delta'))
display(spark.sql('SELECT * FROM a_30mins_delta'))

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
display(df_30mins_delisted_['ABI'])
 
display(spark.sql('SELECT * FROM aaba_30mins_delisted_delta'))
display(spark.sql('SELECT * FROM abi_30mins_delisted_delta'))
display(spark.sql('SELECT * FROM aet_30mins_delisted_delta'))
display(spark.sql('SELECT * FROM yhoo_30mins_delisted_delta'))

# COMMAND ----------

import os
# check if size of file is 0

for filename_delisted in os.listdir(path_delisted):
    if os.stat(filename_delisted).st_size == 0:
        print(f'File {filename_delisted.split("_")[0]} is empty')
        dbutils.fs.rm("/FileStore/tables/FirstRate30mins_Delisted/" + filename_delisted)

# COMMAND ----------

ABI_30min_spark_DF_newRow = StructType([StructField("ABI_date/time", StringType(), True),StructField("ABI_adjOpen", FloatType(), True),StructField("ABI_adjHigh", FloatType(), True),StructField("ABI_adjLow", FloatType(), True),StructField("ABI_adjClose", FloatType(), True),StructField("ABI_adjVolume", IntegerType(), True)])
ABI_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(ABI_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins_Delisted/ABI_DELISTED_30min.txt")
display(ABI_30min_spark_DF)

ABI_30min_spark_DF.write.format("delta").mode("overwrite").saveAsTable("ABI_30mins_delisted_delta")
display(spark.sql('SELECT * FROM abi_30mins_delisted_delta'))

# COMMAND ----------

"""

import os
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

import databricks.koalas as ks 
import seaborn as sns 

AAPL_30min_spark_DF_newRow = StructType([StructField("AAPL_date/time", StringType(), True),StructField("AAPL_adjOpen", FloatType(), True),StructField("AAPL_adjHigh", FloatType(), True),StructField("AAPL_adjLow", FloatType(), True),StructField("AAPL_adjClose", FloatType(), True),StructField("AAPL_adjVolume", IntegerType(), True)])

AAPL_30min_spark_DF = spark.read.format("csv").option("header", "false").schema(AAPL_30min_spark_DF_newRow).load("/FileStore/tables/FirstRate30mins/AAPL_30min.txt")

display(AAPL_30min_spark_DF)

AAPL_30min_koalas_DF = ks.DataFrame(AAPL_30min_spark_DF)

AAPL_30min_koalas_DF.head()

#AAPL_30min_koalas_DF.AAPL_adjCLose.sort_index().pct_change(periods=1)
ks.set_option('compute.ops_on_diff_frames', True)
AAPL_30min_koalas_DF_pct = AAPL_30min_koalas_DF['AAPL_adjClose'] .sort_index().pct_change(periods=1)

AAPL_30min_koalas_DF.sort_index().head()

AAPL_30min_koalas_DF_new = ks.concat([AAPL_30min_koalas_DF, AAPL_30min_koalas_DF_pct])
AAPL_30min_koalas_DF_new.head()

"""