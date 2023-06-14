
##探索纽约市接送服务的公共优步数据集。完成后，您将知道如何获取和缓存数据、绘制图表、在地图上绘制信息以及使用交互式小部件（如滑块）来过滤结果。

import streamlit as st
import pandas as pd
import numpy as np

st.title('纽约的优步接送车')
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
# 缓存函数装饰器
# 第一次调用时正常处理，并将结果保存至缓存中，下次调用完全相同的函数时，则可不经过函数，直接返回缓存中的结果
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
#创建一个文本元素，让读者知道数据正在加载。
data_load_state = st.text('加载数据...')
# 将10,000行数据加载到数据框架中。
data = load_data(10000)
# 通知读取器数据已成功加载。
data_load_state.text("完成! (使用 st.cache_data)")

# st.subheader('原始数据')
# st.write(data) #st.write尝试根据输入的数据类型做正确的事情。可改为指定类型st.dataframe
#显示或隐藏原始数据表
if st.checkbox('展示原始数据'):
    st.subheader('原始数据')
    st.write(data)
#绘制直方图
st.subheader('按小时计算的接送次数')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
#绘制地图

#数值筛选
# hour_to_filter = 17
#滑块筛选
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'数据地图 在 {hour_to_filter}:00')
st.map(filtered_data)