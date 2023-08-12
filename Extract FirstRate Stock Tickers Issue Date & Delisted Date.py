"""
Raw data input:
Ticker    Timeframe
A  (Agilent Technologies Inc)    First Date:3-Jan-2005 -> Last Date:8-Feb-2022
AA  (ALCOA CORPORATION)    First Date:18-Oct-2016 -> Last Date:8-Feb-2022
AAL  (American Airlines Group)    First Date:9-Dec-2013 -> Last Date:8-Feb-2022
AAP  (Advance Auto Parts)    First Date:3-Jan-2005 -> Last Date:8-Feb-2022
AAPL  (Apple)    First Date:3-Jan-2005 -> Last Date:8-Feb-2022
...                                  ...                                              ...
XEC-DELISTED  (Cimarex Energy)    First Date:3-Jan-2005 -> Last Date:30-Sep-2021
XL-DELISTED  (XL GROUP PLC)    First Date:1-Jan-2005 -> Last Date:11-Sep-2018
XLRN-DELISTED  (Acceleron Pharma)    First Date:19-Sep-2013 -> Last Date:19-Nov-2021
XONE-DELISTED  (The Exone Company)    First Date:7-Feb-2013 -> Last Date:11-Nov-2021
YHOO-DELISTED  (YAHOO!)    First Date:1-Jan-2005 -> Last Date:16-Jun-2017
"""

import pandas as pd

data = pd.read_csv('C:/Users/user/Downloads/sp500_bundle_timeframe.txt', sep='    ', header=0)

"""
Pandas data input:
                                  Ticker                                        Timeframe
0          A  (Agilent Technologies Inc)    First Date:3-Jan-2005 -> Last Date:8-Feb-2022
1                AA  (ALCOA CORPORATION)   First Date:18-Oct-2016 -> Last Date:8-Feb-2022
3              AAP  (Advance Auto Parts)    First Date:3-Jan-2005 -> Last Date:8-Feb-2022
4                          AAPL  (Apple)    First Date:3-Jan-2005 -> Last Date:8-Feb-2022
...                                  ...                                              ...
1105      XEC-DELISTED  (Cimarex Energy)   First Date:3-Jan-2005 -> Last Date:30-Sep-2021
1106         XL-DELISTED  (XL GROUP PLC)   First Date:1-Jan-2005 -> Last Date:11-Sep-2018
1107   XLRN-DELISTED  (Acceleron Pharma)  First Date:19-Sep-2013 -> Last Date:19-Nov-2021
1108  XONE-DELISTED  (The Exone Company)   First Date:7-Feb-2013 -> Last Date:11-Nov-2021
1109             YHOO-DELISTED  (YAHOO!)   First Date:1-Jan-2005 -> Last Date:16-Jun-2017

Expected data output:

     Ticker   First Date    Last Date
0         A   3-Jan-2005   8-Feb-2022
1        AA  18-Oct-2016   8-Feb-2022
2       AAL   9-Dec-2013   8-Feb-2022
3       AAP   3-Jan-2005   8-Feb-2022
4      AAPL   3-Jan-2005   8-Feb-2022
...     ...          ...          ...
1105    XEC   3-Jan-2005  30-Sep-2021
1106     XL   1-Jan-2005  11-Sep-2018
1107   XLRN  19-Sep-2013  19-Nov-2021
1108   XONE   7-Feb-2013  11-Nov-2021
1109   YHOO   1-Jan-2005  16-Jun-2017
"""

input_df = pd.DataFrame(data)


# Extracting and formatting information
input_df['Ticker'] = input_df['Ticker'].str.split('  ').str[0]
input_df['Ticker'] = input_df['Ticker'].str.replace(r'-DELISTED', '')  # Remove -DELISTED if present
input_df['First Date'] = input_df['Timeframe'].str.split('First Date:').str[1].str.split(' ->').str[0]
input_df['Last Date'] = input_df['Timeframe'].str.split('Last Date:').str[1]

# Drop the original Timeframe column
input_df.drop(columns=['Timeframe'], inplace=True)

#Convert pandas object data type to datetime
input_df[["First Date", "Last Date"]] = input_df[["First Date", "Last Date"]].apply(pd.to_datetime)

#Sort datetime
input_df.sort_values(by=['First Date', 'Last Date'], inplace = True)

# Print the DataFrame
print(input_df)

import os  
os.makedirs('C:/Users/user/Downloads', exist_ok=True)  
input_df.to_csv('C:/Users/user/Downloads/sp500_bundle_timeframe_output.csv')  
