
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
import random
import matplotlib as mpl
from pyecharts import options as opts
from pyecharts.charts import Line, Grid,Bar,PictorialBar,Pie,Funnel,Scatter,Map,Geo,EffectScatter,Gauge,Polar,Radar,HeatMap,Graph,WordCloud, Timeline
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from matplotlib.ticker import MaxNLocator
import base64
from pandas.api.types import CategoricalDtype
import time
import webbrowser



#侧边栏初始状态为折叠 streamlit 页面布局为 宽
st.set_page_config(initial_sidebar_state='expanded',layout='wide')
st.image("新不二LOGO.png", width=200)  # streamlit系列/新不二LOGO.png
st.write("")

# 页面 标题
# st.title('🎉🎉🎉功能工具汇总🎉🎉🎉')
st.markdown("<h1 style='text-align: center; font-size: 60px;'>🎉🎉🎉功能工具汇总🎉🎉🎉</h1>", unsafe_allow_html=True)
st.write("")

col1, col2, col3 = st.columns([1, 3, 1])  # 调整中间列的宽度
with col1:
    pass  # 可以在此列添加任何你需要的内容
with col2:
    st.image("人指.png")  # 调整图片的宽度
with col3:
    pass  # 可以在此列添加任何你需要的内容

st.write("")
st.image("房屋.png")



# 侧边栏 标题
st.sidebar.header('➡⌛⌛⌛工具选择⌛⌛⌛⬅')


with st.sidebar:
    st.sidebar.subheader('office办公工具')
    # if st.sidebar.button('Word文档调整'):
    st.markdown('<a href="https://app-s7axjcwqm3b5xvpcrmffca.streamlit.app/" target="_blank">Word文档调整</a>', unsafe_allow_html=True)
        # webbrowser.open_new_tab('https://app-s7axjcwqm3b5xvpcrmffca.streamlit.app/')
    # if st.sidebar.button('合并Excel文件'):
    st.markdown(
        '<a href="https://renyidake-streamlit-streamlitexcel-qaktjq.streamlit.app/" target="_blank">合并Excel文件</a>',
        unsafe_allow_html=True)
        # webbrowser.open_new_tab('https://renyidake-streamlit-streamlitexcel-qaktjq.streamlit.app/')
    st.markdown('<a href="https://renyidake-streamlit-streamlitexcel-xi7xi6.streamlit.app/" target="_blank">合并Excel工作表</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://renyidake-streamlit-streamlit-i18h6p.streamlit.app/" target="_blank">数据筛选</a>',
                unsafe_allow_html=True)

    # if st.sidebar.button('合并Excel工作表'):
    #     webbrowser.open_new_tab('https://renyidake-streamlit-streamlitexcel-xi7xi6.streamlit.app/')
    # if st.sidebar.button('数据筛选'):
    #     webbrowser.open_new_tab('https://renyidake-streamlit-streamlit-i18h6p.streamlit.app/')

    st.sidebar.subheader('分析工具')
    st.markdown('<a href="https://renyidake.github.io/" target="_blank">数据大屏</a>', unsafe_allow_html=True)
    st.markdown('<a href="http://113.125.55.194:5000/" target="_blank">网页数据库</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://app-45tgvkzdc9whvcezhwahn4.streamlit.app/" target="_blank">专利分析模板</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://renyidake-streamlit-streamlit-nl7xmx.streamlit.app/" target="_blank">自定义数据可视化</a>', unsafe_allow_html=True)


    # if st.sidebar.button('数据大屏'):
    #     webbrowser.open_new_tab('https://renyidake.github.io/')
    # if st.sidebar.button('网页数据库'):
    #     webbrowser.open_new_tab('http://113.125.55.194:5000/')
    # if st.sidebar.button('专利分析模板'):
    #     webbrowser.open_new_tab('https://app-45tgvkzdc9whvcezhwahn4.streamlit.app/')
    # if st.sidebar.button('自定义数据可视化'):
    #     webbrowser.open_new_tab('https://renyidake-streamlit-streamlit-nl7xmx.streamlit.app/')
    if st.sidebar.button('专利价值评估'):
        st.write("暂无")

    tool_categories = {
        'office办公工具': ['Word文档调整', '合并Excel文件'],
        '分析工具': ['数据大屏', '网页数据库'],
    }
    # 展示侧边栏的工具分类
    selected_category = st.sidebar.radio('选择工具分类', list(tool_categories.keys()))
    print(selected_category)
    if selected_category=='office办公工具':
        st.markdown('<a href="https://app-s7axjcwqm3b5xvpcrmffca.streamlit.app/" target="_blank">Word文档调整</a>',
                    unsafe_allow_html=True)
        st.markdown(
            '<a href="https://renyidake-streamlit-streamlitexcel-qaktjq.streamlit.app/" target="_blank">合并Excel文件</a>',
            unsafe_allow_html=True)
        st.markdown(
            '<a href="https://renyidake-streamlit-streamlitexcel-xi7xi6.streamlit.app/" target="_blank">合并Excel工作表</a>',
            unsafe_allow_html=True)
        st.markdown(
            '<a href="https://renyidake-streamlit-streamlit-i18h6p.streamlit.app/" target="_blank">数据筛选</a>',
            unsafe_allow_html=True)
    if selected_category == '分析工具':
        st.markdown('<a href="https://renyidake.github.io/" target="_blank">数据大屏</a>', unsafe_allow_html=True)
        st.markdown('<a href="http://113.125.55.194:5000/" target="_blank">网页数据库</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://app-45tgvkzdc9whvcezhwahn4.streamlit.app/" target="_blank">专利分析模板</a>',
                    unsafe_allow_html=True)
        st.markdown(
            '<a href="https://renyidake-streamlit-streamlit-nl7xmx.streamlit.app/" target="_blank">自定义数据可视化</a>',
            unsafe_allow_html=True)


    # # 根据所选分类展示页面按钮
    # selected_pages = tool_categories[selected_category]
    # print(selected_pages)
    # for page in selected_pages:
    #     if st.sidebar.button('数据大屏'):
    #         st.markdown('<a href="https://renyidake.github.io/" target="_blank">数据大屏</a>', unsafe_allow_html=True)
    #     if st.sidebar.button('网页数据库'):
    #         st.markdown('<a href="http://113.125.55.194:5000/" target="_blank">网页数据库</a>', unsafe_allow_html=True)
    #
    #
    st.sidebar.subheader('质检部工具')
    if st.sidebar.button('随机抽检'):
        # webbrowser.open_new_tab('https://renyidake.github.io/')
        st.write("暂无")
    st.sidebar.subheader('代理部工具')
    if st.sidebar.button('查新检索'):
        st.write("暂无")
    st.sidebar.subheader('商务部工具')
    if st.sidebar.button('专利数据统计'):
        st.write("暂无")
    st.sidebar.subheader('项目部工具')
    if st.sidebar.button('Word表格自动填充'):
        st.write("暂无")
    st.sidebar.subheader('综合部工具')
    if st.sidebar.button('邮件发送'):
        st.write("暂无")
