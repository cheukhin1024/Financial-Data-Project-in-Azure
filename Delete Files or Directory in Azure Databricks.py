# Databricks notebook source


import os
# check if size of file is 0
path_remove = "/dbfs/user/hive/warehouse"

for filename_remove in os.listdir(path_remove):
   #Delete file if the file is empty
    if os.stat(filename_delisted).st_size == 0:
   #print(f'File {filename_delisted.split("_")[0]} is empty') 
    dbutils.fs.rm("/dbfs/user/hive/warehouse/" + filename_remove)
    
    
 # COMMAND ----------   
    
    
    
    
#Delete directory    
dbutils.fs.rm("/tmp", True)
    
    
    
    
    
