# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# from pylab import mpl
# import docx
# from docx import Document
# from docx.oxml.ns import qn
# from random import choice
# from docx.enum.style import WD_STYLE_TYPE
#
# from docx.shared import Cm
# from openpyxl import load_workbook
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QFileDialog
# import os
# import sys
# import random
# from scipy.interpolate import make_interp_spline
# import pyecharts.options as opts
# from pyecharts.charts import Line, Grid,Bar,PictorialBar,Pie,Funnel,Scatter,Map,Geo,EffectScatter,Gauge,Polar,Radar,HeatMap,Graph,WordCloud
# from pyecharts.commons.utils import JsCode
# from pyecharts.faker import Faker
# from pyecharts.render import make_snapshot
# from snapshot_pyppeteer import snapshot as driver
# from pyecharts.globals import ThemeType
# from pyecharts.globals import SymbolType
# # encoding=utf-8
# #导入pywin32包
# import win32com.client as win32
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.oxml.ns import qn
# from docx.shared import Pt,RGBColor
# from pandas.api.types import CategoricalDtype
# import shutil
# from matplotlib.ticker import MaxNLocator

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

# # 加载自定义字体文件
mpl.font_manager.fontManager.addfont('streamlit报告模版/simhei.ttf')

mpl.rcParams['font.sans-serif'] = ["SimHei"]
# 正常显示中文字符
mpl.rcParams["axes.unicode_minus"] = False
def genOrder(df,orderList,colName): #自定义排序
    cat_order = CategoricalDtype(orderList,ordered=True)
    df[colName] = df[colName].astype(cat_order)
    return df
name_map = {
            'Singapore Rep.': '新加坡',
            'Dominican Rep.': '多米尼加',
            'Palestine': '巴勒斯坦',
            'Bahamas': '巴哈马',
            'Timor-Leste': '东帝汶',
            'Afghanistan': '阿富汗',
            'Guinea-Bissau': '几内亚比绍',
            "Côte d'Ivoire": '科特迪瓦',
            'Siachen Glacier': '锡亚琴冰川',
            "Br. Indian Ocean Ter.": '英属印度洋领土',
            'Angola': '安哥拉',
            'Albania': '阿尔巴尼亚',
            'United Arab Emirates': '阿联酋',
            'Argentina': '阿根廷',
            'Armenia': '亚美尼亚',
            'French Southern and Antarctic Lands': '法属南半球和南极领地',
            'Australia': '澳大利亚',
            'Austria': '奥地利',
            'Azerbaijan': '阿塞拜疆',
            'Burundi': '布隆迪',
            'Belgium': '比利时',
            'Benin': '贝宁',
            'Burkina Faso': '布基纳法索',
            'Bangladesh': '孟加拉国',
            'Bulgaria': '保加利亚',
            'The Bahamas': '巴哈马',
            'Bosnia and Herz.': '波斯尼亚和黑塞哥维那',
            'Belarus': '白俄罗斯',
            'Belize': '伯利兹',
            'Bermuda': '百慕大',
            'Bolivia': '玻利维亚',
            'Brazil': '巴西',
            'Brunei': '文莱',
            'Bhutan': '不丹',
            'Botswana': '博茨瓦纳',
            'Central African Rep.': '中非',
            'Canada': '加拿大',
            'Switzerland': '瑞士',
            'Chile': '智利',
            'China': '中国',
            'Ivory Coast': '象牙海岸',
            'Cameroon': '喀麦隆',
            'Dem. Rep. Congo': '刚果民主共和国',
            'Congo': '刚果',
            'Colombia': '哥伦比亚',
            'Costa Rica': '哥斯达黎加',
            'Cuba': '古巴',
            'N. Cyprus': '北塞浦路斯',
            'Cyprus': '塞浦路斯',
            'Czech Rep.': '捷克',
            'Germany': '德国',
            'Djibouti': '吉布提',
            'Denmark': '丹麦',
            'Algeria': '阿尔及利亚',
            'Ecuador': '厄瓜多尔',
            'Egypt': '埃及',
            'Eritrea': '厄立特里亚',
            'Spain': '西班牙',
            'Estonia': '爱沙尼亚',
            'Ethiopia': '埃塞俄比亚',
            'Finland': '芬兰',
            'Fiji': '斐',
            'Falkland Islands': '福克兰群岛',
            'France': '法国',
            'Gabon': '加蓬',
            'United Kingdom': '英国',
            'Georgia': '格鲁吉亚',
            'Ghana': '加纳',
            'Guinea': '几内亚',
            'Gambia': '冈比亚',
            'Guinea Bissau': '几内亚比绍',
            'Eq. Guinea': '赤道几内亚',
            'Greece': '希腊',
            'Greenland': '格陵兰',
            'Guatemala': '危地马拉',
            'French Guiana': '法属圭亚那',
            'Guyana': '圭亚那',
            'Honduras': '洪都拉斯',
            'Croatia': '克罗地亚',
            'Haiti': '海地',
            'Hungary': '匈牙利',
            'Indonesia': '印度尼西亚',
            'India': '印度',
            'Ireland': '爱尔兰',
            'Iran': '伊朗',
            'Iraq': '伊拉克',
            'Iceland': '冰岛',
            'Israel': '以色列',
            'Italy': '意大利',
            'Jamaica': '牙买加',
            'Jordan': '约旦',
            'Japan': '日本',
            'Kazakhstan': '哈萨克斯坦',
            'Kenya': '肯尼亚',
            'Kyrgyzstan': '吉尔吉斯斯坦',
            'Cambodia': '柬埔寨',
            'Korea': '韩国',
            'Kosovo': '科索沃',
            'Kuwait': '科威特',
            'Lao PDR': '老挝',
            'Lebanon': '黎巴嫩',
            'Liberia': '利比里亚',
            'Libya': '利比亚',
            'Sri Lanka': '斯里兰卡',
            'Lesotho': '莱索托',
            'Lithuania': '立陶宛',
            'Luxembourg': '卢森堡',
            'Latvia': '拉脱维亚',
            'Morocco': '摩洛哥',
            'Moldova': '摩尔多瓦',
            'Madagascar': '马达加斯加',
            'Mexico': '墨西哥',
            'Macedonia': '马其顿',
            'Mali': '马里',
            'Myanmar': '缅甸',
            'Montenegro': '黑山',
            'Mongolia': '蒙古',
            'Mozambique': '莫桑比克',
            'Mauritania': '毛里塔尼亚',
            'Malawi': '马拉维',
            'Malaysia': '马来西亚',
            'Namibia': '纳米比亚',
            'New Caledonia': '新喀里多尼亚',
            'Niger': '尼日尔',
            'Nigeria': '尼日利亚',
            'Nicaragua': '尼加拉瓜',
            'Netherlands': '荷兰',
            'Norway': '挪威',
            'Nepal': '尼泊尔',
            'New Zealand': '新西兰',
            'Oman': '阿曼',
            'Pakistan': '巴基斯坦',
            'Panama': '巴拿马',
            'Peru': '秘鲁',
            'Philippines': '菲律宾',
            'Papua New Guinea': '巴布亚新几内亚',
            'Poland': '波兰',
            'Puerto Rico': '波多黎各',
            'Dem. Rep. Korea': '朝鲜',
            'Portugal': '葡萄牙',
            'Paraguay': '巴拉圭',
            'Qatar': '卡塔尔',
            'Romania': '罗马尼亚',
            'Russia': '俄罗斯',
            'Rwanda': '卢旺达',
            'W. Sahara': '西撒哈拉',
            'Saudi Arabia': '沙特阿拉伯',
            'Sudan': '苏丹',
            'S. Sudan': '南苏丹',
            'Senegal': '塞内加尔',
            'Solomon Is.': '所罗门群岛',
            'Sierra Leone': '塞拉利昂',
            'El Salvador': '萨尔瓦多',
            'Somaliland': '索马里兰',
            'Somalia': '索马里',
            'Serbia': '塞尔维亚',
            'Suriname': '苏里南',
            'Slovakia': '斯洛伐克',
            'Slovenia': '斯洛文尼亚',
            'Sweden': '瑞典',
            'Swaziland': '斯威士兰',
            'Syria': '叙利亚',
            'Chad': '乍得',
            'Togo': '多哥',
            'Thailand': '泰国',
            'Tajikistan': '塔吉克斯坦',
            'Turkmenistan': '土库曼斯坦',
            'East Timor': '东帝汶',
            'Trinidad and Tobago': '特里尼达和多巴哥',
            'Tunisia': '突尼斯',
            'Turkey': '土耳其',
            'Tanzania': '坦桑尼亚',
            'Uganda': '乌干达',
            'Ukraine': '乌克兰',
            'Uruguay': '乌拉圭',
            'United States': '美国',
            'Uzbekistan': '乌兹别克斯坦',
            'Venezuela': '委内瑞拉',
            'Vietnam': '越南',
            'Vanuatu': '瓦努阿图',
            'West Bank': '西岸',
            'Yemen': '也门',
            'South Africa': '南非',
            'Zambia': '赞比亚',
            'Zimbabwe': '津巴布韦',
            'Comoros': '科摩罗'
        }  ## 国家中英文名 对照表
shengfen=['北京','天津','上海','重庆','河北','河南','云南','辽宁','黑龙江','湖南',
           '安徽','山东','新疆','江苏','浙江','江西','湖北','广西','甘肃','山西',
           '内蒙古','陕西','吉林','福建','贵州','广东','青海','西藏','四川','宁夏',
           '海南','台湾','香港','澳门']
zhixiashi=['北京','天津','上海','重庆']
nianfen=['2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
wuju=['中国','美国','日本','韩国','欧洲专利局']

def biaoti(bt):
    paragraph1 = document.add_paragraph('%s'%bt)
    paragraph1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER  # LEFT RIGHT CENTER
    run1 = paragraph1.runs[0]
    run1.font.name = '宋体'
    run1.font.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run1.font.size = Pt(16)
    run1.font.bold = False
    run1.font.color.rgb = RGBColor(0, 0, 0)
def biaoti2(bt2):
    paragraph1 = document.add_paragraph('%s'%bt2)
    paragraph1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT  # LEFT RIGHT CENTER
    run1 = paragraph1.runs[0]
    run1.font.name = '黑体'
    run1.font.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    run1.font.size = Pt(20)
    run1.font.bold = False
    run1.font.color.rgb = RGBColor(146,208,80)
def wenben(wb):
    paragraph1 = document.add_paragraph('%s'%wb)
    paragraph1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT  # LEFT RIGHT CENTER
    paragraph1.paragraph_format.first_line_indent = Cm(0.74)
    run1 = paragraph1.runs[0]

    run1.font.name = '宋体'
    run1.font.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run1.font.size = Pt(12)
    run1.font.bold = False
    run1.font.color.rgb = RGBColor(0, 0, 0)



#侧边栏初始状态为折叠 streamlit 页面布局为 宽
st.set_page_config(initial_sidebar_state='expanded',layout='wide')
# st.image("streamlit报告模版/新不二LOGO.png")  # streamlit系列/新不二LOGO.png
uploaded_files = st.file_uploader('上传Excel文件,请务必包含：公开(公告)号、受理局、标题、专利类型、申请年、优先权国家、[标]当前申请(专利权)人、当前申请(专利权)人数量、发明人、发明人数量、IPC分类号、IPC主分类号(小类)、'
                                  '简单法律状态、法律状态/事件、当前申请(专利权)人州/省、当前申请(专利权)人地市、当前申请(专利权)人区县，请参照下表！', accept_multiple_files=True, type='xlsx')

if not uploaded_files:
    def load_df():
        return pd.read_excel('streamlit报告模版/AR眼镜.XLSX')  # streamlit系列/2020-2022中之信.xlsx
    df = load_df()
else:
    for file in uploaded_files:
        print(file)
        df = pd.read_excel(file)
# 侧边栏 标题
st.sidebar.header('➡⌛⌛⌛分析模版选择⌛⌛⌛⬅')

st.text_input("请输入要分析的城市：如浙江、河南、山东(若未输入则数据范围是总数据)", key="name")
shengji=st.session_state.name
print(shengji)
# 页面 标题
st.title('🎉🎉🎉省级专利数据分析看板🎉🎉🎉')

dfm=df.loc[(df['标题'] != '-')]
dfm=dfm.loc[dfm['当前申请(专利权)人州/省'].str.contains(shengji,na=False),:]
st.dataframe(dfm)
# 指标 计算
zongshenqing = int(dfm['公开(公告)号'].count())

shouquan = dfm.loc[dfm['法律状态/事件'].str.contains('授权', na=False), :]
shouquan = shouquan['法律状态/事件'].count()

bohui = dfm.loc[dfm['法律状态/事件'].str.contains('驳回', na=False),:]
bohui = bohui['法律状态/事件'].count()

faming = dfm.loc[(dfm['专利类型'] == '发明申请')| (dfm['专利类型'] == '授权发明')]
faming = faming['专利类型'].count()
shiyong = dfm.loc[(dfm['专利类型'] == '实用新型')]
shiyong = shiyong['专利类型'].count()
waiguan = dfm.loc[(dfm['专利类型'] == '外观设计')]
waiguan = waiguan['专利类型'].count()

left1, mid1, right1 = st.columns(3)

left2, mid2, right2 = st.columns(3)
# 显示计算度量
with left1:
    st.subheader('📚总申请量:')
    st.subheader(f'{zongshenqing:,}')

with mid1:
    st.subheader('📖授权专利:')
    st.subheader(f'{shouquan: }')

with right1:
    st.subheader('♻驳回专利:')
    st.subheader(f'{bohui:,}')
with left2:
    st.subheader('📗发明专利:')
    st.subheader(f'{faming:,}')
with mid2:
    st.subheader('📘实用新型:')
    st.subheader(f'{shiyong: }')
with right2:
    st.subheader('📙外观设计:')
    st.subheader(f'{waiguan:,}')

# 设置工具箱选项
toolbox_opts = {
    # 工具箱的特性配置，可通过键值对进行配置
    'feature': {
        # 数据视图工具，可以展现当前图表所用的数据，编辑后可以动态更新
        'dataView': {'show': True, 'readOnly': False},
        # 配置项缩放工具，可以选择直接显示在图表上还是弹出模态窗口显示
        'dataZoom': {'show': True, 'yAxisIndex': 'none'},
        # 动态类型切换工具，支持柱状图和折线图的切换
        'magicType': {'show': True, 'type': ['line', 'bar']},
        # 还原工具，用于重置图表的缩放、移动操作
        'restore': {'show': True},
        # 保存为图片工具
        'saveAsImage': {'show': True},
    },
}
# 设置工具箱选项
toolbox_opts2 = {
    # 工具箱的特性配置，可通过键值对进行配置
    'feature': {
        # 数据视图工具，可以展现当前图表所用的数据，编辑后可以动态更新
        'dataView': {'show': True, 'readOnly': False},
        # 配置项缩放工具，可以选择直接显示在图表上还是弹出模态窗口显示
        'dataZoom': {'show': True, 'yAxisIndex': 'none'},

        # 还原工具，用于重置图表的缩放、移动操作
        'restore': {'show': True},
        # 保存为图片工具
        'saveAsImage': {'show': True},
    },
}
# 设置工具箱选项
toolbox_opts3 = {
    # 工具箱的特性配置，可通过键值对进行配置
    'feature': {
        # 数据视图工具，可以展现当前图表所用的数据，编辑后可以动态更新
        'dataView': {'show': True, 'readOnly': False},

        # 还原工具，用于重置图表的缩放、移动操作
        'restore': {'show': True},
        # 保存为图片工具
        'saveAsImage': {'show': True},
    },
}

##专利概况
##专利申请趋势
def huitu11():
    global document
    def cunchupng():
        dfmb=dfm
        df1 = dfmb[['公开(公告)号', '申请年']]
        df1 = df1.astype({'申请年': 'str'})
        df1 = df1.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df1 = df1.sort_values(by='申请年', ascending=True)
        df1.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df1, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df1 = dfx
        df1 = df1.astype({'申请数量': 'int'})
        print(df1)

        dfmb = dfm.loc[(dfm['简单法律状态'] == '有效')]
        df2 = dfmb[['公开(公告)号', '申请年']]
        df2 = df2.astype({'申请年': 'str'})
        df2 = df2.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df2 = df2.sort_values(by='申请年', ascending=True)
        df2.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df2, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df2 = dfx
        df2 = df2.astype({'申请数量': 'int'})
        print(df2)

        dfmb = dfm.loc[(dfm['简单法律状态'] == '失效')]
        df3 = dfmb[['公开(公告)号', '申请年']]
        df3 = df3.astype({'申请年': 'str'})
        df3 = df3.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df3 = df3.sort_values(by='申请年', ascending=True)
        df3.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df3, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df3 = dfx
        df3 = df3.astype({'申请数量': 'int'})
        print(df3)

        dfmb = dfm.loc[(dfm['简单法律状态'] == '审中')]
        df4 = dfmb[['公开(公告)号', '申请年']]
        df4 = df4.astype({'申请年': 'str'})
        df4 = df4.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df4 = df4.sort_values(by='申请年', ascending=True)
        df4.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df4, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df4 = dfx
        df4 = df4.astype({'申请数量': 'int'})
        print(df4)

        listx = list(df1['申请年'])
        listy1 = list(df1['申请数量'])
        listy2 = list(df2['申请数量'])
        listy3 = list(df3['申请数量'])
        listy4 = list(df4['申请数量'])
        line = (
            Line(init_opts=opts.InitOpts(
                bg_color='#FFFFFF'))
            .add_xaxis(listx)
            .add_yaxis(
                series_name='总申请量',
                y_axis=listy1,
                # is_selected=True,##是否选中图例
                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    type_="solid",
                ),  # 线条配置
            ))
        bar = (
            Bar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis(
                series_name='有效',
                y_axis=listy2,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family='serif',  #
                ),  # 标签配置项
            )
            .add_yaxis(
                series_name='无效',
                y_axis=listy3,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family='serif',  #
                ),  # 标签配置项
            )
            .add_yaxis(
                series_name='审中',
                y_axis=listy4,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family='serif',  #
                ),  # 标签配置项
            )
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",  # 坐标轴类型
                    name='申请年',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(
                        rotate=90,
                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                    )
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    name='申请数量',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    type_='plain', is_show=True,
                    pos_right='right',  # 右边
                    orient='vertical',
                    pos_top='10%',  # 距离上边界15%
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                    background_color="transparent",
                    border_color="transparent",
                ),
            ))
        c = bar.overlap(line)
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_bottom="15%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
           <style>
           .chart-container {
               width: 100%;
               height: 100%;
               max-width: 1000px;

               margin: 0 auto;
           }
           </style>
           '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)

