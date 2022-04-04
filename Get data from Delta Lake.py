# After we approve  your application, you can use Azure databricks to view or download data from Delta Lake.

from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql import functions
import pyspark.sql.functions #import avg, col, udf
from pyspark.sql import SQLContext
from pyspark.sql import DataFrame
from pyspark.sql.types import *


# There are 3 Delta Lake formats in our Azure Databricks.

# For S&P500 components data:

# If you want to get current S&P 500 components 1-minute data, please code: "ticker name" + '_1min_delta'. Example of getting Apple (ticker: AAPL) stock data: aapl_1min_delta.
# If you want to get delisted S&P 500 components 1-minute data, please code: "ticker name" + '_1min_delisted_delta'. Example of getting YAHOO! (ticker: YHOO) stock data: yhoo_1min_delta.

# If you want to get current S&P 500 components 30-minutes data, please code: "ticker name" + '_30mins_delta'. Example of getting Apple (ticker: AAPL) stock data: aapl_30mins_delta.
# If you want to get delisted S&P 500 components 30-minutes data, please code: "ticker name" + '_30mins_delisted_delta'. Example of getting YAHOO! (ticker: YHOO) stock data: yhoo_30mins_delta.


# Example of displaying all Apple (ticker: AAPL) 1-minute data
display(spark.sql('SELECT * FROM aapl_1min_delta'))
# Example of displaying all delisted Yahoo! (ticker: YHOO) 1-minute data
display(spark.sql('SELECT * FROM yhoo_1min_delta'))
# Example of displaying all Apple (ticker: AAPL) 30-minutes data
display(spark.sql('SELECT * FROM aapl_30mins_delta'))
# Example of displaying all delisted YAHOO! (ticker: YHOO) 30-minutes data
display(spark.sql('SELECT * FROM yhoo_30mins_delta'))

#Example of displaying all ADS data
display(spark.sql('SELECT * FROM ads_delta'))
# After displaying the Spark Dataframe, you can press "Download" button.
