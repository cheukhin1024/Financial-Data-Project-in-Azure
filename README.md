# Financial Data Project in Azure 
![Me main3](https://user-images.githubusercontent.com/70860455/160253345-b4b9484a-966d-4f03-9419-1354fc8b1934.PNG)

## Description
1. Provide over 2 billion historical S&P 500 constituents with high-frequency data rows (no survivorship
bias) to different users in Azure Databricks Delta Lake.Data can back to 2005.
2. Increased query performance by at least 1000% compared to a traditional database.
3. Introduce a better data-driven sector classification than the traditional S&P GICS sector classification.
4. Provide alternative data (such as Bloomberg TV real-time market sentiment data, Twitter sentiment,
and NASA satellite images).
5. Streaming all IEX market data.
6. Introduce financial portfolio optimization methods (such as the hierarchical risk parity algorithm
developed by Marcos Lopez de Prado (PhD)).
7. Create end-to-end DevOps CI/CD data pipelines in Azure Databricks Delta Live Tables

## System Design
![system design drawio](https://user-images.githubusercontent.com/70860455/199191296-d5d06a08-c074-46f0-a6ce-d15571aea13a.png)
[system design drawio](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=system%20design.drawio#R7VxZd5s4FP41Pqd9iA8IxPLoxE6nM%2Bkyddqmj4qt2DQYeQA3dn79SIAMSGBjm8VN%2BpKAENu93%2F3uoot72tVi%2Fc5Hy%2FkHMsVuDyjTdU8b9gBQbQXQf2xkE4%2FYwIgHZr4zTSalA2PnGSeDSjK6cqY4yE0MCXFDZ5kfnBDPw5MwN4Z8nzzlpz0QN3%2FXJZphaWA8Qa48%2Bt2ZhvN41AJmOv4XdmZzfmfVsOMjC8QnJ28SzNGUPGWGtFFPu%2FIJCeOtxfoKu0x4XC7xedclR7cP5mMvrHLC1eX34d%2FPq%2BHPj%2BrN892Xj3Pr6Z8LK3m2cMNfGE%2Fp%2Bye7xA%2FnZEY85I7S0UufrLwpZldV6F4654aQJR1U6eBPHIabRJloFRI6NA8XbnIUr53wLrP9g12qD5O94Tq5crSz4Tte6G%2FusjuZs9huelq0x8%2BTpZQILiArf4J3iCYBLpNH5sREtu8wWWB6HzrBxy4KnV95vKAEdrPtvO2pn4lDHwUoiYkAJcFHYiBAV%2FKXCJE%2Fw2FyVqpfupF5jHQo0voBCEhe8xdyV8krXDt%2BwB7wCwox%2FTdEIeoBw6Xiu7z36daMbakLx%2BsBektFU7ab%2BtwP5KnyyK2zoPca0DPo28ML%2Bg9IOMyj7GnuhHi8RJHGnijV5BFVquVf2A%2Fxeqf%2BkqO6oAaulqfU6lVuyvOMxVtKucZzujpUMZwBM5qRjdWbDhjJ0b2Ji4LAmeTlkhfiMXZXKtm9dpERHCyQGx870Xw0sMd8YjuXzEe6kC4CoGU7VNUCdceGM1fLTYmP0Htmpwk4oTYQ5pERhD55xFfEJT4d8YjHmP3BcV1hKKA253gzOgDTvduI6KndllgmoWb34EawnDvTKfYkKNZgsBrMK8wqMFi7AHhbK67fYmUu3SqMq2aIXUanyg16ZGIFBlowiXn3wTKvzfsGlIlcZ%2BYxrqBSx3T8kknbocHOIDmwoNqKfHyRVmvXoG7nNaipFTlXa0yDlqTBj4PxYOsFlcHn9%2BwOQPkUzqkE6eUWNAIM%2BJGOfZhIhlXl2ZgP03TZZZ17fJmGlD9yEWVxfPlAvDB5EHWnFvfGm6pd0bGeGnAaJZFOW47OlmyMG9PSxxcuQUz5scUFOAw6typ9v59p1aiAHBi%2BH91xCpIDhI7FB80zIyWgFbjp0wLrlDzAQezBmSplpx8Z3jowIt%2FPMIl3iw18x0T7vGJ83dzDWJVjfGj2oalBW1OBZSkmr0Xx66pq31ShCSwTAqhZwoM2nYjrtcPyCHRloGweBOXjYcmN%2F3eDJVQFYjOPhCXUlL6iGgaElgl0A9oC2mFfM6Bmm4qp0BjZMCvBkuIEbTLTlmxC0AhwjXMAbin%2BzgUtYp1P9G%2BV0SJcSDPajd90TdZuezE997CVMFFfcM7r%2FXs5SgcVUVcZTqfFOqZkm4Pnlc%2Fruve%2BM3lk2WumLIHPIOLWSyDeXcwoFwbkUHu0Dn00YaY6jaoFrCTO0pkee1RxMqbiiNgH48dpxNQPPlkUTh2Nb%2Bm4Yve0Aat8KNQ2APUXdFdR%2BvL0bx%2Fi2jpX9BVZLFdRKf%2FTMnQW1B6mkoZfTE3JUMRsowA6ZgF0GqspATnf5Tpj%2FJTTg%2FHfivADF0HEXEyTqrpcx9XB5HgGcchniGNQu%2FWRFzwQfxHv3sTIezO6vXlbASXvsId9xN7m88pfkkDAy466c%2FwWL71YqakwDyy7iJOgDCxxHaG%2B4hpoAVgZKmOA%2BgOk052bJgBJgTKQlFaBJAcJvCJHZbwKqV6nWySwKlP3EYJhlZQEuit1F0UI9WRBB5Sxj49wOQjOJV2yjL5t5Q1FTHQqZ0zQ7ts2tICpG7aq2kLVR1f6NqTZvAltYOgq71g6m%2FyapxT7Yvg3H9Bk7nhs%2FAYj33O82dvTDLVy%2FnSAGxVWHyDo2nB1WFG8439veulCIE1eN9SLBOcnYqjmC0im3rmIDZkK2ywZmMeXDI5dFzyeiKuXGmBFxj6ViiGl4jxn6kdTsZCewYpdNuVsW1pSzT%2Bwpex%2BLmvnfLoRP0G9xC7HXTwaDpbIOzWAT2oR2f49%2BpjxlV96kK2J%2BizgQKuAAhuLsfXyAlIjyZqcaCWOi1WDXAd5VPyvLfMSjRxWTRoaQwWsfSla8l919nxW9l1nkkRoQoOZLrb%2BVXVbluC29JZ7ZqAcow7xA1ox%2B2XU8G1w9fXrByb4pKpsRmSwCfov15rFSm%2FhIkGrHA%2FlSu%2B141GqdaJyGCdgdxVQ%2BRV2f3ZcVdmSnxAFdZc5cJ025DbjEKnYX2bK6aVNuq%2FDb4odcEWwaNXQjAIv2WY%2BmU0nt97zwHQyl0w2%2BBkTJ6W96WRl332iU1ZFp3xsLil0hel8gabmVFIVUwmlhdTQKGoGqyk1zDog5QbdY5eVt%2BLlwleWJorMVhhDaK1SG%2ByW2k7ortlym1oTt%2B2lLMNoh7KkorUF%2BgLZVCUtEXGGmJLUxFripyDQ0nY%2Blzjf0NtgOblz8NpBacQ8pgFaiGche%2FEhTW1cslzgRC7nFCcbna8%2B8qbQ35A2SvXRulUf%2B%2BmoaNOwLZvO2%2Bj%2B%2BeIvBFR8j2Y5oNnC6LEZ3p%2BMbx%2FBtZrxmeVfR58cDwsrunRzxG5DqYV4ry8i1vKLx1aRazPUNlVfVCPvvs2tsKv21Te3QcGnFnZJqm02t5k1ZNKgBD4cC5cuuY%2FCVeKznxOqyBnBHC3ZJoNeQE8tU1Kz3SLS7890HsuaFb4n4rKj3p1ZQwdyMwQXaRaUDvQCsYnVrvrEVtRNcHZi08U12IKF%2BVbFZtX%2B2WXZEmy%2BjxM0tQZbuS2omzVY89ivJEWiMkQCqinLEu%2FDDfvQ52o0a7Jq%2F%2Bay6kqF2Vw578yQqxp7AFcVueKFLNgMcqX7tLFSYTXaxLakGiSRzrNZWuBEDbmj4eDtq0%2FQzKIG6lYTNFvOzYsbqBMVjicOjtrPlG2dJf7LMm9v5ng4Wpw6v8Zq6SfiGgyV6W7606CxraY%2FsKqN%2Fgc%3D)

## Website
https://matroidevolved.com/

## Contributors 
1. Jesstlyn Clarissa (The University of Hong Kong) 

## StackOverflow
https://stackoverflow.com/c/algorithmic-trading-for-beginners

Notice: 
- Email invitation required. 

## How to access the data?



There are 4 solutions:

1. Download raw .txt zip files from Google Drive

Notice: download links are in StackOverFlow private team.


2. Access Azure Blob Storage

We can assign you as a "Storage Blob Data Contributor -
Allows for read, write and delete access to Azure Storage blob containers and data". Then, you can accept the email invitation and access the data.

3. Access Azure Databricks Delta Lake
We can assign you as a "Contributor -
Allows for read, write and delete access to Azure Databricks". Then, you can accept the email invitation and access the data.

4. Access data through Azure Databricks Delta Sharing (Developing)

For details, please visit: https://docs.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-sharing


5. Acess data through Azure Data Share 

Accept the email invitation and access the data.

For details, https://docs.microsoft.com/en-us/azure/databricks/data-sharing/delta-sharing/

## Main Files Explanations:

###### Count satallite image color area.py

![ms image](https://user-images.githubusercontent.com/70860455/160276772-a8624e36-8d0d-438c-8b98-20c90c29aea5.PNG)
1. Count the color area of the satallite image using OpenCV

###### Count number of file in directory.py

1. Validate files completeness by counting number of files

###### Check Empty File.py

1. Validate files completeness by checking empty files

###### Get data from Delta Lake.py

1. Examples of getting different datasets from Delta Lake in Azure Databricks 
- Current S&P 500 constituents 1-min stock data
- Delisted S&P 500 constituents 1-min stock data
- Current S&P 500 constituents 30-mins stock data
- Delisted S&P 500 constituents 30-mins stock data
- [Aruoba-Diebold-Scotti Business Conditions Index](https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/ads/ads_index_most_current_vintage.xlsx?la=en&hash=6DF4E54DFAE3EDC347F80A80142338E7) in [Federal Reserve Bank of Philadelphia](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/ads) 
- [US Daily News Index](https://www.policyuncertainty.com/media/All_Daily_Policy_Data.csv) in [Economic Policy Uncertainty](https://www.policyuncertainty.com/us_monthly.html)

###### Financial Data Engineering.py

1. REST API getting data from: 
- [Tiingo](https://api.tiingo.com/), 
- [Federal Reserve Bank of Philadelphia](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/ads), 
- [Economic Policy Uncertainity Index Website](https://www.policyuncertainty.com/),
- [NASA](https://data.nasa.gov/).
2. Rename column names
3. Combine multiple columns of multiple dataframes
4. Create Azure Databricks Delta Lake

###### Stream IEX Market data for last trade updates

![iex market data](https://user-images.githubusercontent.com/70860455/186009051-0dfbf87d-5ad0-4034-81fa-272ab698d856.JPG)

1. Stream IEX market data for last trade updates using websocket.

###### Financial Machine Learning using pyspark ml.py

1. K-mean Clustering using pyspark.ml on delta format data


###### Financial Machine Learning using sklearn.py

1. K-mean Clustering using sklearn on delta format data

###### Hierarchical Risk Parity Algorithm.py
![下載](https://user-images.githubusercontent.com/70860455/186008175-34c2f6f0-8489-4a47-b7a9-7847d1c6016b.png))
![下載 (1)](https://user-images.githubusercontent.com/70860455/186008188-260b0348-e764-4983-a502-2bef757948ec.png))

###### FirstRate 1 min data ETL.py / FirstRate 30 min data ETL.py / FirstRate 1 hour data ETL.py

1. Contains 1-minute, 5-minute, 30-minute and 1-hour historical intraday data for :
   500 component stocks of the S&P500
   active stocks previously included in the S&P500
   delisted stocks previously included in the S&P500
   SPX index
   Listing of S&P500 component changes back to 2004
   Data is adjusted for dividends and splits. Out-of-hours trades are included.
2. Add headers and Rename column names 
3. Create Azure Databricks Delta Data Lake. 

The intraday bars and tick data for stocks and ETFs are aggregated from trades on the below exchanges:

- XASE (NYSE American - AMEX)
- XNAS (NASDAQ OMX BX)
- XCIS (National Stock Exchange)
- FINRA (FINRA)
- CQS (Consolidated Quote System)
- XISX (International Securities Exchange)
- EDGA (Cboe EDGA)
- EDGX (Cboe EDGX)
- XCHI (Chicago Stock Exchange)
- XNYS (New York Stock Exchange)
- ARCX (NYSE Arca)
- XNGS (Nasdaq)
- CTS (Consolidated Tape System)
- OOTC (OTC Bulletin Board)
- XOTC (OTC Bulletin Board)
- PSGM (OTC Bulletin Board)
- PINX (OTC Bulletin Board)
- OTCB (OTC Bulletin Board)
- OTCQ (OTC Bulletin Board)
- IEXG (IEX)
- XCBO (Chicago Board Options Exchange)
- PHLX (Nasdaq PSX)
- BATY (Cboe BYX)
- BATS (Cboe BZX)
- XBOS (NASDAQ BX Options/ETF)

Updates (Dec 2021): Added Signature Bank (SBNY)

Updates (Dec 2021): Added SolarEdge (SEDG)

Updates (Dec 2021): Added FactSet (FDS)

Updates (Dec 2021): Added EPAM Systems (EPAM)

Updates (Sept 2021): Added Match Group (MTCH), Ceridian (CDAY) Brown and Brown (BRO)

Updates (August 2021) : Added Bio-Techne (TECH)

- A (Agilent Technologies Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AA (ALCOA CORPORATION) First Date:18-Oct-2016 -> Last Date:15-Feb-2022
- AAL (American Airlines Group) First Date:9-Dec-2013 -> Last Date:15-Feb-2022
- AAP (Advance Auto Parts) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AAPL (Apple) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ABBV (AbbVie) First Date:2-Jan-2013 -> Last Date:15-Feb-2022
- ABC (AmerisourceBergen Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ABMD (ABIOMED Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ABT (Abbott Laboratories) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ACN (Accenture plc) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- ACV (Alberto-Culver Co.) First Date:22-May-2015 -> Last Date:15-Feb-2022
- ADBE (Adobe Systems Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ADI (Analog Devices) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ADM (Archer-Daniels-Midland Co) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ADP (Automatic Data Processing) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ADS (Alliance Data Systems) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ADSK (Autodesk) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ADT (ADT) First Date:19-Jan-2018 -> Last Date:15-Feb-2022
- AEE (Ameren Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AEP (American Electric Power) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AES (AES Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AFL (AFLAC Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AIG (American International Group) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AINV (Apollo Investment Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AIV (Apartment Investment & Management) First Date:21-Jul-2009 -> Last Date:15-Feb-2022
- AIZ (Assurant) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AJG (Arthur J. Gallagher & Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AKAM (Akamai Technologies Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ALB (Albemarle Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ALGN (Align Technology) First Date:1-May-2007 -> Last Date:15-Feb-2022
- ALK (Alaska Air Group Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ALL (Allstate Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ALLE (Allegion) First Date:18-Nov-2013 -> Last Date:15-Feb-2022
- ALTR (ALTAIR ENGINEERING) First Date:1-Nov-2017 -> Last Date:15-Feb-2022
- AMAT (Applied Materials) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AMBC (Ambac Financial Group) First Date:1-May-2013 -> Last Date:15-Feb-2022
- AMCR (AMCOR PLC) First Date:11-Jun-2019 -> Last Date:15-Feb-2022
- AMD (Advanced Micro Devices Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AME (AMETEK) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AMG (Affiliated Managers Group Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AMGN (Amgen) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AMP (Ameriprise Financial) First Date:3-Oct-2005 -> Last Date:15-Feb-2022
- AMT (American Tower) First Date:3-Jan-2012 -> Last Date:15-Feb-2022
- AMZN (Amazon.com) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AN (AUTONATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ANET (Arista Networks) First Date:6-Jun-2014 -> Last Date:15-Feb-2022
- ANF (ABERCROMBIE & FITCH COMPANY) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ANSS (ANSYS) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ANTM (Anthem) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- AON (Aon plc) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- AOS (A.O. Smith Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- APA (Apache Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- APD (Air Products & Chemicals Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- APH (Amphenol Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- APTV (Aptiv Plc) First Date:17-Nov-2011 -> Last Date:15-Feb-2022
- ARE (Alexandria Real Estate Equities) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ARNC (Arconic) First Date:1-Apr-2020 -> Last Date:15-Feb-2022
- ASH (ASHLAND GLOBAL HOLDINGS) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ASO (AmSouth Ban) First Date:2-Oct-2020 -> Last Date:15-Feb-2022
- ATGE (DeVry) First Date:1-May-2007 -> Last Date:15-Feb-2022
- ATI (ALLEGHENY TECHNOLOGIES INCORPORATED) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ATO (Atmos Energy Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ATVI (Activision Blizzard) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- AVB (AvalonBay Communities) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AVGO (Broadcom) First Date:1-Feb-2016 -> Last Date:15-Feb-2022
- AVY (Avery Dennison Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AWK (American Water Works Company Inc) First Date:23-Apr-2008 -> Last Date:15-Feb-2022
- AXP (American Express Co) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AYI (ACUITY BRANDS) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- AZO (AutoZone Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BA (Boeing Company) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BAC (Bank of America Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BAX (Baxter International) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BBBY (BED BATH & BEYOND) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BBY (Best Buy Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BC (BRUNSWICK CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BDX (Becton Dickinson) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BEN (Franklin Resources) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BFB (Brown-Forman) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BIDU (Bidu) First Date:5-Aug-2005 -> Last Date:15-Feb-2022
- BIG (BIG LOTS) First Date:1-Sep-2006 -> Last Date:15-Feb-2022
- BIIB (Biogen) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BIO (Bio-Rad Laboratories) First Date:8-May-2007 -> Last Date:15-Feb-2022
- BK (The Bank of New York Mellon) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- BKNG (Booking Holdings Inc) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- BLK (BlackRock) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BLL (Ball Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BMRN (BioMarin Pharmaceutical) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BMY (Bristol-Myers Squibb) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BR (Broadridge Financial Solutions) First Date:1-May-2007 -> Last Date:15-Feb-2022
- BRKB (BERKSHIRE HATHAWAY) First Date:2-May-2007 -> Last Date:15-Feb-2022
- BRO (Brown & Brown) First Date:3-Jan-2007 -> Last Date:15-Feb-2022
- BSX (Boston Scientific) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BTU (PEABODY ENERGY CORPORATION) First Date:3-Apr-2017 -> Last Date:15-Feb-2022
- BUD (ANHEUSER-BUSCH INBEV SA) First Date:16-Sep-2009 -> Last Date:15-Feb-2022
- BWA (BorgWarner) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- BXP (Boston Properties) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- C (Citigroup) First Date:9-May-2011 -> Last Date:15-Feb-2022
- CAG (Conagra Brands) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- CAH (Cardinal Health) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- CAR (Avis Budget Group) First Date:5-Sep-2006 -> Last Date:15-Feb-2022
- CARR (Carrier Global) First Date:19-Mar-2020 -> Last Date:15-Feb-2022
- CAT (Caterpillar) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- CB (Chubb Limited) First Date:18-Jul-2008 -> Last Date:15-Feb-2022
- CBH (ALLIANZGI CONVERTIBLE & INCOME 2024 TARGET TERM FUND) First Date:28-Jun-2017 -> Last Date:15-Feb-2022
- CBOE (Cboe Global Markets) First Date:15-Jun-2010 -> Last Date:15-Feb-2022
- CBRE (CBRE Group) First Date:3-Jan-2017 -> Last Date:15-Feb-2022
- CC (CHEMOURS COMPANY (THE)) First Date:19-Jun-2015 -> Last Date:15-Feb-2022
- CCI (Crown Castle International) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- CCK (CROWN HOLDINGS) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- CCL (Carnival) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- CCU (COMPANIA CERVECERIAS UNIDAS S.A.) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- CDAY (Ceridian HCM Holding) First Date:26-Apr-2018 -> Last Date:15-Feb-2022
- CDNS (Cadence Design Systems) First Date:31-Oct-2005 -> Last Date:15-Feb-2022
- CDW (CDW CORPORATION) First Date:27-Jun-2013 -> Last Date:15-Feb-2022
- CE (Celanese) First Date:1-Mar-2005 -> Last Date:15-Feb-2022
- CERN (Cerner) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- CF (CF Industries Holdings Inc) First Date:3-Oct-2005 -> Last Date:15-Feb-2022
- CFG (Citizens Financial Group) First Date:24-Sep-2014 -> Last Date:15-Feb-2022
- CHD (Church & Dwight) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CHIR (Chiron) First Date:11-Dec-2018 -> Last Date:15-Feb-2022
- CHK (CHESAPEAKE ENERGY CORPORATION) First Date:10-Feb-2021 -> Last Date:15-Feb-2022
- CHKP (Check Point Software Technologies Ltd) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CHRW (C. H. Robinson Worldwide) First Date:3-Jan-2006 -> Last Date:15-Feb-2022
- CHTR (Charter Communications) First Date:14-Sep-2010 -> Last Date:15-Feb-2022
- CI (CIGNA) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CIEN (CIENA CORPORATION) First Date:1-Dec-2006 -> Last Date:15-Feb-2022
- CINF (Cincinnati Financial) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CIT (CIT GROUP INC (DEL)) First Date:10-Dec-2009 -> Last Date:15-Feb-2022
- CL (Colgate-Palmolive) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CLF (CLEVELAND-CLIFFS) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CLX (The Clorox Company) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CMA (Comerica) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CMCSA (Comcast) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CME (CME Group) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CMG (Chipotle Mexican Grill) First Date:26-Jan-2006 -> Last Date:15-Feb-2022
- CMI (Cummins) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CMS (CMS Energy) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CNC (Centene Corporation) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CNP (CenterPoint Energy) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CNX (CNX RESOURCES CORPORATION) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- COF (Capital One Financial) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- COO (The Cooper Companies) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- COOP (Mr. Cooper Group) First Date:28-Mar-2012 -> Last Date:15-Feb-2022
- COP (ConocoPhillips) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- COST (Costco Wholesale) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- COTY (Coty) First Date:13-Jun-2013 -> Last Date:15-Feb-2022
- CPB (Campbell Soup) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CPRI (Capri Holdings) First Date:15-Dec-2011 -> Last Date:15-Feb-2022
- CPRT (Copart Inc) First Date:2-Jan-2004 -> Last Date:15-Feb-2022-
- CRM (Salesforce.com) First Date:23-Jun-2004 -> Last Date:15-Feb-2022
- CSCO (Cisco Systems) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CSX (CSX) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CTAS (Cintas Corporation) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CTLT (Catalent) First Date:31-Jul-2014 -> Last Date:15-Feb-2022
- CTSH (Cognizant Technology Solutions) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CTVA (CORTEVA) First Date:24-May-2019 -> Last Date:15-Feb-2022
- CTXS (Citrix Systems) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CVS (CVS Health) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CVX (Chevron) First Date:2-Jan-2004 -> Last Date:15-Feb-2022
- CZR (Caesars Entertainment Corporation) First Date:22-Sep-2014 -> Last Date:15-Feb-2022
- D (Dominion Energy) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DAL (Delta Air Lines) First Date:16-May-2007 -> Last Date:15-Feb-2022
- DAN (Dana) First Date:1-Feb-2008 -> Last Date:15-Feb-2022
- DD (DUPONT DE NEMOURS) First Date:24-May-2019 -> Last Date:15-Feb-2022
- DDS (DILLARD'S) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DE (Deere & Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DELL (DELL TECHNOLOGIES) First Date:1-May-2007 -> Last Date:15-Feb-2022
- DFS (Discover Financial Services) First Date:2-Jul-2007 -> Last Date:15-Feb-2022
- DG (Dollar General) First Date:13-Nov-2009 -> Last Date:15-Feb-2022
- DGX (Quest Diagnostics) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DHI (D. R. Horton) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DHR (Danaher) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DIS (The Walt Disney Company) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DISCA (Discovery Class A) First Date:2-May-2007 -> Last Date:15-Feb-2022
- DISCK (Discovery Class C) First Date:18-Sep-2008 -> Last Date:15-Feb-2022
- DISH (Dish Network) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DLR (Digital Realty Trust Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DLTR (Dollar Tree) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- DLX (Deluxe) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DNB (DUN & BRADSTREET CORPORATION (T) First Date:30-Jun-2020 -> Last Date:15-Feb-2022
- DOV (Dover) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DOW (DOW) First Date:20-Mar-2019 -> Last Date:15-Feb-2022
- DPZ (Domino's Pizza) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DRE (Duke Realty Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DRI (Darden Restaurants) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DTE (DTE Energy Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DUK (Duke Energy) First Date:15-Jun-2012 -> Last Date:15-Feb-2022
- DVA (DaVita) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DVN (Devon Energy) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- DXC (DXC Technology) First Date:16-Mar-2017 -> Last Date:15-Feb-2022
- DXCM (Dexcom) First Date:2-May-2005 -> Last Date:15-Feb-2022
- EA (Electronic Arts) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- EBAY (eBay) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ECL (Ecolab) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ED (Consolidated Edison) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EFX (Equifax) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EIX (Edison Int'l) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- EL (Estee Lauder Cos.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EMN (Eastman Chemical) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EMR (Emerson Electric Company) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ENDP (ENDO INTERNATIONAL PLC) First Date:3-Mar-2014 -> Last Date:15-Feb-2022
- ENPH (Enphase Energy) First Date:30-Mar-2012 -> Last Date:15-Feb-2022
- EPAM (EPAM Systems) First Date:8-Feb-2012 -> Last Date:15-Feb-2022
- EOG (EOG Resources) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EQ (EQUILLIUM) First Date:12-Oct-2018 -> Last Date:15-Feb-2022
- EQIX (Equinix) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EQR (Equity Residential) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EQT (EQT CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ES (Eversource Energy) First Date:26-Apr-2007 -> Last Date:15-Feb-2022
- ESS (Essex Property Trust) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ETN (Eaton Corporation) First Date:15-May-2012 -> Last Date:15-Feb-2022
- ETR (Entergy) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ETSY (Etsy) First Date:16-Apr-2015 -> Last Date:15-Feb-2022
- EVRG (Evergy) First Date:2-May-2007 -> Last Date:15-Feb-2022
- EW (Edwards Lifesciences) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EXC (Exelon) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- EXPD (Expeditors) First Date:6-Jun-2005 -> Last Date:15-Feb-2022
- EXPE (Expedia Group) First Date:9-Aug-2005 -> Last Date:15-Feb-2022
- EXR (Extra Space Storage) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- F (Ford Motor) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FANG (Diamondback Energy) First Date:12-Oct-2012 -> Last Date:15-Feb-2022
- FAST (Fastenal Co) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FB (Facebook) First Date:18-May-2012 -> Last Date:15-Feb-2022
- FBHS (Fortune Brands Home & Security) First Date:4-Oct-2011 -> Last Date:15-Feb-2022
- FCX (Freeport-McMoRan) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FDX (FedEx Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FDS (Factset Research Systems) First Date:1-May-2007 -> Last Date:15-Feb-2022
- FE (FirstEnergy Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FFIV (F5 Networks) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FHN (FIRST HORIZON NATIONAL CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FIS (Fidelity National Information Services) First Date:1-Feb-2006 -> Last Date:15-Feb-2022
- FISV (Fiserv Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FITB (Fifth Third Bancorp) First Date:20-Jan-2011 -> Last Date:15-Feb-2022
- FL (Foot Locker Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FLEX (Flex Ltd) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FLR (Fluor) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FLS (Flowserve Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FLT (FleetCor Technologies Inc) First Date:15-Dec-2010 -> Last Date:15-Feb-2022
- FMC (FMC Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FOSL (FOSSIL GROUP) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FOX (Twenty-First Century Fox Class B) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- FOXA (Twenty-First Century Fox Class A) First Date:27-Feb-2019 -> Last Date:15-Feb-2022
- FPL (FIRST TRUST NEW OPPORTUNITIES MLP & ENERGY FUND) First Date:27-Mar-2014 -> Last Date:15-Feb-2022
- FRC (First Republic Bank) First Date:9-Dec-2010 -> Last Date:15-Feb-2022
- FRT (Federal Realty Investment Trust) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- FSLR (FIRST SOLAR) First Date:17-Nov-2006 -> Last Date:15-Feb-2022
- FTI (TechnipFMC) First Date:17-Jan-2017 -> Last Date:15-Feb-2022
- FTNT (Fortinet) First Date:18-Nov-2009 -> Last Date:15-Feb-2022
- FTV (Fortive Corp) First Date:5-Jul-2016 -> Last Date:15-Feb-2022
- GCI (GANNETT CO.) First Date:4-Feb-2014 -> Last Date:15-Feb-2022
- GD (General Dynamics) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GE (General Electric) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GHC (GRAHAM HOLDINGS COMPANY) First Date:16-May-2007 -> Last Date:15-Feb-2022
- GILD (Gilead Sciences) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GIS (General Mills) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GL (GLOBE LIFE) First Date:1-May-2007 -> Last Date:15-Feb-2022
- GLW (Corning) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GM (General Motors) First Date:18-Nov-2010 -> Last Date:15-Feb-2022
- GME (GAMESTOP CORPORATION) First Date:10-Oct-2005 -> Last Date:15-Feb-2022
- GNRC (Generac Holdings) First Date:11-Feb-2010 -> Last Date:15-Feb-2022
- GNW (GENWORTH FINANCIAL INC) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GOOG (Alphabet Inc Class C) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GOOGL (Alphabet Inc Class A) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- GP (Georgia-Pacific Group) First Date:28-Aug-2020 -> Last Date:15-Feb-2022
- GPC (Genuine Parts) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GPN (Global Payments) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GPS (Gap) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GRMN (Garmin Ltd.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GS (Goldman Sachs Group) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GT (THE GOODYEAR TIRE & RUBBER COMPANY) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- GWW (Grainger (W.W.)) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HAL (Halliburton Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HAS (Hasbro) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HBAN (Huntington Bancshares) First Date:18-Sep-2009 -> Last Date:15-Feb-2022
- HBI (Hanesbrands Inc) First Date:6-Sep-2006 -> Last Date:15-Feb-2022
- HCA (HCA Holdings) First Date:10-Mar-2011 -> Last Date:15-Feb-2022
- HD (Home Depot) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HES (Hess Corporation) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- HFC (HollyFrontier Corp) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- HIG (Hartford Financial Svc.Gp.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HII (Huntington Ingalls Industries) First Date:22-Mar-2011 -> Last Date:15-Feb-2022
- HLT (Hilton Worldwide Holdings Inc) First Date:12-Dec-2013 -> Last Date:15-Feb-2022
- HOG (Harley-Davidson) First Date:1-Sep-2006 -> Last Date:15-Feb-2022
- HOLX (Hologic) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HON (Honeywell Int'l) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HP (Helmerich & Payne) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HPE (Hewlett Packard Enterprise) First Date:2-Nov-2015 -> Last Date:15-Feb-2022
- HPQ (HP) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HRB (Block H&R) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HRL (Hormel Foods) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HSIC (Henry Schein) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HST (Host Hotels & Resorts) First Date:18-Apr-2006 -> Last Date:15-Feb-2022
- HSY (The Hershey Company) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- HUM (Humana) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- IAC (IAC/INTERACTIVECORP) First Date:1-Jul-2020 -> Last Date:15-Feb-2022
- IBM (International Business Machines) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ICE (Intercontinental Exchange) First Date:16-Nov-2005 -> Last Date:15-Feb-2022
- IDXX (IDEXX Laboratories) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- IEX (IDEX CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- IFF (Intl Flavors & Fragrances) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- IGT (INTERNATIONAL GAME TECHNOLOGY) First Date:7-Apr-2015 -> Last Date:15-Feb-2022
- IHRT (iHeartMedia) First Date:7-May-2019 -> Last Date:15-Feb-2022
- ILMN (Illumina Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- INCY (Incyte) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- INFO (IHS Markit Ltd.) First Date:19-Jun-2014 -> Last Date:15-Feb-2022
- INFY (Infosys Ltd ADR) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- INTC (Intel) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- INTU (Intuit) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- IP (International Paper) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- IPG (Interpublic Group) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- IPGP (IPG Photonics) First Date:13-Dec-2006 -> Last Date:15-Feb-2022
- IQV (IQVIA Holdings) First Date:9-May-2013 -> Last Date:15-Feb-2022
- IR (Ingersoll-Rand PLC) First Date:12-May-2017 -> Last Date:15-Feb-2022
- IRM (Iron Mountain Incorporated) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ISRG (Intuitive Surgical) First Date:1-Jun-2006 -> Last Date:15-Feb-2022
- IT (Gartner Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ITT (ITT) First Date:1-May-2007 -> Last Date:15-Feb-2022
- ITW (Illinois Tool Works) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- IVZ (Invesco Ltd.) First Date:24-May-2007 -> Last Date:15-Feb-2022
- J (JACOBS ENGINEERING GROUP) First Date:2-May-2007 -> Last Date:15-Feb-2022
- JBHT (J. B. Hunt Transport Services) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- JBL (JABIL) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- JCI (Johnson Controls International) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- JD (JD.Com Inc) First Date:22-May-2014 -> Last Date:15-Feb-2022
- JEF (Jefferies Financial Group) First Date:24-Apr-2007 -> Last Date:15-Feb-2022
- JKHY (Jack Henry & Associates Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- JNJ (Johnson & Johnson) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- JNPR (Juniper Networks) First Date:29-Oct-2009 -> Last Date:15-Feb-2022
- JP (Jefferson-Pilot) First Date:16-Jul-2015 -> Last Date:15-Feb-2022
- JPM (JPMorgan Chase & Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- JWN (Nordstrom) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- K (Kellogg Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KBH (KB HOME) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KEY (KeyCorp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KEYS (Keysight Technologies) First Date:3-Nov-2014 -> Last Date:15-Feb-2022
- KHC (Kraft Heinz Co) First Date:6-Jul-2015 -> Last Date:15-Feb-2022
- KIM (Kimco Realty) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KLAC (KLA-Tencor) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KMB (Kimberly-Clark) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KMI (Kinder Morgan) First Date:11-Feb-2011 -> Last Date:15-Feb-2022
- KMX (Carmax Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KO (Coca-Cola Company) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KODK (Eastman Kodak Co.) First Date:1-Nov-2013 -> Last Date:15-Feb-2022
- KR (Kroger Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KSS (Kohl's) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- KSU (Kansas City Southern) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- L (Loews) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- LBTYK (Liberty Global PLC Class C) First Date:8-Sep-2005 -> Last Date:15-Feb-2022
- LDOS (LEIDOS HOLDINGS) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- LEG (Leggett & Platt) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LEN (Lennar) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LH (Laboratory of America Holding) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LHX (L3HARRIS TECHNOLOGIES) First Date:1-May-2007 -> Last Date:15-Feb-2022
- LIFE (ATYR PHARMA) First Date:7-May-2015 -> Last Date:15-Feb-2022
- LIN (Linde plc) First Date:29-Oct-2018 -> Last Date:15-Feb-2022
- LKQ (LKQ Corporation) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- LLY (Lilly (Eli) & Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LMT (Lockheed Martin) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LNC (Lincoln National) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LNT (Alliant Energy Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LOGI (Logitech International SA) First Date:24-Sep-2012 -> Last Date:15-Feb-2022
- LOW (Lowe's Cos.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LRCX (Lam Research) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LSI (LIFE STORAGE) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- LU (Lucent Technology) First Date:2-Nov-2020 -> Last Date:15-Feb-2022
- LUMN (Lumen Technologies) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- LUV (Southwest Airlines) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- LVS (Las Vegas Sands) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- LW (Lamb Weston Holdings Inc) First Date:1-Nov-2016 -> Last Date:15-Feb-2022
- LYB (LyondellBasell) First Date:14-Oct-2010 -> Last Date:15-Feb-2022
- LYV (Live Nation Entertainment) First Date:3-Jan-2006 -> Last Date:15-Feb-2022
- M (Macy's) First Date:1-Jun-2007 -> Last Date:15-Feb-2022
- MA (Mastercard) First Date:25-May-2006 -> Last Date:15-Feb-2022
- MAA (Mid-America Apartments) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MAC (Macerich) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MAR (Marriott Int'l.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MAS (Masco) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MAT (Mattel) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MBI (MBIA) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MCD (McDonald's) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MCHP (Microchip Technology) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MCK (McKesson) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MCO (Moody's Corp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MDLZ (Mondelez International) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- MDP (MEREDITH CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MDT (Medtronic plc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MET (MetLife) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MGM (MGM Resorts International) First Date:1-Jun-2005 -> Last Date:15-Feb-2022
- MHK (Mohawk Industries) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MKC (McCormick & Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MKTX (MARKETAXESS HOLDINGS) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MLM (Martin Marietta Materials) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- MMC (Marsh & McLennan) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MMI (MARCUS & MILLICHAP) First Date:31-Oct-2013 -> Last Date:15-Feb-2022
- MMM (3M Company) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MNST (Monster Beverage) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MO (Altria Group Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MOS (The Mosaic Company) First Date:20-May-2011 -> Last Date:15-Feb-2022
- MPC (Marathon Petroleum) First Date:23-Jun-2011 -> Last Date:15-Feb-2022
- MPWR (Monolithic Power Systems) First Date:3-Jan-2007 -> Last Date:15-Feb-2022
- MRK (Merck & Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MRO (Marathon Oil) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MRVL (Marvell Technology Group Ltd.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MS (Morgan Stanley) First Date:1-Mar-2006 -> Last Date:15-Feb-2022
- MSCI (MSCI Inc) First Date:15-Nov-2007 -> Last Date:15-Feb-2022
- MSFT (Microsoft) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MSI (Motorola Solutions) First Date:17-Dec-2010 -> Last Date:15-Feb-2022
- MTB (M&T Bank) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MTCH (Match Group) First Date:19-Nov-2015 -> Last Date:15-Feb-2022
- MTD (Mettler Toledo) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MTW (MANITOWOC COMPANY (THE)) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MU (Micron Technology) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- MUR (MURPHY OIL CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NAVI (NAVIENT CORPORATION) First Date:17-Apr-2014 -> Last Date:15-Feb-2022
- NBR (NABORS INDUSTRIES LTD.) First Date:3-Nov-2005 -> Last Date:15-Feb-2022
- NCLH (Norwegian Cruise Line) First Date:18-Jan-2013 -> Last Date:15-Feb-2022
- NDAQ (Nasdaq) First Date:10-Feb-2005 -> Last Date:15-Feb-2022
- NE (NOBLE CORPORATION) First Date:20-Nov-2013 -> Last Date:15-Feb-2022
- NEE (NextEra Energy) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- NEM (Newmont Mining Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NFLX (Netflix) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NI (NiSource) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NKE (Nike) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NKTR (Nektar Therapeutics) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NLOK (NORTONLIFELOCK) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- NLSN (Nielsen Holdings) First Date:31-Aug-2015 -> Last Date:15-Feb-2022
- NOC (Northrop Grumman) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NOV (National Oilwell Varco) First Date:15-Mar-2005 -> Last Date:15-Feb-2022
- NOW (ServiceNow) First Date:29-Jun-2012 -> Last Date:15-Feb-2022
- NRG (NRG Energy) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NSC (Norfolk Southern) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NTAP (NetApp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NTES (NetEase Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NTRS (Northern Trust) First Date:29-Apr-2009 -> Last Date:15-Feb-2022
- NUE (Nucor) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NVDA (Nvidia Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NVR (NVR) First Date:3-May-2007 -> Last Date:15-Feb-2022
- NWL (Newell Brands) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- NWS (News Class B) First Date:19-Jun-2013 -> Last Date:15-Feb-2022
- NWSA (News Class A) First Date:19-Jun-2013 -> Last Date:15-Feb-2022
- NXPI (NXP Semiconductors NV) First Date:6-Aug-2010 -> Last Date:15-Feb-2022
- NYT (NEW YORK TIMES COMPANY (THE)) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- O (Realty Income Corporation) First Date:10-Feb-2012 -> Last Date:15-Feb-2022
- ODFL (Old Dominion Freight Line) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ODP (OFFICE DEPOT) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- OGN (Organon) First Date:14-May-2021 -> Last Date:15-Feb-2022
- OI (O-I GLASS) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- OKE (ONEOK) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- OMC (Omnicom Group) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ONE (Bank One) First Date:28-Mar-2018 -> Last Date:15-Feb-2022
- ORCL (Oracle) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ORLY (O'Reilly Automotive) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- OTIS (Otis Worldwide) First Date:19-Mar-2020 -> Last Date:15-Feb-2022
- OXY (Occidental Petroleum) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PAR (PAR Technology) First Date:16-May-2007 -> Last Date:15-Feb-2022
- PAYC (Paycom) First Date:15-Apr-2014 -> Last Date:15-Feb-2022
- PAYX (Paychex) First Date:6-Jun-2005 -> Last Date:15-Feb-2022
- PBCT (People's United Financial) First Date:29-Mar-2007 -> Last Date:15-Feb-2022
- PBI (PITNEY BOWES) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PCAR (PACCAR) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PCG (PACIFIC GAS & ELECTRIC CO.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PDCO (PATTERSON COMPANIES) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PEAK (HEALTHPEAK PROPERTIES) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- PEG (Public Serv. Enterprise) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PENN (Penn National Gaming) First Date:3-Jan-2007 -> Last Date:15-Feb-2022
- PEP (PepsiCo) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PFE (Pfizer) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PFG (Principal Financial Group) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PG (Procter & Gamble) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PGR (Progressive) First Date:26-Apr-2007 -> Last Date:15-Feb-2022
- PH (Parker-Hannifin) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PHM (Pulte Homes) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PKG (Packaging Corporation of America) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PKI (PerkinElmer) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PLD (Prologis) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PLL (PIEDMONT LITHIUM LIMITED) First Date:22-May-2008 -> Last Date:15-Feb-2022
- PM (Philip Morris International) First Date:31-Mar-2008 -> Last Date:15-Feb-2022
- PNC (PNC Financial Services) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PNR (Pentair plc) First Date:17-Sep-2012 -> Last Date:15-Feb-2022
- PNW (Pinnacle West Capital) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- POOL (Pool Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PPG (PPG Industries) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PPL (PPL) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PRGO (Perrigo) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PRI (Primerica) First Date:1-Apr-2010 -> Last Date:15-Feb-2022
- PRU (Prudential Financial) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PSA (Public Storage) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PSX (Phillips 66) First Date:1-May-2012 -> Last Date:15-Feb-2022
- PTC (PTC) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- PVH (PVH) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PWR (Quanta Services) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PXD (Pioneer Natural Resources) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- PYPL (PayPal) First Date:6-Jul-2015 -> Last Date:15-Feb-2022
- QCOM (QUALCOMM) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- QGEN (Qiagen NV) First Date:15-Feb-2005 -> Last Date:15-Feb-2022
- QRVO (Qorvo) First Date:2-Jan-2015 -> Last Date:15-Feb-2022
- R (RYDER SYSTEM) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RCL (Royal Caribbean Cruises Ltd) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RE (Everest Re Group Ltd.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- REG (Regency Centers Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- REGN (Regeneron) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RF (Regions Financial) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RHI (Robert Half International) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RIG (TRANSOCEAN LTD.) First Date:19-Dec-2008 -> Last Date:15-Feb-2022
- RJF (Raymond James Financial) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RL (Polo Ralph Lauren) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RLGY (Realogy Holdings) First Date:11-Oct-2012 -> Last Date:15-Feb-2022
- RMD (ResMed) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ROK (Rockwell Automation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ROL (Rollins) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ROP (Roper Technologies) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- ROST (Ross Stores) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RRC (RANGE RESOURCES CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RRD (R.R. DONNELLEY & SONS COMPANY) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RSG (Republic Services Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- RTX (Raytheon Co.) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- RYAAY (Ryanair Holdings plc) First Date:11-Feb-2013 -> Last Date:15-Feb-2022
- S (SPRINT CORPORATION) First Date:3-Oct-2005 -> Last Date:15-Feb-2022
- SAIC (SCIENCE APPLICATIONS INTERNATIONAL CORPORATION) First Date:16-Sep-2013 -> Last Date:15-Feb-2022
- SANM (Sanmina) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- SBAC (SBA Communications) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SBNY (Signature Bank) First Date:4-May-2007 -> Last Date:15-Feb-2022
- SBUX (Starbucks) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SCHW (Charles Schwab Corporation) First Date:5-Mar-2010 -> Last Date:15-Feb-2022
- SE (SEA LIMITED) First Date:16-May-2007 -> Last Date:15-Feb-2022
- SEDG (SolarEdge Technologies) First Date:26-Mar-2015 -> Last Date:15-Feb-2022
- SEE (Sealed Air) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SHW (Sherwin-Williams) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SIG (SIGNET JEWELERS LIMITED) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SIRI (Sirius XM Holdings Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SITC (SITE Centers) First Date:1-May-2007 -> Last Date:15-Feb-2022
- SIVB (SVB Financial) First Date:1-Mar-2006 -> Last Date:15-Feb-2022
- SJM (JM Smucker) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SLB (Schlumberger Ltd.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SLG (SL Green Realty) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SLM (SLM CORPORATION) First Date:12-Dec-2011 -> Last Date:15-Feb-2022
- SNA (Snap-on) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SNPS (Synopsys) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SO (Southern Co.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SPG (Simon Property Group Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SPGI (S&P Global) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- SRCL (STERICYCLE) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SRE (Sempra Energy) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SSP (E. W. Scripps Co) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- STE (STERIS plc) First Date:3-Nov-2015 -> Last Date:15-Feb-2022
- STT (State Street) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- STX (Seagate Technology) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- STZ (Constellation Brands) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SUN (SUNOCO LP) First Date:4-May-2012 -> Last Date:15-Feb-2022
- SWK (Stanley Black & Decker) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SWKS (Skyworks Solutions) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SWN (SOUTHWESTERN ENERGY COMPANY) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SYF (Synchrony Financial) First Date:31-Jul-2014 -> Last Date:15-Feb-2022
- SYK (Stryker) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- SYY (Sysco) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- T (AT&T) First Date:3-Jan-2006 -> Last Date:15-Feb-2022
- TAP (Molson Coors Brewing Company) First Date:1-Mar-2005 -> Last Date:15-Feb-2022
- TDC (TERADATA CORPORATION) First Date:1-Oct-2007 -> Last Date:15-Feb-2022
- TDG (TransDigm Group) First Date:15-Mar-2006 -> Last Date:15-Feb-2022
- TDY (Teledyne Technologies Incorporated) First Date:3-Jan-2007 -> Last Date:15-Feb-2022
- TEL (TE Connectivity Ltd.) First Date:26-Jun-2009 -> Last Date:15-Feb-2022
- TER (TERADYNE) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TEVA (Teva Pharmaceutical Industries Ltd) First Date:11-Feb-2013 -> Last Date:15-Feb-2022
- TEX (Terex) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TFC (TRUIST FINANCIAL CORPORATION) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- TFX (Teleflex Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TGNA (TEGNA) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- TGT (Target) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- THC (TENET HEALTHCARE CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TJX (TJX Companies) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TMO (Thermo Fisher Scientific) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TMUS (T-MOBILE US) First Date:16-May-2007 -> Last Date:15-Feb-2022
- TPR (Tapestry) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- TRIP (TripAdvisor) First Date:7-Dec-2011 -> Last Date:15-Feb-2022
- TRMB (Trimble) First Date:3-Jan-2007 -> Last Date:15-Feb-2022
- TROW (T. Rowe Price Group) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TRV (The Travelers Companies) First Date:27-Feb-2007 -> Last Date:15-Feb-2022
- TSCO (Tractor Supply Company) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TSLA (Tesla Inc) First Date:29-Jun-2010 -> Last Date:15-Feb-2022
- TSN (Tyson Foods) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TTWO (Take-Two Interactive) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TUP (Tupperware Brands) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TWTR (Twitter) First Date:7-Nov-2013 -> Last Date:15-Feb-2022
- TXN (Texas Instruments) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TXT (Textron) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- TYL (Tyler Technologies) First Date:3-Jan-2007 -> Last Date:15-Feb-2022
- UA (Under Armour Class C) First Date:23-Mar-2016 -> Last Date:15-Feb-2022
- UAA (Under Armour Class A) First Date:14-May-2007 -> Last Date:15-Feb-2022
- UAL (United Continental Holdings) First Date:1-Oct-2010 -> Last Date:15-Feb-2022
- UCL (Unocal Co) First Date:10-Jun-2020 -> Last Date:15-Feb-2022
- UDR (UDR Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- UHS (Universal Health Services) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ULTA (Ulta Beauty) First Date:25-Oct-2007 -> Last Date:15-Feb-2022 
- UNH (United Health Group) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- UNM (Unum Group) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- UNP (Union Pacific) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- UPC (Union Planters) First Date:23-Mar-2021 -> Last Date:15-Feb-2022
- UPS (United Parcel Service) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- URBN (URBAN OUTFITTERS) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- URI (United Rentals) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- USB (U.S. Bancorp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- V (Visa) First Date:19-Mar-2008 -> Last Date:15-Feb-2022
- VAL (Ensco plc) First Date:3-Sep-2019 -> Last Date:15-Feb-2022
- VFC (V.F.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- VIAV (VIAVI SOLUTIONS) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- VLO (Valero Energy) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- VMC (Vulcan Materials) First Date:1-May-2007 -> Last Date:15-Feb-2022
- VNO (Vornado Realty Trust) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- VNT (Vontier) First Date:24-Sep-2020 -> Last Date:15-Feb-2022
- VOD (Vodafone Group Plc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- VRSK (Verisk Analytics) First Date:7-Oct-2009 -> Last Date:15-Feb-2022
- VRSN (Verisign) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- VRTS (Veritas Software) First Date:2-Jan-2009 -> Last Date:15-Feb-2022
- VRTX (Vertex Pharmaceuticals Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- VTR (Ventas Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- VTRS (Viatris) First Date:12-Nov-2020 -> Last Date:15-Feb-2022
- VZ (Verizon Communications) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WAB (Wabtec Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WAT (Waters Corporation) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WBA (Walgreens Boots Alliance) First Date:31-Dec-2014 -> Last Date:15-Feb-2022
- WDC (Western Digital) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WEC (Wec Energy Group Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WELL (Welltower) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- WFC (Wells Fargo) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WHR (Whirlpool) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WLTW (Willis Towers Watson) First Date:5-Jan-2016 -> Last Date:15-Feb-2022
- WM (Waste Management) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- WMB (Williams Cos.) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WMT (Walmart) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WOR (Worthington Industries) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WRB (W. R. Berkley Corporation) First Date:27-Apr-2007 -> Last Date:15-Feb-2022
- WRK (WestRock) First Date:24-Jun-2015 -> Last Date:15-Feb-2022
- WST (West Pharmaceutical Services) First Date:3-Jan-2007 -> Last Date:15-Feb-2022
- WU (Western Union Co) First Date:2-Oct-2006 -> Last Date:15-Feb-2022
- WY (Weyerhaeuser) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- WYNN (Wynn Resorts Ltd) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- X (UNITED STATES STEEL CORPORATION) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- XEL (Xcel Energy Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- XLNX (Xilinx) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- XOM (Exxon Mobil) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- XRAY (Dentsply Sirona) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- XRX (Xerox) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- XYL (Xylem) First Date:13-Oct-2011 -> Last Date:15-Feb-2022
- YUM (Yum! Brands Inc) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ZBH (Zimmer Biomet Holdings) First Date:30-Apr-2007 -> Last Date:15-Feb-2022
- ZBRA (Zebra Technologies) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ZION (Zions Bancorp) First Date:3-Jan-2005 -> Last Date:15-Feb-2022
- ZTS (Zoetis) First Date:1-Feb-2013 -> Last Date:15-Feb-2022
- AABA-DELISTED () First Date:27-Apr-2007 -> Last Date:2-Oct-2019
- AAXN-DELISTED (Axon Enterprise) First Date:1-May-2007 -> Last Date:22-Jan-2021
- ABI-DELISTED (SAFETY FIRST TRUST SERIES 2009-) First Date:30-Apr-2007 -> Last Date:28-Apr-2014
- ABK-DELISTED (AMBAC FINANCIAL GROUP INC) First Date:1-Jan-2005 -> Last Date:9-Nov-2010
- ABS-DELISTED (Albertsons) First Date:1-Jan-2005 -> Last Date:1-Jun-2006
- ACAS-DELISTED (American Capital) First Date:1-Jan-2005 -> Last Date:3-Jan-2017
- ACIA-DELISTED (Acacia Communications) First Date:13-May-2016 -> Last Date:26-Feb-2021
- ACXM-DELISTED (Acxiom Holdings) First Date:1-Jan-2005 -> Last Date:1-Oct-2018
- ADSW-DELISTED (Advanced Disposal Services) First Date:6-Oct-2016 -> Last Date:29-Oct-2020
- AEGN-DELISTED (Aegion) First Date:3-May-2007 -> Last Date:14-May-2021
- AET-DELISTED (AETNA COMMON STOCK) First Date:1-Jan-2005 -> Last Date:28-Nov-2018
- AGN-DELISTED (Allergan) First Date:30-Apr-2007 -> Last Date:8-May-2020
- AIMT-DELISTED () First Date:6-Aug-2015 -> Last Date:12-Oct-2020
- AKCA-DELISTED () First Date:14-Jul-2017 -> Last Date:9-Oct-2020
- AKS-DELISTED (AK STEEL HOLDING CORPORATION) First Date:3-Jan-2005 -> Last Date:12-Mar-2020
- ALSK-DELISTED (Alaska Comm Sys) First Date:1-May-2007 -> Last Date:22-Jul-2021
- ALXN-DELISTED (Alexion Pharmaceuticals) First Date:3-Jan-2005 -> Last Date:20-Jul-2021
- AMAG-DELISTED () First Date:1-May-2007 -> Last Date:13-Nov-2020
- AMCC-DELISTED (Applied Micro Circuits) First Date:1-May-2007 -> Last Date:26-Jan-2017
- AMLN-DELISTED (AMYLIN PHARMACEUTICALS) First Date:1-Jan-2005 -> Last Date:8-Aug-2012
- AMTBB-DELISTED (Amerant Bancorp Inc. Class B Common Stock) First Date:29-Aug-2018 -> Last Date:17-Nov-2021
- AMTD-DELISTED (TD Ameritrade Holding Corporation) First Date:25-Apr-2012 -> Last Date:5-Oct-2020
- ANDV-DELISTED (Andeavor) First Date:30-Apr-2007 -> Last Date:28-Sep-2018
- ANDW-DELISTED (Andrew) First Date:3-Jan-2005 -> Last Date:27-Dec-2007
- ANH-DELISTED (Anworth Mortgage Asset) First Date:3-May-2007 -> Last Date:19-Mar-2021
- ANR-DELISTED (ALPHA NATURAL RESOURCES C) First Date:15-Feb-2005 -> Last Date:15-Jul-2015
- APC-DELISTED (Anadarko Petroleum Corp) First Date:1-Jan-2005 -> Last Date:8-Aug-2019
- APOL-DELISTED (APOLLO EDUCATION GROUP) First Date:1-Jan-2005 -> Last Date:31-Jan-2017
- ARA-DELISTED (American Renal Associates) First Date:21-Apr-2016 -> Last Date:22-Jan-2021
- ARCP-DELISTED (VEREIT) First Date:7-Sep-2011 -> Last Date:30-Jul-2015
- ARD-DELISTED (Ardagh Group S.A.) First Date:15-Mar-2017 -> Last Date:5-Oct-2021
- ARG-DELISTED (AIRGAS COMMON STOCK) First Date:1-Jan-2005 -> Last Date:20-May-2016
- ASBC-DELISTED (Associated Banc-Corp (old ticker)) First Date:1-Jan-2005 -> Last Date:22-Dec-2014
- ASPL-DELISTED (Aspirational Consumer Lifestyle Corp.) First Date:13-Nov-2020 -> Last Date:13-Jul-2021
- AT-DELISTED (ATLANTIC POWER CORPORATION) First Date:23-Jul-2010 -> Last Date:14-May-2021
- AV-DELISTED (AVIVA PLC UNSPONSORED ADR (UK)) First Date:20-Oct-2009 -> Last Date:22-Dec-2016
- AVP-DELISTED (AVON PRODUCTS) First Date:1-Jan-2005 -> Last Date:3-Jan-2020
- BBT-DELISTED (BB&T Corporation) First Date:1-Jan-2005 -> Last Date:6-Dec-2019
- BCEI-DELISTED (Bonanza Creek Energy) First Date:15-Dec-2011 -> Last Date:1-Nov-2021
- BCR-DELISTED (C.R. BARD COMMON STOCK) First Date:1-Jan-2005 -> Last Date:28-Dec-2017
- BEAM-DELISTED First Date:1-May-2007 -> Last Date:30-Apr-2014
- BEAT-DELISTED (Biotelemetry) First Date:1-Aug-2013 -> Last Date:8-Feb-2021
- BFYT-DELISTED () First Date:8-Feb-2013 -> Last Date:20-Aug-2020
- BHGE-DELISTED (Baker Hughes) First Date:5-Jul-2017 -> Last Date:17-Oct-2019
- BHI-DELISTED (BAKER HUGHES INCORPORATED COMMO) First Date:1-Jan-2005 -> Last Date:3-Jul-2017
- BIVV-DELISTED (Bioverativ) First Date:12-Jan-2017 -> Last Date:8-Mar-2018
- BLS-DELISTED (BellSouth) First Date:3-Jan-2005 -> Last Date:29-Dec-2006
- BMC-DELISTED (BMC SOFTWARE) First Date:1-Jan-2005 -> Last Date:10-Sep-2013
- BMCH-DELISTED () First Date:9-Aug-2013 -> Last Date:31-Dec-2020
- BMS-DELISTED (BEMIS COMPANY COMMON STOC) First Date:1-Jan-2005 -> Last Date:10-Jun-2019
- BOCH-DELISTED (Bank Of Commerce) First Date:16-May-2007 -> Last Date:30-Sep-2021
- BPFH-DELISTED (Boston Private Financial) First Date:8-May-2007 -> Last Date:30-Jun-2021
- BPY-DELISTED (Brookfield Property Partners L.P.) First Date:22-Mar-2013 -> Last Date:26-Jul-2021
- BPYU-DELISTED (Brookfield Property Reit) First Date:28-Aug-2018 -> Last Date:26-Jul-2021
- BRCM-DELISTED (BROADCOM CORP.) First Date:1-Jan-2005 -> Last Date:29-Jan-2016
- BREW-DELISTED () First Date:16-May-2007 -> Last Date:29-Sep-2020
- BRKS-DELISTED (Brooks Automation) First Date:3-Jan-2007 -> Last Date:30-Nov-2021
- BSTC-DELISTED () First Date:16-May-2007 -> Last Date:1-Dec-2020
- BWC-DELISTED (BWX Technologies (old ticker)) First Date:1-Nov-2005 -> Last Date:30-Jun-2015
- BXG-DELISTED (Bluegreen Vacations Corp) First Date:17-Nov-2017 -> Last Date:5-May-2021
- BXLT-DELISTED () First Date:15-Jun-2015 -> Last Date:2-Jun-2016
- BXS-DELISTED (BancorpSouth Bank) First Date:7-Nov-2017 -> Last Date:28-Oct-2021
- CA-DELISTED (CA TECHNOLOGIES) First Date:1-Jan-2005 -> Last Date:2-Nov-2018
- CAI-DELISTED (Cai International) First Date:16-May-2007 -> Last Date:22-Nov-2021
- CAM-DELISTED (CAMERON INTERNATIONAL CORPORATI) First Date:1-Jan-2005 -> Last Date:1-Apr-2016
- CATB-DELISTED (Catabasis Pharmaceuticals) First Date:25-Jun-2015 -> Last Date:7-Sep-2021
- CATM-DELISTED (Cardtronics) First Date:11-Dec-2007 -> Last Date:18-Jun-2021
- CBB-DELISTED (Cincinnati Bell) First Date:20-Dec-2012 -> Last Date:3-Sep-2021
- CBE-DELISTED (COOPER INDUSTRIES PLC (IRELAN) First Date:1-Jan-2005 -> Last Date:30-Nov-2012
- CBG-DELISTED (CBRE GROUP INC COMMON STOCK CLA) First Date:1-Jan-2005 -> Last Date:19-Mar-2018
- CBMG-DELISTED (Cellular Biomedicine Group In) First Date:4-Jun-2007 -> Last Date:19-Feb-2021
- CCC-DELISTED (Clarivate Plc) First Date:29-Oct-2018 -> Last Date:29-Jan-2021
- CCE-DELISTED (COCA-COLA ENTERPRISES COM) First Date:1-Jan-2005 -> Last Date:6-Nov-2018
- CCIV-DELISTED (Churchill Capital IV) First Date:18-Sep-2020 -> Last Date:23-Jul-2021
- CEG-DELISTED (CONSTELLATION ENERGY GROUP INC) First Date:1-Jan-2005 -> Last Date:12-Mar-2012
- CELG-DELISTED (Celgene) First Date:1-Jan-2005 -> Last Date:20-Nov-2019
- CERC-DELISTED (Cerecor) First Date:13-Nov-2015 -> Last Date:24-Aug-2021
- CETV-DELISTED () First Date:2-May-2007 -> Last Date:12-Oct-2020
- CFN-DELISTED (CAREFUSION CORPORATION COMMON S) First Date:1-Sep-2009 -> Last Date:16-Mar-2015
- CHMA-DELISTED (Chiasma) First Date:16-Jul-2015 -> Last Date:5-Aug-2021
- CHUBK-DELISTED (CommerceHub) First Date:22-Jul-2016 -> Last Date:18-May-2018
- CHU-DELISTED (China Unicom (Hong Kong) Limited) First Date:26-Apr-2007 -> Last Date:8-Jan-2021
- CIN-DELISTED (Cinergy) First Date:3-Jan-2005 -> Last Date:31-Mar-2006
- CKH-DELISTED (Seacor) First Date:26-Apr-2007 -> Last Date:15-Apr-2021
- CLCT-DELISTED (Collectors Universe) First Date:16-May-2007 -> Last Date:5-Feb-2021
- CLDR-DELISTED (Cloudera) First Date:28-Apr-2017 -> Last Date:7-Oct-2021
- CLGX-DELISTED (CoreLogic) First Date:2-Jun-2010 -> Last Date:3-Jun-2021
- CLNC-DELISTED (Colony Credit Real Estate) First Date:1-Feb-2018 -> Last Date:14-May-2021
- CLNY-DELISTED (Colony Capital) First Date:11-Jan-2017 -> Last Date:14-May-2021
- CMCSK-DELISTED (COMCAST CORPORATION) First Date:1-Jan-2005 -> Last Date:11-Dec-2015
- CMD-DELISTED (Cantel Medical Corp) First Date:8-May-2007 -> Last Date:1-Jun-2021
- CMO-DELISTED (Capstead Mortgage) First Date:7-May-2007 -> Last Date:18-Oct-2021
- CMVT-DELISTED (Comverse Technology) First Date:2-Jan-2004 -> Last Date:4-Feb-2013
- CMX-DELISTED (Caremark Rx) First Date:3-Jan-2005 -> Last Date:21-Mar-2007
- CNBKA-DELISTED (Century Bancorp) First Date:16-May-2007 -> Last Date:12-Nov-2021
- CNST-DELISTED (Constellation Pharmaceuticals) First Date:19-Jul-2018 -> Last Date:14-Jul-2021
- COG-DELISTED (Cabot Oil & Gas) First Date:2-Jan-2004 -> Last Date:1-Oct-2021
- COH-DELISTED (COACH COMMON STOCK) First Date:1-Jan-2005 -> Last Date:30-Oct-2017
- COL-DELISTED (ROCKWELL COLLINS COMMON S) First Date:1-Jan-2005 -> Last Date:26-Nov-2018
- CORE-DELISTED (Core Mark Holding Co) First Date:26-Jan-2017 -> Last Date:1-Sep-2021
- COV-DELISTED (COVIDIEN PLC. ORDINARY SHARES) First Date:2-Jul-2007 -> Last Date:26-Jan-2015
- CPGX-DELISTED () First Date:17-Jun-2015 -> Last Date:30-Jun-2016
- CPL-DELISTED (Carolina Power & Light) First Date:1-Jan-2005 -> Last Date:27-Jan-2020
- CPN-DELISTED (Calpine) First Date:7-Feb-2008 -> Last Date:8-Mar-2018
- CREE-DELISTED (Cree) First Date:3-Jan-2007 -> Last Date:1-Oct-2021
- CSC-DELISTED (COMPUTER SCIENCES CORPORATION C) First Date:1-Jan-2005 -> Last Date:31-Mar-2017
- CSOD-DELISTED (Cornerstone OnDemand) First Date:17-Mar-2011 -> Last Date:14-Oct-2021
- CSRA-DELISTED () First Date:16-Nov-2015 -> Last Date:3-Apr-2018
- CTB-DELISTED (Cooper Tire & Rubber Co.) First Date:3-Jan-2005 -> Last Date:4-Jun-2021
- CTL-DELISTED (CenturyLink Inc) First Date:2-Jan-2004 -> Last Date:17-Sep-2020
- CTRP-DELISTED (CTRIP.COM INTERNATIONAL LTD.) First Date:1-Jan-2005 -> Last Date:4-Nov-2019
- CTRX-DELISTED (CATAMARAN CORPORATION) First Date:23-Jun-2006 -> Last Date:23-Jul-2015
- CTX-DELISTED (CENTEX CORP) First Date:30-Apr-2007 -> Last Date:31-Aug-2018
- CUB-DELISTED (Cubic) First Date:8-May-2007 -> Last Date:24-May-2021
- CU-DELISTED (CUC International) First Date:1-Jan-2005 -> Last Date:18-Dec-2015
- CVA-DELISTED (Covanta Holding) First Date:2-May-2007 -> Last Date:29-Nov-2021
- CVC-DELISTED (CABLEVISION SYSTEMS CORPORATION) First Date:1-Jan-2005 -> Last Date:20-Jun-2016
- CVG-DELISTED (CONVERGYS CORPORATION COMMON ST) First Date:1-Jan-2005 -> Last Date:4-Oct-2018
- CVH-DELISTED (COVENTRY HEALTH CARE COMM) First Date:1-Jan-2005 -> Last Date:6-May-2013
- CXO-DELISTED (Concho Resources) First Date:3-Aug-2007 -> Last Date:15-Jan-2021
- CZZ-DELISTED (Cosan Limited) First Date:16-Aug-2007 -> Last Date:5-Mar-2021
- DDR-DELISTED (DDR CORP. COMMON STOCK) First Date:1-Jan-2005 -> Last Date:11-Oct-2018
- DEH-DELISTED (D8 Holdings) First Date:4-Sep-2020 -> Last Date:16-Sep-2021
- DF-DELISTED (DEAN FOODS COMPANY COMMON STOCK) First Date:1-Jan-2005 -> Last Date:11-Nov-2019
- DLPH-DELISTED (DELPHI TECHNOLOGIES PLC) First Date:15-Nov-2017 -> Last Date:1-Oct-2020
- DNK-DELISTED (Phoenix Tree Holdings) First Date:17-Jan-2020 -> Last Date:15-Mar-2021
- DNKN-DELISTED (Dunkin' Brands Group) First Date:27-Jul-2011 -> Last Date:14-Dec-2020
- DNR-DELISTED (DENBURY RESOURCES) First Date:3-Jan-2005 -> Last Date:29-Jul-2020
- DO-DELISTED (DIAMOND OFFSHORE DRILLING) First Date:3-Jan-2005 -> Last Date:24-Apr-2020
- DPH-DELISTED (Delphi (Old)) First Date:3-Jan-2005 -> Last Date:10-Oct-2005
- DPS-DELISTED (DR PEPPER SNAPPLE GROUP INC DR) First Date:7-May-2008 -> Last Date:9-Jul-2018
- DSSI-DELISTED (Diamond S Shipping) First Date:28-Mar-2019 -> Last Date:15-Jul-2021
- DV-DELISTED (DEVRY COMMON STOCK) First Date:1-Jan-2005 -> Last Date:23-May-2017
- DWDP-DELISTED (DowDuPont) First Date:27-Apr-2007 -> Last Date:31-May-2019
- DYN-DELISTED () First Date:3-Oct-2012 -> Last Date:6-Apr-2018
- EBSB-DELISTED (Meridian Bancorp Common) First Date:23-Jan-2008 -> Last Date:12-Nov-2021
- ECHO-DELISTED (Echo Global Logistics) First Date:2-Oct-2009 -> Last Date:22-Nov-2021
- EDS-DELISTED (EXCEED COMPANY LTD.) First Date:30-Apr-2007 -> Last Date:29-Apr-2015
- EE-DELISTED (El Paso Electric Company) First Date:3-Jan-2007 -> Last Date:29-Jul-2020
- EGOV-DELISTED (Nic) First Date:30-Apr-2007 -> Last Date:20-Apr-2021
- EIDX-DELISTED (Eidos Therapeutics) First Date:20-Jun-2018 -> Last Date:25-Jan-2021
- EIGI-DELISTED (Endurance International Group) First Date:25-Oct-2013 -> Last Date:10-Feb-2021
- EMC-DELISTED (EMC CORPORATION COMMON STOCK) First Date:1-Jan-2005 -> Last Date:6-Sep-2016
- EOP-DELISTED (Equity Office Properties Trust) First Date:3-Jan-2005 -> Last Date:9-Feb-2007
- EP-DELISTED (EL PASO CORPORATION COMMON STOC) First Date:1-Jan-2005 -> Last Date:24-May-2012
- EQM-DELISTED (EQM Midstream Partners LP) First Date:27-Jun-2012 -> Last Date:16-Jun-2020
- ERI-DELISTED (Eldorado Resorts) First Date:3-Nov-2014 -> Last Date:20-Jul-2020
- ESRX-DELISTED (EXPRESS SCRIPTS HOLDING COMPANY) First Date:1-Jan-2005 -> Last Date:20-Dec-2018
- ESV-DELISTED (ENSCO PLC AMERICAN DEPOSITARY S) First Date:1-Jan-2005 -> Last Date:30-Jul-2019
- ETFC-DELISTED (E*Trade) First Date:16-May-2007 -> Last Date:1-Oct-2020
- ETH-DELISTED (Ethan Allen Interiors) First Date:26-Apr-2007 -> Last Date:13-Aug-2021
- ETM-DELISTED (Entercom Communications) First Date:27-Apr-2007 -> Last Date:26-Feb-2021
- EV-DELISTED (Eaton Vance) First Date:3-Jan-2007 -> Last Date:26-Feb-2021
- EVHC-DELISTED () First Date:14-Aug-2013 -> Last Date:10-Oct-2018
- FBM-DELISTED (Foundation Building Materials) First Date:10-Feb-2017 -> Last Date:28-Jan-2021
- FCAU-DELISTED (Fiat Chrysler Automobiles N.V.) First Date:5-Mar-2015 -> Last Date:5-Jan-2021
- FCBP-DELISTED (First Choice Bancorp) First Date:2-May-2007 -> Last Date:21-Jul-2021
- FDC-DELISTED (FIRST DATA CORP) First Date:1-Jan-2005 -> Last Date:26-Jul-2019
- FDO-DELISTED (FAMILY DOLLAR STORES COMM) First Date:1-Jan-2005 -> Last Date:6-Jul-2015
- FEYE-DELISTED (FireEye) First Date:20-Sep-2013 -> Last Date:4-Oct-2021
- FFG-DELISTED (Fbl Financial Group) First Date:10-May-2007 -> Last Date:25-May-2021
- FI-DELISTED (Franks International) First Date:9-Aug-2013 -> Last Date:1-Oct-2021
- FII-DELISTED (FEDERATED INVESTORS) First Date:1-Jan-2005 -> Last Date:31-Jan-2020
- FIT-DELISTED () First Date:18-Jun-2015 -> Last Date:13-Jan-2021
- FLIR-DELISTED (FLIR Systems) First Date:3-Jan-2005 -> Last Date:13-May-2021
- FLXN-DELISTED (Flexion Therapeutics Com) First Date:12-Feb-2014 -> Last Date:18-Nov-2021
- FPRX-DELISTED (Five Prime Therapeutics) First Date:18-Sep-2013 -> Last Date:15-Apr-2021
- FRX-DELISTED (FOREST LABORATORIES CLASS) First Date:1-Jan-2005 -> Last Date:1-Apr-2021
- FSB-DELISTED () First Date:26-Mar-2015 -> Last Date:14-Aug-2020
- FSCT-DELISTED () First Date:27-Oct-2017 -> Last Date:14-Aug-2020
- FSH-DELISTED (Fisher Scientific Int'l) First Date:3-Jan-2005 -> Last Date:9-Nov-2006
- FTR-DELISTED (FRONTIER COMMUNICATIONS CORPORATION) First Date:31-Jul-2008 -> Last Date:23-Apr-2020
- FWLT-DELISTED (FOSTER WHEELER AG) First Date:3-Jun-2005 -> Last Date:3-Dec-2014
- GAS-DELISTED (AGL RESOURCES COMMON STOC) First Date:1-Jan-2005 -> Last Date:30-Jun-2016
- GCAP-DELISTED () First Date:15-Dec-2010 -> Last Date:30-Jul-2020
- GDI-DELISTED (Gardner Denver) First Date:12-May-2017 -> Last Date:28-Feb-2020
- GDT-DELISTED (Guidant) First Date:3-Jan-2005 -> Last Date:21-Apr-2006
- GDW-DELISTED (Golden West Financial) First Date:3-Jan-2005 -> Last Date:29-Sep-2006
- GFN-DELISTED (General Finance) First Date:17-May-2007 -> Last Date:25-May-2021
- GGP-DELISTED (GENERAL GROWTH PROPERTIES) First Date:1-Jan-2005 -> Last Date:27-Aug-2018
- GLIBA-DELISTED (GCI Liberty) First Date:12-Mar-2018 -> Last Date:18-Dec-2020
- GLK-DELISTED (Great Lakes Chemical) First Date:1-Jun-2006 -> Last Date:15-Feb-2008
- GLUU-DELISTED (Glu Mobile) First Date:16-May-2007 -> Last Date:28-Apr-2021
- GMCR-DELISTED (KEURIG GREEN MOUNTAIN) First Date:1-Jan-2005 -> Last Date:2-Mar-2016
- GNCMA-DELISTED (GCI Liberty) First Date:1-Jan-2005 -> Last Date:8-Mar-2018
- GNMK-DELISTED (Genmark Diagnostics) First Date:28-May-2010 -> Last Date:21-Apr-2021
- GPX-DELISTED (Gp Strategies) First Date:16-May-2007 -> Last Date:14-Oct-2021
- GRA-DELISTED (W.R. GRACE & CO.) First Date:3-Jan-2005 -> Last Date:21-Sep-2021
- GR-DELISTED (GOODRICH CORPORATION (THE) COMM) First Date:1-Jan-2005 -> Last Date:26-Jul-2012
- GSB-DELISTED () First Date:19-Jul-2007 -> Last Date:27-Aug-2020
- GSX-DELISTED (GSX Techedu) First Date:6-Jun-2019 -> Last Date:12-Apr-2021
- GTT-DELISTED (Gtt Communications) First Date:17-Jun-2013 -> Last Date:2-Jul-2021
- GTW-DELISTED (Gateway) First Date:3-Jan-2005 -> Last Date:16-Oct-2007
- GWPH-DELISTED (GW Pharmaceuticals plc) First Date:1-May-2013 -> Last Date:4-May-2021
- HAR-DELISTED (HARMAN INTERNATIONAL INDUSTRIES) First Date:1-Jan-2005 -> Last Date:10-Mar-2017
- HBHC-DELISTED (Hancock Holding) First Date:1-Jan-2005 -> Last Date:24-May-2018
- HCBK-DELISTED (HUDSON CITY BANCORP) First Date:1-Jan-2005 -> Last Date:30-Oct-2015
- HCHC-DELISTED (Hc2) First Date:23-Jun-2011 -> Last Date:17-Sep-2021
- HCN-DELISTED (HEALTH CARE REIT COMMON S) First Date:1-Jan-2005 -> Last Date:27-Feb-2018
- HCP-DELISTED (HCP) First Date:1-Jan-2005 -> Last Date:4-Nov-2019
- HCR-DELISTED (HI-CRUSH) First Date:3-Jun-2019 -> Last Date:10-Jul-2020
- HDS-DELISTED (HD Supply Holdings) First Date:14-Jun-2007 -> Last Date:23-Dec-2020
- HLS-DELISTED (HLS Therapeutics) First Date:1-Nov-2006 -> Last Date:29-Dec-2017
- HMA-DELISTED (Health Management Associates) First Date:3-Jan-2005 -> Last Date:24-Jan-2014
- HMSY-DELISTED (HMS Holdings) First Date:3-Jan-2007 -> Last Date:31-Mar-2021
- HMT-DELISTED (Host Marriott Corp) First Date:1-Jan-2005 -> Last Date:17-Apr-2006
- HNZ-DELISTED (H.J. HEINZ COMPANY COMMON STOCK) First Date:1-Jan-2005 -> Last Date:7-Jun-2013
- HOME-DELISTED (At Home Group) First Date:4-Jun-2007 -> Last Date:22-Jul-2021
- HOT-DELISTED (STARWOOD HOTELS & RESORTS WORLD) First Date:1-Jan-2005 -> Last Date:22-Sep-2016
- HRS-DELISTED (Harris Corporation) First Date:1-Jan-2005 -> Last Date:28-Jun-2019
- HSH-DELISTED (HILLSHIRE BRANDS COMPANY) First Date:12-Jun-2012 -> Last Date:28-Aug-2014
- HSP-DELISTED (HOSPIRA INC) First Date:1-Jan-2005 -> Last Date:2-Sep-2015
- HTZ-DELISTED () First Date:20-Jun-2016 -> Last Date:29-Oct-2020
- HUD-DELISTED () First Date:1-Feb-2018 -> Last Date:30-Nov-2020
- IBKC-DELISTED (IBERIABANK Corporation) First Date:3-Jan-2007 -> Last Date:1-Jul-2020
- IMMU-DELISTED (Immunomedics) First Date:3-Jan-2007 -> Last Date:22-Oct-2020
- IMS-DELISTED (IMS Health Holdings) First Date:16-May-2007 -> Last Date:30-Sep-2016
- INOV-DELISTED (Inovalon Holdings) First Date:12-Feb-2015 -> Last Date:23-Nov-2021
- IPHI-DELISTED (Inphi Corporation) First Date:11-Nov-2010 -> Last Date:20-Apr-2021
- JCAP-DELISTED () First Date:27-Mar-2015 -> Last Date:5-Nov-2020
- JCOM-DELISTED (J2 Global) First Date:3-Jan-2007 -> Last Date:7-Oct-2021
- JCP-DELISTED (J.C. PENNEY COMPANY HOLDING COMPANY) First Date:3-Jan-2005 -> Last Date:18-May-2020
- JEC-DELISTED (Jacobs Engineering Group) First Date:1-Jan-2005 -> Last Date:9-Dec-2019
- JNS-DELISTED (JANUS CAPITAL GROUP CMN S) First Date:1-Jan-2005 -> Last Date:26-May-2017
- JNY-DELISTED (JONES GROUP (THE) COMMON) First Date:1-Jan-2005 -> Last Date:8-Apr-2014
- JOY-DELISTED (JOY GLOBAL COMMON STOCK) First Date:30-Apr-2007 -> Last Date:5-Apr-2017
- JOYG-DELISTED () First Date:1-Jan-2005 -> Last Date:5-Dec-2011
- KATE-DELISTED (Kate Spade & Co) First Date:30-Apr-2007 -> Last Date:11-Jul-2017
- KDMN-DELISTED (Kadmon) First Date:27-Jul-2016 -> Last Date:8-Nov-2021
- KFT-DELISTED (KRAFT FOODS COMMON STOCK) First Date:1-Jan-2005 -> Last Date:1-Oct-2012
- KIN-DELISTED (Kindred Biosciences Comm) First Date:12-Dec-2013 -> Last Date:27-Aug-2021
- KMG-DELISTED (Kerr-McGee) First Date:16-May-2007 -> Last Date:14-Nov-2018
- KNL-DELISTED (Knoll) First Date:4-May-2007 -> Last Date:19-Jul-2021
- KORS-DELISTED (MICHAEL KORS HOLDINGS LIMITED O) First Date:15-Dec-2011 -> Last Date:31-Dec-2018
- KRB-DELISTED (MBNA) First Date:3-Jan-2005 -> Last Date:30-Dec-2005
- KRFT-DELISTED (KRAFT FOODS GROUP) First Date:17-Sep-2012 -> Last Date:2-Jul-2015
- KRI-DELISTED (Knight-Ridder) First Date:3-Jan-2005 -> Last Date:27-Jun-2006
- LB-DELISTED (L Brands) First Date:27-Apr-2007 -> Last Date:2-Aug-2021
- LDL-DELISTED (Lydall) First Date:11-May-2007 -> Last Date:30-Sep-2021
- LEH-DELISTED (Lehman Brothers) First Date:1-Jan-2005 -> Last Date:17-Sep-2008
- LIVX-DELISTED (Livexlive Media) First Date:14-Dec-2017 -> Last Date:5-Oct-2021
- LIZ-DELISTED (Liz Claiborne) First Date:1-Jan-2005 -> Last Date:14-May-2012
- LLL-DELISTED (L-3 Communications Holdings) First Date:30-Apr-2007 -> Last Date:28-Jun-2019
- LLTC-DELISTED (LINEAR TECHNOLOGY CORPORATION) First Date:1-Jan-2005 -> Last Date:10-Mar-2017
- LMCA-DELISTED (LIBERTY MEDIA CORPORATION) First Date:1-Feb-2013 -> Last Date:24-Jan-2017
- LMCK-DELISTED () First Date:8-Aug-2014 -> Last Date:24-Jan-2017
- LM-DELISTED (LEGG MASON) First Date:3-Jan-2005 -> Last Date:31-Jul-2020
- LMNX-DELISTED (Luminex) First Date:25-Apr-2007 -> Last Date:13-Jul-2021
- LO-DELISTED (LORILLARD INC COMMON STOCK) First Date:10-Jun-2008 -> Last Date:11-Jun-2015
- LOGM-DELISTED (LogMeIn) First Date:1-Jul-2009 -> Last Date:28-Aug-2020
- LORL-DELISTED (Loral Space) First Date:7-May-2007 -> Last Date:18-Nov-2021
- LUK-DELISTED (LEUCADIA NATIONAL CORPORATION C) First Date:1-Jan-2005 -> Last Date:23-May-2018
- LVGO-DELISTED (Livongo Health) First Date:25-Jul-2019 -> Last Date:29-Oct-2020
- LVLT-DELISTED (LEVEL 3 COMMUNICATIONS CO) First Date:1-Jan-2005 -> Last Date:31-Oct-2017
- LVNTA-DELISTED (LIBERTY VENTURES) First Date:10-Aug-2012 -> Last Date:9-Mar-2018
- LXK-DELISTED (LEXMARK INTERNATIONAL COM) First Date:1-Jan-2005 -> Last Date:28-Nov-2016
- MAY-DELISTED (May Dept Stores) First Date:20-Jun-2007 -> Last Date:17-Aug-2012
- MDLA-DELISTED (Medallia) First Date:19-Jul-2019 -> Last Date:28-Oct-2021
- MEDI-DELISTED (MedImmune) First Date:3-Jan-2005 -> Last Date:18-Jun-2007
- MEET-DELISTED () First Date:4-May-2007 -> Last Date:3-Sep-2020
- MEL-DELISTED (Mellon Financial) First Date:3-Jan-2005 -> Last Date:29-Jun-2007
- MER-DELISTED (Merrill Lynch & Co) First Date:3-Jan-2005 -> Last Date:31-Dec-2008
- MERQ-DELISTED (Mercury Interactive) First Date:3-Jan-2005 -> Last Date:12-Aug-2005
- MFCB-DELISTED () First Date:1-May-2007 -> Last Date:3-Jun-2019
- MFNC-DELISTED (Mackinac Financial) First Date:16-May-2007 -> Last Date:3-Sep-2021
- MHS-DELISTED (MEDCOHEALTH SOLUTIONS INC COMMO) First Date:1-Jan-2005 -> Last Date:30-Mar-2012
- MIK-DELISTED (The Michaels Companies c) First Date:27-Jun-2014 -> Last Date:14-Apr-2021
- MINI-DELISTED () First Date:1-May-2007 -> Last Date:30-Jun-2020
- MJCO-DELISTED () First Date:29-Jun-2015 -> Last Date:21-Sep-2020
- MJN-DELISTED (MEAD JOHNSON NUTRITION COMPANY) First Date:11-Feb-2009 -> Last Date:14-Jun-2017
- MLHR-DELISTED (Herman Miller) First Date:30-Apr-2007 -> Last Date:29-Oct-2021
- MMAC-DELISTED (Mma Capital Management Co) First Date:6-Feb-2008 -> Last Date:12-Aug-2021
- MNK-DELISTED (MALLINCKRODT PLC) First Date:17-Jul-2013 -> Last Date:9-Oct-2020
- MNTA-DELISTED (Momenta Pharmaceuticals) First Date:3-Jan-2007 -> Last Date:30-Sep-2020
- MOBL-DELISTED () First Date:12-Jun-2014 -> Last Date:30-Nov-2020
- MOLX-DELISTED (MOLEX INCORPORATED) First Date:24-Mar-2005 -> Last Date:6-Dec-2013
- MON-DELISTED (MONSANTO COMPANY COMMON STOCK) First Date:1-Jan-2005 -> Last Date:31-Mar-2021
- MR-DELISTED () First Date:20-Jun-2014 -> Last Date:12-Nov-2020
- MSGN-DELISTED (The Madison Square Garden Company) First Date:10-Feb-2010 -> Last Date:8-Jul-2021
- MSON-DELISTED (Misonix) First Date:16-May-2007 -> Last Date:28-Oct-2021
- MTSC-DELISTED (Mts Systems) First Date:30-Apr-2007 -> Last Date:6-Apr-2021
- MWV-DELISTED (MEADWESTVACO CORPORATION COMMON) First Date:1-Jan-2005 -> Last Date:1-Jul-2015
- MWW-DELISTED (MONSTER WORLDWIDE COMMON) First Date:27-Apr-2007 -> Last Date:31-Oct-2016
- MXIM-DELISTED (Maxim Integrated Products Inc) First Date:27-Apr-2007 -> Last Date:25-Aug-2021
- MYG-DELISTED (Maytag) First Date:18-Nov-2008 -> Last Date:29-Jan-2009
- MYL-DELISTED (Mylan N.V.) First Date:3-Jan-2005 -> Last Date:16-Nov-2020
- MYOK-DELISTED (MyoKardia) First Date:29-Oct-2015 -> Last Date:16-Nov-2020
- NAV-DELISTED (Navistar International Corporation) First Date:30-Jun-2008 -> Last Date:30-Jun-2021
- NBL-DELISTED (Noble Energy Inc) First Date:3-Jan-2005 -> Last Date:2-Oct-2020
- NCC-DELISTED (National City) First Date:3-Jan-2005 -> Last Date:31-Dec-2008
- NFB-DELISTED (North Fork Ban) First Date:3-Jan-2005 -> Last Date:30-Nov-2006
- NFX-DELISTED (NEWFIELD EXPLORATION COMPANY CO) First Date:1-Jan-2005 -> Last Date:13-Feb-2019
- NGHC-DELISTED () First Date:20-Feb-2014 -> Last Date:31-Dec-2020
- NIHD-DELISTED (NII HOLDINGS) First Date:26-Apr-2007 -> Last Date:31-Dec-2019
- NSCO-DELISTED (Nesco) First Date:6-Oct-2017 -> Last Date:26-Feb-2021
- NSM-DELISTED (NATIONAL SEMICONDUCTOR CORP) First Date:25-Apr-2007 -> Last Date:30-Jul-2018
- NXTL-DELISTED (Nextel Communications) First Date:3-Jan-2005 -> Last Date:12-Aug-2005
- NYX-DELISTED (NYSE EURONEXT COMMON STOCK) First Date:8-Mar-2006 -> Last Date:12-Nov-2013
- OMX-DELISTED (OfficeMax (Old)) First Date:3-Jan-2005 -> Last Date:5-Nov-2013
- ONNN-DELISTED (ON Semiconductor (old ticker)) First Date:1-Jan-2005 -> Last Date:2-Apr-2015
- ORBC-DELISTED (Orbcomm) First Date:7-May-2007 -> Last Date:31-Aug-2021
- OZRK-DELISTED (Bank OZK (old ticker)) First Date:1-Jan-2005 -> Last Date:13-Jul-2018
- PAND-DELISTED (Pandion Therapeutics) First Date:17-Jul-2020 -> Last Date:31-Mar-2021
- PCL-DELISTED (PLUM CREEK TIMBER COMPANY) First Date:1-Jan-2005 -> Last Date:19-Feb-2016
- PCLN-DELISTED (THE PRICELINE GROUP) First Date:1-Jan-2005 -> Last Date:26-Feb-2018
- PCP-DELISTED (PRECISION CASTPARTS CORPORATION) First Date:1-Jan-2005 -> Last Date:29-Jan-2016
- PDLI-DELISTED () First Date:26-Apr-2007 -> Last Date:30-Dec-2020
- PE-DELISTED (Parsley Energy) First Date:23-May-2014 -> Last Date:12-Jan-2021
- PETM-DELISTED (PETSMART INC) First Date:1-Jan-2005 -> Last Date:11-Mar-2015
- PFBI-DELISTED (Premier Financial) First Date:17-May-2007 -> Last Date:17-Sep-2021
- PFNX-DELISTED () First Date:24-Jul-2014 -> Last Date:30-Sep-2020
- PFPT-DELISTED (Proofpoint) First Date:20-Apr-2012 -> Last Date:30-Aug-2021
- PGL-DELISTED (Peoples Energy) First Date:3-Jan-2005 -> Last Date:21-Feb-2007
- PGN-DELISTED (PROGRESS ENERGY COMMON ST) First Date:2-Sep-2014 -> Last Date:17-Dec-2015
- PKY-DELISTED (New Parkway) First Date:4-Oct-2016 -> Last Date:11-Oct-2017
- PLT-DELISTED (Plantronics) First Date:26-Apr-2007 -> Last Date:21-May-2021
- PMCS-DELISTED (PMC-Sierra) First Date:3-Jan-2005 -> Last Date:14-Jan-2016
- PMTC-DELISTED (Parametric Technology) First Date:1-May-2006 -> Last Date:2-Dec-2013
- POL-DELISTED (PolyOne Corporation) First Date:3-Jan-2007 -> Last Date:10-Jul-2020
- POM-DELISTED (PEPCO HOLDINGS INC COMMON STOCK) First Date:1-Jan-2005 -> Last Date:23-Mar-2016
- PPDI-DELISTED (PHARMACEUTICAL PRODUCT DEVELOPMENT INC) First Date:1-Jan-2005 -> Last Date:5-Dec-2011
- PQG-DELISTED (Pq Group) First Date:29-Sep-2017 -> Last Date:2-Aug-2021
- PRAH-DELISTED (Pra Health Sciences Comm) First Date:13-Nov-2014 -> Last Date:30-Jun-2021
- PRNB-DELISTED () First Date:14-Sep-2018 -> Last Date:25-Sep-2020
- PROS-DELISTED (Prosight Global) First Date:25-Jul-2019 -> Last Date:3-Aug-2021
- PRSP-DELISTED (Perspecta) First Date:1-Nov-2007 -> Last Date:6-May-2021
- PRVL-DELISTED (Prevail Therapeutics) First Date:20-Jun-2019 -> Last Date:21-Jan-2021
- PS-DELISTED (Pluralsight) First Date:17-May-2018 -> Last Date:5-Apr-2021
- PSFT-DELISTED (People Soft) First Date:7-Oct-2008 -> Last Date:19-Aug-2021
- PTLA-DELISTED () First Date:22-May-2013 -> Last Date:1-Jul-2020
- PTVCB-DELISTED (Protective Insurance) First Date:16-May-2007 -> Last Date:28-May-2021
- PVAC-DELISTED (Penn Virginia) First Date:15-Nov-2016 -> Last Date:15-Oct-2021
- PVN-DELISTED (Providian Financial) First Date:3-Jan-2005 -> Last Date:30-Sep-2005
- PWER-DELISTED (Power-One) First Date:3-Jan-2005 -> Last Date:25-Jul-2013
- PX-DELISTED (PRAXAIR COMMON STOCK) First Date:1-Jan-2005 -> Last Date:30-Oct-2018
- QADA-DELISTED (Qad) First Date:16-Dec-2010 -> Last Date:4-Nov-2021
- QCP-DELISTED (Quality Care Properties) First Date:20-Oct-2016 -> Last Date:26-Jul-2018
- Q-DELISTED (QWEST COMMUNICATIONS INTERNATIONAL INC) First Date:3-Jun-2013 -> Last Date:14-Nov-2017
- QEP-DELISTED (QEP RESOURCES) First Date:1-Jul-2010 -> Last Date:16-Mar-2021
- QLGC-DELISTED (QLOGIC CORPORATION) First Date:1-Jan-2005 -> Last Date:15-Aug-2016
- QTS-DELISTED (QTS Realty Trust) First Date:9-Oct-2013 -> Last Date:31-Aug-2021
- QVCA-DELISTED (LIBERTY INTERACTIVE CORPORATION) First Date:26-Apr-2007 -> Last Date:9-Mar-2018
- RAI-DELISTED (REYNOLDS AMERICAN INC COMMON ST) First Date:1-Jan-2005 -> Last Date:24-Jul-2017
- RAVN-DELISTED (Raven Industries) First Date:30-Apr-2007 -> Last Date:29-Nov-2021
- RBC-DELISTED (Regal Beloit Corporation) First Date:3-Jan-2007 -> Last Date:4-Oct-2021
- RBK-DELISTED (Reebok Int'l Ltd) First Date:3-Jan-2005 -> Last Date:31-Jan-2006
- RBS-DELISTED (The Royal Bank of Scotland Group plc) First Date:18-Oct-2007 -> Last Date:22-Jul-2020
- RDC-DELISTED (ROWAN COMPANIES COMMON ST) First Date:1-Jan-2005 -> Last Date:10-Apr-2019
- RESI-DELISTED () First Date:24-Dec-2012 -> Last Date:11-Jan-2021
- RHT-DELISTED (Red Hat) First Date:14-May-2007 -> Last Date:8-Jul-2019
- ROH-DELISTED (Rohm & Hass Co) First Date:3-Jan-2005 -> Last Date:1-Apr-2009
- RPAI-DELISTED (Retail Properties) First Date:5-Apr-2012 -> Last Date:21-Oct-2021
- RP-DELISTED (Realpage) First Date:12-Aug-2010 -> Last Date:21-Apr-2021
- RSH-DELISTED (RADIOSHACK CORPORATION COMMON S) First Date:1-Jan-2005 -> Last Date:2-Feb-2015
- RST-DELISTED () First Date:16-Apr-2009 -> Last Date:14-Oct-2020
- RTP-DELISTED (Reinvent Technology Partners) First Date:9-Nov-2020 -> Last Date:10-Aug-2021
- RTPY-DELISTED (Reinvent Technology Partners Y) First Date:10-May-2021 -> Last Date:3-Nov-2021
- RXN-DELISTED (Rexnord Corporation) First Date:29-Mar-2012 -> Last Date:4-Oct-2021
- SAF-DELISTED (Safeco) First Date:3-Mar-2008 -> Last Date:30-Aug-2021
- SBBP-DELISTED (Strongbridge Biopharma) First Date:16-Oct-2015 -> Last Date:5-Oct-2021
- SBBX-DELISTED () First Date:16-May-2007 -> Last Date:31-Jul-2020
- SCG-DELISTED (SCANA CORPORATION COMMON STOCK) First Date:1-Jan-2005 -> Last Date:31-Dec-2018
- SCR-DELISTED (Score Media & Gaming) First Date:10-Jan-2014 -> Last Date:18-Oct-2021
- SEBL-DELISTED (Siebel Systems) First Date:3-Jan-2005 -> Last Date:31-Jan-2006
- SERV-DELISTED (ServiceMaster Global Holdings) First Date:1-Aug-2014 -> Last Date:2-Oct-2020
- SFA-DELISTED (Scientific-Atlanta) First Date:3-Oct-2008 -> Last Date:22-Sep-2010
- SGP-DELISTED (MERCK & CO/INC) First Date:1-Jan-2005 -> Last Date:3-Nov-2009
- SIAL-DELISTED (SIGMA-ALDRICH CORPORATION) First Date:1-Jan-2005 -> Last Date:17-Nov-2015
- SINA-DELISTED (SINA Corporation) First Date:3-Jan-2007 -> Last Date:22-Mar-2021
- SLCT-DELISTED (Select Bancorp) First Date:16-May-2007 -> Last Date:15-Oct-2021
- SLR-DELISTED (Solectron) First Date:1-Jan-2005 -> Last Date:1-Oct-2007
- SMTA-DELISTED (Spirit MTA REIT) First Date:17-May-2018 -> Last Date:31-Dec-2019
- SNDK-DELISTED (SANDISK CORP.) First Date:1-Jan-2005 -> Last Date:11-May-2016
- SNIDELISTED (SCRIPPS NETWORKS INTERACTIVE I) First Date:1-Jul-2008 -> Last Date:6-Mar-2018
- SNR-DELISTED (New Senior Investment Group i) First Date:7-Nov-2014 -> Last Date:20-Sep-2021
- SONA-DELISTED (Southern National Bancorp) First Date:16-May-2007 -> Last Date:26-Feb-2021
- SOTR-DELISTED (SouthTrust) First Date:15-Feb-2008 -> Last Date:19-Feb-2009
- SOV-DELISTED (Sovereign Ban) First Date:3-Jan-2005 -> Last Date:29-Jan-2009
- SPKE-DELISTED (Spark Energy Com) First Date:29-Jul-2014 -> Last Date:9-Aug-2021
- SSS-DELISTED (Sovran Self Storage) First Date:1-Jan-2005 -> Last Date:12-Aug-2016
- STI-DELISTED (SunTrust Banks) First Date:1-Jan-2005 -> Last Date:6-Dec-2019
- STJ-DELISTED (ST. JUDE MEDICAL COMMON S) First Date:1-Jan-2005 -> Last Date:4-Jan-2017
- STMP-DELISTED (Stamps.com) First Date:3-Jan-2007 -> Last Date:4-Oct-2021
- STND-DELISTED (Standard Avb Financial Corp.) First Date:7-Oct-2010 -> Last Date:28-May-2021
- STPK-DELISTED (Star Peak Energy Transition) First Date:12-Apr-2021 -> Last Date:12-Apr-2021
- STR-DELISTED (QUESTAR CORPORATION COMMON STOC) First Date:1-Jan-2005 -> Last Date:16-Sep-2016
- SUNE-DELISTED () First Date:3-Jun-2013 -> Last Date:21-Apr-2016
- SVA-DELISTED (Sinovac Biotech, Ltd) First Date:26-Apr-2007 -> Last Date:22-Feb-2019
- SVMK-DELISTED (SVMK) First Date:26-Sep-2018 -> Last Date:14-May-2021
- SVU-DELISTED (SUPERVALU COMMON STOCK) First Date:1-Jan-2005 -> Last Date:19-Oct-2018
- SWY-DELISTED (SAFEWAY COMMON STOCK) First Date:1-Jan-2005 -> Last Date:29-Jan-2015
- SYKE-DELISTED (Sykes Enterprises) First Date:30-Apr-2007 -> Last Date:26-Aug-2021
- SYMC-DELISTED (Symantec) First Date:2-Jan-2018 -> Last Date:4-Nov-2019
- SYX-DELISTED (Systemax) First Date:1-May-2007 -> Last Date:14-May-2021
- TBA-DELISTED (Thoma Bravo Advantage) First Date:15-Jan-2021 -> Last Date:28-Jun-2021
- TBIO-DELISTED (Translate Bio) First Date:28-Jun-2018 -> Last Date:13-Sep-2021
- TCF-DELISTED (TCF Financial Corporation) First Date:27-Apr-2007 -> Last Date:8-Jun-2021
- TCO-DELISTED (Taubman Centers) First Date:3-Jan-2007 -> Last Date:28-Dec-2020
- TCP-DELISTED (TC PipeLines LP) First Date:10-May-2007 -> Last Date:2-Mar-2021
- TECD-DELISTED (Tech Data Corporation) First Date:3-Jan-2007 -> Last Date:29-Jun-2020
- TE-DELISTED (TECO ENERGY COMMON STOCK) First Date:1-Jan-2005 -> Last Date:30-Jun-2016
- TEG-DELISTED (INTEGRYS ENERGY GROUP COM) First Date:22-Feb-2007 -> Last Date:29-Jun-2015
- TEK-DELISTED (Tektronix) First Date:3-Jan-2005 -> Last Date:21-Nov-2007
- TERP-DELISTED (TerraForm Power) First Date:18-Jul-2014 -> Last Date:30-Jul-2020
- TIE-DELISTED (TITANIUM METALS CORPORATION COM) First Date:1-Jan-2005 -> Last Date:7-Jan-2013
- TIF-DELISTED (Tiffany & Co.) First Date:3-Jan-2005 -> Last Date:6-Jan-2021
- TIN-DELISTED (Temple-Inland) First Date:3-Jan-2005 -> Last Date:10-Feb-2012
- TLAB-DELISTED (TELLABS) First Date:1-Jan-2005 -> Last Date:3-Dec-2013
- TMK-DELISTED (Torchmark) First Date:1-Jan-2005 -> Last Date:8-Aug-2019
- TNAV-DELISTED (Telenav) First Date:13-May-2010 -> Last Date:16-Feb-2021
- TNB-DELISTED (Thomas & Betts) First Date:3-Jan-2005 -> Last Date:16-May-2012
- TPCO-DELISTED (Tribune Publishing Company) First Date:20-Jun-2016 -> Last Date:24-May-2021
- TRCO-DELISTED (Tribune Media Co) First Date:5-Dec-2014 -> Last Date:18-Sep-2019
- TRIL-DELISTED (Trillium Therapeutics Inc.) First Date:19-Dec-2014 -> Last Date:16-Nov-2021
- TSG-DELISTED (Sabre Holdings) First Date:1-Jan-2005 -> Last Date:4-May-2020
- TSO-DELISTED (TESORO CORPORATION COMMON STOCK) First Date:1-Jan-2005 -> Last Date:31-Jul-2017
- TSS-DELISTED (Total System Services) First Date:1-Jan-2005 -> Last Date:17-Sep-2019
- TSU-DELISTED (TIM Participacoes S.A.) First Date:30-May-2017 -> Last Date:12-Oct-2020
- TWC-DELISTED (TIME WARNER CABLE INC COMMON ST) First Date:1-Mar-2007 -> Last Date:17-May-2016
- TWX-DELISTED (TIME WARNER NEW COMMON STO) First Date:1-Jan-2005 -> Last Date:14-Jun-2018
- TXU-DELISTED (TXU) First Date:3-Jan-2005 -> Last Date:10-Oct-2007
- UFS-DELISTED (Domtar) First Date:16-May-2007 -> Last Date:29-Nov-2021
- USCR-DELISTED (Us Concrete) First Date:15-Oct-2010 -> Last Date:25-Aug-2021
- UST-DELISTED () First Date:1-Jan-2005 -> Last Date:1-Apr-2021
- UTX-DELISTED (United Technologies) First Date:3-Jan-2005 -> Last Date:2-Apr-2020
- UVN-DELISTED (Univision Comm) First Date:3-Jan-2005 -> Last Date:28-Mar-2007
- VAR-DELISTED (Varian Medical Systems) First Date:3-Jan-2005 -> Last Date:14-Apr-2021
- VEDL-DELISTED (Vedanta Limited) First Date:9-Sep-2013 -> Last Date:8-Nov-2021
- VEI-DELISTED (VINE ENERGY INC.) First Date:18-Mar-2021 -> Last Date:1-Nov-2021
- VER-DELISTED (VEREIT) First Date:7-Sep-2011 -> Last Date:29-Oct-2021
- VIAB-DELISTED (Viacom) First Date:30-Apr-2007 -> Last Date:4-Dec-2019
- VIA-DELISTED (Viacom Inc) First Date:1-Jan-2005 -> Last Date:4-Dec-2019
- VIE-DELISTED (Viela Bio) First Date:3-Oct-2019 -> Last Date:12-Mar-2021
- VIP-DELISTED (VIMPELCOM LTD.) First Date:1-Jan-2005 -> Last Date:30-Mar-2017
- VMED-DELISTED (VIRGIN MEDIA) First Date:8-Feb-2007 -> Last Date:7-Jun-2013
- VRTU-DELISTED (Virtusa) First Date:3-Aug-2007 -> Last Date:10-Feb-2021
- VSLR-DELISTED () First Date:1-Oct-2014 -> Last Date:7-Oct-2020
- VSM-DELISTED (Versum Materials) First Date:19-Sep-2016 -> Last Date:4-Oct-2019
- WCG-DELISTED (WellCare) First Date:1-Jan-2005 -> Last Date:23-Jan-2020
- WCRX-DELISTED (WARNER CHILCOTT PLC) First Date:21-Sep-2006 -> Last Date:30-Sep-2013
- WDR-DELISTED (Waddell & Reed Fnancial) First Date:30-Apr-2007 -> Last Date:30-Apr-2021
- WFM-DELISTED (WHOLE FOODS MARKET) First Date:27-Apr-2007 -> Last Date:25-Aug-2017
- WFT-DELISTED (Weatherford Int'l plc) First Date:3-Jan-2005 -> Last Date:10-May-2019
- WIFI-DELISTED (Boingo Wireless) First Date:4-May-2011 -> Last Date:1-Jun-2021
- WIN-DELISTED (WINDSTREAM CORPORATION) First Date:18-Jul-2006 -> Last Date:5-Mar-2019
- WMGI-DELISTED (Wright Medical Group N.V.) First Date:18-Jun-2010 -> Last Date:10-Nov-2020
- WORK-DELISTED (Slack Technologies) First Date:20-Jun-2019 -> Last Date:20-Jul-2021
- WPX-DELISTED (WPX ENERGY) First Date:3-Jan-2012 -> Last Date:6-Jan-2021
- WRI-DELISTED (Weingarten Realty Investors) First Date:3-Jan-2007 -> Last Date:3-Aug-2021
- WSH-DELISTED (Willis Group Holdings) First Date:1-Jan-2005 -> Last Date:4-Jan-2016
- WTRE-DELISTED (Watford Common Shares) First Date:28-Mar-2019 -> Last Date:1-Jul-2021
- WUBA-DELISTED (58.com) First Date:31-Oct-2013 -> Last Date:17-Sep-2020
- WWY-DELISTED (Wrigley Co.) First Date:3-Jan-2005 -> Last Date:6-Oct-2008
- WXS-DELISTED (WEX (old ticker)) First Date:1-Mar-2005 -> Last Date:12-Apr-2013
- WYND-DELISTED (Wyndham Destinations) First Date:21-May-2018 -> Last Date:12-Feb-2021
- WYN-DELISTED (WYNDHAM WORLDWIDE CORP COMMON) First Date:1-Aug-2006 -> Last Date:31-May-2018
- XEC-DELISTED (Cimarex Energy) First Date:3-Jan-2005 -> Last Date:30-Sep-2021
- XL-DELISTED (XL GROUP PLC) First Date:1-Jan-2005 -> Last Date:11-Sep-2018
- XLRN-DELISTED (Acceleron Pharma) First Date:19-Sep-2013 -> Last Date:19-Nov-2021
- XONE-DELISTED (The Exone Company) First Date:7-Feb-2013 -> Last Date:11-Nov-2021
- YHOO-DELISTED (YAHOO!) First Date:1-Jan-2005 -> Last Date:16-Jun-2017
