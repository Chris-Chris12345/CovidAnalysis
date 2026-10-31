import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#plotly is a data visualisation library for interactive graphs

dataset = pd.read_csv("covid_data.csv")
print(dataset.head()) #shows the first five rows (except if you choose how many rows)
print(dataset.info()) #shows column names, datatypes and missing values
print(dataset.shape) #shows the number of rows and columns
print(dataset.describe()) #shows the statistical informations of numerical columns

#Selecting the required columns for the analysis
dataset = dataset[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]

#Renaming the columns to make them short and easy to use
dataset.columns = ("State","Country","Upd","Lat","Long","Conf","Rec","Deaths","Act")
print(dataset.columns)

#Handling missing values
dataset["State"].fillna(value="",inplace = True)

#Finding the 10 countries with the highest confirmed cases
"""
example = pd.DataFrame(dataset.groupby("Country")["Conf"].sum())
print(example)
"""

top10_con = pd.DataFrame(
    dataset.groupby("Country")["Conf"].sum().nlargest(10).sort_values(ascending = False)
)
print(top10_con)

#Creating a bubble chart
fig1 = px.scatter(
    top10_con,
    x=top10_con.index,
    y="Conf",
    size="Conf",
    size_max=120,
    color=top10_con.index,
    title="Top 10 Countries by Confirmed Cases"
)

fig1.write_html("fig1.html",auto_open=True)

top10_rec = pd.DataFrame(
    dataset.groupby("Country")["Rec"].sum().nlargest(10).sort_values(ascending = False)
)

fig2 = px.bar(
    top10_rec,
    x=top10_rec.index,
    y="Rec",
    height=600,
    color="Rec",
    title="Top 10 Recovered Cases Countries",
    color_continuous_scale=px.colors.sequential.Viridis
)

fig2.write_html("fig2.html",auto_open=True)