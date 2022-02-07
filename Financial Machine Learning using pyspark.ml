# Databricks notebook source
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler

import numpy as np
import pandas as pd

# COMMAND ----------

data = spark.read.format("delta").load("/user/hive/warehouse/dataset_delta")

data = data.select("spy_adjClose","xlb_adjClose","xlv_adjClose","xlc_adjClose","xlk_adjClose","xlf_adjClose","xlp_adjClose","xli_adjClose","xlu_adjClose","xly_adjClose","xlre_adjClose","xle_adjClose")

data = data.dropna()

features =   ("spy_adjClose","xlb_adjClose","xlv_adjClose","xlc_adjClose","xlk_adjClose","xlf_adjClose","xlp_adjClose","xli_adjClose","xlu_adjClose","xly_adjClose","xlre_adjClose","xle_adjClose")      

assemble = VectorAssembler(inputCols = features, outputCol = 'features')

assembled_data = assemble.transform(data)

assembled_data.show()

# COMMAND ----------

scale=StandardScaler(inputCol='features',outputCol='standardized')

data_scale=scale.fit(assembled_data)

data_scale_output=data_scale.transform(assembled_data)

data_scale_output.show(2)

# COMMAND ----------

silhouette_score=[]
evaluator = ClusteringEvaluator(predictionCol='prediction', featuresCol='standardized', \
                                metricName='silhouette', distanceMeasure='squaredEuclidean')

for i in range(2,30):
    
    KMeans_algo=KMeans(featuresCol='standardized', k=i)
    
    KMeans_fit=KMeans_algo.fit(data_scale_output)
    
    output=KMeans_fit.transform(data_scale_output)
    
    
    
    score=evaluator.evaluate(output)
    
    silhouette_score.append(score)
    
    print("Silhouette Score:",score)

# COMMAND ----------

#Visualizing the silhouette scores in a plot

fig, ax = plt.subplots(1,1, figsize =(8,6))
ax.plot(range(2,30),silhouette_score)
ax.set_xlabel('k')
ax.set_ylabel('cost')