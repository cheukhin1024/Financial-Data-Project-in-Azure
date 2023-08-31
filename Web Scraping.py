# Databricks notebook source
# DBTITLE 1,Web Scraping from Hindenburg Research
from bs4 import BeautifulSoup 
import requests

url = "https://hindenburgresearch.com/page/{}/"
page_num = 1
page = requests.get(url.format(page_num))

# COMMAND ----------

soup = BeautifulSoup(page.text, 'html')
print(soup.prettify())

# COMMAND ----------

headline = soup.find('h1').text
print(headline)
print(type(headline))

# COMMAND ----------

titles_arr = []

next_text = soup.find("a", class_="next page-numbers")

while next_text is not None:
    #titles = soup.find_all(['h2','span'], class_ = ['post-title','entry-title-primary'])
    titles = soup.find_all(['h2'], class_ = ['post-title'])
    for title in titles:
        print(title.text)
        titles_arr.append(title.text)
    page_num+=1
    page = requests.get(url.format(page_num))
    soup = BeautifulSoup(page.text, 'html')
    next_text = soup.find("a", class_="next page-numbers")

# COMMAND ----------

#Last page that does not have next button
if next_text is None:
    titles = soup.find_all(['h2'], class_ = ['post-title'])
    for title in titles:
        print(title.text)
        titles_arr.append(title.text)

# COMMAND ----------

print(page_num)
print(url.format(page_num))

# COMMAND ----------

print(len(titles_arr))

# COMMAND ----------

for title_text in titles_arr:
    print(title_text)