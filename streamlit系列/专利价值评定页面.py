import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import random
import base64
from pandas.api.types import CategoricalDtype
import time
from docxtpl import DocxTemplate
import xlwings as xw
import tempfile
import os

path='D:\工具'
name='产出'
isExists=os.path.exists(path+name)
if not isExists:
    os.makedirs(path+name)

# 创建一个临时文件夹用于存储上传的文件
temp_dir = tempfile.TemporaryDirectory()
uploaded_files = st.file_uploader('上传Excel文件,请务必保持格式正确，具体请参照下表！', accept_multiple_files=True, type='xlsx')

if not uploaded_files:
    df=pd.read_excel('streamlit系列/评分表2.xlsx')  # streamlit系列/2020-2022中之信.xlsx
    st.write("数据表格式:")
    df
    st.write("Word表格模版:")
    st.image("streamlit系列/专利价值评分表.png")  # streamlit系列/新不二LOGO.png
    st.write("产出评分表样式:")
    st.image("streamlit系列/专利价值评分表示例.png")  # streamlit系列/新不二LOGO.png
else:
    for file in uploaded_files:
        # 将上传的文件保存到临时文件夹中
        with open(f"{temp_dir.name}/{file.name}", "wb") as f:
            f.write(file.getbuffer())
        # 获取临时文件的完整路径
        excel_file_path = f"{temp_dir.name}/{file.name}"
        df = pd.read_excel(excel_file_path)
    st.write("数据表格式:")
    df
    st.write("Word表格模版:")
    st.image("streamlit系列/专利价值评分表.png")  # streamlit系列/新不二LOGO.png
    st.write("产出评分表样式:")
    st.image("streamlit系列/专利价值评分表示例.png")  # streamlit系列/新不二LOGO.png

    excel_file = excel_file_path
    word_template = 'streamlit系列/评分表模板.docx'

    list_value = []
    app = xw.App(visible=True, add_book=False)
    workbook = app.books.open(excel_file)
    sheet = workbook.sheets[0]
    sheet_list = sheet.used_range.value
    for i in range(1, len(sheet_list)):  # From the second row onwards (excluding header)
        row_data = {}
        for j in range(len(sheet_list[i])):
            if isinstance(sheet_list[i][j], float):
                row_data[sheet_list[0][j]] = str(sheet_list[i][j])[:-2]
            else:
                row_data[sheet_list[0][j]] = sheet_list[i][j]
        list_value.append(row_data)
        row_data['技术价值分数'] = round(float(row_data['技术价值分数']), 2)
        row_data['法律价值分数'] = round(float(row_data['法律价值分数']), 2)
        row_data['经济价值分数'] = round(float(row_data['经济价值分数']), 2)
        row_data['总分数'] = round(float(row_data['总分数']), 2)

    workbook.close()
    app.quit()
    for i, data in enumerate(list_value):
        data_m = data['申请号'].replace('/', '-')
        document = DocxTemplate(word_template)  # 使用DocxTemplate打开Word模板文件
        document.render(data)  # 将数据填充到模板中
        output_path = r'D:\工具产出\%s.专利%s的价值评分表.docx' % (i + 1, data_m)  # 每行数据生成一个单独的Word文档文件名
        document.save(output_path)  # 保存填充后的模板为新的Word文档

temp_dir.cleanup()
