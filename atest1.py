import pandas as pd
import streamlit as st
from streamlit_apex_charts import line_chart, bar_chart, pie_chart, area_chart, radar_chart
# encoding=utf-8
st.set_page_config(page_title="快速基于Dataframe构建数据大屏", layout="wide")

file = st.sidebar.file_uploader("请上传execl表格", type=["xlsx"])
if file is not None:
    df1 = pd.read_excel(file)
    column = df1.columns  # 获取表头
    df = pd.DataFrame(df1, columns=column)

    # df['订单日期'] = df['订单日期'].dt.strftime('%Y-%m-%d %H:%M:%S')
    line_chart('Line chart', df)

    # line_chart('Line chart', df)
    c1, c2 = st.columns(2)

    with c1:
        bar_chart('Bar chart', df)
        pie_chart('Pie chart', df)
    with c2:
        area_chart('Area chart', df)
        radar_chart('Radar chart', df)