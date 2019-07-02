import pandas as pd

#GET DATA:
PATH="./Input/country_population.csv"
def get_data(path=PATH):
    df=pd.read_csv(path,",")
    return df