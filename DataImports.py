#importing needed libraries
import pandas as pd
import os

os.getcwd()  #check working directory

price=pd.read_csv('prices.csv')  #import dataset into a var
price.head()
price.describe()
price.dtypes #Checking the types of variables in each column
pd.to_datetime(price.date)  #Convert date column to datetime format
price.dtypes

import numpy as np  #import numpy library
type(price)  #check if data is in DataFrame format
pd.pivot_table(price,index=["symbol"])  #use pivot tables
pvt=pd.pivot_table(price,index=["symbol","date"])  #include date as the index. Cannot convert date to numeric format. Code too complex
pvt

from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import seaborn as sns  #import all needed libraries.
get_ipython().magic('matplotlib inline')
plt.show()
sns.set(rc={'figure.figsize':(25,15)})

type(pvt) #checking if pvt is in DataFrame
funda=pd.read_csv('fundamentals.csv') #imported fundamentals.csv
type(funda) #checked for type
funda.head() #showing first 5 rows of the imported data.
sns.barplot(data=funda, x='Ticker Symbol', y='Gross Profit')