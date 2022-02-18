# Databricks notebook source
#Example: https://databricks.com/notebooks/segment-p13n//sg_03_clustering.html

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.model_selection import train_test_split
from scipy.cluster.hierarchy import dendrogram, set_link_color_palette
 
import os

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors
import seaborn as sns
 
import numpy as np
import pandas as pd
 
import mlflow
import os

# COMMAND ----------

data = spark.read.format("delta").load("/user/hive/warehouse/dataset_delta").select("spy_adjClose","xlb_adjClose","xlv_adjClose","xlc_adjClose","xlk_adjClose","xlf_adjClose","xlp_adjClose","xli_adjClose","xlu_adjClose","xly_adjClose","xlre_adjClose","xle_adjClose")

data = data.dropna()

data_X_pd = data.toPandas()

X = data_X_pd.pct_change(1)

X = X.dropna()


# COMMAND ----------

# initial cluster count
initial_n = 13

# train the model
initial_model = KMeans(
  n_clusters=initial_n,
  max_iter=1000
  )
 
# fit and predict per-household cluster assignment
init_clusters = initial_model.fit_predict(X)
 
# combine households with cluster assignments
labeled_X_pd = (
  pd.concat( 
    [X, pd.DataFrame(init_clusters,columns=['cluster'])],
    axis=1
    )
  )
 
# visualize cluster assignments
fig, ax = plt.subplots(figsize=(10,8))
sns.scatterplot(
  data=labeled_X_pd,
  x='spy_adjClose',
  y='xlb_adjClose',
  hue='cluster',
  palette=[cm.nipy_spectral(float(i) / initial_n) for i in range(initial_n)],
  legend='brief',
  alpha=0.5,
  ax = ax
  )
_ = ax.legend(loc='lower right', ncol=1, fancybox=True)