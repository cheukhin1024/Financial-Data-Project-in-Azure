#After we approve  your application, you can use Azure databricks to view or download data from Delta Lake.

from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql import functions
import pyspark.sql.functions #import avg, col, udf
from pyspark.sql import SQLContext
from pyspark.sql import DataFrame
from pyspark.sql.types import *

#After displaying the Spark Dataframe, you can press "Download" button.
display(spark.sql('SELECT * FROM aal_30mins_delta'))
display(spark.sql('SELECT * FROM aa_30mins_delta'))
display(spark.sql('SELECT * FROM aapl_30mins_delta'))
display(spark.sql('SELECT * FROM a_30mins_delta'))
