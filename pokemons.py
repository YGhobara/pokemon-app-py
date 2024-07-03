import streamlit as st
import numpy as np
import pandas as pd
import time # to simulate real time data
import plotly.express as px # interactive charts
import matplotlib.pyplot as plt

dataset = 'pokedex.csv'

st.set_page_config(
    page_title = 'Pokemon Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset).fillna('None')

df = get_data()
st.title("Pokemon Dashboard")
st.markdown("## Pokemon Analysis")

#unique_pokemon_filter = st.selectbox("Select the Pokemon", pd.unique(df["Name"]))
type1_filter = st.selectbox("Select the Type 1", pd.unique(df["Type_1"]))
type2_filter = st.selectbox("Select the Type 2", pd.unique(df["Type_2"]))

#df = df[df["Name"] == unique_pokemon_filter]
df = df[df["Type_1"] == type1_filter]
df = df[df["Type_2"] == type2_filter]


avgHP = np.mean(df['HP'])
avgAtk = np.mean(df['Attack'])
avgDef = np.mean(df['Defense'])
avgSpAtk = np.mean(df['Special Attack'])
avgSpDef = np.mean(df['Special Defense'])
avgSpd = np.mean(df['Speed'])

st.dataframe(df[0:100])

count_types = len(df)

st.metric(
    label="Number of Pokemons of Type "+str(type1_filter)+" and "+str(type2_filter),
    value=round(count_types)
)

ndf =pd.DataFrame(
        {
            'stats': [avgHP, avgAtk, avgDef, avgSpAtk, avgSpDef, avgSpd],
            'labels':['Average HP', 'Average Attack', 'Average Defense', 'Average Special Attack', 'Average Special Defense', 'Average Speed']            
        })

fig = px.pie(
    data_frame=ndf, values='stats', names='labels')

st.write(fig)

if st.button("Home"):
    st.switch_page("app.py")