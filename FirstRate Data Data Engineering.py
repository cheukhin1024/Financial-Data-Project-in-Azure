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
path_1min = '/dbfs/FileStore/tables/FirstRate1min'
filename_lists_1min = os.listdir(path_1min)

df_1min_ = {}
delta_1min ={}

for filename_1min in os.listdir(path_1min):
    
    #split file name
    name_1min = filename_1min.split('_')[0]
    
    #create clolumn header names
    temp_1min = StructType([StructField(name_1min+"_date/time", StringType(), True),StructField(name_1min+"_adjOpen", FloatType(), True),StructField(name_1min+"_adjHigh", FloatType(), True),StructField(name_1min+"_adjLow", FloatType(), True),StructField(name_1min+"_adjClose", FloatType(), True),StructField(name_1min+"_adjVolume", IntegerType(), True)])
    
    #list and create csv dataframes
    temp_df_1min = spark.read.format("csv").option("header", "false").schema(temp_1min).load("/FileStore/tables/FirstRate1min/"+filename_1min)
    
    #name each dataframes
    df_1min_[name_1min] = temp_df_1min
    
    #name each table
    table_name_1min = name_1min+'_1min_delta'
    
    #create delta lake for each dataframes
    df_1min_[name_1min].write.format("delta").mode("overwrite").saveAsTable(table_name_1min)
    
display(df_1min_['AAL'])

display(spark.sql('SELECT * FROM aal_1min_delta'))

# COMMAND ----------

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
path_30mins = '/dbfs/FileStore/tables/FirstRate30mins'
filename_lists_30mins = os.listdir(path_30mins)

df_30mins_ = {}
delta_30mins ={}

for filename_30mins in os.listdir(path_30mins):
    
    #split file name
    name_30mins = filename_30mins.split('_')[0]
    
    #create clolumn header names
    temp_30mins = StructType([StructField(name_30mins+"_date/time", StringType(), True),StructField(name_30mins+"_adjOpen", FloatType(), True),StructField(name_30mins+"_adjHigh", FloatType(), True),StructField(name_30mins+"_adjLow", FloatType(), True),StructField(name_30mins+"_adjClose", FloatType(), True),StructField(name_30mins+"_adjVolume", IntegerType(), True)])
    
    #list and create csv dataframes
    temp_df_30mins = spark.read.format("csv").option("header", "false").schema(temp_30mins).load("/FileStore/tables/FirstRate30mins/"+filename_30mins)
    
    #name each dataframes
    df_30mins_[name_30mins] = temp_df_30mins
    
    #name each table
    table_name_30mins = name_30mins+'_30mins_delta'
    
    #create delta lake for each dataframes
    df_30mins_[name_30mins].write.format("delta").mode("overwrite").saveAsTable(table_name_30mins)
    
display(df_30mins_['AAL'])

display(spark.sql('SELECT * FROM aal_30mins_delta'))

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
path_remove = "/dbfs/FileStore/tables/FirstRate30mins_Delisted"

for filename_remove in os.listdir(path_remove):
   #if os.stat(filename_delisted).st_size == 0:
   #print(f'File {filename_delisted.split("_")[0]} is empty') 
    dbutils.fs.rm("/FileStore/tables/FirstRate30mins_Delisted" + filename_remove)

# COMMAND ----------

# MAGIC %fs
# MAGIC 
# MAGIC ls /FileStore/tables/FirstRate30mins_Delisted/

# COMMAND ----------

dbutils.fs.rm("/FileStore/tables/FirstRate1min/BBY_1min-1.txt")


# COMMAND ----------

display(spark.table('default.a_1min_delta').orderBy('A_date/time'))

# COMMAND ----------

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