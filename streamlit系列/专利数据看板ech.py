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

# 加载自定义字体文件
mpl.font_manager.fontManager.addfont('streamlit系列/simhei.ttf')

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
nianfen10=['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
wuju=['中国','美国','日本','韩国','欧洲专利局']
fusheng='浙江'
dishi='台州'


#侧边栏初始状态为折叠 streamlit 页面布局为 宽
st.set_page_config(initial_sidebar_state='expanded',layout='wide')
# # 添加背景
# def add_local_backgound_image_(image):
#     with open(image, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
#
#     css = f"""
#     <style>
#     .stApp {{
#         background-image: url('data:image/png;base64,{encoded_string}');
#         background-size: 80% 50%;
#         background-repeat: no-repeat;
#         background-position: center center;
#         opacity: 1;
#         z-index: -1;
#     }}
#     </style>
#     """
#
#     st.markdown(css, unsafe_allow_html=True)
#
# add_local_backgound_image_('新不二LOGO.png')



#添加水印效果

# 缓存Excel数据到load-df
# @st.cache_data
# def load_df():
#     return pd.read_excel('streamlit系列/AR眼镜.XLSX')  # streamlit系列/2020-2022中之信.xlsx
#
#
# df = load_df()
st.image("streamlit系列/新不二LOGO.png")  # streamlit系列/新不二LOGO.png
uploaded_files = st.file_uploader('上传Excel文件', accept_multiple_files=True, type='xlsx')

if not uploaded_files:
    def load_df():
        return pd.read_excel('streamlit系列/AR眼镜.XLSX')  # streamlit系列/2020-2022中之信.xlsx
    df = load_df()
else:
    for file in uploaded_files:
        print(file)
        df = pd.read_excel(file)

df=df.rename(columns={'公开(公告)号': '公开公告号'})
df=df.rename(columns={'[标]当前申请(专利权)人': '当前申请专利权人'})
df=df.rename(columns={'当前申请(专利权)人数量': '当前申请专利权人数量'})
df=df.rename(columns={'IPC主分类号(小类)': 'IPC主分类号小类'})
df=df.rename(columns={'法律状态/事件': '法律状态事件'})
df=df.rename(columns={'当前申请(专利权)人州/省': '当前申请专利权人州省'})
df=df.rename(columns={'当前申请(专利权)人地市': '当前申请专利权人地市'})
df=df.rename(columns={'当前申请(专利权)人区县': '当前申请专利权人区县'})
df=df.rename(columns={'当前发明(专利权)人': '当前发明专利权人'})
df = df.loc[(df['标题'] != '-')]


# 侧边栏 标题
st.sidebar.header('➡⌛⌛⌛筛选条件⌛⌛⌛⬅')
# 返回列的唯一值数组
market_values = df['受理局'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets = st.sidebar.multiselect('🌏受理局：', market_values_with_all, market_values_with_all[0])
if '全选' in markets:
    # Select all market values
    markets= market_values.tolist()
# # 多选择的部件

market_values = df['专利类型'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets1 = st.sidebar.multiselect('📖专利类型：', market_values_with_all, market_values_with_all[0])
if '全选' in markets1:
    # Select all market values
    markets1 = market_values.tolist()

# # 返回列的唯一值数组
# market_values = df['简单法律状态'].unique()
# # 多选择的部件
# markets2 = st.sidebar.multiselect('☸简单法律状态：', market_values, market_values)

# 返回列的唯一值数组
market_values = df['简单法律状态'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets2 = st.sidebar.multiselect('☸简单法律状态：', market_values_with_all, market_values_with_all[0])
if '全选' in markets2:
    # Select all market values
    markets2 = market_values.tolist()

# 返回列的唯一值数组
market_values = df['申请年'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets3 = st.sidebar.multiselect('📅申请年：', market_values_with_all, market_values_with_all[0])
if '全选' in markets3:
    # Select all market values
    markets3 = market_values.tolist()
# 返回列的唯一值数组
market_values = df['当前申请专利权人州省'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets4 = st.sidebar.multiselect('🗺当前申请专利权人州省：', market_values_with_all, market_values_with_all[0])
if '全选' in markets4:
    # Select all market values
    markets4 = market_values.tolist()

market_values = df['战略新兴产业分类'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets5 = st.sidebar.multiselect('🏭战略新兴产业分类：：', market_values_with_all, market_values_with_all[0])
if '全选' in markets5:
    markets5 = market_values.tolist()

# 做数据筛选 根据上面选择的类别
dfm = df.query('受理局 in @markets and 专利类型 in @markets1  and'
               ' 简单法律状态 in @markets2 and 申请年 in @markets3 and 当前申请专利权人州省 in @markets4 and 战略新兴产业分类 in @markets5')


# 页面 标题
st.title('🎉🎉🎉专利数据看板🎉🎉🎉')

st.dataframe(dfm)


# 指标 计算
zongshenqing = int(dfm['公开公告号'].count())

shouquan = dfm.loc[dfm['法律状态事件'].str.contains('授权', na=False), :]
shouquan = shouquan['法律状态事件'].count()

bohui = dfm.loc[dfm['法律状态事件'].str.contains('驳回', na=False), :]
bohui = bohui['法律状态事件'].count()

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

biaoji=1
##全球专利发展趋势分析
def huitu1():
    global biaoji
    def cunchupng():
        dfmb=dfm
        df1 = dfmb[['公开公告号', '申请年']]
        df1 = df1.astype({'申请年': 'str'})
        df1 = df1.groupby('申请年', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='申请年', ascending=True)
        df1.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df1, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df1 = dfx
        df1 = df1.astype({'申请数量': 'int'})


        dfmb = dfm.loc[(dfm['简单法律状态'] == '有效')]
        df2 = dfmb[['公开公告号', '申请年']]
        df2 = df2.astype({'申请年': 'str'})
        df2 = df2.groupby('申请年', as_index=False)['公开公告号'].count()
        df2 = df2.sort_values(by='申请年', ascending=True)
        df2.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df2, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df2 = dfx
        df2 = df2.astype({'申请数量': 'int'})


        dfmb = dfm.loc[(dfm['简单法律状态'] == '失效')]
        df3 = dfmb[['公开公告号', '申请年']]
        df3 = df3.astype({'申请年': 'str'})
        df3 = df3.groupby('申请年', as_index=False)['公开公告号'].count()
        df3 = df3.sort_values(by='申请年', ascending=True)
        df3.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df3, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df3 = dfx
        df3 = df3.astype({'申请数量': 'int'})


        dfmb = dfm.loc[(dfm['简单法律状态'] == '审中')]
        df4 = dfmb[['公开公告号', '申请年']]
        df4 = df4.astype({'申请年': 'str'})
        df4 = df4.groupby('申请年', as_index=False)['公开公告号'].count()
        df4 = df4.sort_values(by='申请年', ascending=True)
        df4.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df4, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df4 = dfx
        df4 = df4.astype({'申请数量': 'int'})


        listx=list(df1['申请年'])
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
                    font_style='normal',#字体 正常 倾斜
                    font_weight='bold', #加粗
                    color= 'auto', #系列颜色
                    # font_family= 'serif',#
                ),  # 标签配置项
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    type_="solid",
                ),  # 线条配置
            ))
        bar= (
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
##五局流向图
def huitu2():
    def cunchupng():
        global biaoji
        dfmb=dfm
        df1 = dfmb.query('受理局 in %s ' % wuju)
        if df1.empty:
            biaoji=0
        else:

            df1 = df1[['公开公告号', '受理局', '优先权国家']]
            series = df1['优先权国家'].str.split('|', expand=True)  # 按照 分隔符拆分字段
            df_z = df1[['公开公告号', '受理局']]
            df_11 = pd.DataFrame()
            for i in range(0, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
                df_l.columns = ['公开公告号', '受理局', '优先权国家']
                df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
            df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_11 = pd.concat([df_11['公开公告号'],df_11['受理局'], df_11['优先权国家'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
            for i in range(0,len(df_11['优先权国家'])):
                if df_11.iat[i,2]=='CN':
                    df_11.iat[i,2] = '中国'
                if df_11.iat[i,2]=='US':
                    df_11.iat[i,2] = '美国'
                if df_11.iat[i,2]=='JP':
                    df_11.iat[i,2] = '日本'
                if df_11.iat[i,2]=='KR':
                    df_11.iat[i,2] = '韩国'
                if df_11.iat[i,2]=='EP':
                    df_11.iat[i,2] = '欧洲专利局'
            df_11=df_11.query('优先权国家 in %s ' % wuju)
            df_11=df_11.drop_duplicates()
            df_11 = df_11.groupby(['受理局', '优先权国家'], as_index=False)['公开公告号'].count()
            df_11 = df_11.sort_values(by=['受理局', '优先权国家'], ascending=True)
            df_11.columns = ['受理局', '优先权国家', '申请数量']
            df1=df_11

            if df1.empty:
                biaoji = 0
            else:



                xmax = max(df1['申请数量'])
                xmin = min(df1['申请数量'])

                # 类别一数据
                df2 = df1.loc[(df1['受理局'] == '中国')]
                # 类别二数据
                df3 = df1.loc[(df1['受理局'] == '美国')]
                # 类别三数据
                df4 = df1.loc[(df1['受理局'] == '日本')]
                df5 = df1.loc[(df1['受理局'] == '韩国')]
                df6 = df1.loc[(df1['受理局'] == '欧洲专利局')]


                # listx=['中国','日本','欧洲专利局','美国','韩国']
                listx=list(df2['优先权国家'])
                listy2 = list(df2['申请数量'])
                listy3 = list(df3['申请数量'])
                listy4 = list(df4['申请数量'])
                listy5 = list(df5['申请数量'])
                listy6 = list(df6['申请数量'])

                c = (
                    EffectScatter(init_opts=opts.InitOpts(
                        bg_color='#FFFFFF'))
                    .add_xaxis(listx)
                    .add_yaxis('中国', listy2)
                    .add_yaxis('美国', listy3)
                    .add_yaxis('日本', listy4)
                    .add_yaxis('韩国', listy5)
                    .add_yaxis('欧洲专利局', listy6)
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

                        visualmap_opts=opts.VisualMapOpts(is_show=False, type_="size", max_=xmax, min_=xmin),  # 气泡尺寸大小范围
                        xaxis_opts=opts.AxisOpts(
                            type_="category",  # 坐标轴类型
                            name='技术来源地区',  # 坐标轴名字
                            name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                            axislabel_opts=opts.LabelOpts(

                                font_size=15,
                                font_style='normal',
                                font_weight='bold',
                            )
                        ),
                        yaxis_opts=opts.AxisOpts(
                            type_="value",
                            name='专利数量',  # 坐标轴名字
                            name_location="end",
                            axislabel_opts=opts.LabelOpts(

                                font_size=15,
                                font_style='normal',
                                font_weight='bold',
                            )
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
                    )
                )
                return c
    # 创建图表
    bar_chart = cunchupng()
    if biaoji !=0:
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
##全球 地区分布分析
def huitu3():
    global biaoji
    def cunchupng() -> map:
        global biaoji
        dfmb=dfm
        df1 = dfmb[['受理局', '公开公告号']]
        df1 = df1.groupby('受理局', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='公开公告号', ascending=False)
        # df1=df1.head(10)
        if df1.empty:
            biaoji=0
        else:
            listx = list(df1['受理局'])
            listy = list(df1['公开公告号'])
            data_pair = [list(z) for z in zip(listx, listy)]
            xmin = 0
            xmax = max(listy)/2
            map = (
                Map(init_opts=opts.InitOpts(
                    bg_color='#FFFFFF',

                ))
                .add(series_name="专利数量", data_pair=data_pair, maptype="world",  # world，china 省 市
                     is_map_symbol_show=False, name_map=name_map)  # 更改地图中文显示

                .set_series_opts(
                    label_opts=opts.LabelOpts(  # 标签配置
                        is_show=False, ))
                .set_global_opts(
                    toolbox_opts=opts.ToolboxOpts(
                        orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                        item_size=15,
                        item_gap=5,
                        feature=toolbox_opts2['feature']
                    ),
                    legend_opts=opts.LegendOpts(
                        is_show=False, ),
                    visualmap_opts=opts.VisualMapOpts(  # 颜色映射
                        is_show=True,
                        min_=xmin,
                        max_=xmax,
                        range_text=['高', '低'],
                        pos_left="10%",
                        range_color=["Gainsboro", "yellow", "red"],
                    )
                )
            )

            return map

    # 创建图表
    bar_chart = cunchupng()
    if biaoji !=0:
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
    #申请人排名
def huitu4():
    global biaoji
    def cunchupng():
        global biaoji
        dfmb=dfm
        df1 = dfmb.astype({'申请年': 'str'})
        df1 = df1.query('申请年 in %s ' % nianfen)
        df1 = df1[['公开公告号', '当前申请专利权人']]
        series = df1['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['公开公告号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开公告号', '当前申请专利权人']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开公告号'], df_11['当前申请专利权人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        df_11 = df_11.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
        df_11 = df_11.sort_values(by='公开公告号', ascending=False)
        df_11.columns = ['当前申请专利权人', '申请数量']
        df3=df_11.head(10)
        df3 = df3.sort_values(by='申请数量', ascending=True)
        if df3.empty:
            biaoji=0
        else:

            # for j in range(0, len(df3['当前申请专利权人'])):
            #     if len(df3.iat[j, 0]) > 8:
            #         df3.iat[j, 0] = df3.iat[j, 0][0:7] + '...'
            #     else:
            #         df3.iat[j, 0] = df3.iat[j, 0]
            listx = list(df3['当前申请专利权人'])
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
                        feature=toolbox_opts3['feature']
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
                         is_show=False,)
                )
            )
            grid = (
                Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
                # 设置距离 bar为x轴标签过长的柱状图
                .add(c, grid_opts=opts.GridOpts(pos_left="25%")))

            return grid

    bar_chart = cunchupng()
    if biaoji!=0:
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
##协同申请趋势
def huitu5():
    global biaoji
    def cunchupng():
        dfmb=dfm.loc[(dfm['当前申请专利权人数量'] != '-') & (dfm['当前申请专利权人数量'] != '1')]
        df1 = dfmb[['公开公告号', '申请年']]
        df1 = df1.astype({'申请年': 'str'})
        df1 = df1.groupby('申请年', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='申请年', ascending=True)
        df1.columns = ['申请年', '申请数量']
        dfx = pd.DataFrame({'申请年': nianfen,
                            '申请次数': 0})
        dfx = pd.merge(dfx, df1, how='left', on='申请年')  # 补充df_1 缺失的年份数据
        dfx = dfx[['申请年', '申请数量']]
        dfx = dfx.fillna(0)  # 对为空的 属性补 0
        df1 = dfx
        df1 = df1.astype({'申请数量': 'int'})

        if df1.empty:
            biaoji=0
        else:

            listx = list(df1['申请年'])
            listy = list(df1['申请数量'])


            c = (
                Line(init_opts=opts.InitOpts(
                    bg_color='#FFFFFF'))
                .add_xaxis(listx)
                .add_yaxis(
                    series_name='申请数量',
                    y_axis=listy,
                    # is_selected=True,##是否选中图例
                    is_smooth=True,  # 是否平滑曲线
                    is_symbol_show=True,  # 是否显示 symbol
                    label_opts=opts.LabelOpts(
                        is_show=True,
                        position="top",
                        font_size=15,
                        font_style='normal',  # 字体 正常 倾斜
                        font_weight='bold',  # 加粗
                        color='auto',  # 系列颜色
                        # font_family= 'serif',#
                    ),  # 标签配置项

                    linestyle_opts=opts.LineStyleOpts(
                        width=5,
                        type_="solid",
                    ),  # 线条配置
                    areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
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
                            font_size=15,
                            font_style='normal',
                            font_weight='bold',
                            rotate=45)
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
                    legend_opts=opts.LegendOpts(is_show=False)
                )
            )
            return c

    bar_chart = cunchupng()
    if biaoji!=0:
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
##专利类型构成
def huitu7():
    global biaoji
    def cunchupng():
        dfmb = dfm
        df1 = dfmb[['专利类型', '公开公告号']]
        df1 = df1.loc[(df1['专利类型'] != '-')]
        df1 = df1.groupby('专利类型', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='公开公告号', ascending=False)
        df1.columns = ['专利类型', '申请数量']
        df1 = df1.head(5)
        if df1.empty:
            biaoji=0
        else:
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
    if biaoji!=0:
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
##简单法律状态构成
def huitu8():
    global biaoji
    def cunchupng():
        dfmb = dfm
        df1 = dfmb[['简单法律状态', '公开公告号']]
        df1 = df1.groupby('简单法律状态', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='公开公告号', ascending=False)
        df1.columns = ['简单法律状态', '申请数量']

        if len(df1['简单法律状态']) >=5:
            df1 = df1.head(5)

        else:
            df1= df1.head(len(df1['简单法律状态']))

        if df1.empty:
            biaoji=0
        else:
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
                        font_weight='bold',
                        color='auto',  # 系列颜色
                    ))
            )
            return c


    bar_chart = cunchupng()
    if biaoji!=0:
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
##专利运营情况
def huitu9():
    global biaoji
    def cunchupng():
        global biaoji
        dfmb=dfm
        df1 = dfmb[['法律状态事件','申请年', '公开公告号' ]]
        df1 = df1.astype({'申请年': 'str'})
        df1 = df1.query('申请年 in %s ' % nianfen)
        series = df1['法律状态事件'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['申请年', '公开公告号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['申请年', '公开公告号', '法律状态事件']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['申请年'],df_11['公开公告号'], df_11['法律状态事件'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格

        df1 = df_11
        df1.columns=['申请年','公开公告号','法律状态事件',]

        df1 = df1.loc[(df1['法律状态事件'].str.contains('权利转移', na=False)) | (
            df1['法律状态事件'].str.contains('质押', na=False))| (
            df1['法律状态事件'].str.contains('许可', na=False))]


        df1 = df1.groupby(['申请年', '法律状态事件'], as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='申请年', ascending=True)

        df1.columns = ['申请年', '法律状态事件', '申请数量']

        if df1.empty:
            biaoji=0
        else:

            xmax = max(df1['申请数量'])
            xmin = min(df1['申请数量'])

            # 类别一数据
            df2 = df1.loc[(df1['法律状态事件'] == '权利转移')]
            dfx = pd.DataFrame({'申请年': nianfen,
                                '申请次数': 0})
            dfx = pd.merge(dfx, df2, how='left', on='申请年')  # 补充df_1 缺失的年份数据
            dfx = dfx[['申请年', '申请数量']]
            dfx = dfx.fillna(0)  # 对为空的 属性补 0
            df2 = dfx
            # 类别二数据
            df3 = df1.loc[(df1['法律状态事件'] == '质押')]
            dfx = pd.DataFrame({'申请年': nianfen,
                                '申请次数': 0})
            dfx = pd.merge(dfx, df3, how='left', on='申请年')  # 补充df_1 缺失的年份数据
            dfx = dfx[['申请年', '申请数量']]
            dfx = dfx.fillna(0)  # 对为空的 属性补 0
            df3 = dfx
            # 类别三数据
            df4 = df1.loc[(df1['法律状态事件'] == '许可')]
            dfx = pd.DataFrame({'申请年': nianfen,
                                '申请次数': 0})
            dfx = pd.merge(dfx, df4, how='left', on='申请年')  # 补充df_1 缺失的年份数据
            dfx = dfx[['申请年', '申请数量']]
            dfx = dfx.fillna(0)  # 对为空的 属性补 0
            df4 = dfx




            listx = nianfen
            listy2 = list(df2['申请数量'])
            listy3 = list(df3['申请数量'])
            listy4 = list(df4['申请数量'])
            c = (
                EffectScatter(init_opts=opts.InitOpts(
                    bg_color='#FFFFFF'))
                .add_xaxis(listx)
                .add_yaxis('权利转移', listy2)
                .add_yaxis('质押', listy3)
                .add_yaxis('许可', listy4)

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

                    visualmap_opts=opts.VisualMapOpts(is_show=False, type_="size", max_=xmax, min_=1),  # 气泡尺寸大小范围
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
                        name='专利数量',  # 坐标轴名字
                        name_location="end",
                        axislabel_opts=opts.LabelOpts(

                            font_size=15,
                            font_style='normal',
                            font_weight='bold',

                        )
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
                )
            )
            return c



    bar_chart = cunchupng()

    if biaoji!=0:
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
#基础功效 前五ipc 申请趋势
def huitu10():
    global biaoji
    def cunchupng():
        global biaoji
        dfmb=dfm
        df1 = dfmb.astype({'申请年': 'str'})
        df1= df1.query('申请年 in %s ' % nianfen)
        df1 = df1[['IPC分类号','申请年', '公开公告号' ]]
        series = df1['IPC分类号'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['申请年', '公开公告号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['申请年', '公开公告号', 'IPC分类号']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['申请年'],df_11['公开公告号'], df_11['IPC分类号'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格

        dfx = df_11[['IPC分类号', '公开公告号']]
        dfx = dfx.groupby(['IPC分类号'], as_index=False)['公开公告号'].count()
        dfx = dfx.sort_values(by='公开公告号', ascending=False)
        dfx = dfx.head(5)

        listx = list(dfx['IPC分类号'])


        df1=df_11

        df1 = df1.groupby(['申请年', 'IPC分类号'], as_index=False).count()
        df1 = df1.sort_values(by='申请年', ascending=True)
        df1.columns = ['申请年', 'IPC主分类号小类', '申请数量']
        df1 = df1.query('IPC主分类号小类 in %s ' % listx)
        if df1.empty:
            biaoji=0
        else:


            df_1 = df1.loc[(df1['IPC主分类号小类'] == listx[0])]
            df_1.columns = ['申请年', 'IPC分类号', '申请数量']

            df_2 = df1.loc[(df1['IPC主分类号小类'] == listx[1])]
            df_2.columns = ['申请年', 'IPC分类号', '申请数量']

            df_3 = df1.loc[(df1['IPC主分类号小类'] == listx[2])]
            df_3.columns = ['申请年', 'IPC分类号', '申请数量']

            df_4 = df1.loc[(df1['IPC主分类号小类'] == listx[3])]
            df_4.columns = ['申请年', 'IPC分类号', '申请数量']

            df_5 = df1.loc[(df1['IPC主分类号小类'] == listx[4])]
            df_5.columns = ['申请年', 'IPC分类号', '申请数量']


            listx1 = list(df_1['申请年'])
            listx2 = list(df_2['申请年'])
            listx3 = list(df_3['申请年'])
            listx4 = list(df_4['申请年'])
            listx5 = list(df_5['申请年'])
            listy1 = list(df_1['申请数量'])
            listy2 = list(df_2['申请数量'])
            listy3 = list(df_3['申请数量'])
            listy4 = list(df_4['申请数量'])
            listy5 = list(df_5['申请数量'])


            c = (
                Line(init_opts=opts.InitOpts(
                    bg_color='#FFFFFF'))
                .add_xaxis(listx1)
                .add_yaxis(
                    series_name=listx[0],
                    y_axis=listy1,

                    is_smooth=True,  # 是否平滑曲线
                    is_symbol_show=True,  # 是否显示 symbol

                    linestyle_opts=opts.LineStyleOpts(
                        width=3,
                        type_="solid",
                    ),  # 线条配置
                )
                .add_xaxis(listx2)
                .add_yaxis(
                    series_name=listx[1],
                    y_axis=listy2,

                    is_smooth=True,  # 是否平滑曲线
                    is_symbol_show=True,  # 是否显示 symbol

                    linestyle_opts=opts.LineStyleOpts(
                        width=3,
                        type_="solid",
                    ),  # 线条配置
                )
                .add_xaxis(listx3)
                .add_yaxis(
                    series_name=listx[2],
                    y_axis=listy3,

                    is_smooth=True,  # 是否平滑曲线
                    is_symbol_show=True,  # 是否显示 symbol

                    linestyle_opts=opts.LineStyleOpts(
                        width=3,
                        type_="solid",
                    ),  # 线条配置
                )
                .add_xaxis(listx4)
                .add_yaxis(
                    series_name=listx[3],
                    y_axis=listy4,

                    is_smooth=True,  # 是否平滑曲线
                    is_symbol_show=True,  # 是否显示 symbol

                    linestyle_opts=opts.LineStyleOpts(
                        width=3,
                        type_="solid",
                    ),  # 线条配置
                )
                .add_xaxis(listx5)
                .add_yaxis(
                    series_name=listx[4],
                    y_axis=listy5,

                    is_smooth=True,  # 是否平滑曲线
                    is_symbol_show=True,  # 是否显示 symbol

                    linestyle_opts=opts.LineStyleOpts(
                        width=3,
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
                            rotate=45)
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
                        pos_right='right',  # 右边
                        orient='vertical',
                        pos_top='10%',  # 距离上边界15%
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
                        font_size=15,
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
                .add(c, grid_opts=opts.GridOpts(pos_bottom="10%")))

            return grid


    bar_chart = cunchupng()
    if biaoji!=0:
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
#前三联合申请人的联合情况
def huitu11():
    global biaoji
    def cunchupng():
        global biaoji
        dfmb = dfm.loc[(dfm['当前申请专利权人数量'] != '-')]
        dfmb = dfmb.astype({'当前申请专利权人数量': 'int'})
        dfmb = dfmb.loc[(dfmb['当前申请专利权人数量'] != 1)]
        dfm1 = dfmb[['公开公告号', '当前申请专利权人']]
        series = dfm1['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfm1[['公开公告号']]
        dfx = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开公告号', '当前申请专利权人']
            dfx = pd.concat([dfx, df_l])  ##所有新表叠加
        dfx.dropna(inplace=True)  # 删除空数据，获得有效数据
        dfx = pd.concat([dfx['公开公告号'], dfx['当前申请专利权人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        dfx = dfx.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
        dfx = dfx.sort_values(by='公开公告号', ascending=False)
        dfx.columns = ['当前申请专利权人', '申请数量']
        dfx = dfx.head(10)
        listx = list(dfx['当前申请专利权人'])


        # 节点数据
        df1 = dfmb.loc[dfmb['当前申请专利权人'].str.contains(listx[0], na=False), :]
        if df1.empty:
            biaoji=0
        else:
            df1 = df1.astype({'当前申请专利权人数量': 'int'})
            df1 = df1.loc[(df1['当前申请专利权人数量'] != 1)]
            series = df1['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            df_z = df1[['公开公告号']]
            df_11 = pd.DataFrame()
            for i in range(0, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
                df_l.columns = ['公开公告号', '当前申请专利权人']
                df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
            df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_11 = pd.concat([df_11['公开公告号'], df_11['当前申请专利权人'].str.strip()],
                              axis=1)  # 用strip（）删除字符串头尾多余空格
            df_11 = df_11.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
            df_11 = df_11.sort_values(by='公开公告号', ascending=False)
            df_11.columns = ['当前申请专利权人', '申请数量']

            # 关系数据
            df2 = dfmb.loc[dfmb['当前申请专利权人'].str.contains(listx[0], na=False), :]
            df2 = df2[['公开公告号', '当前申请专利权人']]
            series = df2['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            df_z = df2[['公开公告号']]
            df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一申请人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
            df_z.columns = ['公开公告号', '第一当前申请专利权人']
            df_22 = pd.DataFrame()
            for i in range(1, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
                df_l.columns = ['公开公告号', '第一申请人', '联合申请人']
                df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
            df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_22 = pd.concat([df_22['公开公告号'], df_22['第一申请人'], df_22['联合申请人'].str.strip()],
                              axis=1)  # 用strip（）删除字符串头尾多余空格
            df_22 = df_22.groupby(['第一申请人', '联合申请人'], as_index=False)['公开公告号'].count()
            df_22 = df_22.sort_values(by='公开公告号', ascending=False)
            df_22.columns = ['第一申请人', '联合申请人', '申请数量']

            nodes = []
            for i in range(len(df_11)):
                node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),"value":int(df_11.iat[i, 1])}

                nodes.append(node)

            links = []
            for i in range(len(df_22)):
                link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
                        "value": int(df_22.iat[i, 2])}
                links.append(link)

            # # 节点数据2
            # df1 = dfmb.loc[dfmb['当前申请专利权人'].str.contains(listx[1], na=False), :]
            # df1 = df1.astype({'当前申请专利权人数量': 'int'})
            # df1 = df1.loc[(df1['当前申请专利权人数量'] != 1)]
            # series = df1['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            # df_z = df1[['公开公告号']]
            # df_11 = pd.DataFrame()
            # for i in range(0, series.columns.size):
            #     df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            #     df_l.columns = ['公开公告号', '当前申请专利权人']
            #     df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
            # df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
            # df_11 = pd.concat([df_11['公开公告号'], df_11['当前申请专利权人'].str.strip()],
            #                   axis=1)  # 用strip（）删除字符串头尾多余空格
            # df_11 = df_11.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
            # df_11 = df_11.sort_values(by='公开公告号', ascending=False)
            # df_11.columns = ['当前申请专利权人', '申请数量']
            #
            # # 关系数据
            # df2 = dfmb.loc[dfmb['当前申请专利权人'].str.contains(listx[1], na=False), :]
            # df2 = df2[['公开公告号', '当前申请专利权人']]
            # series = df2['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            # df_z = df2[['公开公告号']]
            # df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一申请人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
            # df_z.columns = ['公开公告号', '第一当前申请专利权人']
            # df_22 = pd.DataFrame()
            # for i in range(1, series.columns.size):
            #     df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            #     df_l.columns = ['公开公告号', '第一申请人', '联合申请人']
            #     df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
            # df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
            # df_22 = pd.concat([df_22['公开公告号'], df_22['第一申请人'], df_22['联合申请人'].str.strip()],
            #                   axis=1)  # 用strip（）删除字符串头尾多余空格
            # df_22 = df_22.groupby(['第一申请人', '联合申请人'], as_index=False)['公开公告号'].count()
            # df_22 = df_22.sort_values(by='公开公告号', ascending=False)
            # df_22.columns = ['第一申请人', '联合申请人', '申请数量']
            #
            # nodes2 = []
            # for i in range(len(df_11)):
            #     node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),"value":int(df_11.iat[i, 1])}
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
            # df1 = dfmb.loc[dfmb['当前申请专利权人'].str.contains(listx[2], na=False), :]
            # df1 = df1.astype({'当前申请专利权人数量': 'int'})
            # df1 = df1.loc[(df1['当前申请专利权人数量'] != 1)]
            # series = df1['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            # df_z = df1[['公开公告号']]
            # df_11 = pd.DataFrame()
            # for i in range(0, series.columns.size):
            #     df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            #     df_l.columns = ['公开公告号', '当前申请专利权人']
            #     df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
            # df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
            # df_11 = pd.concat([df_11['公开公告号'], df_11['当前申请专利权人'].str.strip()],
            #                   axis=1)  # 用strip（）删除字符串头尾多余空格
            # df_11 = df_11.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
            # df_11 = df_11.sort_values(by='公开公告号', ascending=False)
            # df_11.columns = ['当前申请专利权人', '申请数量']
            #
            # # 关系数据3
            # df2 = dfmb.loc[dfmb['当前申请专利权人'].str.contains(listx[2], na=False), :]
            # df2 = df2[['公开公告号', '当前申请专利权人']]
            # series = df2['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            # df_z = df2[['公开公告号']]
            # df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一申请人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
            # df_z.columns = ['公开公告号', '第一当前申请专利权人']
            # df_22 = pd.DataFrame()
            # for i in range(1, series.columns.size):
            #     df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            #     df_l.columns = ['公开公告号', '第一申请人', '联合申请人']
            #     df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
            # df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
            # df_22 = pd.concat([df_22['公开公告号'], df_22['第一申请人'], df_22['联合申请人'].str.strip()],
            #                   axis=1)  # 用strip（）删除字符串头尾多余空格
            # df_22 = df_22.groupby(['第一申请人', '联合申请人'], as_index=False)['公开公告号'].count()
            # df_22 = df_22.sort_values(by='公开公告号', ascending=False)
            # df_22.columns = ['第一申请人', '联合申请人', '申请数量']
            #
            # nodes3 = []
            # for i in range(len(df_11)):
            #     node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),"value":int(df_11.iat[i, 1])}
            #
            #     nodes3.append(node)
            #
            # links3 = []
            # for i in range(len(df_22)):
            #     link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
            #             "value": int(df_22.iat[i, 2])}
            #     links3.append(link)
            c = (
                Graph()
                .add(listx[0],
                     nodes,
                     links,
                     repulsion=150,
                     layout="force",
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
                #      is_draggable=True,
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
                #      is_draggable= True,
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
                    ), )
                .set_series_opts(
                    itemstyle_opts=opts.ItemStyleOpts(color="rgb(80,196,143)",  # 节点颜色
                                                      border_color="rgb(245,97,111)",  # 节点边线颜色
                                                      border_width=1,  # 节点边线宽度
                                                      opacity=0.9,  # 节点透明度
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
    if biaoji!=0:
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
#联合申请人排名 圆柱
def huitu12():
    global biaoji
    def cunchupng():

        dfmb = dfm.loc[(dfm['当前申请专利权人数量'] != '-')]
        dfmb = dfmb.astype({'当前申请专利权人数量': 'int'})
        dfmb = dfmb.loc[(dfmb['当前申请专利权人数量'] != 1)]
        dfm1 = dfmb[['公开公告号', '当前申请专利权人']]
        series = dfm1['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfm1[['公开公告号']]
        dfx = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开公告号', '当前申请专利权人']
            dfx = pd.concat([dfx, df_l])  ##所有新表叠加
        dfx.dropna(inplace=True)  # 删除空数据，获得有效数据
        dfx = pd.concat([dfx['公开公告号'], dfx['当前申请专利权人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        dfx = dfx.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
        dfx = dfx.sort_values(by='公开公告号', ascending=False)
        dfx.columns = ['当前申请专利权人', '申请数量']
        dfx = dfx.head(10)
        dfx = dfx.sort_values(by='申请数量', ascending=True)
        if dfx.empty:
            biaoji=0
        else:
            # for j in range(0, len(dfx['当前申请专利权人'])):
            #     if len(dfx.iat[j, 0]) > 8:
            #         dfx.iat[j, 0] = dfx.iat[j, 0][0:7] + '...'
            #     else:
            #         dfx.iat[j, 0] = dfx.iat[j, 0]
            listx = list(dfx['当前申请专利权人'])
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
                .add(c, grid_opts=opts.GridOpts(pos_left="25%")))
            return grid

    bar_chart = cunchupng()
    if biaoji!=0:

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
#联合发明人团队情况
def huitu13():
    global biaoji
    def cunchupng():

        dfmb = dfm.loc[(dfm['发明人数量'] != '-')]
        dfmb = dfmb.astype({'发明人数量': 'int'})
        dfmb = dfmb.loc[(dfmb['发明人数量'] != 1)]
        dfm1 = dfmb[['公开公告号', '发明人']]
        series = dfm1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfm1[['公开公告号']]
        dfx = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
            df_l.columns = ['公开公告号', '发明人']
            dfx = pd.concat([dfx, df_l])  ##所有新表叠加
        dfx.dropna(inplace=True)  # 删除空数据，获得有效数据
        dfx = pd.concat([dfx['公开公告号'], dfx['发明人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        dfx = dfx.groupby('发明人', as_index=False)['公开公告号'].count()
        dfx = dfx.sort_values(by='公开公告号', ascending=False)
        dfx.columns = ['发明人', '申请数量']
        dfx = dfx.head(10)

        listx = list(dfx['发明人'])


        # 节点数据
        df1 = dfmb.loc[dfmb['发明人'].str.contains(listx[0], na=False), :]
        if df1.empty:
            biaoji=0
        else:
            df1 = df1.astype({'发明人数量': 'int'})
            df1 = df1.loc[(df1['发明人数量'] != 1)]
            series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            df_z = df1[['公开公告号']]
            df_11 = pd.DataFrame()
            for i in range(0, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
                df_l.columns = ['公开公告号', '发明人']
                df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
            df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_11 = pd.concat([df_11['公开公告号'], df_11['发明人'].str.strip()],
                              axis=1)  # 用strip（）删除字符串头尾多余空格
            df_11 = df_11.groupby('发明人', as_index=False)['公开公告号'].count()
            df_11 = df_11.sort_values(by='公开公告号', ascending=False)
            df_11.columns = ['发明人', '申请数量']

            # 关系数据
            df2 = dfmb.loc[dfmb['发明人'].str.contains(listx[0], na=False), :]
            df2 = df2[['公开公告号', '发明人']]
            series = df2['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            df_z = df2[['公开公告号']]
            df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一发明人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
            df_z.columns = ['公开公告号', '第一发明人']
            df_22 = pd.DataFrame()
            for i in range(1, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
                df_l.columns = ['公开公告号', '第一发明人', '联合发明人']
                df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
            df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_22 = pd.concat([df_22['公开公告号'], df_22['第一发明人'], df_22['联合发明人'].str.strip()],
                              axis=1)  # 用strip（）删除字符串头尾多余空格
            df_22 = df_22.groupby(['第一发明人', '联合发明人'], as_index=False)['公开公告号'].count()
            df_22 = df_22.sort_values(by='公开公告号', ascending=False)
            df_22.columns = ['第一发明人', '联合发明人', '申请数量']

            nodes = []
            for i in range(len(df_11)):
                node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),"value":int(df_11.iat[i, 1])}

                nodes.append(node)

            links = []
            for i in range(len(df_22)):
                link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
                        "value": int(df_22.iat[i, 2])}
                links.append(link)

            # 节点数据2
            df1 = dfmb.loc[dfmb['发明人'].str.contains(listx[1], na=False), :]
            df1 = df1.astype({'发明人数量': 'int'})
            df1 = df1.loc[(df1['发明人数量'] != 1)]
            series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            df_z = df1[['公开公告号']]
            df_11 = pd.DataFrame()
            for i in range(0, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
                df_l.columns = ['公开公告号', '发明人']
                df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
            df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_11 = pd.concat([df_11['公开公告号'], df_11['发明人'].str.strip()],
                              axis=1)  # 用strip（）删除字符串头尾多余空格
            df_11 = df_11.groupby('发明人', as_index=False)['公开公告号'].count()
            df_11 = df_11.sort_values(by='公开公告号', ascending=False)
            df_11.columns = ['发明人', '申请数量']

            # 关系数据
            df2 = dfmb.loc[dfmb['发明人'].str.contains(listx[1], na=False), :]
            df2 = df2[['公开公告号', '发明人']]
            series = df2['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            df_z = df2[['公开公告号']]
            df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一发明人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
            df_z.columns = ['公开公告号', '第一发明人']
            df_22 = pd.DataFrame()
            for i in range(1, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
                df_l.columns = ['公开公告号', '第一发明人', '联合发明人']
                df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
            df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_22 = pd.concat([df_22['公开公告号'], df_22['第一发明人'], df_22['联合发明人'].str.strip()],
                              axis=1)  # 用strip（）删除字符串头尾多余空格
            df_22 = df_22.groupby(['第一发明人', '联合发明人'], as_index=False)['公开公告号'].count()
            df_22 = df_22.sort_values(by='公开公告号', ascending=False)
            df_22.columns = ['第一发明人', '联合发明人', '申请数量']

            nodes2 = []
            for i in range(len(df_11)):
                node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),"value":int(df_11.iat[i, 1])}

                nodes2.append(node)

            links2 = []
            for i in range(len(df_22)):
                link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
                        "value": int(df_22.iat[i, 2])}
                links2.append(link)

            # 节点数据3
            df1 = dfmb.loc[dfmb['发明人'].str.contains(listx[2], na=False), :]
            df1 = df1.astype({'发明人数量': 'int'})
            df1 = df1.loc[(df1['发明人数量'] != 1)]
            series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            df_z = df1[['公开公告号']]
            df_11 = pd.DataFrame()
            for i in range(0, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
                df_l.columns = ['公开公告号', '发明人']
                df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
            df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_11 = pd.concat([df_11['公开公告号'], df_11['发明人'].str.strip()],
                              axis=1)  # 用strip（）删除字符串头尾多余空格
            df_11 = df_11.groupby('发明人', as_index=False)['公开公告号'].count()
            df_11 = df_11.sort_values(by='公开公告号', ascending=False)
            df_11.columns = ['发明人', '申请数量']

            # 关系数据3
            df2 = dfmb.loc[dfmb['发明人'].str.contains(listx[2], na=False), :]
            df2 = df2[['公开公告号', '发明人']]
            series = df2['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
            df_z = df2[['公开公告号']]
            df_z = pd.concat([df_z, series[0]], axis=1)  # 这里提取第一发明人的时候 未去除空格 会导致连接数据找不到中心节点 无法显示连接关系
            df_z.columns = ['公开公告号', '第一发明人']
            df_22 = pd.DataFrame()
            for i in range(1, series.columns.size):
                df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
                df_l.columns = ['公开公告号', '第一发明人', '联合发明人']
                df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
            df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
            df_22 = pd.concat([df_22['公开公告号'], df_22['第一发明人'], df_22['联合发明人'].str.strip()],
                              axis=1)  # 用strip（）删除字符串头尾多余空格
            df_22 = df_22.groupby(['第一发明人', '联合发明人'], as_index=False)['公开公告号'].count()
            df_22 = df_22.sort_values(by='公开公告号', ascending=False)
            df_22.columns = ['第一发明人', '联合发明人', '申请数量']

            nodes3 = []
            for i in range(len(df_11)):
                node = {"name": str(df_11.iat[i, 0]).strip(), "symbolSize": int(df_11.iat[i, 1]),"value":int(df_11.iat[i, 1])}

                nodes3.append(node)

            links3 = []
            for i in range(len(df_22)):
                link = {"source": str(df_22.iat[i, 0]).strip(), "target": str(df_22.iat[i, 1]).strip(),
                        "value": int(df_22.iat[i, 2])}
                links3.append(link)
            c = (
                Graph(init_opts=opts.InitOpts(
                        bg_color='#FFFFFF',))
                .add(listx[0],
                     nodes,
                     links,
                     repulsion=150,
                     layout="force",
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
                        feature=toolbox_opts3['feature']
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
                                                      opacity=0.9,  # 节点透明度
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
    if biaoji!=0:
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
#联合发明人团队发明人排名
def huitu14():
    global biaoji
    def cunchupng():

        dfmb = dfm.loc[(dfm['发明人数量'] != '-')]
        dfmb = dfmb.astype({'发明人数量': 'int'})
        dfmb = dfmb.loc[(dfmb['发明人数量'] != 1)]
        dfm1 = dfmb[['公开公告号', '发明人']]
        series = dfm1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = dfm1[['公开公告号']]
        dfx = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列发明人数据结合成新表
            df_l.columns = ['公开公告号', '发明人']
            dfx = pd.concat([dfx, df_l])  ##所有新表叠加
        dfx.dropna(inplace=True)  # 删除空数据，获得有效数据
        dfx = pd.concat([dfx['公开公告号'], dfx['发明人'].str.strip()], axis=1)  # 用strip（）删除字符串头尾多余空格
        dfx = dfx.groupby('发明人', as_index=False)['公开公告号'].count()
        dfx = dfx.sort_values(by='公开公告号', ascending=False)
        dfx.columns = ['发明人', '申请数量']
        dfx = dfx.head(10)
        dfx = dfx.sort_values(by='申请数量', ascending=True)
        if dfx.empty:
            biaoji=0
        else:

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
                .add(c, grid_opts=opts.GridOpts(pos_left="25%")))
            return grid

    bar_chart = cunchupng()
    if biaoji!=0:
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
#发明人词云图
def huitu15():
    global document
    def cunchupng():
        dfmb=dfm
        df1 = dfmb[['公开公告号', '发明人']]
        df1 = df1.loc[(df1['发明人'] != '-')]

        series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
        df_z = df1[['公开公告号']]
        df_11 = pd.DataFrame()
        for i in range(0, series.columns.size):
            df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
            df_l.columns = ['公开公告号', '发明人']
            df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
        df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
        df_11 = pd.concat([df_11['公开公告号'], df_11['发明人'].str.strip()],
                          axis=1)  # 用strip（）删除字符串头尾多余空格

        df_11 = df_11.groupby('发明人', as_index=False)['公开公告号'].count()
        df_11 = df_11.sort_values(by='公开公告号', ascending=False)
        df_11.columns = ['发明人', '申请数量']
        df1=df_11[['发明人', '申请数量']]
        if df1.empty:
            biaoji=0
        else:

            listx = list(df1['发明人'])
            listy = list(df1['申请数量'])
            xmax = max(listy)
            xmin = min(listy)

            data_pair = [list(z) for z in zip(listx, listy)]
            data_pair.sort(key=lambda x: x[1], reverse=True)

            c = (
                WordCloud(init_opts=opts.InitOpts(
                        bg_color='#FFFFFF',

                )
                )
                    .add(series_name="发明人",
                         data_pair=data_pair,
                         shape="circle",
                         # word_gap=40,
                         # word_size_range=(xmin,xmax)
                         )
                .set_global_opts(
                    toolbox_opts=opts.ToolboxOpts(
                        orient='horizontal',  # 工具箱的方向，可选值为 'horizontal' 或 'vertical'
                        item_size=15,
                        item_gap=5,
                        feature=toolbox_opts3['feature']
                    ),)
            )
            return c

    bar_chart = cunchupng()
    if biaoji!=0:
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
#专利类型 趋势 时间轴
def huitu16():
    global biaoji
    def cunchupng():
        biaoji1=0
        dfmb = dfm.astype({'申请年': 'str'})
        tl = Timeline()
        for i in range(0, len(nianfen10)):
            df1 = dfmb.loc[(dfmb['申请年'] == nianfen10[i])]
            df1 = df1[['专利类型', '公开公告号']]
            df1 = df1.loc[(df1['专利类型'] != '-')]
            df1 = df1.groupby('专利类型', as_index=False)['公开公告号'].count()
            df1 = df1.sort_values(by='公开公告号', ascending=False)
            df1.columns = ['专利类型', '申请数量']
            if df1.empty:
                biaoji1 = biaoji1+1
            else:
                listx = list(df1['专利类型'])
                listy = list(df1['申请数量'])
                data_pair = [list(z) for z in zip(listx, listy)]
                data_pair.sort(key=lambda x: x[0], reverse=True)  # 排序


                pie = (
                    Pie(init_opts=opts.InitOpts(
                        bg_color='#FFFFFF',
                    ))
                    .add(
                        nianfen10[i],
                        data_pair,
                        rosetype="radius",
                        radius=["40%", "65%"],
                        center=["50%", "45%"],
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
                        title_opts=opts.TitleOpts(title="{}年专利类型构成".format(nianfen10[i]),  # 标题
                                                               pos_top='2%',  # 位置
                                                               pos_left='center',  # 位置
                                                               title_textstyle_opts=opts.TextStyleOpts(font_size=30), ),
                                     # 字体大小
                                     legend_opts=opts.LegendOpts(
                                         type_='plain',
                                         is_show=True,
                                         pos_right='right',  # 右边
                                         orient='vertical',
                                         pos_top='15%',  # 距离上边界15%
                                         item_width=37,  # 图例宽
                                         item_height=21,  # 图例高
                                         background_color="transparent",
                                         border_color="transparent",
                                         textstyle_opts=opts.TextStyleOpts(font_size=20, font_style='normal',
                                                                           font_weight='bold', ))
                                     )
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
                tl.add(pie, "{}年".format(nianfen10[i]))
            if biaoji1!=0:
                biaoji=0
        return tl

    bar_chart = cunchupng()
    if biaoji!=0:
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
#受理局排名趋势 时间轴
def huitu17():
    global biaoji
    def cunchupng():
        dfmb = dfm.astype({'申请年': 'str'})
        tl = Timeline()
        for i in range(0, len(nianfen10)):
            df1 = dfmb.loc[(dfmb['申请年'] == nianfen10[i])]
            df1 = df1[['受理局', '公开公告号']]
            df1 = df1.groupby('受理局', as_index=False)['公开公告号'].count()
            df1 = df1.sort_values(by='公开公告号', ascending=False)
            df1=df1.head(10)
            df1 = df1.sort_values(by='公开公告号', ascending=True)

            listx = list(df1['受理局'])
            listy = list(df1['公开公告号'])

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
                    title_opts=opts.TitleOpts(title="{}年专利受理局排名".format(nianfen10[i]),  # 标题
                                              pos_top='1%',  # 位置
                                              pos_left='center',  # 位置
                                              title_textstyle_opts=opts.TextStyleOpts(font_size=30), ),
                    xaxis_opts=opts.AxisOpts(
                        # type_="category",  # 坐标轴类型
                        name='申请数量',  # 坐标轴名字
                        name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                        axislabel_opts=opts.LabelOpts(

                            font_size=15,
                            font_style='normal',
                            font_weight='bold',
                        )
                    ),
                    yaxis_opts=opts.AxisOpts(

                        # type_="value",
                        name='受理局',  # 坐标轴名字
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
            tl.add(grid, "{}年".format(nianfen10[i]))
        return tl

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
##申请人排名趋势 时间轴
def huitu18():
    global biaoji
    def cunchupng():
        biaoji1 = 0
        dfmb = dfm.astype({'申请年': 'str'})
        tl = Timeline()
        for i in range(0, len(nianfen10)):

            df1 = dfmb.loc[(dfmb['申请年'] == nianfen10[i])]
            if df1.empty:
                biaoji1 = biaoji1+1
            else:
                df1 = df1[['当前申请专利权人', '公开公告号']]
                series = df1['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
                df_z = df1[['公开公告号']]
                df_11 = pd.DataFrame()
                for j in range(0, series.columns.size):
                    df_l = pd.concat([df_z, series[j]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
                    df_l.columns = ['公开公告号', '当前申请专利权人']
                    df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
                df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
                df_11 = pd.concat([df_11['公开公告号'], df_11['当前申请专利权人'].str.strip()],
                                  axis=1)  # 用strip（）删除字符串头尾多余空格
                df_11 = df_11.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
                df_11 = df_11.sort_values(by='公开公告号', ascending=False)
                df_11.columns = ['当前申请专利权人', '申请数量']
                df1=df_11.head(10)
                df1 = df1.sort_values(by='申请数量', ascending=True)
                listx = list(df1['当前申请专利权人'])
                listy = list(df1['申请数量'])

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
                        title_opts=opts.TitleOpts(title="{}年专利申请人排名".format(nianfen10[i]),  # 标题
                                                  pos_top='1%',  # 位置
                                                  pos_left='center',  # 位置
                                                  title_textstyle_opts=opts.TextStyleOpts(font_size=30), ),
                        xaxis_opts=opts.AxisOpts(
                            # type_="category",  # 坐标轴类型
                            name='申请数量',  # 坐标轴名字
                            name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                            axislabel_opts=opts.LabelOpts(

                                font_size=15,
                                font_style='normal',
                                font_weight='bold',
                            )
                        ),
                        yaxis_opts=opts.AxisOpts(

                            # type_="value",
                            name='当前申请专利权人',  # 坐标轴名字
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
                    .add(bar, grid_opts=opts.GridOpts(pos_left="30%")))

                tl.add(grid, "{}年".format(nianfen10[i]))
            if biaoji1!=0:
                biaoji=0
        return tl

    bar_chart = cunchupng()
    if biaoji!=0:
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
#发明人排名趋势 时间轴
def huitu19():
    global biaoji
    def cunchupng():
        biaoji1=0
        dfmb = dfm.astype({'申请年': 'str'})
        tl = Timeline()
        for i in range(0, len(nianfen10)):
            df1 = dfmb.loc[(dfmb['申请年'] == nianfen10[i])]
            if df1.empty:
                biaoji1 = biaoji1+1
            else:

                df1 = df1[['发明人', '公开公告号']]
                df1 = df1.loc[(df1['发明人'] != '-')]
                series = df1['发明人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
                df_z = df1[['公开公告号']]
                df_11 = pd.DataFrame()
                for j in range(0, series.columns.size):
                    df_l = pd.concat([df_z, series[j]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
                    df_l.columns = ['公开公告号', '发明人']
                    df_11 = pd.concat([df_11, df_l])  ##所有新表叠加
                df_11.dropna(inplace=True)  # 删除空数据，获得有效数据
                df_11 = pd.concat([df_11['公开公告号'], df_11['发明人'].str.strip()],
                                  axis=1)  # 用strip（）删除字符串头尾多余空格
                df_11 = df_11.groupby('发明人', as_index=False)['公开公告号'].count()
                df_11 = df_11.sort_values(by='公开公告号', ascending=False)
                df_11.columns = ['发明人', '申请数量']

                df1 = df_11.head(10)
                df1 = df1.sort_values(by='申请数量', ascending=True)

                listx = list(df1['发明人'])
                listy = list(df1['申请数量'])

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
                        title_opts=opts.TitleOpts(title="{}年专利发明人排名".format(nianfen10[i]),  # 标题
                                                  pos_top='1%',  # 位置
                                                  pos_left='center',  # 位置
                                                  title_textstyle_opts=opts.TextStyleOpts(font_size=30), ),
                        xaxis_opts=opts.AxisOpts(
                            # type_="category",  # 坐标轴类型
                            name='申请数量',  # 坐标轴名字
                            name_location="end",  # 坐标轴位置'start', 'middle' 或者 'center','end'
                            axislabel_opts=opts.LabelOpts(

                                font_size=15,
                                font_style='normal',
                                font_weight='bold',
                            )
                        ),
                        yaxis_opts=opts.AxisOpts(

                            # type_="value",
                            name='发明人',  # 坐标轴名字
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
                    .add(bar, grid_opts=opts.GridOpts(pos_left="25%")))
                tl.add(grid, "{}年".format(nianfen10[i]))
            if biaoji1!=0:
                biaoji=0
        return tl

    bar_chart = cunchupng()
    if biaoji != 0:
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
if dfm.empty:
    st.write('该数据范围无相应图表！')
else:

    st.subheader("""申请趋势""")
    st.write('该图表展示了近20年的专利申请趋势。图表包括了总申请量的折线图以及有效、无效和审中专利的簇型柱状图。'
             '折线图显示了总申请量随时间的变化趋势。通过观察折线的上升或下降趋势，可以得出专利申请的整体趋势。'
             '如果折线呈现上升趋势，表示专利申请量逐年增加，可能反映了创新活动的增加或对知识产权保护的关注度提高。'
             '相反，如果折线呈下降趋势，可能表示专利申请量逐年减少，可能源于创新活动的减少或其他因素导致的减少对知识产权的申请。'
             '簇型柱状图展示了有效、无效和审中专利在不同年份的分布情况。每个柱状图表示一年的专利申请情况，并根据专利的状态进行颜色区分。'
             '通过比较不同柱状图之间的高度和颜色分布，可以得出不同专利状态的相对趋势。'
             '该图表揭示了专利申请趋势和专利状态的变化情况。通过观察总申请量的变化，可以了解到创新活动的整体趋势和对知识产权的关注程度。'
             '簇型柱状图则提供了不同专利状态（有效、无效和审中）的比较和分布情况，帮助我们了解专利的审批和有效性情况。'
             '可用于研究专利申请的趋势、知识产权保护策略以及创新活动的变化等方面。')
    huitu1()

    st.subheader("""五局流向""")
    st.write('通过观察圆的大小，可以了解到各个地区的专利数量的相对差异。较大的圆表示该地区拥有更多的专利数量，而较小的圆表示专利数量较少。'
             '通过比较圆的大小，可以看出各个地区在技术目标地区的专利数量贡献程度。此外，圆的颜色也提供了额外的信息。不同颜色的圆表示不同的技术目标地区。'
             '通过观察圆的颜色分布，可以了解各个技术目标地区的专利来源地区分布情况。该图表揭示了不同地区之间的专利流向和技术合作情况。'
             '通过观察圆的大小和颜色分布，可以了解到哪些地区在专利数量上具有优势，以及各个地区之间的技术合作状况。可用于分析技术转移、知识合作以及技术创新的全球趋势。')
    huitu2()
    print(biaoji)
    biaoji=1

    st.subheader("""专利受理局排名变化""")
    st.write('该图展示了专利受理局的排名情况，并以轮播的形式展示了近10年的变化。每个图表示一年的数据。通过观察每个图之间柱状条的变化，可以了解到近10年来专利受理局排名的变化趋势。'
             '如果某个受理局的柱状条在连续几年中保持较高的位置，表示该受理局的排名相对稳定。'
             '相反，如果某个受理局的柱状条在不同年份中出现较大的波动，表示该受理局的排名变动较大。'
             '这种类型的图表可以用于比较不同专利受理局之间的实力和影响力，以及了解受理局在专利审批中的角色和地位。'
             '同时，通过观察近10年的变化，可以了解到专利申请和受理的趋势以及受理局之间的竞争和变化')
    huitu17()
    print(biaoji)
    biaoji = 1

    st.subheader("""地区分布""")
    st.write('该地图展示了不同地区的专利数量分布情况。每个地区的专利数量用颜色填充区分，红色表示专利数量最高，黄色表示专利数量居中，灰色表示专利数量最低。'
             '颜色填充的程度反映了各地区专利数量的相对差异。红色填充的地区表示专利数量较多，可能代表着创新活动较为活跃，专利保护较为重视。'
             '黄色填充的地区表示专利数量适中，可能表明该地区在创新和专利申请方面存在一定程度的活动。灰色填充的地区表示专利数量较少，可能说明该地区的创新活动和专利保护相对较低。'
             '通过观察地图上不同地区的颜色分布，可以比较各地区之间的专利数量差异。颜色填充的深浅程度可以反映出不同地区之间专利活动的相对强度。'
             '该图表可以用于分析全球范围内的创新热点地区、知识产权保护程度以及专利申请的地域分布。同时，通过观察专利数量的分布情况，可以了解不同地区的创新活动水平、科技发展情况以及知识产权的重要性。')
    huitu3()
    print(biaoji)
    biaoji = 1

    st.subheader("""专利类型构成变化""")
    st.write('每个饼图表示一年的数据，将专利类型按照比例划分成不同的扇形区域。每个扇形区域的大小表示该专利类型在总专利数量中的比例。'
             '通过观察每个图之间扇形区域的变化，可以了解到近10年来专利类型构成的变化趋势。'
             '如果某个专利类型的扇形区域在连续几年中保持相对稳定的大小，表示该专利类型在这段时间内占据了相对稳定的比例。'
             '相反，如果某个专利类型的扇形区域在不同年份中出现较大的变化，表示该专利类型在这段时间内的比例发生了明显的变动。'
             '该图表可用于了解专利类型的变化趋势、技术创新的方向以及不同类型专利的相对重要性。'
             '通过观察近10年的数据变化，可以了解到专利类型在不同年份中的相对增长或下降情况，以及技术领域的发展方向。')
    huitu16()
    print(biaoji)
    biaoji = 1

    st.subheader("""专利类型构成""")
    st.write('饼图的圆环区域代表了总体专利数量。每个专利类型在饼图中以扇形区域的形式表示，并且每个扇形区域的大小反映了该专利类型在总体专利数量中所占比例的大小。'
             '通过观察每个专利类型扇形区域的大小，可以了解到不同专利类型在总体中的相对重要性。如果某个专利类型的扇形区域较大，表示该专利类型在总体中所占比例较高，具有较大的影响力。'
             '相反，如果某个专利类型的扇形区域较小，表示该专利类型在总体中所占比例较低，具有较小的影响力。该图可以用于展示总体专利类型的构成情况，帮助我们了解不同专利类型的相对重要性和影响力。'
             '它可以用于研究专利领域的整体分布情况，揭示专利类型的偏好和技术创新的方向。通过观察饼图中不同扇形区域的比例关系，可以洞察专利申请者和创新者的兴趣和趋势。')
    huitu7()
    print(biaoji)
    biaoji = 1

    st.subheader("""简单法律状态构成""")
    st.write('饼图的圆环区域代表了总体专利的数量。每个简单法律状态在饼图中以扇形区域的形式表示，并且每个扇形区域的大小反映了该法律状态在总体专利数量中所占比例的大小。'
             '通过观察每个简单法律状态扇形区域的大小，可以了解不同法律状态在总体中的相对分布。如果某个简单法律状态的扇形区域较大，表示该法律状态在总体中所占比例较高，相应的专利具有该法律状态的较高比例。'
             '相反，如果某个简单法律状态的扇形区域较小，表示该法律状态在总体中所占比例较低，相应的专利数量较少。该图可以用于展示总体专利的简单法律状态构成情况，帮助我们了解不同法律状态的分布情况和比例关系。'
             '它可以用于研究专利的法律状态变化、知识产权保护情况和专利审批的进展。通过观察饼图中不同扇形区域的比例关系，可以洞察专利的法律保护状况以及专利申请者在不同法律状态下的选择策略。')
    huitu8()
    print(biaoji)
    biaoji = 1

    st.subheader("""专利运营情况""")
    st.write('该图表展示了近20年专利运营情况，包括权力转移、质押和许可。不同颜色区分不同的运营方式，圆的大小表示专利数量。'
             '通过观察圆形的大小和颜色分布，可以比较不同运营方式在不同年份中的专利数量变化。'
             '如果某个运营方式的圆形在连续几年中保持较大的大小和相对稳定的颜色，表示该运营方式在这段时间内具有较高的专利数量。'
             '相反，如果某个运营方式的圆形在不同年份中出现较大的变化，表示该运营方式的专利数量有较大的波动。'
             '该图表可以用于分析专利的运营方式及其变化趋势，帮助了解专利的商业利用和价值实现方式。'
             '通过观察不同运营方式的圆形大小和颜色分布，可以了解到各个运营方式的相对重要性和在不同年份的演变情况。这有助于评估专利的商业价值和知识产权的管理策略。')
    huitu9()
    print(biaoji)
    biaoji = 1

    st.subheader("""技术发展趋势""")
    st.write('该图展示了近20年来排名前五的IPC分类号专利的申请趋势。每条折线代表一个IPC分类号，表示该IPC分类号在近20年中的专利申请数量或申请趋势。'
             '不同的IPC分类号用不同的颜色来区分。通过观察每条折线的趋势，可以了解到排名前五的IPC分类号在近20年中的专利申请情况。'
             '如果某个IPC分类号的折线呈现逐年上升的趋势，表示该领域的专利申请数量在增加，可能代表该技术领域的发展较为活跃。'
             '相反，如果某个IPC分类号的折线呈现逐年下降或波动不定的趋势，表示该领域的专利申请数量可能在减少或变化不大。'
             '该图表可以用于研究特定技术领域的发展趋势，帮助了解不同IPC分类号的专利申请情况及其变化。通过观察近20年的数据变化，可以揭示出技术领域的发展方向和热点，为科技创新和专利战略提供参考。')
    huitu10()
    print(biaoji)
    biaoji = 1

    st.subheader("""专利申请人排名变化""")
    st.write('该柱状图以轮播的形式展示了近10年专利申请人的排名变化情况。每个图表示一年的数据，反映了每个专利申请人在相应年份内的专利申请数量。'
             '柱状图的长度表示专利申请数量的大小，较长的柱状图表示专利申请数量较多，排名靠前。通过观察每个图表中的柱状图排列顺序和长度变化，可以了解近10年专利申请人排名的变化趋势。'
             '如果某个专利申请人的柱状图在多个年份中保持较长的长度和相对稳定的位置，表示该专利申请人在这段时间内一直保持较高的申请数量。'
             '相反，如果某个专利申请人的柱状图在不同年份中出现较大的变化，表示该申请人的专利申请数量有较大的波动，排名可能发生了变化。'
             '这种类型的图表可以用于分析专利申请人的活跃程度和在特定时间段内的排名情况。通过观察柱状图的变化，可以了解到专利申请人的发展趋势、创新实力以及在技术领域中的地位。'
             '这对于评估专利申请人的研发实力、创新能力以及技术竞争态势具有重要意义。')
    huitu18()
    print(biaoji)
    biaoji = 1

    st.subheader("""申请人排名""")
    st.write('该柱状图展示了总体专利申请人的排名情况。每个柱体代表一个专利申请人，柱体的长度表示该专利申请人的专利申请数量。较长的柱体表示专利申请数量较多，排名靠前。'
             '通过观察柱状图的排列顺序和长度，可以了解总体专利申请人的排名情况。排名靠前的柱状图表示专利申请数量较多，排名较高，反之排名靠后的柱状图表示专利申请数量较少。'
             '该图表可以用于分析总体专利申请人的活跃程度和在整体专利申请中的排名情况。通过观察柱状图的变化，可以了解到哪些专利申请人在整体中申请数量较多，具有较高的创新实力和影响力。'
             '这有助于评估专利申请人的研发实力、创新能力以及在技术领域中的地位。同时，该图表也可以用于比较不同专利申请人之间的差距，揭示技术竞争态势和创新活动的重点领域。')
    huitu4()
    print(biaoji)
    biaoji = 1

    st.subheader("""协同申请趋势""")
    st.write('该图展示了协同专利的申请趋势。折线表示协同专利申请数量随时间的变化趋势，面积图则填充了折线和X轴之间的区域。'
             '通过观察折线的趋势和面积图的填充情况，可以了解到协同专利申请的整体趋势。如果折线逐年上升，并且面积图逐渐扩大，表示协同专利申请数量不断增加，表明协同创新活动在相关领域中得到了更广泛的应用。'
             '相反，如果折线呈现下降或波动的趋势，并且面积图逐渐减小，表示协同专利申请数量在减少，可能意味着协同创新活动的参与程度有所下降。该图表可以用于分析协同创新活动的发展趋势和重要性。'
             '通过观察折线和面积图的变化，可以了解到协同创新的趋势以及不同时间段协同专利申请的数量变化。这有助于评估协同创新的影响力、合作伙伴关系以及技术交流的程度。')
    huitu5()
    print(biaoji)
    biaoji = 1

    st.subheader("""协同申请前三的申请人联合情况""")
    st.write('该图展示了排名前三的协同申请人之间的申请关系。每个申请人用一个圆形表示，圆的大小表示该申请人的申请数量，颜色则用于区分排名前三的申请人。'
             '连线表示申请人之间的关系。如果两个申请人之间有连线，表示它们之间存在协同申请关系。通过观察圆形的大小、颜色以及连线的连接情况，可以了解每组的协同申请人之间的关系。'
             '该图表可以用于分析协同申请人之间的合作关系和协同创新活动。通过观察圆形的大小、颜色以及连线的模式，可以了解到协同申请人的主导地位、合作伙伴关系以及协同创新的程度。'
             '这有助于评估协同创新活动的影响力、合作模式以及技术交流的程度，为进一步推动协同创新提供参考。')
    huitu11()
    print(biaoji)
    biaoji = 1

    st.subheader("""协同申请的申请人排名""")
    st.write('该柱状图展示了协同专利申请人的排名情况。每个柱体代表一个协同专利申请人，柱体的长度表示该协同专利申请人的专利申请数量。较长的柱体表示专利申请数量较多，排名靠前。'
             '通过观察柱体的排列顺序和长度，可以了解协同专利申请人的排名情况。排名靠前的柱状图表示专利申请数量较多，排名较高，反之排名靠后的柱状图表示专利申请数量较少。'
             '这该图表可以用于分析协同创新活动中的专利申请人的活跃程度和在协同专利申请中的排名情况。通过观察柱状图的变化，可以了解到哪些协同专利申请人在协同创新活动中的贡献较大，具有较高的创新实力和影响力。'
             '这有助于评估协同创新活动中的合作伙伴关系、创新能力以及技术交流的程度。同时，该图表还可以用于比较不同协同专利申请人之间的差距，揭示协同创新活动的核心参与者和主导地位。')
    huitu12()
    print(biaoji)
    biaoji = 1

    st.subheader("""专利发明人排名变化""")
    st.write('该柱状图以轮播的形式展示了近10年专利发明人的排名变化情况。每个图表示一年的数据。每个图表中的柱体反映了每个专利发明人在相应年份内的专利数量。'
             '柱体的长度表示专利数量的大小，较长的柱体表示专利数量较多，排名靠前。通过观察每个图表中的柱体排列顺序和长度变化，可以了解近10年专利发明人排名的变化趋势。'
             '如果某个专利发明人的柱体在多个年份中保持较长的长度和相对稳定的位置，表示该专利发明人在这段时间内一直保持较高的发明数量。'
             '相反，如果某个专利发明人的柱体在不同年份中出现较大的变化，表示该发明人的专利数量有较大的波动，排名可能发生了变化。'
             '这种类型的图表可以用于分析专利发明人的活跃程度和在特定时间段内的排名情况。通过观察柱状图的变化，可以了解到专利发明人的发展趋势、创新实力以及在技术领域中的地位。'
             '这对于评估专利发明人的创新能力、研发实力以及技术竞争态势具有重要意义。同时，该图表也可以用于比较不同发明人之间的差距，揭示创新活动的重点领域和核心发明人。')
    huitu19()
    print(biaoji)
    biaoji = 1
    # st.subheader("""专利发明人分布""")
    # st.write('该词云图展示了专利发明人的分布情况，词云图中的每个词汇代表一个发明人的名称，词汇的显示大小反映了该发明人的专利申请数量的多少。'
    #          '显示较大的词汇表示该发明人具有较多的专利申请数量，显示较小的词汇则表示该发明人的专利申请数量较少。'
    #          '通过观察词云图中词汇的大小和分布情况，可以了解到专利发明人的数量分布以及在专利申请中的重要性。'
    #          '较大的词汇代表专利申请数量较多的发明人，可能是该领域的专家或核心创新者。相反，较小的词汇则代表专利申请数量较少的发明人，可能是新兴的创新者或者在该领域中的边缘角色。'
    #          '该图表可以用于呈现专利发明人的整体分布情况，为研究专利创新活动中的人员参与和合作关系提供参考。通过观察词云图，可以快速了解到哪些发明人在专利申请中起到重要的作用，以及整体专利申请人群的数量分布情况。'
    #          '这有助于评估专利创新活动的核心人员、合作伙伴关系以及技术交流的程度。')
    # huitu15()
    st.subheader("""协同申请的发明人联合情况""")
    st.write('该关系图展示了排名第一的协同申请发明人的发明团队关系。每个申请人用一个圆形表示，圆的大小表示该申请人的申请数量，较大的圆形表示申请数量较多。'
             '连线表示申请人之间的关系。通过观察圆形的大小和连线的连接情况，可以了解排名第一的协同申请发明人的发明团队关系。较大的圆形代表申请数量较多的申请人，而连线则表示不同申请人之间的合作关系。'
             '该图表可以用于分析协同创新活动中的发明团队关系和协同创新活动的组织结构。通过观察圆形的大小、连线的模式以及团队内外的连接情况，可以了解到排名第一的协同申请发明人在发明团队中的地位、'
             '合作伙伴关系以及协同创新的程度。这有助于评估协同创新活动的核心团队、合作模式以及技术交流的程度，为进一步推动协同创新提供参考。')
    huitu13()

    st.subheader("""协同申请的发明人排名""")
    st.write('该柱状图展示了协同专利发明人的排名情况。每个柱体代表一个协同专利发明人，柱体的长度表示该发明人的协同专利申请数量。较长的柱体表示专利申请数量较多，排名靠前。'
             '通过观察柱体的排列顺序和长度，可以了解协同专利发明人的排名情况。排名靠前的柱体表示专利申请数量较多，排名较高，反之排名靠后的柱状图表示专利申请数量较少。'
             '该图表可以用于分析协同创新活动中的专利发明人的活跃程度和在协同专利申请中的排名情况。通过观察柱状图的变化，可以了解到哪些协同专利发明人在协同创新活动中的贡献较大，具有较高的创新实力和影响力。'
             '这有助于评估协同创新活动中的合作伙伴关系、创新能力以及技术交流的程度。同时，该图表还可以用于比较不同协同专利发明人之间的差距，揭示协同创新活动的核心参与者和主导地位。')
    huitu14()
#气球
st.balloons()
#雪花
st.snow()