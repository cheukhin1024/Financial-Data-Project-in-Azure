###### Transpose PySpark DataFrame for Apache Spark Distributed System

from pyspark.sql.functions import *
from pyspark.sql import SparkSession

def TransposeDF(df, columns, pivotCol):
    columnsValue = list(map(lambda x: str("'") + str(x) + str("',")  + str(x), columns))
    stackCols = ','.join(x for x in columnsValue)
    df_1 = df.selectExpr(pivotCol, "stack(" + str(len(columns)) + "," + stackCols + ")")\
             .select(pivotCol, "col0", "col1")
    final_df = df_1.groupBy(col("col0")).pivot(pivotCol).agg(concat_ws("", collect_list(col("col1"))))\
                   .withColumnRenamed("col0", pivotCol)
    return final_df

df = TransposeDF(df, df.columns, "AAPL_dateTime")
#df = TransposeDF(df, ColumnList, "Products")

###### Monte Carlo Simulation for Apache Spark Distributed System

import random
import time
from operator import add

#The function generates a random return on the investment, as a percentage, every year for the duration of a specified term. 
#The function takes a seed value as a parameter. 
#This value is used to reseed the random number generator, which ensures that the function doesn't get the same list of random numbers each time it runs. 
#The random.normalvariate function ensures that random values occur across a normal distribution for the specified mean and standard deviation. 
#The function increases the value of the portfolio by the growth amount, which could be positive or negative, and adds a yearly sum that represents further investment.
def grow(seed):
    random.seed(seed)
    portfolio_value = INVESTMENT_INIT
    for i in range(TERM):
        growth = random.normalvariate(MKT_AVG_RETURN, MKT_STD_DEV)
        portfolio_value += portfolio_value * growth + INVESTMENT_ANN
    return portfolio_value

#Create many seeds to feed to the function  
seeds = sc.parallelize([time.time() + i for i in range(10000)])
#Feed the RDD that contains the seeds to the growth function
results = seeds.map(grow)

#Specify some values for the function
INVESTMENT_INIT = 100000  # starting amount
INVESTMENT_ANN = 0  # yearly new investment
TERM = 252  # number of years
MKT_AVG_RETURN = df.select(avg('portfolio_daily_return')) # percentage
MKT_STD_DEV = df.select(stddev ('portfolio_daily_return'))  # standard deviation

#Aggregate the values in the RDD
sum = results.reduce(add)

final_mc = (sum / 10000.)
#Display the average return
print (final_mc)


###### Shapley Additive Explanations (SHAP) for small datasets
import shap

def shap_small():
    explainer = shap.TreeExplainer(clf)
    shap_values = explainer.shap_values(df)
return shap_values


###### Shapley Additive Explanations (SHAP) for Apache Spark Distributed System
# https://www.databricks.com/blog/2022/02/02/scaling-shap-calculations-with-pyspark-and-pandas-udf.html
import shap

def calculate_shap(iterator: Iterator[pd.DataFrame]) -> Iterator[pd.DataFrame]:
    explainer = shap.TreeExplainer(clf)
    shap_values = explainer.shap_values(df)

    for X in iterator:
        yield pd.DataFrame(
            explainer.shap_values(np.array(X), check_additivity=False)[0],
            columns=columns_for_shap_calculation,
        )

return_schema = StructType()
for feature in columns_for_shap_calculation:
    return_schema = return_schema.add(StructField(feature, FloatType()))

shap_values = df.mapInPandas(calculate_shap, schema=return_schema)

#Strike a balance between creating small enough partitions and not so small that the overhead of creating them outweighs the benefits of parallelizing the calculations.
df = df.repartition(sc.defaultParallelism)
