import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout='wide')

@st.cache_data
def load_df():
    return pd.read_excel('某咖啡公司销售数据(带评分).xlsx')

df=load_df()

#侧边栏

st.sidebar.header('筛选条件：')

market_values = df['市场类别'].unique()
markets = st.sidebar.multiselect('市场类别',market_values,market_values)

zones = df['区域'].unique()
zones = st.sidebar.selectbox('区域',zones)

product_cat_values = df['产品类别'].unique()
product_cats = st.sidebar.multiselect('产品类别',product_cat_values,product_cat_values) or product_cat_values


df = df.query('市场类别 in @markets and 区域 in @zones and 产品类别 in @product_cats')

# st.dataframe(df)


# 页面

st.title('咖啡销售数据看板')

# 指标
total_sales = int(df['销售额'].sum())

avg_rate = int(round(df['rate'].mean(),0))
stars = ':star:' * avg_rate

avg_sales = round(df['销售额'].mean(),2)

left,mid,right = st.columns(3)

with left:
    st.subheader('总销售额:')
    st.subheader(f'{total_sales:,}')

with mid:
    st.subheader('评分(平均):')
    st.subheader(f'{avg_rate} {stars}')

with right:
    st.subheader('平均销售额:')
    st.subheader(f'{avg_sales:,}')


c = alt.Chart(df).mark_bar().encode(
    x = alt.X('sum(销售额)',title='总销售额'),
    y = '产品名称'
)

st.altair_chart(c,use_container_width=True)
