# %%
import pandas as pd 
import numpy as np 
import quandl as quandl

# %%
quandl.ApiConfig.api_key = "b9K1Pc8yb8neKpUCwvcw"

mydata = quandl.get('FRED/GDP')

print(mydata)

# %%


