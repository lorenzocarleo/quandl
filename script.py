# %%
import pandas as pd 
import numpy as np 
import quandl as quandl

# %%
quandl.ApiConfig.api_key = "xxxxxx"

mydata = quandl.get('FRED/GDP')

print(mydata)

# %%


