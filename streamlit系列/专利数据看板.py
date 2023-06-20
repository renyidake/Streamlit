import streamlit as st
import pandas as pd
import altair as alt

#streamlit 页面布局为 宽
st.set_page_config(layout='wide')

#缓存Excel数据到load-df
#
# @st.cache_data
def load_df():
    return pd.read_excel('streamlit系列/2020-2022中之信.xlsx')

df=load_df()

#侧边栏 标题
st.sidebar.header('筛选条件：')
#返回列的唯一值数组
market_values = df['受理局'].unique()
#多选择的部件
markets = st.sidebar.multiselect('受理局',market_values,market_values)

market_values = df['专利类型'].unique()
#多选择的部件
markets1 = st.sidebar.multiselect('专利类型',market_values,market_values)


#返回列的唯一值数组
market_values = df['简单法律状态'].unique()
#多选择的部件
markets2 = st.sidebar.multiselect('简单法律状态',market_values,market_values)

#返回列的唯一值数组
market_values = df['申请年'].unique()
#多选择的部件
markets3= st.sidebar.multiselect('申请年',market_values,market_values)

#返回列的唯一值数组
market_values = df['当前申请专利权人州省'].unique()
#多选择的部件
markets4 = st.sidebar.multiselect('当前申请专利权人州省',market_values,market_values)

#做数据筛选 根据上面选择的类别
df1 = df.query('受理局 in @markets and 专利类型 in @markets1  and'
              ' 简单法律状态 in @markets2 and 申请年 in @markets3 and 当前申请专利权人州省 in @markets4')

st.dataframe(df1)


# 页面 标题
st.title('专利数据看板')

# 指标 计算
zongshenqing = int(df1['公开公告号'].count())


shouquan=df1.loc[df1['法律状态事件'].str.contains('授权',na=False),:]
shouquan=shouquan['法律状态事件'].count()

bohui=df1.loc[df1['法律状态事件'].str.contains('驳回',na=False),:]
bohui=bohui['法律状态事件'].count()

faming = df1.loc[(df1['专利类型'] == '发明专利')]
faming=faming['专利类型'].count()
shiyong = df1.loc[(df1['专利类型'] == '实用新型')]
shiyong=shiyong['专利类型'].count()
waiguan = df1.loc[(df1['专利类型'] == '外观设计')]
waiguan=waiguan['专利类型'].count()

left1,mid1,right1= st.columns(3)

left2,mid2,right2 = st.columns(3)
#显示计算度量
with left1:
    st.subheader('总申请量:')
    st.subheader(f'{zongshenqing:,}')

with mid1:
    st.subheader('授权专利:')
    st.subheader(f'{shouquan: }')

with right1:
    st.subheader('驳回专利:')
    st.subheader(f'{bohui:,}')
with left2:
    st.subheader('发明专利:')
    st.subheader(f'{faming:,}')
with mid2:
    st.subheader('实用新型:')
    st.subheader(f'{shiyong: }')
with right2:
    st.subheader('外观设计:')
    st.subheader(f'{waiguan:,}')

df_1 = df1.groupby('代理人', as_index=False)['公开公告号'].count()
df_1 = df_1.sort_values(by='公开公告号', ascending=False)

# 创建条形图 显示 X轴 sum(销售额)  Y轴产品名称
c1 = alt.Chart(df_1).mark_bar().encode(
    x = alt.X('公开公告号',title='代理人代理量'),
    y = alt.Y('代理人',sort='-x')
)
#显示图表 并根据可用空间调整宽度
st.altair_chart(c1,use_container_width=True)

df_2 = df1.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
df_2 = df_2.sort_values(by='公开公告号', ascending=False)
df_2=df_2.head(30)
# 创建条形图 显示 X轴 sum(销售额)  Y轴产品名称
c = alt.Chart(df_2).mark_bar().encode(
    x = alt.X('公开公告号',title='申请人申请量'),
    y = alt.Y('当前申请专利权人',sort='-x')
)
#显示图表 并根据可用空间调整宽度
st.altair_chart(c,use_container_width=True)