st.subheader("""🎈🎈🎈专利概况🎈🎈🎈""")
st.write('专利概况部分提供了关于研究领域的总体情况。这包括专利数量的趋势，例如每年的专利申请数量和授予数量的变化。还可以考虑专利类型的分布，' \
          '如发明专利、实用新型专利和外观设计专利。通过分析专利概况，我们可以了解该领域的发展状况和创新活动的强度。')
st.subheader("""专利申请趋势""")
st.write('该图表展示了近20年的专利申请趋势。图表包括了总申请量的折线图以及有效、无效和审中专利的簇型柱状图。折线图显示了总申请量随时间的变化趋势。通过观察折线的上升或下降趋势，' \
         '可以得出专利申请的整体趋势。如果折线呈现上升趋势，表示专利申请量逐年增加，可能反映了创新活动的增加或对知识产权保护的关注度提高。相反，如果折线呈下降趋势，可能表示专利申请量逐年减少，' \
         '可能源于创新活动的减少或其他因素导致的减少对知识产权的申请。簇型柱状图展示了有效、无效和审中专利在不同年份的分布情况。每个柱状图表示一年的专利申请情况，并根据专利的状态进行颜色区分。' \
         '通过比较不同柱状图之间的高度和颜色分布，可以得出不同专利状态的相对趋势。该图表揭示了专利申请趋势和专利状态的变化情况。通过观察总申请量的变化，可以了解到创新活动的整体趋势和对知识产权的关注程度。' \
         '簇型柱状图则提供了不同专利状态（有效、无效和审中）的比较和分布情况，帮助我们了解专利的审批和有效性情况。可用于研究专利申请的趋势、知识产权保护策略以及创新活动的变化等方面。')
huitu11()
##简单法律状态构成
def huitu12():
    global document
    def cunchupng():
        dfmb = dfm
        df1 = dfmb[['简单法律状态', '公开(公告)号']]
        df1 = df1.groupby('简单法律状态', as_index=False)['公开(公告)号'].count()
        df1 = df1.sort_values(by='公开(公告)号', ascending=False)
        df1.columns = ['简单法律状态', '申请数量']
        df1 = df1.loc[(df1['简单法律状态'] != '-')]
        print(df1)
        listx = list(df1['简单法律状态'])
        listy = list(df1['申请数量'])
        data_pair = [list(z) for z in zip(listx, listy)]
        data_pair.sort(key=lambda x: x[1], reverse=True)  # 排序

        c = (
            Pie(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add(
                series_name="",
                data_pair=data_pair,
                radius=["40%", "65%"],
                center=["40%", "45%"],

            )
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts3['feature']
                ),

                legend_opts=opts.LegendOpts(
                    type_='plain', is_show=True,
                    pos_right='right',  # 右边
                    orient='vertical',
                    pos_top='10%',  # 距离上边界15%
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                    background_color="transparent",
                    border_color="transparent",

                    textstyle_opts=opts.TextStyleOpts(font_size=20, font_style='normal', font_weight='bold', )))
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{b}:{c}\n{d}%",
                    font_size=20,
                    font_style='normal',
                    font_weight='bold',
                    color='auto',  # 系列颜色
                ))
        )
        return c

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
               <style>
               .chart-container {
                   width: 100%;
                   height: 100%;
                   max-width: 1000px;

                   margin: 0 auto;
               }
               </style>
               '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""法律状态构成""")
st.write('饼图的圆环区域代表了总体专利的数量。每个简单法律状态在饼图中以扇形区域的形式表示，并且每个扇形区域的大小反映了该法律状态在总体专利数量中所占比例的大小。通过观察每个简单法律状态扇形区域的大小，' \
         '可以了解不同法律状态在总体中的相对分布。如果某个简单法律状态的扇形区域较大，表示该法律状态在总体中所占比例较高，相应的专利具有该法律状态的较高比例。相反，如果某个简单法律状态的扇形区域较小，' \
         '表示该法律状态在总体中所占比例较低，相应的专利数量较少。该图可以用于展示总体专利的简单法律状态构成情况，帮助我们了解不同法律状态的分布情况和比例关系。它可以用于研究专利的法律状态变化、' \
         '知识产权保护情况和专利审批的进展。通过观察饼图中不同扇形区域的比例关系，可以洞察专利的法律保护状况以及专利申请者在不同法律状态下的选择策略。')
huitu12()


##专利类型构成
def huitu13():
    global document
    def cunchupng():
        dfmb = dfm
        df1 = dfmb[['专利类型', '公开(公告)号']]
        df1 = df1.loc[(df1['专利类型'] != '-')]
        df1 = df1.groupby('专利类型', as_index=False)['公开(公告)号'].count()
        df1 = df1.sort_values(by='公开(公告)号', ascending=False)
        df1.columns = ['专利类型', '申请数量']
        df1 = df1.loc[(df1['专利类型'] != '-')]
        listx = list(df1['专利类型'])
        listy = list(df1['申请数量'])
        data_pair = [list(z) for z in zip(listx, listy)]
        data_pair.sort(key=lambda x: x[1], reverse=True)  # 排序

        c = (
            Pie(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add(
                series_name="",
                data_pair=data_pair,
                radius=["40%", "65%"],
                center=["40%", "45%"],
                rosetype="radius",
            )
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts3['feature']
                ),

                legend_opts=opts.LegendOpts(
                    type_='plain', is_show=True,
                    pos_right='right',  # 右边
                    orient='vertical',
                    pos_top='10%',  # 距离上边界15%
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                    background_color="transparent",
                    border_color="transparent",

                    textstyle_opts=opts.TextStyleOpts(font_size=20, font_style='normal', font_weight='bold', )))
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{b}:{c}\n{d}%",
                    font_size=20,
                    font_style='normal',

                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                )

            )
        )
        return c

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                   <style>
                   .chart-container {
                       width: 100%;
                       height: 100%;
                       max-width: 1000px;

                       margin: 0 auto;
                   }
                   </style>
                   '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""专利类型构成""")
st.write('饼图的圆环区域代表了总体专利数量。每个专利类型在饼图中以扇形区域的形式表示，并且每个扇形区域的大小反映了该专利类型在总体专利数量中所占比例的大小。通过观察每个专利类型扇形区域的大小，' \
         '可以了解到不同专利类型在总体中的相对重要性。如果某个专利类型的扇形区域较大，表示该专利类型在总体中所占比例较高，具有较大的影响力。相反，如果某个专利类型的扇形区域较小，' \
         '表示该专利类型在总体中所占比例较低，具有较小的影响力。该图可以用于展示总体专利类型的构成情况，帮助我们了解不同专利类型的相对重要性和影响力。它可以用于研究专利领域的整体分布情况，' \
         '揭示专利类型的偏好和技术创新的方向。通过观察饼图中不同扇形区域的比例关系，可以洞察专利申请者和创新者的兴趣和趋势。')
huitu13()


##技术生命周期
def huitu14():
    global document
    dfmb=dfm[['申请年','当前申请(专利权)人数量','公开(公告)号']]
    dfmb = dfmb.astype({'申请年': 'str'})
    dfmb = dfmb.query('申请年 in %s ' % nianfen)
    dfmb = dfmb.loc[(dfmb['当前申请(专利权)人数量'] != '-')]
    dfmb = dfmb.astype({'当前申请(专利权)人数量': 'int'})
    df1 = dfmb.groupby('申请年', as_index=False).agg({'公开(公告)号':'count','当前申请(专利权)人数量':sum})
    df1.columns= ['申请年', '申请数量','申请人数量']
    print(df1)

    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.12)  # 图与画布四周距离
    plt.plot( df1['申请数量'],df1['申请人数量'], color="#F5616F", linestyle='-', linewidth=2,)  # X轴Y轴数据，颜色，线条样式，粗度，标记点，填充
    plt.xlabel('申请数量', fontdict={'size': 14})
    plt.ylabel('申请人数量', fontdict={'size': 14})
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    for a, b ,c in zip(df1['申请数量'],df1['申请人数量'],df1['申请年'], ):
        plt.text(a, b, format(c), ha='center', va='bottom', fontsize=10, alpha=0.9)
    st.pyplot(fig)

st.subheader("""技术生命周期""")
st.write('通过该图表，可以观察到专利申请趋势以及参与该领域的申请人数量的变化趋势。若折线上升可能表示该技术领域的活跃度增加，申请数量和申请人数量都在增长。' \
         '下降可能表示技术的成熟度增加或市场饱和，导致申请数量和申请人数量减少。高峰和低谷可以表示某些特定事件或趋势的发生。' \
         '比较不同年份之间的数据，可以观察到技术领域的发展情况。如申请数量和申请人数量的增加或减少可以指示技术的普及度或竞争状况。')
