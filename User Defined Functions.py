###### Monte Carlo Simulation

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
