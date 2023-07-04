import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
import random
import matplotlib as mpl
from pyecharts import options as opts
from pyecharts.charts import Line, Grid, Bar, PictorialBar, Pie, Funnel, Scatter, Map, Geo, EffectScatter, Gauge, Polar, \
    Radar, HeatMap, Graph, WordCloud, Timeline
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from matplotlib.ticker import MaxNLocator
import base64
from pandas.api.types import CategoricalDtype

# 加载自定义字体文件
mpl.font_manager.fontManager.addfont('streamlit系列/simhei.ttf')

mpl.rcParams['font.sans-serif'] = ["SimHei"]
# 正常显示中文字符
mpl.rcParams["axes.unicode_minus"] = False


def genOrder(df, orderList, colName):  # 自定义排序
    cat_order = CategoricalDtype(orderList, ordered=True)
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
shengfen = ['北京', '天津', '上海', '重庆', '河北', '河南', '云南', '辽宁', '黑龙江', '湖南',
            '安徽', '山东', '新疆', '江苏', '浙江', '江西', '湖北', '广西', '甘肃', '山西',
            '内蒙古', '陕西', '吉林', '福建', '贵州', '广东', '青海', '西藏', '四川', '宁夏',
            '海南', '台湾', '香港', '澳门']
zhixiashi = ['北京', '天津', '上海', '重庆']
nianfen = ['2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
           '2016', '2017', '2018', '2019', '2020', '2021', '2022']
nianfen10 = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
wuju = ['中国', '美国', '日本', '韩国', '欧洲专利局']
fusheng = '浙江'
dishi = '台州'

# 侧边栏初始状态为折叠 streamlit 页面布局为 宽
st.set_page_config(initial_sidebar_state='collapsed', layout='wide')

# st.image("新不二LOGO.png")  # streamlit系列/新不二LOGO.png
uploaded_files = st.file_uploader('上传Excel文件', accept_multiple_files=True, type='xlsx')

if not uploaded_files:
    def load_df():
        return pd.read_excel('streamlit系列/分析部工作进度表.xlsx')  # streamlit系列/2020-2022中之信.xlsx


    df = load_df()
else:
    for file in uploaded_files:
        print(file)
        df = pd.read_excel(file)



# 侧边栏 标题
st.sidebar.header('➡⌛⌛⌛筛选条件⌛⌛⌛⬅')
# 返回列的唯一值数组
market_values = df['类型'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets = st.sidebar.multiselect('🌏类型：', market_values_with_all, market_values_with_all[0])
if '全选' in markets:
    # Select all market values
    markets = market_values.tolist()
# # 多选择的部件

market_values = df['状态'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets1 = st.sidebar.multiselect('📖状态：', market_values_with_all, market_values_with_all[0])
if '全选' in markets1:
    # Select all market values
    markets1 = market_values.tolist()

# 做数据筛选 根据上面选择的类别
dfm = df.query('类型 in @markets and 状态 in @markets1'
               )

# 页面 标题
st.title('🎉🎉🎉工作进度看板🎉🎉🎉')

st.dataframe(dfm)


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

def huitu1():
    df1 = dfm
    df1 = df1.sort_values(by='序号', ascending=False)
    print(df1)

    #双X轴设置
    fig = plt.figure(dpi=720)
    ax1 = fig.add_subplot(111)
    ax1.spines['right'].set_color('none')  # 上边框
    ax1.barh(df1['项目名称'], df1['项目进度'], color="#3685fe", alpha=0.3, tick_label=df1['项目名称'])
    ax1.set_ylabel('项目名称', fontdict={'size': 12})
    ax1.set_xlabel('项目进度(%)', fontdict={'size': 12})
    plt.xticks(size=10)
    plt.xlim(0, 100)

    ax2 = ax1.twiny() #共享Y轴
    ax2.spines['right'].set_color('none')  # 上边框
    ax2.xaxis.set_tick_params(labelcolor="#f5616f")
    ax2.barh(df1['项目名称'], df1['项目进度'], color="#3685fe", alpha=0.3, tick_label=df1['项目名称'])
    lt=['进度及时间','类型','人员','目标及时间']
    plt.xticks([1,25,50,75],lt,size=10)


    # plt.figure(dpi=720)  # 配置画布大小，分辨率
    # fig, ax = plt.subplots()  # 去除多余边框
    # ax.spines['right'].set_visible(False)  # 右边框
    # # ax.spines['top'].set_visible(False)  # 上边框
    # plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)  # 图与画布四周距离
    # plt.barh( df1['项目名称'],df1['项目进度'], color="#3685fe",alpha=0.5)
    # plt.ylabel('项目名称', fontdict={'size': 12})
    # plt.xlabel('项目进度(%)', fontdict={'size': 12})
    # plt.xticks(size=10)
    # plt.xlim(0,100)
    # plt.yticks(size=8)

    for a, b,c,d,e,f in zip(df1['项目进度'],df1['项目名称'],df1['类型'],df1['人员'],df1['目标'],df1['目标时间']):
        plt.text(1, b, format(a), ha='left', va='bottom', fontsize=8, alpha=0.9)
    for a, b,c,d,e,f in zip(df1['项目进度'],df1['项目名称'],df1['类型'],df1['人员'],df1['目标'],df1['目标时间']):
        plt.text(25, b, format(c), ha='left', va='center', fontsize=8, alpha=0.9)
    for a, b,c,d,e,f in zip(df1['项目进度'],df1['项目名称'],df1['进度时间'],df1['人员'],df1['目标'],df1['目标时间']):
        plt.text(1, b, format(c), ha='left', va='top', fontsize=8, alpha=0.9)
    for a, b,c,d,e,f in zip(df1['项目进度'],df1['项目名称'],df1['类型'],df1['人员'],df1['目标'],df1['目标时间']):
        plt.text(50, b, format(d), ha='left', va='center', fontsize=8, alpha=0.9)
    for a, b,c,d,e,f in zip(df1['项目进度'],df1['项目名称'],df1['类型'],df1['人员'],df1['目标'],df1['目标时间']):
        plt.text(75, b, format(e), ha='left', va='bottom', fontsize=8, alpha=0.9)
    for a, b,c,d,e,f in zip(df1['项目进度'],df1['项目名称'],df1['类型'],df1['人员'],df1['目标'],df1['目标时间']):
        plt.text(75, b, format(f), ha='left', va='top', fontsize=8, alpha=0.9)

    st.pyplot(fig)

if dfm.empty:
    st.write('该数据范围无相应图表！')
else:
    st.subheader("""分析部项目进度""")
    st.write('分析部项目进度,进度更新时间：2023.6.13')
    huitu1()

# 气球
st.balloons()
# #雪花
st.snow()