huitu14()
#专利运营
def huitu15():
    global document
    dfmb=dfm
    df1 = dfmb[['法律状态/事件','申请年', '公开(公告)号' ]]
    df1 = df1.astype({'申请年': 'str'})
    df1 = df1.query('申请年 in %s ' % nianfen)
    series = df1['法律状态/事件'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df1[['申请年', '公开(公告)号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['申请年', '公开(公告)号', '法律状态/事件']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['申请年'],df_11['公开(公告)号'], df_11['法律状态/事件'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)
    df1 = df_11
    df1.columns=['申请年','公开(公告)号','法律状态事件',]
    print(df1)
    df1 = df1.loc[(df1['法律状态事件'].str.contains('权利转移', na=False)) | (
        df1['法律状态事件'].str.contains('质押', na=False))| (
        df1['法律状态事件'].str.contains('许可', na=False))]
    print(df1)
    df1 = df1.groupby(['申请年', '法律状态事件'], as_index=False)['公开(公告)号'].count()
    df1 = df1.sort_values(by='申请年', ascending=True)
    df1.columns = ['申请年', '法律状态事件', '申请数量']
    print(df1)

    xmax = max(df1['申请数量'])
    xmin = min(df1['申请数量'])
    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.2, right=0.95, top=0.95, bottom=0.15) #图与画布四周距离
    print(len(df1['申请数量']))
    color=["#3685fe", "#f5616f","#50c48f",  "#26ccd8", "#9977ef",
            "#f7b13f", "#f9e264", "#f47a75", "#009db2", "#024b51",]
    for i in range(0,len(df1['申请数量'])):
        if len(df1['申请数量']) > i*10:
            color.extend(color)
        if len(color)>len(df1['申请数量']):
            break

    color=random.sample(color, len(df1['申请数量']))

    plt.grid(ls='-.', lw=0.35)  # 增加栅格
    plt.scatter( df1['申请年'],df1['法律状态事件'], df1['申请数量']/xmax*1000,c=color, alpha=0.7)
    plt.xlabel('申请年',fontdict={ 'size':14})
    plt.ylabel('专利运营情况',fontdict={ 'size':14})
    plt.xticks(size=12,rotation=90)  # X轴刻度，标签，旋转度
    plt.yticks(size=12)
    plt.ylim(-1,3)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    for a, b, c in zip(df1['申请年'],df1['法律状态事件'],  df1['申请数量']):
        plt.text(a, b, c, ha='center', va='center', fontsize=10, alpha=0.9)
    st.pyplot(fig)

st.subheader("""专利运营情况""")
st.write('该图表展示了近20年专利运营情况，包括权力转移、质押和许可。不同颜色区分不同的运营方式，圆的大小表示专利数量。通过观察圆形的大小和颜色分布，可以比较不同运营方式在不同年份中的专利数量变化。' \
         '如果某个运营方式的圆形在连续几年中保持较大的大小和相对稳定的颜色，表示该运营方式在这段时间内具有较高的专利数量。相反，如果某个运营方式的圆形在不同年份中出现较大的变化，表示该运营方式的专利数量有较大的波动。' \
         '该图表可以用于分析专利的运营方式及其变化趋势，帮助了解专利的商业利用和价值实现方式。通过观察不同运营方式的圆形大小和颜色分布，可以了解到各个运营方式的相对重要性和在不同年份的演变情况。' \
         '这有助于评估专利的商业价值和知识产权的管理策略。')
huitu15()


#专利联合趋势
def huitu16():
    global document
    dfmb=dfm.loc[(dfm['当前申请(专利权)人数量'] != '-') & (dfm['当前申请(专利权)人数量'] != '1')]
    df1 = dfmb[['公开(公告)号', '申请年']]
    df1 = df1.astype({'申请年': 'str'})
    df1 = df1.groupby('申请年', as_index=False)['公开(公告)号'].count()
    df1 = df1.sort_values(by='申请年', ascending=True)
    df1.columns = ['申请年', '申请数量']
    dfx = pd.DataFrame({'申请年': nianfen,
                        '申请次数': 0})
    dfx = pd.merge(dfx, df1, how='left', on='申请年')  # 补充df_1 缺失的年份数据
    dfx = dfx[['申请年', '申请数量']]
    dfx = dfx.fillna(0)  # 对为空的 属性补 0
    df1 = dfx
    df1 = df1.astype({'申请数量': 'int'})
    print(df1)

    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    ax.spines['left'].set_visible(False)  # 右边框
    ax.spines['bottom'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.15)  # 图与画布四周距离
    plt.plot(df1['申请年'], df1['申请数量'], color="#F5616F", linestyle='-', linewidth=2,marker='o',mfc="#F5616F",markersize=5,
             )  # X轴Y轴数据，颜色，线条样式，粗度，标记点，填充
    plt.stem(df1['申请年'], df1['申请数量'],linefmt='c-.',markerfmt='r',basefmt='-',)

    plt.ylabel('申请数量', fontdict={'size': 14})
    plt.xlabel('申请年', fontdict={'size': 14})
    plt.xticks(size=12,rotation=90)
    plt.yticks(size=12)
    # x,y轴整数刻度显示
    # plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    for a, b in zip(df1['申请年'], df1['申请数量']):
        plt.text(a, b, format(b), ha='center', va='bottom', fontsize=10, alpha=0.9)
    st.pyplot(fig)

st.subheader("""专利协同申请趋势""")
st.write('该图展示了协同专利的申请趋势。折线表示协同专利申请数量随时间的变化趋势，棉棒图则填充了折线和X轴之间的区域。通过观察折线的趋势和棉棒图的填充情况，可以了解到协同专利申请的整体趋势。' \
         '如果折线逐年上升，并且棉棒图逐渐扩大，表示协同专利申请数量不断增加，表明协同创新活动在相关领域中得到了更广泛的应用。相反，表示协同专利申请数量在减少，可能意味着协同创新活动的参与程度有所下降。' \
         '该图表可以用于分析协同创新活动的发展趋势和重要性。通过观察折线和棉棒图的变化，可以了解到协同创新的趋势以及不同时间段协同专利申请的数量变化。这有助于评估协同创新的影响力、合作伙伴关系以及技术交流的程度')
huitu16()




##地域分布 全球国家分布 国外国家分布 中国各省分布 省级各市分布 市级各区分布
##地图
def huitu21():
    global document
    def cunchupng() -> map:
        dfmb=dfm
        dfmb = dfmb.rename(columns={'当前申请(专利权)人地市': '当前申请人地市'})
        df1 = dfmb[['当前申请人地市', '公开(公告)号']]
        series = df1['当前申请人地市'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['公开(公告)号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '当前申请人地市']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开(公告)号'], df_11['当前申请人地市'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格
        df_11 = df_11.groupby('当前申请人地市', as_index=False)['公开(公告)号'].count()
        df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        df_11.columns = ['当前申请人地市', '申请数量']

        df1 = df_11
        for i in range(0, len(df1['当前申请人地市'])):
            df1.iat[i, 0] = df1.iat[i, 0] + '市'
        print(df1)
        listx = list(df1['当前申请人地市'])
        listy = list(df1['申请数量'])
        data_pair = [list(z) for z in zip(listx, listy)]
        xmin = min(listy)
        xmax = max(listy)
        map = (
            Map(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
                width="1000px",
                height="700px"
            ))
            .add(series_name="", data_pair=data_pair, maptype=shengji,  # world，china 省 市
                 is_map_symbol_show=False, name_map=name_map)  # 更改地图中文显示

            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="inside",
                    formatter="{b}",
                    font_size=8,

                    font_weight='bold',
                    color='black'))
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    is_show=False, ),
                visualmap_opts=opts.VisualMapOpts(  # 颜色映射
                    is_show=True,
                    min_=xmin,
                    max_=xmax,
                    range_text=['高', '低'],
                    pos_left="10%",
                    pos_bottom="30%",
                    range_color=["Gainsboro", "yellow", "red"],
                )
            )
        )

        # geo = (
        #     Geo(init_opts=opts.InitOpts(
        #         bg_color='#FFFFFF',
        #         width="1000px",
        #         height="700px"
        #     ))
        #     ## 新增坐标点
        #     .add_coordinate(
        #         name='中国',
        #         longitude=104,
        #         latitude=35,
        #     )
        #     .add_coordinate(
        #         name='日本',
        #         longitude=138,
        #         latitude=36,
        #     )
        #     .add_coordinate(
        #         name='韩国',
        #         longitude=128,
        #         latitude=36,
        #     )
        #     .add_coordinate(
        #         name='俄罗斯',
        #         longitude=87,
        #         latitude=64,
        #     )
        #     .add_coordinate(
        #         name='印度',
        #         longitude=78,
        #         latitude=20,
        #     )
        #     .add_coordinate(
        #         name='德国',
        #         longitude=10,
        #         latitude=51,
        #     )
        #     .add_coordinate(
        #         name='美国',
        #         longitude=-95,
        #         latitude=37,
        #     )
        #     .add_coordinate(
        #         name='加拿大',
        #         longitude=-106,
        #         latitude=56,
        #     )
        #
        #     # .add_coordinate(
        #     #     name='欧洲专利局',
        #     #     longitude=5,
        #     #     latitude=52,
        #     # )
        #     # .add_coordinate(
        #     #     name='世界知识产权组织',
        #     #     longitude=8,
        #     #     latitude=46,
        #     # )
        #     .add_coordinate(
        #         name='欧洲专利局',
        #         longitude=38.4,
        #         latitude=-52,
        #     )
        #     .add_coordinate(
        #         name='世界知识产权组织',
        #         longitude=-26.7,
        #         latitude=-52.1,
        #     )
        #     .add_coordinate(
        #         name='泰国',
        #         longitude=101,
        #         latitude=15,
        #     )
        #     .add_coordinate(
        #         name='新加坡',
        #         longitude=103.8,
        #         latitude=1.3,
        #     )
        #     .add_coordinate(
        #         name='英国',
        #         longitude=-3.4,
        #         latitude=55.3,
        #     )
        #     .add_coordinate(
        #         name='法国',
        #         longitude=2,
        #         latitude=46,
        #     )
        #     .add_coordinate(
        #         name='西班牙',
        #         longitude=-3.7,
        #         latitude=40,
        #     )
        #     .add_coordinate(
        #         name='葡萄牙',
        #         longitude=-82,
        #         latitude=39.4,
        #     )
        #     .add_coordinate(
        #         name='墨西哥',
        #         longitude=-102.5,
        #         latitude=23.6,
        #     )
        #     .add_coordinate(
        #         name='丹麦',
        #         longitude=9.5,
        #         latitude=56.2,
        #     )
        #     .add_coordinate(
        #         name='南非',
        #         longitude=22.9,
        #         latitude=-30.6,
        #     )
        #     .add_coordinate(
        #         name='巴西',
        #         longitude=-51.9,
        #         latitude=-14.2,
        #     )
        #     .add_coordinate(
        #         name='波兰',
        #         longitude=19,
        #         latitude=52,
        #     )
        #     .add_coordinate(
        #         name='土耳其',
        #         longitude=35.2,
        #         latitude=38.9,
        #     )
        #     .add_coordinate(
        #         name='哈萨克斯坦',
        #         longitude=66.9,
        #         latitude=48,
        #     )
        #     .add_coordinate(
        #         name='澳大利亚',
        #         longitude=133.7,
        #         latitude=-25.3,
        #     )
        #     .add_coordinate(
        #         name='欧盟',
        #         longitude=4.3,
        #         latitude=50.8,
        #     )
        #     .add_coordinate(
        #         name='印度尼西亚',
        #         longitude=113.9,
        #         latitude=-0.8,
        #     )
        #     .add_coordinate(
        #         name='菲律宾',
        #         longitude=122.08,
        #         latitude=13.72,
        #     )
        #     .add_coordinate(
        #         name='马来西亚',
        #         longitude=102.2,
        #         latitude=4.8,
        #     )
        #     .add_coordinate(
        #         name='以色列',
        #         longitude=35.2,
        #         latitude=31.8,
        #     )
        #
        #     .add_schema(maptype="world")  # 地图类型
        #     .add("geo", data_pair, symbol_size=20, )  # 名字 数据 尺寸
        #     .set_series_opts(
        #         label_opts=opts.LabelOpts(
        #             is_show=True,
        #             position="inside",
        #             formatter="{b}",
        #             font_size=10,
        #             font_style='normal',
        #             font_weight='bold',
        #             color='black'))
        #     .set_global_opts(
        #         legend_opts=opts.LegendOpts(
        #             is_show=False, ), )
        # )
        # grid = (
        #     Grid(init_opts=opts.InitOpts(
        #         bg_color='#FFFFFF',
        #         width="1000px",
        #         height="700px"
        #     ))
        #     .add(map, grid_opts=opts.GridOpts(), )  # 地图叠加
        #     .add(geo, grid_opts=opts.GridOpts())
        # )
        return map

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
               <style>
               .chart-container {
                   width: 100%;
                   height: 100%;
                   max-width: 1000px;

                   margin: 0 auto;
               }
               </style>
               '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)

st.subheader("""🎈🎈🎈专利地域分布🎈🎈🎈""")
st.write('地域分布部分涉及到专利申请和授予的地理位置信息。这可以揭示不同地区在特定领域的创新活动水平和技术优势。地域分布分析可以帮助确定研究重点区域，了解不同地区的专利产出情况，并评估各地区间的竞争态势。')
st.subheader("""专利地区分布""")
st.write('该地图展示了不同地区的专利数量分布情况。每个地区的专利数量用颜色填充区分，红色表示专利数量最高，黄色表示专利数量居中，灰色表示专利数量最低。颜色填充的程度反映了各地区专利数量的相对差异。' \
         '红色填充的地区表示专利数量较多，可能代表着创新活动较为活跃，专利保护较为重视。黄色填充的地区表示专利数量适中，可能表明该地区在创新和专利申请方面存在一定程度的活动。' \
         '灰色填充的地区表示专利数量较少，可能说明该地区的创新活动和专利保护相对较低。通过观察地图上不同地区的颜色分布，可以比较各地区之间的专利数量差异。' \
         '颜色填充的深浅程度可以反映出不同地区之间专利活动的相对强度。该图表可以用于分析全球范围内的创新热点地区、知识产权保护程度以及专利申请的地域分布。' \
         '同时，通过观察专利数量的分布情况，可以了解不同地区的创新活动水平、科技发展情况以及知识产权的重要性。')
huitu21()

##前五受理局申请趋势
def huitu22():
    global document
    def cunchupng() -> Line:

        dfmb=dfm
        dfmb = dfmb.rename(columns={'当前申请(专利权)人地市': '当前申请人地市'})
        df1 = dfmb[['当前申请人地市', '公开(公告)号']]
        series = df1['当前申请人地市'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['公开(公告)号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '当前申请人地市']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开(公告)号'], df_11['当前申请人地市'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格
        df_11 = df_11.groupby('当前申请人地市', as_index=False)['公开(公告)号'].count()
        df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        df_11.columns = ['当前申请人地市', '申请数量']
        dfx = df_11.head()
        print(dfx)
        ltx = list(dfx['当前申请人地市'])
        print(ltx)

        df1 = dfmb[['公开(公告)号', '申请年', '当前申请人地市', ]]
        df1 = df1.loc[(df1['当前申请人地市'] == ltx[0])]
        df1 = df1[['公开(公告)号', '申请年']]
        df1 = df1.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df1 = df1.sort_values(by='申请年', ascending=False)
        df1.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df1, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df1 = dfy
        df1 = df1.astype({'申请数量': 'int'})
        print(df1)

        df2 = dfmb[['公开(公告)号', '申请年', '当前申请人地市', ]]
        df2 = df2.loc[(df2['当前申请人地市'] == ltx[1])]
        df2 = df2[['公开(公告)号', '申请年']]
        df2 = df2.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df2 = df2.sort_values(by='申请年', ascending=False)
        df2.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df2, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df2 = dfy
        df2 = df2.astype({'申请数量': 'int'})
        print(df2)

        df3 = dfmb[['公开(公告)号', '申请年', '当前申请人地市', ]]
        df3 = df3.loc[(df3['当前申请人地市'] == ltx[2])]
        df3 = df3[['公开(公告)号', '申请年']]
        df3 = df3.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df3 = df3.sort_values(by='申请年', ascending=False)
        df3.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df3, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df3 = dfy
        df3 = df3.astype({'申请数量': 'int'})
        print(df3)

        df4 = dfmb[['公开(公告)号', '申请年', '当前申请人地市', ]]
        df4 = df4.loc[(df4['当前申请人地市'] == ltx[3])]
        df4 = df4[['公开(公告)号', '申请年']]
        df4 = df4.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df4 = df4.sort_values(by='申请年', ascending=False)
        df4.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df4, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df4 = dfy
        df4 = df4.astype({'申请数量': 'int'})
        print(df4)

        df5 = dfmb[['公开(公告)号', '申请年', '当前申请人地市', ]]
        df5 = df5.loc[(df5['当前申请人地市'] == ltx[4])]
        df5 = df5[['公开(公告)号', '申请年']]
        df5 = df5.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df5 = df5.sort_values(by='申请年', ascending=False)
        df5.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df5, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df5 = dfy
        df5 = df5.astype({'申请数量': 'int'})
        print(df5)

        listx = list(df1['申请年'])
        listy = list(df1['申请数量'])
        listx2 = list(df2['申请年'])
        listy2 = list(df2['申请数量'])
        listx3 = list(df3['申请年'])
        listy3 = list(df3['申请数量'])
        listx4= list(df4['申请年'])
        listy4= list(df4['申请数量'])
        listx5= list(df5['申请年'])
        listy5= list(df5['申请数量'])
        c = (
            Line(init_opts=opts.InitOpts(
                bg_color='#FFFFFF'))
            .add_xaxis(listx)
            .add_yaxis(
                series_name=ltx[0],
                y_axis=listy,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx2)
            .add_yaxis(
                series_name=ltx[1],
                y_axis=listy2,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx3)
            .add_yaxis(
                series_name=ltx[2],
                y_axis=listy3,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx4)
            .add_yaxis(
                series_name=ltx[3],
                y_axis=listy4,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx5)
            .add_yaxis(
                series_name=ltx[4],
                y_axis=listy5,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(

                xaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    type_="category",  # 坐标轴类型
                    name='申请年',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                        rotate=90)
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    name='申请次数',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    type_='plain', is_show=True,
                    pos_right='center',  # 右边
                    orient='horizontal',
                    pos_bottom='0%',  # 距离上边界15%
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                    background_color="transparent",
                    border_color="transparent",
                ),

            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
            )
        )
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_bottom="15%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
               <style>
               .chart-container {
                   width: 100%;
                   height: 100%;
                   max-width: 1000px;

                   margin: 0 auto;
               }
               </style>
               '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)
st.subheader("""主要受理局申请趋势""")
st.write('该图通过比较不同受理局的折线，可以了解它们在专利申请数量方面的相对变化。高折线表示该受理局的专利申请数量较多，而低折线表示申请数量较少。' \
         '图表中的高峰和低谷表示某些特定年份的专利申请数量。观察折线的走势可以了解专利申请数量的变化趋势。' \
         '通过比较不同受理局的折线，可以观察到它们在排名方面的变化。折线交叉或靠近表示受理局之间在排名上发生了变化。')
huitu22()




##技术主题分布
#词云图
def huitu31():
    global document
    def cunchupng():
        dfmb = dfm
        df1 = dfmb[['公开(公告)号', 'IPC分类号']]
        df1 = df1.loc[(df1['IPC分类号'] != '-')]
        series = df1['IPC分类号'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['公开(公告)号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', 'IPC分类号']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开(公告)号'], df_11['IPC分类号'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格

        df_11 = df_11.groupby('IPC分类号', as_index=False)['公开(公告)号'].count()
        df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        df_11.columns = ['IPC分类号', '申请数量']
        df1 = df_11[['IPC分类号', '申请数量']]

        listx = list(df1['IPC分类号'])
        listy = list(df1['申请数量'])
        xmax = max(listy)
        xmin = min(listy)

        data_pair = [list(z) for z in zip(listx, listy)]
        data_pair.sort(key=lambda x: x[1], reverse=True)
        print(data_pair)

        c = (
            WordCloud(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',

            )
            )
            .add(series_name="IPC分类号",
                 data_pair=data_pair,
                 )
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts2['feature']
                ),)

        )
        return c

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                           <style>
                           .chart-container {
                               width: 100%;
                               height: 100%;
                               max-width: 1000px;

                               margin: 0 auto;
                           }
                           </style>
                           '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)
