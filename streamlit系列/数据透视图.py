import streamlit as st
import pandas as pd
import pygwalker as pyg
#数据透视
st.set_page_config(layout='wide')

# excel文件选择框
@st.cache_data
def load_df(file):
    return pd.read_excel(file)

uploaded_file = st.file_uploader("excel文件",type=['xlsx'])

if uploaded_file is None:
    st.stop()

df = load_df(uploaded_file)
pyg.walk(df,env='Streamlit')

