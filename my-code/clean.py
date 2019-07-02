import pandas as pd
import numpy as np


#CLEAN DATA:
def clean_data(df):
    col_drop=["Indicator Name","Indicator Code"]
    count_drop=[
        "Arab World",
        "Central Europe and the Baltics",
        "Caribbean small states",
        "East Asia & Pacific (excluding high income)",
        "Early-demographic dividend",
        'East Asia & Pacific',
        'Europe & Central Asia (excluding high income)',
        'Europe & Central Asia',
        'Euro area',
        'European Union',
        'Fragile and conflict affected situations',
        'High income',
        'Heavily indebted poor countries (HIPC)',
        'IBRD only',
        'IDA & IBRD total',
        'IDA total',
        'IDA blend',
        'IDA only',
        'Not classified',
        'Latin America & Caribbean (excluding high income)',
        'Latin America & Caribbean',
        'Least developed countries: UN classification',
        'Low income',
        'Lower middle income',
        'Low & middle income',
        'Late-demographic dividend',
        'Middle East & North Africa',
        'Middle income',
        'Middle East & North Africa (excluding high income)',
        'North America',
        'OECD members',
        'Other small states',
        'Pre-demographic dividend',
        'West Bank and Gaza',
        'Pacific island small states',
        'Post-demographic dividend',
        'South Asia',
        'Sub-Saharan Africa (excluding high income)',
        'Sub-Saharan Africa',
        'Small states',
        'East Asia & Pacific (IDA & IBRD countries)',
        'Europe & Central Asia (IDA & IBRD countries)',
        'Latin America & the Caribbean (IDA & IBRD countries)',
        'Middle East & North Africa (IDA & IBRD countries)',
        'South Asia (IDA & IBRD)',
        'Sub-Saharan Africa (IDA & IBRD countries)',
        'Upper middle income','World']
    cdf=df.copy()
    cdf=cdf.drop(col_drop, axis=1)
    bad_countries=cdf[cdf["Country Name"].isin(count_drop)==True].index
    cdf=cdf.drop(bad_countries,axis=0)
    cdf["Country Name"] = cdf["Country Name"].apply(lambda x: " ".join(x.split(",")[::-1]) if x in ["Congo, Dem. Rep.","Congo, Rep.","Korea, Rep.","Korea, Dem. People’s Rep."] else x)
    cdf["Country Name"] = cdf["Country Name"].apply(lambda x: x.split(",")[0])
    cdf=cdf.fillna(0)
    cdf["Country Name"] = cdf["Country Name"].apply(lambda x: x.upper().strip())
    return cdf