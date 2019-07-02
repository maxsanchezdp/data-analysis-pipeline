import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#ANALYSE DATA:

def get_growth(df):
    gdf=df.copy()
    lista=[0]
    for i in range(1,len(df["Population"])):
        lista.append(((df["Population"][i]/df["Population"][i-1])-1)*100)
    gdf["Growth rate %"]=np.array(lista)
    return gdf[1:]

def plot_population(df):
    plt.figure(figsize=(18,6))
    plt.plot(df.groupby(["Year"]).sum()["Population"]/1000000, c='blue')
    plt.legend(loc=1)
    plt.title('Population by year')
    plt.xlabel('Year')
    plt.ylabel('Population (Millions)')
    plt.savefig('./Output/population.png')
    plt.show()
    return './Output/population.png'

def plot_growth(df):
    plt.figure(figsize=(18,6))
    plt.plot(df.groupby(["Year"]).sum()["Growth rate %"], c='blue')
    plt.legend(loc=1)
    plt.title('Population growth rate by year')
    plt.xlabel('Year')
    plt.ylabel('Growth rate %')
    plt.savefig('./Output/growth.png')
    plt.show()
    return './Output/growth.png'
    
def analyse_this(df):
    gr=get_growth(df)
    pop_pr=plot_population(df)
    gr_pr=plot_growth(gr)
    return pop_pr, gr_pr