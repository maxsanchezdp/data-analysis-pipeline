import pandas as pd

#GET DATA:
PATH="./Input/country_population.csv"
def get_data(path):
    df=pd.read_csv(path,",")
    return df