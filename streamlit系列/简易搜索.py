import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

@st.cache_data
def load_df():
    return pd.read_excel('streamlit系列/emoji中文对照表.xlsx')

df = load_df()

query = st.text_input('搜索')

cond = df['中文'].str.contains(query)
res_df = df[cond]

if len(res_df)==0:
    cond = df['拼音'].str.contains(query)
    res_df = df[cond]

st.dataframe(res_df,use_container_width=True)
