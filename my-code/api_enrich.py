import pandas as pd
import numpy as np
import requests as req

#API ENRICH:
#BASE_URL="https://restcountries.eu/rest/v2/alpha/"
def get_country(df):
    name=df["Country Name"].unique()[0]
    return str(name)

def get_ccode(df):
    code=df["Country Code"].unique()[0]
    return str(code)

def get_capital(code):
    query_params={"fields":"capital"}
    res = req.get("https://restcountries.eu/rest/v2/alpha/{}".format(code),params=query_params)
    content=res.json()
    capital=content["capital"]
    return capital

def get_alt_names(code):
    query_params={"fields":"altSpellings"}
    res = req.get("https://restcountries.eu/rest/v2/alpha/{}".format(code),params=query_params)
    content=res.json()
    names=", ".join(content["altSpellings"])
    return names

def get_region(code):
    query_params={"fields":"region"}
    res = req.get("https://restcountries.eu/rest/v2/alpha/{}".format(code),params=query_params)
    content=res.json()
    region=content["region"]
    return region

def get_population(code):
    query_params={"fields":"population"}
    res = req.get("https://restcountries.eu/rest/v2/alpha/{}".format(code),params=query_params)
    content=res.json()
    pop=str(content["population"])
    return pop

def get_lang(code):
    query_params={"fields":"languages"}
    res = req.get("https://restcountries.eu/rest/v2/alpha/{}".format(code),params=query_params)
    content=res.json()
    lang_list=[l["name"] for l in content["languages"]]
    languages=", ".join(lang_list)
    return languages

def enrich_that(df):
        name=get_country(df)
        cod=get_ccode(df)
        altn=get_alt_names(cod)
        cap=get_capital(cod)
        reg=get_region(cod)
        lan=get_lang(cod)
        cpop=get_population(cod)
        return name, altn, cap, reg, lan, cpop