st.subheader("""🎈🎈🎈专利技术主题分布🎈🎈🎈""")
st.write(
    '技术主题分布是对专利中涉及的技术领域和主题进行分类和分析。通过识别专利中的关键词、引用和专利分类信息，可以揭示该领域的技术热点和研究方向。' \
         '技术主题分布的分析有助于发现新的研究领域和技术趋势，为创新提供指导和灵感。')
st.subheader("""热点技术分布""")
st.write('该图用于展示不同IPC技术的申请量分布。可以迅速获取关于申请量最高的技术和相对较低的技术的信息。' \
         '词云图中尺寸较大的技术词表示其对应的IPC技术在申请量方面较为热门，申请量较大。这可能意味着该技术在相关领域具有更高的创新和应用活跃度。' \
         '反之，可能意味着该技术在相关领域的创新和应用相对较少。')
huitu31()


#前五ipc申请趋势
def huitu32():
    global document
    def cunchupng() -> Line:

        dfmb=dfm
        dfx = dfmb[['公开(公告)号', '申请年','IPC主分类号(小类)',]]
        dfx = dfx.groupby('IPC主分类号(小类)', as_index=False)['公开(公告)号'].count()
        dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
        dfx = dfx.head()
        print(dfx)
        ltx = list(dfx['IPC主分类号(小类)'])
        print(ltx)

        df1 = dfmb[['公开(公告)号', '申请年', 'IPC主分类号(小类)', ]]
        df1 = df1.astype({'申请年': 'str'})
        df1 = df1.query('申请年 in %s ' % nianfen)
        df1 = df1.loc[(df1['IPC主分类号(小类)'] == ltx[0])]
        df1 = df1[['公开(公告)号', '申请年']]
        df1 = df1.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df1 = df1.sort_values(by='申请年', ascending=False)
        df1.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df1, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df1 = dfy
        df1 = df1.astype({'申请数量': 'int'})
        print(df1)

        df2 = dfmb[['公开(公告)号', '申请年', 'IPC主分类号(小类)', ]]
        df2 = df2.astype({'申请年': 'str'})
        df2 = df2.query('申请年 in %s ' % nianfen)
        df2 = df2.loc[(df2['IPC主分类号(小类)'] == ltx[1])]
        df2 = df2[['公开(公告)号', '申请年']]
        df2 = df2.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df2 = df2.sort_values(by='申请年', ascending=False)
        df2.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df2, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df2 = dfy
        df2 = df2.astype({'申请数量': 'int'})
        print(df2)

        df3 = dfmb[['公开(公告)号', '申请年', 'IPC主分类号(小类)', ]]
        df3 = df3.astype({'申请年': 'str'})
        df3 = df3.query('申请年 in %s ' % nianfen)
        df3 = df3.loc[(df3['IPC主分类号(小类)'] == ltx[2])]
        df3 = df3[['公开(公告)号', '申请年']]
        df3 = df3.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df3 = df3.sort_values(by='申请年', ascending=False)
        df3.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df3, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df3 = dfy
        df3 = df3.astype({'申请数量': 'int'})
        print(df3)

        df4 = dfmb[['公开(公告)号', '申请年', 'IPC主分类号(小类)', ]]
        df4 = df4.astype({'申请年': 'str'})
        df4 = df4.query('申请年 in %s ' % nianfen)
        df4 = df4.loc[(df4['IPC主分类号(小类)'] == ltx[3])]
        df4 = df4[['公开(公告)号', '申请年']]
        df4 = df4.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df4 = df4.sort_values(by='申请年', ascending=False)
        df4.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df4, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df4 = dfy
        df4 = df4.astype({'申请数量': 'int'})
        print(df4)

        df5 = dfmb[['公开(公告)号', '申请年', 'IPC主分类号(小类)', ]]
        df5 = df5.astype({'申请年': 'str'})
        df5 = df5.query('申请年 in %s ' % nianfen)
        df5 = df5.loc[(df5['IPC主分类号(小类)'] == ltx[4])]
        df5 = df5[['公开(公告)号', '申请年']]
        df5 = df5.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df5 = df5.sort_values(by='申请年', ascending=False)
        df5.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df5, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df5 = dfy
        df5 = df5.astype({'申请数量': 'int'})
        print(df5)

        listx = list(df1['申请年'])
        listy = list(df1['申请数量'])
        listx2 = list(df2['申请年'])
        listy2 = list(df2['申请数量'])
        listx3 = list(df3['申请年'])
        listy3 = list(df3['申请数量'])
        listx4= list(df4['申请年'])
        listy4= list(df4['申请数量'])
        listx5= list(df5['申请年'])
        listy5= list(df5['申请数量'])
        c = (
            Line(init_opts=opts.InitOpts(
                bg_color='#FFFFFF'))
            .add_xaxis(listx)
            .add_yaxis(
                series_name=ltx[0],
                y_axis=listy,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx2)
            .add_yaxis(
                series_name=ltx[1],
                y_axis=listy2,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx3)
            .add_yaxis(
                series_name=ltx[2],
                y_axis=listy3,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx4)
            .add_yaxis(
                series_name=ltx[3],
                y_axis=listy4,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx5)
            .add_yaxis(
                series_name=ltx[4],
                y_axis=listy5,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts2['feature']
                ),

                xaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    type_="category",  # 坐标轴类型
                    name='申请年',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                        rotate=90)
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    name='申请次数',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    type_='plain', is_show=True,
                    pos_right='center',  # 右边
                    orient='horizontal',
                    pos_bottom='0%',  # 距离上边界15%
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                    background_color="transparent",
                    border_color="transparent",
                ),

            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
            )
        )
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_bottom="15%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                               <style>
                               .chart-container {
                                   width: 100%;
                                   height: 100%;
                                   max-width: 1000px;

                                   margin: 0 auto;
                               }
                               </style>
                               '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)

st.subheader("""主要技术分支申请趋势""")
st.write('该图展示了近20年来排名前五的IPC分类号专利的申请趋势。每条折线代表一个IPC分类号，表示该IPC分类号在近20年中的专利申请数量或申请趋势。' \
         '不同的IPC分类号用不同的颜色来区分。通过观察每条折线的趋势，可以了解到排名前五的IPC分类号在近20年中的专利申请情况。如果某个IPC分类号的折线呈现逐年上升的趋势，' \
         '表示该领域的专利申请数量在增加，可能代表该技术领域的发展较为活跃。相反，如果某个IPC分类号的折线呈现逐年下降或波动不定的趋势，表示该领域的专利申请数量可能在减少或变化不大。' \
         '该图表可以用于研究特定技术领域的发展趋势，帮助了解不同IPC分类号的专利申请情况及其变化。通过观察近20年的数据变化，可以揭示出技术领域的发展方向和热点，为科技创新和专利战略提供参考。')
huitu32()

