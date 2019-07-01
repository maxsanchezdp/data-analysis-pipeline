import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#FILTER AND FIX DATA:
def filter_data(df,country="WORLD",desde=2006,hasta=2016):
    lista_años_st=list(map(str,list(range(desde,hasta+1))))
    lista_total=["Country Name","Country Code"]+lista_años_st
    fdf=df[df["Country Name"]==(country.upper())][lista_total]
    return fdf

def fix_data(df):
    melt=pd.melt(df, id_vars=["Country Name","Country Code"], value_vars=df.columns[3:],var_name="Year",value_name="Population")
    melt=melt.sort_values(by=["Country Name", "Year"])
    return melt