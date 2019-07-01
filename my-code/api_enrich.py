import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests as req

#API ENRICH:
BASE_URL="https://restcountries.eu/rest/v2/alpha/"
def get_country(df):
    code=df["Country Code"].unique()[0]
    return str(code)

def get_capital(url,code):
    query_params={"fields":"capital"}
    res = req.get("{}{}".format(url,code),params=query_params)
    content=res.json()
    capital=content["capital"]
    return capital

def get_alt_names(url,code):
    query_params={"fields":"altSpellings"}
    res = req.get("{}{}".format(url,code),params=query_params)
    content=res.json()
    names=", ".join(content["altSpellings"])
    return names

def get_region(url,code):
    query_params={"fields":"region"}
    res = req.get("{}{}".format(url,code),params=query_params)
    content=res.json()
    region=content["region"]
    return region

def get_population(url,code):
    query_params={"fields":"population"}
    res = req.get("{}{}".format(url,code),params=query_params)
    content=res.json()
    pop=str(content["population"])
    return pop

def get_lang(url,code):
    query_params={"fields":"languages"}
    res = req.get("{}{}".format(url,code),params=query_params)
    content=res.json()
    lang_list=[l["name"] for l in content["languages"]]
    languages=", ".join(lang_list)
    return languages

def get_flag(url,code):
    query_params={"fields":"flag"}
    res = req.get("{}{}".format(url,code),params=query_params)
    content=res.json()
    img_url=content["flag"]
    pic_res = req.get(img_url)
    if pic_res.status_code == 200:
        with open("./Output/flag.svg", 'wb') as f:
            f.write(pic_res.content)