def huitu33():
    global document
    dfmb=dfm
    df1 = dfmb.astype({'申请年': 'str'})
    df1= df1.query('申请年 in %s ' % nianfen)
    df1 = df1[['IPC分类号','申请年', '公开(公告)号' ]]
    series = df1['IPC分类号'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df1[['申请年', '公开(公告)号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['申请年', '公开(公告)号', 'IPC分类号']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['申请年'],df_11['公开(公告)号'], df_11['IPC分类号'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)
    dfx = df_11[['IPC分类号', '公开(公告)号']]
    dfx = dfx.groupby(['IPC分类号'], as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx = dfx.head(10)
    print(dfx)
    listx = list(dfx['IPC分类号'])
    print(listx)

    df1=df_11

    df1 = df1.groupby(['申请年', 'IPC分类号'], as_index=False).count()
    df1 = df1.sort_values(by='申请年', ascending=True)
    df1.columns = ['申请年', 'IPC主分类号小类', '申请数量']
    print(df1)
    df1 = df1.query('IPC主分类号小类 in %s ' % listx)
    df1.columns = ['申请年', 'IPC分类号', '申请数量']
    print(df1)


    xmax = max(df1['申请数量'])
    xmin = min(df1['申请数量'])
    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.2, right=0.95, top=0.95, bottom=0.15) #图与画布四周距离
    print(len(df1['申请数量']))
    color=["#3685fe", "#f5616f","#50c48f",  "#26ccd8", "#9977ef",
            "#f7b13f", "#f9e264", "#f47a75", "#009db2", "#024b51",]
    for i in range(0,len(df1['申请数量'])):
        if len(df1['申请数量']) > i*10:
            color.extend(color)
        if len(color)>len(df1['申请数量']):
            break

    color=random.sample(color, len(df1['申请数量']))

    plt.grid(ls='-.', lw=0.35)  # 增加栅格
    plt.scatter( df1['申请年'],df1['IPC分类号'], df1['申请数量']/xmax*1000,c=color, alpha=0.7)
    plt.xlabel('申请年',fontdict={ 'size':14})
    plt.ylabel('IPC分类号',fontdict={ 'size':14})
    plt.xticks(rotation=90,size=12)  # X轴刻度，标签，旋转度
    plt.yticks(size=12)
    for a, b, c in zip(df1['申请年'],df1['IPC分类号'],  df1['申请数量']):
        plt.text(a, b, c, ha='center', va='center', fontsize=8, alpha=0.9)
    st.pyplot(fig)

st.subheader("""主要技术分支申请趋势""")
st.write('该图表展示不同IPC分类在近20年内的相对变化趋势，而气泡的大小表示该IPC分类在相应年份的重要性或活跃度。较大的气泡表示该IPC分类在相应年份具有更高的重要性或活跃度，而较小的气泡则表示重要性或活跃度较低。' \
         '通过比较不同IPC分类的气泡大小，可以了解它们在不同年份之间的相对重要性或活跃度。较大的气泡表示该IPC分类在多个年份具有较高的重要性或活跃度，而较小的气泡则表示重要性或活跃度较低。')
huitu33()


#ipc受理局气泡
def huitu34():
    global document
    dfmb = dfm
    dfmb = dfmb.rename(columns={'当前申请(专利权)人地市': '当前申请人地市'})
    df1 = dfmb[['IPC分类号', '当前申请人地市', '公开(公告)号']]

    series = df1['IPC分类号'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df1[['当前申请人地市', '公开(公告)号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['当前申请人地市', '公开(公告)号', 'IPC分类号']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['当前申请人地市'], df_11['公开(公告)号'], df_11['IPC分类号'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)

    series = df_11['当前申请人地市'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df_11[['公开(公告)号', 'IPC分类号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['公开(公告)号', 'IPC分类号', '当前申请人地市']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['公开(公告)号'], df_11['IPC分类号'], df_11['当前申请人地市'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)

    dfx = df_11[['IPC分类号', '公开(公告)号']]
    dfx = dfx.groupby(['IPC分类号'], as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx = dfx.head(10)
    print(dfx)
    listx = list(dfx['IPC分类号'])
    print(listx)

    dfx = df_11.groupby('当前申请人地市', as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx.columns = ['当前申请人地市', '申请数量']
    dfx = dfx.head()
    print(dfx)
    listx2 = list(dfx['当前申请人地市'])
    print(listx2)

    df1 = df_11

    df1 = df1.groupby(['当前申请人地市', 'IPC分类号'], as_index=False).count()
    df1 = df1.sort_values(by='当前申请人地市', ascending=True)
    df1.columns = ['当前申请人地市', 'IPC主分类号小类', '申请数量']
    print(df1)
    df1 = df1.query('IPC主分类号小类 in %s ' % listx)
    df1 = df1.query('当前申请人地市 in %s ' % listx2)
    df1.columns = ['当前申请人地市', 'IPC分类号', '申请数量']
    print(df1)


    xmax = max(df1['申请数量'])
    xmin = min(df1['申请数量'])
    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.25, right=0.95, top=0.95, bottom=0.15) #图与画布四周距离
    print(len(df1['申请数量']))
    color=["#3685fe", "#f5616f","#50c48f",  "#26ccd8", "#9977ef",
            "#f7b13f", "#f9e264", "#f47a75", "#009db2", "#024b51",]
    for i in range(0,len(df1['申请数量'])):
        if len(df1['申请数量']) > i*10:
            color.extend(color)
        if len(color)>len(df1['申请数量']):
            break

    color=random.sample(color, len(df1['申请数量']))

    plt.grid(ls='-.', lw=0.35)  # 增加栅格
    plt.scatter( df1['IPC分类号'],df1['当前申请人地市'], df1['申请数量']/xmax*1000,c=color, alpha=0.7)
    # plt.ylabel('当前申请人地市',fontdict={ 'size':14})
    # plt.xlabel('IPC分类号',fontdict={ 'size':14})
    plt.xticks(rotation=45,size=12)  # X轴刻度，标签，旋转度
    plt.yticks(size=12)
    for a, b, c in zip(df1['IPC分类号'],df1['当前申请人地市'],  df1['申请数量']):
        plt.text(a, b, c, ha='center', va='center', fontsize=8, alpha=0.9)
    st.pyplot(fig)

st.subheader("""主要技术分支地域分布""")
st.write('该图表每个气泡的位置表示某个IPC分类和受理局的组合，而气泡的大小可以表示该组合的相关度、重要性或其他指标。通过观察气泡的位置，可以判断某个IPC分类和受理局之间的相关度。' \
         '气泡的大小可以表示IPC分类和受理局的重要性或活跃度。较大的气泡表示该IPC分类和受理局在申请数量或其他指标上具有较高的重要性或活跃度，而较小的气泡则表示重要性或活跃度较低。' \
         '通过观察气泡图在不同时间上的变化，可以了解IPC分类和受理局的趋势。')
huitu34()

#ipc申请人气泡
def huitu35():
    global document
    dfmb=dfm
    df1 = dfmb[['IPC分类号','[标]当前申请(专利权)人', '公开(公告)号' ]]

    series = df1['IPC分类号'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df1[['[标]当前申请(专利权)人', '公开(公告)号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['[标]当前申请(专利权)人', '公开(公告)号', 'IPC分类号']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['[标]当前申请(专利权)人'],df_11['公开(公告)号'], df_11['IPC分类号'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)
    dfx = df_11[['IPC分类号', '公开(公告)号']]
    dfx = dfx.groupby(['IPC分类号'], as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx = dfx.head(10)
    print(dfx)
    listx = list(dfx['IPC分类号'])
    print(listx)
    df1 = df_11

    series = df1['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df1[['IPC分类号', '公开(公告)号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['IPC分类号', '公开(公告)号', '[标]当前申请(专利权)人']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['IPC分类号'], df_11['公开(公告)号'], df_11['[标]当前申请(专利权)人'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)
    dfx = df_11[['[标]当前申请(专利权)人', '公开(公告)号']]
    dfx = dfx.groupby(['[标]当前申请(专利权)人'], as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx = dfx.head(10)
    print(dfx)
    listx2 = list(dfx['[标]当前申请(专利权)人'])
    print(listx2)



    df1=df_11

    df1 = df1.groupby(['[标]当前申请(专利权)人', 'IPC分类号'], as_index=False).count()
    df1 = df1.sort_values(by='[标]当前申请(专利权)人', ascending=True)
    df1.columns = ['当前申请人', 'IPC主分类号小类', '申请数量']
    print(df1)
    df1 = df1.query('IPC主分类号小类 in %s ' % listx)
    df1 = df1.query('当前申请人 in %s ' % listx2)
    df1.columns = ['[标]当前申请(专利权)人', 'IPC分类号', '申请数量']
    print(df1)
    for i in range(0,len(df1)):
        if len(df1.iat[i,0])>8:
            df1.iat[i, 0]=df1.iat[i, 0][:7]+'...'


    xmax = max(df1['申请数量'])
    xmin = min(df1['申请数量'])
    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.25, right=0.95, top=0.95, bottom=0.15) #图与画布四周距离
    print(len(df1['申请数量']))
    color=["#3685fe", "#f5616f","#50c48f",  "#26ccd8", "#9977ef",
            "#f7b13f", "#f9e264", "#f47a75", "#009db2", "#024b51",]
    for i in range(0,len(df1['申请数量'])):
        if len(df1['申请数量']) > i*10:
            color.extend(color)
        if len(color)>len(df1['申请数量']):
            break

    color=random.sample(color, len(df1['申请数量']))

    plt.grid(ls='-.', lw=0.35)  # 增加栅格
    plt.scatter( df1['IPC分类号'],df1['[标]当前申请(专利权)人'], df1['申请数量']/xmax*1000,c=color, alpha=0.7)
    # plt.ylabel('[标]当前申请(专利权)人',fontdict={ 'size':14})
    # plt.xlabel('IPC分类号',fontdict={ 'size':14})
    plt.xticks(rotation=45,size=12)  # X轴刻度，标签，旋转度
    plt.yticks(size=12)
    for a, b, c in zip(df1['IPC分类号'],df1['[标]当前申请(专利权)人'],  df1['申请数量']):
        plt.text(a, b, c, ha='center', va='center', fontsize=8, alpha=0.9)
    st.pyplot(fig)

st.subheader("""主要技术分支主要申请人分布""")
st.write('每个气泡的位置表示某个IPC分类和申请人的组合，而气泡的大小可以表示该组合的相关度、重要性或其他指标。通过观察气泡的位置，可以判断某个IPC分类和申请人之间的相关度。' \
         '气泡的大小可以表示IPC分类和申请人的重要性或活跃度。较大的气泡表示该IPC分类和申请人在专利申请数量或其他指标上具有较高的重要性或活跃度，而较小的气泡则表示重要性或活跃度较低。' \
         '通过观察气泡图在不同时间上的变化，可以了解IPC分类和申请人之间的趋势。')
huitu35()



##申请人分布
#申请人排名
def huitu41():
    global document
    dfmb=dfm
    df1 = dfmb.astype({'申请年': 'str'})
    df1 = df1.query('申请年 in %s ' % nianfen)
    df1 = df1[['公开(公告)号', '[标]当前申请(专利权)人']]
    series = df1['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df1[['公开(公告)号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['公开(公告)号', '[标]当前申请(专利权)人']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['公开(公告)号'], df_11['[标]当前申请(专利权)人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
    df_11 = df_11.groupby('[标]当前申请(专利权)人', as_index=False)['公开(公告)号'].count()
    df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
    df_11.columns = ['[标]当前申请(专利权)人', '申请数量']
    # df_11 = df_11.head(30)
    print(df_11)


    df2 = dfmb.astype({'申请年': 'str'})
    df2 = df2.query('申请年 in %s ' % nianfen)
    # df2 = df2.loc[(df2['授权年'] != '-')]
    df2 = df2.loc[df2['法律状态/事件'].str.contains('授权', na=False), :]
    df2 = df2[['公开(公告)号', '[标]当前申请(专利权)人']]
    series = df2['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df2[['公开(公告)号']]
    df_22 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['公开(公告)号', '[标]当前申请(专利权)人']
        df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
    df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_22 = pd.concat([df_22['公开(公告)号'], df_22['[标]当前申请(专利权)人'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    df_22 = df_22.groupby('[标]当前申请(专利权)人', as_index=False)['公开(公告)号'].count()
    df_22 = df_22.sort_values(by='公开(公告)号', ascending=False)
    df_22.columns = ['[标]当前申请(专利权)人', '授权数量']
    # df_22 = df_22.head(30)
    print(df_22)
    df3=pd.merge(df_11,df_22,on='[标]当前申请(专利权)人')
    df3.columns=['当前申请人','申请数量','授权数量']
    print(df3)
    df3=df3.head(10)
    df3 = df3.sort_values(by='申请数量', ascending=True)

    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.35, right=0.95, top=0.95, bottom=0.12)  # 图与画布四周距离
    plt.barh(df3['当前申请人'], df3['申请数量'], height=0.8, color="#50c48f",alpha=0.7)
    plt.barh(df3['当前申请人'], df3['授权数量'], height=0.5, color="#f5616f") #先后顺序影响色彩显示
    plt.xticks(size=12)
    plt.yticks(size=10)
    for a, b in zip(df3['申请数量'],df3['当前申请人'], ):
        plt.text(a, b, format(a), ha='left', va='center', fontsize=10, alpha=0.9)
    # for a, b in zip(df3['授权数量'],df3['当前申请人'], ):
    #     plt.text(a , b, format(a), ha='left', va='center', fontsize=10, alpha=0.9)
    plt.legend(['专利申请','专利授权'], loc='lower center', frameon=False, prop={'size': 12}, ncol=2,
               bbox_to_anchor=(0.5, -0.15), borderaxespad=0)  # 去掉图例边框
    st.pyplot(fig)
st.subheader("""🎈🎈🎈专利申请人分布🎈🎈🎈""")
st.write(
    '申请人分布部分关注的是专利申请人的身份和组织情况。这可以帮助我们了解到哪些公司、研究机构或个人在该领域内活跃，并评估各个主体之间的竞争态势。' \
         '申请人分布的分析还可以揭示出具有较强创新实力和技术优势的组织或个人。')
st.subheader("""主要申请人排名""")
st.write('该图用于表示申请人的排名以及其专利申请和授权情况。通过观察，可以了解不同申请人的排名顺序。排名靠前的申请人在柱状图的顶部，而排名靠后的申请人在底部。了解每个申请人的专利申请和授权数量。' \
         '通过比较不同申请人的柱状图，可以了解他们在专利申请和授权方面的差异。柱状图高度较高的申请人表示其在专利领域具有较高的活跃度和数量，而柱状图较低的申请人表示其专利申请和授权数量较少。')
huitu41()


#前五申请人趋势
def huitu42():
    global document
    def cunchupng() -> Line:

        dfmb=dfm
        dfx = dfmb[['公开(公告)号', '[标]当前申请(专利权)人']]
        series = dfx['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfx[['公开(公告)号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '[标]当前申请(专利权)人']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开(公告)号'], df_11['[标]当前申请(专利权)人'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格
        df_11 = df_11.groupby('[标]当前申请(专利权)人', as_index=False)['公开(公告)号'].count()
        df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        df_11.columns = ['[标]当前申请(专利权)人', '申请数量']
        df_11 = df_11.head()
        ltx = list(df_11['[标]当前申请(专利权)人'])
        print(ltx)

        df1 = dfmb[['公开(公告)号', '申请年', '[标]当前申请(专利权)人', ]]
        df1 = df1.astype({'申请年': 'str'})
        df1 = df1.query('申请年 in %s ' % nianfen)
        df1 = df1.loc[df1['[标]当前申请(专利权)人'].str.contains(ltx[0], na=False), :]
        df1 = df1[['公开(公告)号', '申请年']]
        df1 = df1.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df1 = df1.sort_values(by='申请年', ascending=False)
        df1.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df1, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df1 = dfy
        df1 = df1.astype({'申请数量': 'int'})
        print(df1)

        df2 = dfmb[['公开(公告)号', '申请年', '[标]当前申请(专利权)人', ]]
        df2 = df2.astype({'申请年': 'str'})
        df2 = df2.query('申请年 in %s ' % nianfen)
        df2 = df2.loc[df2['[标]当前申请(专利权)人'].str.contains(ltx[1], na=False), :]
        df2 = df2[['公开(公告)号', '申请年']]
        df2 = df2.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df2 = df2.sort_values(by='申请年', ascending=False)
        df2.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df2, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df2 = dfy
        df2 = df2.astype({'申请数量': 'int'})
        print(df2)

        df3 = dfmb[['公开(公告)号', '申请年', '[标]当前申请(专利权)人', ]]
        df3 = df3.astype({'申请年': 'str'})
        df3 = df3.query('申请年 in %s ' % nianfen)
        df3 = df3.loc[df3['[标]当前申请(专利权)人'].str.contains(ltx[2], na=False), :]
        df3 = df3[['公开(公告)号', '申请年']]
        df3 = df3.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df3 = df3.sort_values(by='申请年', ascending=False)
        df3.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df3, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df3 = dfy
        df3 = df3.astype({'申请数量': 'int'})
        print(df3)

        df4 = dfmb[['公开(公告)号', '申请年', '[标]当前申请(专利权)人', ]]
        df4 = df4.astype({'申请年': 'str'})
        df4 = df4.query('申请年 in %s ' % nianfen)
        df4 = df4.loc[df4['[标]当前申请(专利权)人'].str.contains(ltx[3], na=False), :]
        df4 = df4[['公开(公告)号', '申请年']]
        df4 = df4.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df4 = df4.sort_values(by='申请年', ascending=False)
        df4.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df4, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df4 = dfy
        df4 = df4.astype({'申请数量': 'int'})
        print(df4)

        df5 = dfmb[['公开(公告)号', '申请年', '[标]当前申请(专利权)人', ]]
        df5 = df5.astype({'申请年': 'str'})
        df5 = df5.query('申请年 in %s ' % nianfen)
        df5 = df5.loc[df5['[标]当前申请(专利权)人'].str.contains(ltx[4], na=False), :]
        df5 = df5[['公开(公告)号', '申请年']]
        df5 = df5.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df5 = df5.sort_values(by='申请年', ascending=False)
        df5.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df5, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df5 = dfy
        df5 = df5.astype({'申请数量': 'int'})
        print(df5)

        listx = list(df1['申请年'])
        listy = list(df1['申请数量'])
        listx2 = list(df2['申请年'])
        listy2 = list(df2['申请数量'])
        listx3 = list(df3['申请年'])
        listy3 = list(df3['申请数量'])
        listx4= list(df4['申请年'])
        listy4= list(df4['申请数量'])
        listx5= list(df5['申请年'])
        listy5= list(df5['申请数量'])
        c = (
            Line(init_opts=opts.InitOpts(
                bg_color='#FFFFFF'))
            .add_xaxis(listx)
            .add_yaxis(
                series_name=ltx[0],
                y_axis=listy,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx2)
            .add_yaxis(
                series_name=ltx[1],
                y_axis=listy2,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx3)
            .add_yaxis(
                series_name=ltx[2],
                y_axis=listy3,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx4)
            .add_yaxis(
                series_name=ltx[3],
                y_axis=listy4,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx5)
            .add_yaxis(
                series_name=ltx[4],
                y_axis=listy5,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),

                xaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    type_="category",  # 坐标轴类型
                    name='申请年',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                        rotate=90)
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    name='申请次数',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    type_='scroll', is_show=True,
                    pos_right='center',  # 右边
                    orient='horizontal',
                    pos_bottom='0%',  # 距离上边界15%
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                    background_color="transparent",
                    border_color="transparent",
                ),

            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
            )
        )
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_bottom="15%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                               <style>
                               .chart-container {
                                   width: 100%;
                                   height: 100%;
                                   max-width: 1000px;

                                   margin: 0 auto;
                               }
                               </style>
                               '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)

st.subheader("""主要申请人申请趋势""")
st.write('通过观察五个申请人在近20年内的专利申请数量的变化趋势。了解其申请数量随时间的变化趋势。上升的趋势可能表示该申请人在专利申请数量上有增长，而下降的趋势可能表示申请数量减少。' \
         '通过比较不同申请人的折线，可以观察到它们之间的相对变化。通过观察折线的相对位置和大小，可以了解申请人在排名方面的变化。')
huitu42()

#申请人受理局气泡
def huitu44():
    global document
    dfmb = dfm
    dfmb = dfmb.rename(columns={'当前申请(专利权)人地市': '当前申请人地市'})
    df1 = dfmb[['[标]当前申请(专利权)人', '当前申请人地市', '公开(公告)号']]

    series = df1['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df1[['当前申请人地市', '公开(公告)号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['当前申请人地市', '公开(公告)号', '[标]当前申请(专利权)人']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['当前申请人地市'], df_11['公开(公告)号'], df_11['[标]当前申请(专利权)人'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)

    series = df_11['当前申请人地市'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df_11[['公开(公告)号', '[标]当前申请(专利权)人']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['公开(公告)号', '[标]当前申请(专利权)人', '当前申请人地市']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['公开(公告)号'], df_11['[标]当前申请(专利权)人'], df_11['当前申请人地市'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)

    dfx = df_11[['[标]当前申请(专利权)人', '公开(公告)号']]
    dfx = dfx.groupby(['[标]当前申请(专利权)人'], as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx = dfx.head(10)
    print(dfx)
    listx = list(dfx['[标]当前申请(专利权)人'])
    print(listx)

    dfx = df_11[['当前申请人地市', '公开(公告)号']]
    dfx = dfx.groupby(['当前申请人地市'], as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx = dfx.head(10)
    print(dfx)
    listx2 = list(dfx['当前申请人地市'])
    print(listx2)

    df1 = df_11

    df1 = df1.groupby(['当前申请人地市', '[标]当前申请(专利权)人'], as_index=False).count()
    df1 = df1.sort_values(by='当前申请人地市', ascending=True)
    df1.columns = ['当前申请人地市', 'IPC主分类号小类', '申请数量']
    print(df1)
    df1 = df1.query('IPC主分类号小类 in %s ' % listx)
    df1 = df1.query('当前申请人地市 in %s ' % listx2)
    df1.columns = ['当前申请人地市', '[标]当前申请(专利权)人', '申请数量']
    print(df1)


    xmax = max(df1['申请数量'])
    xmin = min(df1['申请数量'])
    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.35, right=0.95, top=0.95, bottom=0.25) #图与画布四周距离
    print(len(df1['申请数量']))
    color=["#3685fe", "#f5616f","#50c48f",  "#26ccd8", "#9977ef",
            "#f7b13f", "#f9e264", "#f47a75", "#009db2", "#024b51",]
    for i in range(0,len(df1['申请数量'])):
        if len(df1['申请数量']) > i*10:
            color.extend(color)
        if len(color)>len(df1['申请数量']):
            break

    color=random.sample(color, len(df1['申请数量']))

    plt.grid(ls='-.', lw=0.35)  # 增加栅格
    plt.scatter( df1['当前申请人地市'],df1['[标]当前申请(专利权)人'], df1['申请数量']/xmax*1000,c=color, alpha=0.7)
    # plt.ylabel('受理局',fontdict={ 'size':14})
    # plt.xlabel('[标]当前申请(专利权)人',fontdict={ 'size':14})
    plt.xticks(rotation=45,size=10,ha='right')  # X轴刻度，标签，旋转度
    plt.tick_params(axis='x', pad=-5)
    plt.yticks(size=10)
    for a, b, c in zip(df1['当前申请人地市'],df1['[标]当前申请(专利权)人'],  df1['申请数量']):
        plt.text(a, b, c, ha='center', va='center', fontsize=8, alpha=0.9)
    st.pyplot(fig)

st.subheader("""主要申请人地域分布""")
st.write('用于表示前十个受理局和前十个申请人之间的关系和活跃度。通过观察气泡的位置，可以判断受理局和申请人之间的关联程度。' \
         '气泡的大小可以表示受理局和申请人的重要性或活跃度。较大的气泡表示该受理局和申请人在专利申请数量或其他指标上具有较高的重要性或活跃度，而较小的气泡则表示重要性或活跃度较低。' \
         '通过比较不同受理局和申请人的气泡大小，可以了解它们在专利申请方面的差异。')
huitu44()

#联合申请人排名
def huitu45():
    global document
    def cunchupng():

        dfmb = dfm.loc[(dfm['当前申请(专利权)人数量'] != '-')]
        dfmb = dfmb.astype({'当前申请(专利权)人数量': 'int'})
        dfmb = dfmb.loc[(dfmb['当前申请(专利权)人数量'] != 1)]
        dfm1 = dfmb[['公开(公告)号', '[标]当前申请(专利权)人']]

        series = dfm1['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfm1[['公开(公告)号']]
        dfx = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '[标]当前申请(专利权)人']
            dfx = pd.concat([dfx, df_l])  ##所有新表叠加
        dfx.dropna(inplace=True)  # 删除空数据，获得有效数据
        dfx = pd.concat([dfx['公开(公告)号'], dfx['[标]当前申请(专利权)人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        dfx = dfx.groupby('[标]当前申请(专利权)人', as_index=False)['公开(公告)号'].count()
        dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
        dfx.columns = ['[标]当前申请(专利权)人', '申请数量']
        dfx = dfx.head(10)
        dfx = dfx.sort_values(by='申请数量', ascending=True)

        for j in range(0, len(dfx['[标]当前申请(专利权)人'])):
            if len(dfx.iat[j, 0]) > 11:
                dfx.iat[j, 0] = dfx.iat[j, 0][0:10] + '...'
            else:
                dfx.iat[j, 0] = dfx.iat[j, 0]
        listx = list(dfx['[标]当前申请(专利权)人'])
        listy = list(dfx['申请数量'])

        c = (
            Bar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis('申请数量', listy)
            .reversal_axis()
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁

            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),

                xaxis_opts=opts.AxisOpts(

                    name='申请数量',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(

                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                    )
                ),
                yaxis_opts=opts.AxisOpts(

                    name='申请人',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False,
                ),
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=15,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项

                itemstyle_opts={
                    "normal": {
                        "color": JsCode(
                            """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(0, 244, 255, 1)'
                    }, {
                        offset: 1,
                        color: 'rgba(0, 77, 167, 1)'
                    }], false)"""
                        ),
                        "barBorderRadius": [30, 30, 30, 30],
                        "shadowColor": "rgb(0, 160, 221)",
                    }
                }

            )

        )

        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_left="20%")))
        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                   <style>
                                   .chart-container {
                                       width: 100%;
                                       height: 100%;
                                       max-width: 1000px;

                                       margin: 0 auto;
                                   }
                                   </style>
                                   '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""申请人协同申请排名""")
st.write('该图表可以了解不同申请人的排名顺序。排名靠前的申请人在柱状图的顶部，而排名靠后的申请人在底部。' \
         '通过比较不同申请人的柱状图，可以了解他们在联合申请专利方面的差异。柱状图高度较高的申请人表示其在联合申请专利中的出现次数较多，而柱状图较低的申请人表示其联合申请数量较少。')
huitu45()


#申请人联合情况
def huitu46():
    global document
    def cunchupng():
        global biaoji
        dfmb = dfm.loc[(dfm['当前申请(专利权)人数量'] != '-')]
        dfmb = dfmb.astype({'当前申请(专利权)人数量': 'int'})
        dfmb = dfmb.loc[(dfmb['当前申请(专利权)人数量'] != 1)]

        dfm1 = dfmb[['公开(公告)号', '[标]当前申请(专利权)人']]

        series = dfm1['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfm1[['公开(公告)号']]
        dfx = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '[标]当前申请(专利权)人']
            dfx = pd.concat([dfx, df_l])  ##所有新表叠加
        dfx.dropna(inplace=True)  # 删除空数据，获得有效数据
        dfx = pd.concat([dfx['公开(公告)号'], dfx['[标]当前申请(专利权)人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        dfx = dfx.groupby('[标]当前申请(专利权)人', as_index=False)['公开(公告)号'].count()
        dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
        dfx.columns = ['[标]当前申请(专利权)人', '申请数量']
        dfx = dfx.head(10)
        listx = list(dfx['[标]当前申请(专利权)人'])

        # 节点数据
        df1 = dfmb.loc[dfmb['[标]当前申请(专利权)人'].str.contains(listx[0], na=False), :]

        df1 = df1.astype({'当前申请(专利权)人数量': 'int'})
        df1 = df1.loc[(df1['当前申请(专利权)人数量'] != 1)]
        series = df1['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['公开(公告)号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '[标]当前申请(专利权)人']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开(公告)号'], df_11['[标]当前申请(专利权)人'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格
        df_11 = df_11.groupby('[标]当前申请(专利权)人', as_index=False)['公开(公告)号'].count()
        df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        df_11.columns = ['[标]当前申请(专利权)人', '申请数量']

        # 关系数据
        df2 = dfmb.loc[dfmb['[标]当前申请(专利权)人'].str.contains(listx[0], na=False), :]
        df2 = df2[['公开(公告)号', '[标]当前申请(专利权)人']]
        series = df2['[标]当前申请(专利权)人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df2[['公开(公告)号']]
        df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一申请人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
        df_z.columns = ['公开(公告)号', '第一申请人']
        df_22 = pd.DataFrame()
        for i in range(1, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '第一申请人', '联合申请人']
            df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
        df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_22 = pd.concat([df_22['公开(公告)号'], df_22['第一申请人'], df_22['联合申请人'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格
        df_22 = df_22.groupby(['第一申请人', '联合申请人'], as_index=False)['公开(公告)号'].count()
        df_22 = df_22.sort_values(by='公开(公告)号', ascending=False)
        df_22.columns = ['第一申请人', '联合申请人', '申请数量']

        nodes = []
        for i in range(len(df_11)):
            node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),
                    "value": int(df_11.iat[i, 1])}

            nodes.append(node)

        links = []
        for i in range(len(df_22)):
            link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
                    "value": int(df_22.iat[i, 2])}
            links.append(link)


        c = (
            Graph(init_opts=opts.InitOpts(
                bg_color='#FFFFFF', ))
            .add(listx[0],
                 nodes,
                 links,
                 repulsion=120,
                 layout="force", #force circular
                 edge_length=120,
                 gravity=0.1,
                 is_draggable=True,
                 linestyle_opts=opts.LineStyleOpts(
                     width=2,
                     curve=0.3,
                 ),  # 线条配置
                 )
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),

                legend_opts=opts.LegendOpts(
                    type_='plain', is_show=True,
                    pos_right='right',  # 右边
                    orient='vertical',
                    pos_top='10%',  # 距离上边界15%
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                    background_color="transparent",
                    border_color="transparent",
                ), )
            .set_series_opts(
                itemstyle_opts=opts.ItemStyleOpts(color="rgb(80,196,143)",  # 节点颜色
                                                  border_color="rgb(245,97,111)",  # 节点边线颜色
                                                  border_width=1,  # 节点边线宽度
                                                  opacity=0.7,  # 节点透明度
                                                  ),
                linestyle_opts=opts.LineStyleOpts(is_show=True,
                                                  width=1,
                                                  opacity=0.6,
                                                  curve=0.2,  # 弯曲度
                                                  type_="solid",  # 线条类型 'solid', 'dashed', 'dotted'
                                                  color="red",
                                                  ),
                label_opts=opts.LabelOpts(
                    is_show=True,
                    # position="top",
                    color="rgb(54,133,254)",
                    font_size=10,
                    font_style='normal',  # 正常
                    font_weight='bold',  # 加粗
                    # color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
            )
        )
        return c

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                       <style>
                                       .chart-container {
                                           width: 100%;
                                           height: 100%;
                                           max-width: 1000px;

                                           margin: 0 auto;
                                       }
                                       </style>
                                       '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""申请人协同情况""")
st.write('通过观察申请人之间的连线，可以了解哪些申请人之间存在联合申请的关系。连线的存在表示申请人之间曾经合作申请专利。' \
         '通过观察圆的大小，可以了解每个申请人的专利数量。圆越大，表示该申请人参与的联合申请数量越多。' \
         '通过观察连线的数量和连接的方式，可以分析申请人之间的协同情况。如果一个申请人与多个其他申请人有连线，表示该申请人与其他申请人之间有更多的联合申请。')
huitu46()



##发明人分布
#发明人排名
def huitu51():
    global document
    def cunchupng():
        dfmb = dfm
        df1 = dfmb.astype({'申请年': 'str'})
        df1 = df1.loc[(df1['发明人'] != '-')]
        df1 = df1.query('申请年 in %s ' % nianfen)
        df1 = df1[['公开(公告)号', '发明人']]
        series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['公开(公告)号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '发明人']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开(公告)号'], df_11['发明人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        df_11 = df_11.groupby('发明人', as_index=False)['公开(公告)号'].count()
        df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        df_11.columns = ['发明人', '申请数量']
        df3 = df_11.head(10)
        df3 = df3.sort_values(by='申请数量', ascending=True)


        # for j in range(0, len(df3['发明人'])):
        #     if len(df3.iat[j, 0]) > 8:
        #         df3.iat[j, 0] = df3.iat[j, 0][0:7] + '...'
        #     else:
        #         df3.iat[j, 0] = df3.iat[j, 0]
        listx = list(df3['发明人'])
        listy = list(df3['申请数量'])

        c = (
            PictorialBar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis(
                "",
                listy,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=15,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
                symbol_size=24,
                symbol_repeat="fixed",
                symbol_offset=[0, 0],
                is_symbol_clip=True,
                symbol=SymbolType.ROUND_RECT,
            )
            .reversal_axis()
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),

                xaxis_opts=opts.AxisOpts(is_show=False),
                yaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(opacity=0)
                    ),
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False, )
            )
        )
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_left="25%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                           <style>
                                           .chart-container {
                                               width: 100%;
                                               height: 100%;
                                               max-width: 1000px;

                                               margin: 0 auto;
                                           }
                                           </style>
                                           '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)
st.subheader("""🎈🎈🎈专利发明人分布🎈🎈🎈""")
st.write(
    '发明人分布部分关注的是专利申请中涉及的发明人信息。这可以揭示创新团队或个人在该领域的贡献和影响力。通过分析发明人分布，' \
         '我们可以了解到哪些个人具备较强的创新能力和专业知识，以及他们在领域内的合作网络和影响力。')
st.subheader("""发明人排名""")
st.write('通过观察柱状图的顺序，可以了解不同发明人的排名顺序。柱状图靠前的表示排名较高的发明人，而柱状图靠后的表示排名较低的发明人。' \
         '通过比较不同柱状图的高度，可以了解不同发明人之间的数量差异。较高的柱状图表示该发明人在专利申请数量上较为活跃，而较低的柱状图表示申请数量较少。')
huitu51()


#前五发明人申请趋势
def huitu52():
    global document
    def cunchupng() -> Line:

        dfmb=dfm
        dfx = dfmb[['公开(公告)号', '发明人']]
        series = dfx['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfx[['公开(公告)号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '发明人']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开(公告)号'], df_11['发明人'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格
        df_11 = df_11.groupby('发明人', as_index=False)['公开(公告)号'].count()
        df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        df_11.columns = ['发明人', '申请数量']
        df_11 = df_11.loc[(df_11['发明人'] != '-')]
        df_11 = df_11.head()
        ltx = list(df_11['发明人'])
        print(ltx)

        df1 = dfmb[['公开(公告)号', '申请年', '发明人', ]]
        df1 = df1.loc[df1['发明人'].str.contains(ltx[0], na=False), :]
        df1 = df1[['公开(公告)号', '申请年']]
        df1 = df1.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df1 = df1.sort_values(by='申请年', ascending=False)
        df1.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df1, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df1 = dfy
        df1 = df1.astype({'申请数量': 'int'})
        print(df1)

        df2 = dfmb[['公开(公告)号', '申请年', '发明人', ]]
        df2 = df2.loc[df2['发明人'].str.contains(ltx[1], na=False), :]
        df2 = df2[['公开(公告)号', '申请年']]
        df2 = df2.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df2 = df2.sort_values(by='申请年', ascending=False)
        df2.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df2, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df2 = dfy
        df2 = df2.astype({'申请数量': 'int'})
        print(df2)

        df3 = dfmb[['公开(公告)号', '申请年', '发明人', ]]
        df3 = df3.loc[df3['发明人'].str.contains(ltx[2], na=False), :]
        df3 = df3[['公开(公告)号', '申请年']]
        df3 = df3.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df3 = df3.sort_values(by='申请年', ascending=False)
        df3.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df3, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df3 = dfy
        df3 = df3.astype({'申请数量': 'int'})
        print(df3)

        df4 = dfmb[['公开(公告)号', '申请年', '发明人', ]]
        df4 = df4.loc[df4['发明人'].str.contains(ltx[3], na=False), :]
        df4 = df4[['公开(公告)号', '申请年']]
        df4 = df4.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df4 = df4.sort_values(by='申请年', ascending=False)
        df4.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df4, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df4 = dfy
        df4 = df4.astype({'申请数量': 'int'})
        print(df4)

        df5 = dfmb[['公开(公告)号', '申请年', '发明人', ]]
        df5 = df5.loc[df5['发明人'].str.contains(ltx[4], na=False), :]
        df5 = df5[['公开(公告)号', '申请年']]
        df5 = df5.groupby('申请年', as_index=False)['公开(公告)号'].count()
        df5 = df5.sort_values(by='申请年', ascending=False)
        df5.columns = ['申请年', '申请数量']
        dfy = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfy = pd.merge(dfy, df5, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfy = dfy[['申请年', '申请数量']]
        dfy = dfy.fillna(0)  # 对为空的 属性补 0
        df5 = dfy
        df5 = df5.astype({'申请数量': 'int'})
        print(df5)

        listx = list(df1['申请年'])
        listy = list(df1['申请数量'])
        listx2 = list(df2['申请年'])
        listy2 = list(df2['申请数量'])
        listx3 = list(df3['申请年'])
        listy3 = list(df3['申请数量'])
        listx4= list(df4['申请年'])
        listy4= list(df4['申请数量'])
        listx5= list(df5['申请年'])
        listy5= list(df5['申请数量'])
        c = (
            Line(init_opts=opts.InitOpts(
                bg_color='#FFFFFF'))
            .add_xaxis(listx)
            .add_yaxis(
                series_name=ltx[0],
                y_axis=listy,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx2)
            .add_yaxis(
                series_name=ltx[1],
                y_axis=listy2,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx3)
            .add_yaxis(
                series_name=ltx[2],
                y_axis=listy3,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx4)
            .add_yaxis(
                series_name=ltx[3],
                y_axis=listy4,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx5)
            .add_yaxis(
                series_name=ltx[4],
                y_axis=listy5,

                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol

                linestyle_opts=opts.LineStyleOpts(
                    width=2,
                    type_="solid",
                ),  # 线条配置
            )
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),

                xaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    type_="category",  # 坐标轴类型
                    name='申请年',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                        rotate=90)
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    name='申请次数',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    type_='plain', is_show=True,
                    pos_right='center',  # 右边
                    orient='horizontal',
                    pos_bottom='0%',  # 距离上边界15%
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                    background_color="transparent",
                    border_color="transparent",
                ),

            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
            )
        )
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_bottom="15%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                               <style>
                                               .chart-container {
                                                   width: 100%;
                                                   height: 100%;
                                                   max-width: 1000px;

                                                   margin: 0 auto;
                                               }
                                               </style>
                                               '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""主要发明人申请趋势""")
st.write('通过观察折线的走势，可以了解每个发明人的专利申请数量随时间的变化趋势。上升的趋势可能表示该发明人在专利申请数量上有增长，而下降的趋势可能表示申请数量减少。' \
         '通过比较不同发明人的折线，可以观察到他们之间的相对变化。较高的折线表示该发明人的专利申请数量较多，而较低的折线表示申请数量较少。' \
         '通过观察折线的相对位置和大小，可以了解发明人在排名方面的变化。')
huitu52()

#发明人受理局气泡
def huitu54():
    global document
    dfmb = dfm
    dfmb = dfmb.rename(columns={'当前申请(专利权)人地市': '当前申请人地市'})
    df1 = dfmb[['发明人', '当前申请人地市', '公开(公告)号']]
    df1 = df1.loc[(df1['发明人'] != '-')]
    series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df1[['当前申请人地市', '公开(公告)号']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['当前申请人地市', '公开(公告)号', '发明人']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['当前申请人地市'], df_11['公开(公告)号'], df_11['发明人'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)

    series = df_11['当前申请人地市'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df_11[['公开(公告)号', '发明人']]
    df_11 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['公开(公告)号', '发明人', '当前申请人地市']
        df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
    df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_11 = pd.concat([df_11['公开(公告)号'], df_11['发明人'], df_11['当前申请人地市'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    print(df_11)


    dfx = df_11[['发明人', '公开(公告)号']]
    dfx = dfx.groupby(['发明人'], as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx = dfx.head(10)
    print(dfx)
    listx = list(dfx['发明人'])
    print(listx)

    dfx = df_11[['当前申请人地市', '公开(公告)号']]
    dfx = dfx.groupby(['当前申请人地市'], as_index=False)['公开(公告)号'].count()
    dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
    dfx = dfx.head(10)
    print(dfx)
    listx2 = list(dfx['当前申请人地市'])
    print(listx2)

    df1 = df_11

    df1 = df1.groupby(['当前申请人地市', '发明人'], as_index=False).count()
    df1 = df1.sort_values(by='当前申请人地市', ascending=True)
    df1.columns = ['当前申请人地市', 'IPC主分类号小类', '申请数量']
    print(df1)
    df1 = df1.query('IPC主分类号小类 in %s ' % listx)
    df1 = df1.query('当前申请人地市 in %s ' % listx2)
    df1.columns = ['当前申请人地市', '发明人', '申请数量']
    print(df1)


    xmax = max(df1['申请数量'])
    xmin = min(df1['申请数量'])
    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.35, right=0.95, top=0.95, bottom=0.25) #图与画布四周距离
    print(len(df1['申请数量']))
    color=["#3685fe", "#f5616f","#50c48f",  "#26ccd8", "#9977ef",
            "#f7b13f", "#f9e264", "#f47a75", "#009db2", "#024b51",]
    for i in range(0,len(df1['申请数量'])):
        if len(df1['申请数量']) > i*10:
            color.extend(color)
        if len(color)>len(df1['申请数量']):
            break

    color=random.sample(color, len(df1['申请数量']))

    plt.grid(ls='-.', lw=0.35)  # 增加栅格
    plt.scatter( df1['当前申请人地市'],df1['发明人'], df1['申请数量']/xmax*1000,c=color, alpha=0.7)
    # plt.ylabel('受理局',fontdict={ 'size':14})
    # plt.xlabel('发明人',fontdict={ 'size':14})
    plt.xticks(rotation=35,size=12)  # X轴刻度，标签，旋转度
    plt.yticks(size=12)
    for a, b, c in zip(df1['当前申请人地市'],df1['发明人'],  df1['申请数量']):
        plt.text(a, b, c, ha='center', va='center', fontsize=8, alpha=0.9)
    st.pyplot(fig)

st.subheader("""主要发明人地域分布""")
st.write('通过观察气泡的位置，可以判断受理局和发明人之间的关联程度。气泡的大小可以表示受理局和发明人的重要性或活跃度。' \
         '较大的气泡表示该受理局和发明人在专利申请数量或其他指标上具有较高的重要性或活跃度，而较小的气泡则表示重要性或活跃度较低。' \
         '通过比较不同受理局和发明人的气泡大小，可以了解它们在专利申请方面的差异。')
huitu54()

#联合发明人排名
def huitu55():
    global document
    def cunchupng():

        dfmb = dfm.loc[(dfm['发明人数量'] != '-')]
        dfmb = dfmb.astype({'发明人数量': 'int'})
        dfmb = dfmb.loc[(dfmb['发明人数量'] != 1)]
        dfm1 = dfmb[['公开(公告)号', '发明人']]

        series = dfm1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfm1[['公开(公告)号']]
        dfx = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开(公告)号', '发明人']
            dfx = pd.concat([dfx, df_l])  ##所有新表叠加
        dfx.dropna(inplace=True)  # 删除空数据，获得有效数据
        dfx = pd.concat([dfx['公开(公告)号'], dfx['发明人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        dfx = dfx.groupby('发明人', as_index=False)['公开(公告)号'].count()
        dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
        dfx.columns = ['发明人', '申请数量']
        dfx = dfx.head(10)
        dfx = dfx.sort_values(by='申请数量', ascending=True)

        for j in range(0, len(dfx['发明人'])):
            if len(dfx.iat[j, 0]) > 11:
                dfx.iat[j, 0] = dfx.iat[j, 0][0:10] + '...'
            else:
                dfx.iat[j, 0] = dfx.iat[j, 0]
        listx = list(dfx['发明人'])
        listy = list(dfx['申请数量'])

        c = (
            Bar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis('申请数量', listy)
            .reversal_axis()
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁

            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),

                xaxis_opts=opts.AxisOpts(

                    name='申请数量',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(

                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                    )
                ),
                yaxis_opts=opts.AxisOpts(

                    name='发明人',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False,
                ),
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=15,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项

                itemstyle_opts={
                    "normal": {
                        "color": JsCode(
                            """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(0, 244, 255, 1)'
                    }, {
                        offset: 1,
                        color: 'rgba(0, 77, 167, 1)'
                    }], false)"""
                        ),
                        "barBorderRadius": [30, 30, 30, 30],
                        "shadowColor": "rgb(0, 160, 221)",
                    }
                }

            )

        )

        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_left="20%")))
        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                                   <style>
                                                   .chart-container {
                                                       width: 100%;
                                                       height: 100%;
                                                       max-width: 1000px;

                                                       margin: 0 auto;
                                                   }
                                                   </style>
                                                   '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""发明人协同申请排名""")
st.write('通过观察柱状图，可以了解不同发明人的排名顺序。柱状图靠前的表示排名较高的发明人，而柱状图靠后的表示排名较低的发明人。' \
         '通过比较不同发明人的柱状图，可以了解他们在联合申请专利方面的差异。柱状图高度较高的发明人表示其在联合申请专利中的出现次数较多，而柱状图较低的发明人表示其联合申请数量较少。')
huitu55()

#发明人联合情况
def huitu56():
    global document
    def cunchupng():
        dfmb = dfm.loc[(dfm['发明人数量'] != '-')]
        dfmb = dfmb.astype({'发明人数量': 'int'})
        dfmb = dfmb.loc[(dfmb['发明人数量'] != 1)]
        dfm1 = dfmb[['公开(公告)号', '发明人']]
        series = dfm1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfm1[['公开(公告)号']]
        dfx = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
            df_l.columns = ['公开(公告)号', '发明人']
            dfx = pd.concat([dfx, df_l])  ##所有新表叠加
        dfx.dropna(inplace=True)  # 删除空数据，获得有效数据
        dfx = pd.concat([dfx['公开(公告)号'], dfx['发明人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        dfx = dfx.groupby('发明人', as_index=False)['公开(公告)号'].count()
        dfx = dfx.sort_values(by='公开(公告)号', ascending=False)
        dfx.columns = ['发明人', '申请数量']
        dfx = dfx.head(10)

        listx = list(dfx['发明人'])

        # 节点数据
        df1 = dfmb.loc[dfmb['发明人'].str.contains(listx[0], na=False), :]

        df1 = df1.astype({'发明人数量': 'int'})
        df1 = df1.loc[(df1['发明人数量'] != 1)]
        series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['公开(公告)号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
            df_l.columns = ['公开(公告)号', '发明人']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开(公告)号'], df_11['发明人'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格
        df_11 = df_11.groupby('发明人', as_index=False)['公开(公告)号'].count()
        df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        df_11.columns = ['发明人', '申请数量']

        # 关系数据
        df2 = dfmb.loc[dfmb['发明人'].str.contains(listx[0], na=False), :]
        df2 = df2[['公开(公告)号', '发明人']]
        series = df2['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df2[['公开(公告)号']]
        df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一发明人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
        df_z.columns = ['公开(公告)号', '第一发明人']
        df_22 = pd.DataFrame()
        for i in range(1, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
            df_l.columns = ['公开(公告)号', '第一发明人', '联合发明人']
            df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
        df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_22 = pd.concat([df_22['公开(公告)号'], df_22['第一发明人'], df_22['联合发明人'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格
        df_22 = df_22.groupby(['第一发明人', '联合发明人'], as_index=False)['公开(公告)号'].count()
        df_22 = df_22.sort_values(by='公开(公告)号', ascending=False)
        df_22.columns = ['第一发明人', '联合发明人', '申请数量']

        nodes = []
        for i in range(len(df_11)):
            node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),
                    "value": int(df_11.iat[i, 1])}

            nodes.append(node)

        links = []
        for i in range(len(df_22)):
            link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
                    "value": int(df_22.iat[i, 2])}
            links.append(link)

        # # 节点数据2
        # df1 = dfmb.loc[dfmb['发明人'].str.contains(listx[1], na=False), :]
        # df1 = df1.astype({'发明人数量': 'int'})
        # df1 = df1.loc[(df1['发明人数量'] != 1)]
        # series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        # df_z = df1[['公开(公告)号']]
        # df_11 = pd.DataFrame()
        # for i in range(0, series.columns.size):
        #     df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
        #     df_l.columns = ['公开(公告)号', '发明人']
        #     df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        # df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        # df_11 = pd.concat([df_11['公开(公告)号'], df_11['发明人'].str.strip()],
        #                   axis=1)  # 用strip（）删除字符串头尾多余空格
        # df_11 = df_11.groupby('发明人', as_index=False)['公开(公告)号'].count()
        # df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        # df_11.columns = ['发明人', '申请数量']
        #
        # # 关系数据
        # df2 = dfmb.loc[dfmb['发明人'].str.contains(listx[1], na=False), :]
        # df2 = df2[['公开(公告)号', '发明人']]
        # series = df2['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        # df_z = df2[['公开(公告)号']]
        # df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一发明人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
        # df_z.columns = ['公开(公告)号', '第一发明人']
        # df_22 = pd.DataFrame()
        # for i in range(1, series.columns.size):
        #     df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
        #     df_l.columns = ['公开(公告)号', '第一发明人', '联合发明人']
        #     df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
        # df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
        # df_22 = pd.concat([df_22['公开(公告)号'], df_22['第一发明人'], df_22['联合发明人'].str.strip()],
        #                   axis=1)  # 用strip（）删除字符串头尾多余空格
        # df_22 = df_22.groupby(['第一发明人', '联合发明人'], as_index=False)['公开(公告)号'].count()
        # df_22 = df_22.sort_values(by='公开(公告)号', ascending=False)
        # df_22.columns = ['第一发明人', '联合发明人', '申请数量']
        #
        # nodes2 = []
        # for i in range(len(df_11)):
        #     node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),
        #             "value": int(df_11.iat[i, 1])}
        #
        #     nodes2.append(node)
        #
        # links2 = []
        # for i in range(len(df_22)):
        #     link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
        #             "value": int(df_22.iat[i, 2])}
        #     links2.append(link)
        #
        # # 节点数据3
        # df1 = dfmb.loc[dfmb['发明人'].str.contains(listx[2], na=False), :]
        # df1 = df1.astype({'发明人数量': 'int'})
        # df1 = df1.loc[(df1['发明人数量'] != 1)]
        # series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        # df_z = df1[['公开(公告)号']]
        # df_11 = pd.DataFrame()
        # for i in range(0, series.columns.size):
        #     df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
        #     df_l.columns = ['公开(公告)号', '发明人']
        #     df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        # df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        # df_11 = pd.concat([df_11['公开(公告)号'], df_11['发明人'].str.strip()],
        #                   axis=1)  # 用strip（）删除字符串头尾多余空格
        # df_11 = df_11.groupby('发明人', as_index=False)['公开(公告)号'].count()
        # df_11 = df_11.sort_values(by='公开(公告)号', ascending=False)
        # df_11.columns = ['发明人', '申请数量']
        #
        # # 关系数据3
        # df2 = dfmb.loc[dfmb['发明人'].str.contains(listx[2], na=False), :]
        # df2 = df2[['公开(公告)号', '发明人']]
        # series = df2['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        # df_z = df2[['公开(公告)号']]
        # df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一发明人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
        # df_z.columns = ['公开(公告)号', '第一发明人']
        # df_22 = pd.DataFrame()
        # for i in range(1, series.columns.size):
        #     df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
        #     df_l.columns = ['公开(公告)号', '第一发明人', '联合发明人']
        #     df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
        # df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
        # df_22 = pd.concat([df_22['公开(公告)号'], df_22['第一发明人'], df_22['联合发明人'].str.strip()],
        #                   axis=1)  # 用strip（）删除字符串头尾多余空格
        # df_22 = df_22.groupby(['第一发明人', '联合发明人'], as_index=False)['公开(公告)号'].count()
        # df_22 = df_22.sort_values(by='公开(公告)号', ascending=False)
        # df_22.columns = ['第一发明人', '联合发明人', '申请数量']
        #
        # nodes3 = []
        # for i in range(len(df_11)):
        #     node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),
        #             "value": int(df_11.iat[i, 1])}
        #
        #     nodes3.append(node)
        #
        # links3 = []
        # for i in range(len(df_22)):
        #     link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
        #             "value": int(df_22.iat[i, 2])}
        #     links3.append(link)
        c = (
            Graph(init_opts=opts.InitOpts(
                bg_color='#FFFFFF', ))
            .add(listx[0],
                 nodes,
                 links,
                 repulsion=120,
                 layout="force",  #force circular
                 edge_length=120,
                 gravity=0.2,
                 is_draggable=True,
                 linestyle_opts=opts.LineStyleOpts(
                     width=2,
                     curve=0.3,
                 ),  # 线条配置

                 )
            # .add(listx[1],
            #      nodes2,
            #      links2,
            #      repulsion=200,
            #      layout="force",
            #      gravity=0.2,
            #      linestyle_opts=opts.LineStyleOpts(
            #          width=2,
            #          curve=0.3,
            #      ),  # 线条配置
            #
            #      )
            # .add(listx[2],
            #      nodes3,
            #      links3,
            #      repulsion=200,
            #      layout="force",  # 引力布局
            #      gravity=0.2,  # 斥力因子
            #      linestyle_opts=opts.LineStyleOpts(
            #          width=2,
            #          curve=0.3,
            #      ),  # 线条配置
            #
            #      )
            # .set_colors(
            #     ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
            #      "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
            #      "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),

                legend_opts=opts.LegendOpts(orient="vertical",
                                            pos_left="2%",
                                            pos_top="20%",
                                            background_color="transparent",
                                            border_color="transparent",
                                            ), )
            .set_series_opts(
                itemstyle_opts=opts.ItemStyleOpts(color="rgb(80,196,143)",  # 节点颜色
                                                  border_color="rgb(245,97,111)",  # 节点边线颜色
                                                  border_width=1,  # 节点边线宽度
                                                  opacity=0.7,  # 节点透明度
                                                  ),
                linestyle_opts=opts.LineStyleOpts(is_show=True,
                                                  width=1,
                                                  opacity=0.6,
                                                  curve=0.2,  # 弯曲度
                                                  type_="solid",  # 线条类型 'solid', 'dashed', 'dotted'
                                                  color="red",
                                                  ),
                label_opts=opts.LabelOpts(
                    is_show=True,
                    # position="top",
                    color="rgb(54,133,254)",
                    font_size=10,
                    font_style='normal',  # 正常
                    font_weight='bold',  # 加粗
                    # color='auto',  # 系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
            )
        )
        return c

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                                       <style>
                                                       .chart-container {
                                                           width: 100%;
                                                           height: 100%;
                                                           max-width: 1000px;

                                                           margin: 0 auto;
                                                       }
                                                       </style>
                                                       '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""发明人团队情况""")
st.write('通过观察发明人之间的连线，可以了解哪些发明人之间存在联合申请的关系。' \
         '通过观察圆的大小，可以了解每个发明人的专利数量。圆越大，表示该发明人拥有的专利数量越多。' \
         '通过观察连线的数量和连接的方式，可以分析发明人之间的协同情况。如果一个发明人与多个其他发明人有连线，表示该发明人与其他发明人之间有更多的联合申请。')
huitu56()



##重点专利
#被引用
def huitu61():
    global document
    def cunchupng():
        dfmb=dfm
        df1 = dfmb.loc[(dfmb['被引用专利数量'] != '-')]
        df1 = df1.loc[(df1['被引用专利数量'] != '该数据不支持导出')]
        df1 = df1.astype({'被引用专利数量': 'int'})
        df1 = df1[['公开(公告)号', '被引用专利数量']]

        df1 = df1.sort_values(by='被引用专利数量', ascending=False)
        df1 = df1.head(15)
        df1 = df1.sort_values(by='被引用专利数量', ascending=True)
        print(df1)
        listx = list(df1['公开(公告)号'])
        listy = list(df1['被引用专利数量'])

        bar = (
            Bar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis(
                series_name='',
                y_axis=listy,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=15,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family='serif',  #
                ),  # 标签配置项
            )
            .reversal_axis()
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),
                xaxis_opts=opts.AxisOpts(
                    # type_="category",  # 坐标轴类型
                    name='被引用数量',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(

                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                    )
                ),
                yaxis_opts=opts.AxisOpts(

                    # type_="value",
                    name='专利公开号',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False, )

            ))
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(bar, grid_opts=opts.GridOpts(pos_left="20%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                               <style>
                               .chart-container {
                                   width: 100%;
                                   height: 100%;
                                   max-width: 1000px;

                                   margin: 0 auto;
                               }
                               </style>
                               '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""🎈🎈🎈重点专利情况🎈🎈🎈""")
st.write(
    '重点专利部分关注的是在分析领域内具有重要意义或具有突破性创新的专利。' \
         '这些专利可能涉及关键技术、重要发明或对行业发展具有重要影响的专利。通过对重点专利的深入研究，我们可以深入了解技术创新的方向和前沿，为公司战略规划和竞争优势的构建提供参考。')
st.subheader("""被引用数量排名""")
st.write('该图表显示各个专利被引用的数量大小，并通过高度的大小来反映其排名情况。一个专利被引用的数量较多，那么它的柱子就会比其他专利高；' \
         '反之，如果一个专利被引用的数量较少，那么它的柱子就会比其他专利矮。通过比较各个专利被引用之间的数量差异，我们可以了解到哪些专利在该领域中具有更强的技术实力和竞争优势。')
huitu61()

#同族数
def huitu62():
    global document
    def cunchupng():
        dfmb=dfm
        df1 = dfmb.loc[(dfmb['简单同族成员数量'] != '-')]
        df1 = df1.loc[(df1['简单同族成员数量'] != '该数据不支持导出')]
        df1 = df1.astype({'简单同族成员数量': 'int'})
        df1 = df1[['公开(公告)号', '简单同族成员数量']]

        df1 = df1.sort_values(by='简单同族成员数量', ascending=False)
        df1 = df1.head(15)
        df1 = df1.sort_values(by='简单同族成员数量', ascending=True)
        print(df1)
        listx = list(df1['公开(公告)号'])
        listy = list(df1['简单同族成员数量'])

        bar = (
            Bar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis(
                series_name='',
                y_axis=listy,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=15,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family='serif',  #
                ),  # 标签配置项
            )
            .reversal_axis()
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),
                xaxis_opts=opts.AxisOpts(
                    # type_="category",  # 坐标轴类型
                    name='简单同族数量',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(

                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                    )
                ),
                yaxis_opts=opts.AxisOpts(

                    # type_="value",
                    name='专利公开号',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False, )

            ))
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(bar, grid_opts=opts.GridOpts(pos_left="20%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                   <style>
                                   .chart-container {
                                       width: 100%;
                                       height: 100%;
                                       max-width: 1000px;

                                       margin: 0 auto;
                                   }
                                   </style>
                                   '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)



st.subheader("""简单同族数量排名""")
st.write('该图表显示各个专利简单同族的数量大小，并通过高度的大小来反映其排名情况。一个专利简单同族的数量较多，那么它的柱子就会比其他专利简单同族的高；' \
         '反之，如果一个专利简单同族的数量较少，那么它的柱子就会比其他专利简单同族矮。通过比较各个专利简单同族之间的数量差异，我们可以了解到哪些专利在该领域中具有更强的技术实力和竞争优势。')
huitu62()

#权要数
def huitu63():
    global document
    def cunchupng():
        dfmb=dfm
        df1 = dfmb.loc[(dfmb['权利要求数量'] != '-')]
        df1 = df1.loc[(df1['权利要求数量'] != '该数据不支持导出')]
        df1 = df1.astype({'权利要求数量': 'int'})
        df1 = df1[['公开(公告)号', '权利要求数量']]

        df1 = df1.sort_values(by='权利要求数量', ascending=False)
        df1 = df1.head(15)
        df1 = df1.sort_values(by='权利要求数量', ascending=True)
        print(df1)
        listx = list(df1['公开(公告)号'])
        listy = list(df1['权利要求数量'])

        bar = (
            Bar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis(
                series_name='',
                y_axis=listy,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=15,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family='serif',  #
                ),  # 标签配置项
            )
            .reversal_axis()
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),
                xaxis_opts=opts.AxisOpts(
                    # type_="category",  # 坐标轴类型
                    name='权利要求数量',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(

                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                    )
                ),
                yaxis_opts=opts.AxisOpts(

                    # type_="value",
                    name='专利公开号',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False, )

            ))
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(bar, grid_opts=opts.GridOpts(pos_left="20%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                       <style>
                                       .chart-container {
                                           width: 100%;
                                           height: 100%;
                                           max-width: 1000px;

                                           margin: 0 auto;
                                       }
                                       </style>
                                       '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""权要数量排名""")
st.write('该图表显示各个专利申请中的权利要求数量，并通过高度的大小来反映其排名情况。一个专利申请中的权利要求数量较高，那么它的柱子就会比其他专利申请的高；' \
         '反之，如果一个专利申请中的权利要求数量较低，那么它的柱子就会比其他专利申请的矮。通过比较各个专利申请之间的权利要求数量差异，我们可以了解到哪些专利在该领域中具有更强的技术实力和竞争优势。')
huitu63()

#价值
def huitu64():
    global document
    def cunchupng():
        dfmb=dfm
        df1 = dfmb.loc[(dfmb['专利价值'] !='-')]
        df1 = df1.loc[(df1['专利价值'] != '该数据不支持导出')]
        df1['专利价值'] = df1['专利价值'].replace({'\$': ''}, regex=True)
        df1['专利价值'] = df1['专利价值'].replace({'\,': ''}, regex=True)
        df1 = df1.astype({'专利价值': 'int'})
        df1 = df1[['公开(公告)号', '专利价值']]

        df1 = df1.sort_values(by='专利价值', ascending=False)
        df1 = df1.head(15)
        df1 = df1.sort_values(by='专利价值', ascending=True)
        print(df1)
        listx = list(df1['公开(公告)号'])
        listy = list(df1['专利价值'])

        bar = (
            Bar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis(
                series_name='',
                y_axis=listy,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=15,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family='serif',  #
                ),  # 标签配置项
            )
            .reversal_axis()
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),
                xaxis_opts=opts.AxisOpts(
                    # type_="category",  # 坐标轴类型
                    name='专利价值',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(

                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                    )
                ),
                yaxis_opts=opts.AxisOpts(

                    # type_="value",
                    name='专利公开号',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False, )

            ))
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(bar, grid_opts=opts.GridOpts(pos_left="20%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                           <style>
                                           .chart-container {
                                               width: 100%;
                                               height: 100%;
                                               max-width: 1000px;

                                               margin: 0 auto;
                                           }
                                           </style>
                                           '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""专利价值排名""")
st.write('该图表显示各个专利的价值大小，并通过高度的大小来反映其排名情况。一个专利的价值较高，那么它的柱子就会比其他专利的高；' \
         '反之，如果一个专利的价值较低，那么它的柱子就会比其他专利矮。通过比较各个专利之间的价值差异，我们可以了解到哪些专利在该领域中具有更强的技术实力和竞争优势。')
huitu64()

#文献页数
def huitu65():
    global document
    def cunchupng():
        dfmb=dfm
        df1 = dfmb.loc[(dfmb['文献页数'] != '-')]
        df1 = df1.loc[(df1['文献页数'] != '该数据不支持导出')]
        df1 = df1.astype({'文献页数': 'int'})
        df1 = df1[['公开(公告)号', '文献页数']]

        df1 = df1.sort_values(by='文献页数', ascending=False)
        df1 = df1.head(15)
        df1 = df1.sort_values(by='文献页数', ascending=True)
        print(df1)
        listx = list(df1['公开(公告)号'])
        listy = list(df1['文献页数'])

        bar = (
            Bar(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
            ))
            .add_xaxis(listx)
            .add_yaxis(
                series_name='',
                y_axis=listy,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=15,
                    font_style='normal',  # 字体 正常 倾斜
                    font_weight='bold',  # 加粗
                    color='auto',  # 系列颜色
                    # font_family='serif',  #
                ),  # 标签配置项
            )
            .reversal_axis()
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                toolbox_opts=opts.ToolboxOpts(
                    orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                    item_size=15,
                    item_gap=5,
                    feature=toolbox_opts['feature']
                ),
                xaxis_opts=opts.AxisOpts(
                    # type_="category",  # 坐标轴类型
                    name='文献页数',  # 坐标轴名字
                    name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                    axislabel_opts=opts.LabelOpts(

                        font_size=15,
                        font_style='normal',
                        font_weight='bold',
                    )
                ),
                yaxis_opts=opts.AxisOpts(

                    # type_="value",
                    name='专利公开号',  # 坐标轴名字
                    name_location="end",
                    axislabel_opts=opts.LabelOpts(
                        font_size=15,
                        font_style='normal',
                        font_weight='bold', )
                ),
                legend_opts=opts.LegendOpts(
                    is_show=False, )

            ))
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(bar, grid_opts=opts.GridOpts(pos_left="20%")))

        return grid

    bar_chart = cunchupng()
    # 渲染图表并生成HTML内容
    html = bar_chart.render_embed()
    css = '''
                                               <style>
                                               .chart-container {
                                                   width: 100%;
                                                   height: 100%;
                                                   max-width: 1000px;

                                                   margin: 0 auto;
                                               }
                                               </style>
                                               '''
    # 组合HTML内容和CSS样式
    html_with_css = f'{css}<div class="chart-container">{html}</div>'
    # 使用st.components.v1.html显示HTML内容
    st.components.v1.html(html_with_css, height=500, scrolling=True)


st.subheader("""文献页数排名""")
st.write('该图表显示各个专利文献的页数大小，并通过高度的大小来反映其排名情况。一个专利文献的页数较多，那么它的柱子就会比其他专利文献的高；' \
         '反之，如果一个专利文献的页数较少，那么它的柱子就会比其他专利文献矮。通过比较各个专利文献之间的页数差异，我们可以了解到哪些专利在该领域中具有更强的技术实力和竞争优势。')
huitu65()


#气球
st.balloons()
#雪花
st.snow()



