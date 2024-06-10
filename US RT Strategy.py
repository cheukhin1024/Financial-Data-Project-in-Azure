import pandas as pd
import requests
headers = {
    'Content-Type': 'application/json'
}

requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/XLK/prices?startDate=2005-01-03&token=ff008f598182931d7eb1f0b03600aebb4feeb732", headers=headers)
data = requestResponse.json()

# Create a DataFrame directly from the list of dictionaries
df = pd.DataFrame(data)

# Select only the desired columns
columns_to_keep = ['date', 'close', 'high', 'low', 'open', 'volume', 'adjClose', 'adjHigh', 'adjLow', 'adjOpen', 'adjVolume', 'divCash', 'splitFactor']
df = df[columns_to_keep]

# Display the first few rows of the DataFrame
print(df.head(10))
print(df.tail(10))
