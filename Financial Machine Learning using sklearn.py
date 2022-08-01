# Databricks notebook source
#Example: https://databricks.com/notebooks/segment-p13n//sg_03_clustering.html

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.pipeline import make_pipeline
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.model_selection import train_test_split
from scipy.cluster.hierarchy import dendrogram, set_link_color_palette
 
import os

from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions
from pyspark.sql.functions import * #import avg, col, udf
from pyspark.sql import SQLContext
from pyspark.sql import DataFrame
from pyspark.sql.types import *
import json

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors
import seaborn as sns
 
import databricks.koalas as ks

import numpy as np
import pyspark.pandas as ps

import mlflow.sklearn

# COMMAND ----------

spark.sql("set spark.databricks.delta.autoCompact.enabled = true")

# COMMAND ----------

#data = spark.select('Ticker').where("Ticker like '%30min'")

#data = spark.sql(" SELECT A_adjClose, AA_adjClose, AAL_adjClose, AAP_adjClose, AAPL_adjClose, ABBV_adjClose, ABC_adjClose, ABMD_adjClose, ABT_adjClose, ACN_adjClose, ACV_adjClose FROM deltabase.a_30min_delta, deltabase.aa_30min_delta, deltabase.aal_30min_delta, deltabase.aap_30min_delta ,deltabase.aapl_30min_delta ,deltabase.abbv_30min_delta ,deltabase.abc_30min_delta , deltabase.abmd_30min_delta, deltabase.abt_30min_delta, deltabase.acn_30min_delta, deltabase.acv_30min_delta ORDER BY A_dateTime")

data = spark.sql("select A_adjClose, AA_adjClose from deltabase.a_30min_delta FULL JOIN deltabase.aa_30min_delta ON A_dateTime == AA_dateTime")

display(data)

# COMMAND ----------

spark.conf.set("spark.sql.execution.arrow.enabled", "true")

#https://cumsum.wordpress.com/2021/03/05/pandas-attributeerror-function-object-has-no-attribute-xxx/
data_pd = data.pandas_api()

# COMMAND ----------

data_pd_pct = data_pd.pct_change()

display(data_pd_pct)


# COMMAND ----------

mlflow.sklearn.autolog()

with mlflow.start_run():

silhouette_avg = []

for num_clusters in range(1,20):
# create a K-means model with 10 clusters
initial_model = KMeans(n_clusters=num_clusters)

init_clusters = initial_model.fit(data_pd_pct)

cluster_labels = kmeans.labels_

# combine households with cluster assignments
labeled_df_pct = (
  pd.concat( 
    [data_pd_pct, pd.DataFrame(init_clusters,columns=['cluster'])],
    axis=1
    )
  )
 
# visualize cluster assignments
fig, ax = plt.subplots(figsize=(10,8))
sns.scatterplot(
  data=labeled_df_pct,
  x='Dim_1',
  y='Dim_2',
  hue='cluster',
  palette=[cm.nipy_spectral(float(i) / initial_n) for i in range(initial_n)],
  legend='brief',
  alpha=0.5,
  ax = ax
  )
_ = ax.legend(loc='lower right', ncol=1, fancybox=True)