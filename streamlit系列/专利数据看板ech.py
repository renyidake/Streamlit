import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
import random
import matplotlib as mpl
from pyecharts import options as opts
from pyecharts.charts import Line, Grid,Bar,PictorialBar,Pie,Funnel,Scatter,Map,Geo,EffectScatter,Gauge,Polar,Radar,HeatMap,Graph,WordCloud
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
wuju=['中国','美国','日本','韩国','欧洲专利局']
fusheng='浙江'
dishi='台州'


#侧边栏初始状态为折叠 streamlit 页面布局为 宽
st.set_page_config(initial_sidebar_state='collapsed',layout='wide')
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
##全球专利发展趋势分析
def huitu1():
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
                    font_style='normal',
                    font_weight='bold',
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
                y_axis=listy2, )
            .add_yaxis(
                series_name='无效',
                y_axis=listy3, )
            .add_yaxis(
                series_name='审中',
                y_axis=listy4, )
            .set_colors(
                ["rgb(54,133,254)", "rgb(245,97,111)", "rgb(80,196,143)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
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
                    pos_right='center',  # 右边
                    orient='horizontal',
                    pos_bottom='bottom',
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
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
        dfmb=dfm
        df1 = dfmb.query('受理局 in %s ' % wuju)
        if df1.empty:
            st.write('该数据范围无相应图表！')
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
            print(df1)

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
            print(df2)
            print(df3)
            print(df4)
            print(df5)
            print(df6)

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
                    ),
                )
                .set_series_opts(
                    label_opts=opts.LabelOpts(
                        is_show=True,
                        position="right",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                    ),  # 标签配置项
                )
            )
            return c
    # 创建图表
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
##全球 地区分布分析
def huitu3():
    def cunchupng() -> map:
        dfmb=dfm
        df1 = dfmb[['受理局', '公开公告号']]
        df1 = df1.groupby('受理局', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='公开公告号', ascending=False)
        # df1=df1.head(10)
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

def huitu4():
    def cunchupng():
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
                label_opts=opts.LabelOpts(is_show=True, position='right',font_size=15,#字体大小
                    font_weight= 'bold'),
                symbol_size=18,
                symbol_repeat="fixed",
                symbol_offset=[0, 0],
                is_symbol_clip=True,
                symbol=SymbolType.ROUND_RECT,
            )
            .reversal_axis()
            .set_global_opts(
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
##协同申请趋势
def huitu5():
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
        print(df1)
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
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
                ),  # 标签配置项

                linestyle_opts=opts.LineStyleOpts(
                    width=5,
                    type_="solid",
                ),  # 线条配置
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            )
            .set_global_opts(
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
    def cunchupng():
        dfmb = dfm
        df1 = dfmb[['专利类型', '公开公告号']]
        df1 = df1.loc[(df1['专利类型'] != '-')]
        df1 = df1.groupby('专利类型', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='公开公告号', ascending=False)
        df1.columns = ['专利类型', '申请数量']
        df1 = df1.head(5)
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
                center=["50%", "45%"],
            )
            .set_colors(
                ["rgb(80,196,143)", "rgb(245,97,111)", "rgb(54,133,254)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    type_='plain',
                    is_show=True,
                    pos_bottom='10%',
                    orient='horizontal',
                    item_width=50,
                    item_height=28,
                    textstyle_opts=opts.TextStyleOpts(font_size=30, font_style='normal', font_weight='bold', )))
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{d}%",
                    font_size=30,
                    font_style='normal',
                    font_weight='bold', ))
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
##简单法律状态构成
def huitu8():
    def cunchupng():
        dfmb = dfm
        df1 = dfmb[['简单法律状态', '公开公告号']]
        df1 = df1.groupby('简单法律状态', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='公开公告号', ascending=False)
        df1.columns = ['简单法律状态', '申请数量']
        print(df1)
        if len(df1['简单法律状态']) >=5:
            df1 = df1.head(5)
            print(df1)
        else:
            df1= df1.head(len(df1['简单法律状态']))
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
                center=["50%", "45%"],
                rosetype="radius",
            )
            .set_colors(
                ["rgb(80,196,143)", "rgb(245,97,111)", "rgb(54,133,254)", "rgb(38,204,216)", "rgb(153,119,239)",
                 "rgb(247,177,63)", "rgb(249,226,100)", "rgb(244,122,117)", "rgb(0,157,178)", "rgb(2,75,81)",
                 "rgb(7,128,207)", "rgb(118,80,5)"])  # 简洁
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    type_='plain',
                    is_show=True,
                    pos_bottom='10%',
                    orient='horizontal',
                    item_width=50,
                    item_height=28,
                    textstyle_opts=opts.TextStyleOpts(font_size=30, font_style='normal', font_weight='bold', )))
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{d}%",
                    font_size=30,
                    font_style='normal',
                    font_weight='bold', ))
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
##专利运营情况
def huitu9():
    def cunchupng():
        global document
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
        print(df_11)
        df1 = df_11
        df1.columns=['申请年','公开公告号','法律状态事件',]
        print(df1)
        df1 = df1.loc[(df1['法律状态事件'].str.contains('权利转移', na=False)) | (
            df1['法律状态事件'].str.contains('质押', na=False))| (
            df1['法律状态事件'].str.contains('许可', na=False))]
        print(df1)

        df1 = df1.groupby(['申请年', '法律状态事件'], as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='申请年', ascending=True)

        df1.columns = ['申请年', '法律状态事件', '申请数量']
        print(df1)
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
        print(df2)
        print(df3)
        print(df4)



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
                ),
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="right",
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
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
#基础功效 ipc 申请趋势
def huitu10():
    def cunchupng():
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
        print(df_11)
        dfx = df_11[['IPC分类号', '公开公告号']]
        dfx = dfx.groupby(['IPC分类号'], as_index=False)['公开公告号'].count()
        dfx = dfx.sort_values(by='公开公告号', ascending=False)
        dfx = dfx.head(5)
        print(dfx)
        listx = list(dfx['IPC分类号'])
        print(listx)

        df1=df_11

        df1 = df1.groupby(['申请年', 'IPC分类号'], as_index=False).count()
        df1 = df1.sort_values(by='申请年', ascending=True)
        df1.columns = ['申请年', 'IPC主分类号小类', '申请数量']
        print(df1)
        df_1 = df1.loc[(df1['IPC主分类号小类'] == listx[0])]
        df_1.columns = ['申请年', 'IPC分类号', '申请数量']
        print(df_1)
        df_2 = df1.loc[(df1['IPC主分类号小类'] == listx[1])]
        df_2.columns = ['申请年', 'IPC分类号', '申请数量']
        print(df_2)
        df_3 = df1.loc[(df1['IPC主分类号小类'] == listx[2])]
        df_3.columns = ['申请年', 'IPC分类号', '申请数量']
        print(df_3)
        df_4 = df1.loc[(df1['IPC主分类号小类'] == listx[3])]
        df_4.columns = ['申请年', 'IPC分类号', '申请数量']
        print(df_4)
        df_5 = df1.loc[(df1['IPC主分类号小类'] == listx[4])]
        df_5.columns = ['申请年', 'IPC分类号', '申请数量']
        print(df_5)

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
                is_selected=True,  ##是否选中图例
                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
                ),  # 标签配置项
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx2)
            .add_yaxis(
                series_name=listx[1],
                y_axis=listy2,
                is_selected=True,  ##是否选中图例
                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
                ),  # 标签配置项
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx3)
            .add_yaxis(
                series_name=listx[2],
                y_axis=listy3,
                is_selected=True,  ##是否选中图例
                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
                ),  # 标签配置项
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx4)
            .add_yaxis(
                series_name=listx[3],
                y_axis=listy4,
                is_selected=True,  ##是否选中图例
                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
                ),  # 标签配置项
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    type_="solid",
                ),  # 线条配置
            )
            .add_xaxis(listx5)
            .add_yaxis(
                series_name=listx[4],
                y_axis=listy5,
                is_selected=True,  ##是否选中图例
                is_smooth=True,  # 是否平滑曲线
                is_symbol_show=True,  # 是否显示 symbol
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="top",
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
                ),  # 标签配置项
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    type_="solid",
                ),  # 线条配置
            )
            .set_colors(
                ["rgb(80,196,143)", "rgb(245,97,111)", "rgb(54,133,254)", "rgb(38,204,216)", "rgb(153,119,239)",
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
                    pos_left='10%',  # 右边
                    orient='vertical',
                    pos_top='10%',
                    item_width=37,  # 图例宽
                    item_height=21,  # 图例高
                ),

            ))
        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
            # 设置距离 bar为x轴标签过长的柱状图
            .add(c, grid_opts=opts.GridOpts(pos_bottom="10%")))

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
if dfm.empty:
    st.write('该数据范围无相应图表！')
else:
    st.subheader("""申请趋势""")
    st.write('展示该领域专利的有效（蓝）、失效（绿）、审中（黄）以及总申请量（红）的变化趋势，'
             '通过观察趋势图的整体走势，可以判断专利申请数量是呈增长、下降还是保持稳定。可反应该领域技术创新的活跃程度。'
             '也可以清晰的看到该领域专利申请的峰值或谷值以及周期性变化，以便于进一步解读分析。')
    huitu1()
    st.subheader("""五局流向""")
    st.write('展示该领域专利在五个较为重要的专利局（中、日、美、韩、欧专局）之间的流动情况，通过技术来源国和技术目标国对应的数量关系判断'
             '来源国技术创新能力以及目标国的技术需求量。也可表示不同专利局之间的合作、竞争、信息共享等关系，'
             '有助于促进技术交流和创新发展以及评估行业的技术交流和创新合作活动。')
    huitu2()
    st.subheader("""地区分布""")
    st.write('在世界地图上展示各个国家或地区的专利申请情况。通过颜色标注数量的多少，'
             '红色表示该地区技术创新活跃、经济发展较快，'
             '灰色表示该地区技术创新不活跃、经济发展较慢。')
    huitu3()
    st.subheader("""申请人排名""")
    st.write('展示该领域专利申请量排名前十的申请人，反映申请人在专利申请方面的活跃程度和竞争力，突出该领域较为重要的申请人，'
             '以供其他申请人选取合作对象、明确自身在领域地位、学习同领域申请人的专利布局、分析竞争对手专利申请情况等')
    huitu4()
    st.subheader("""协同申请趋势""")
    st.write('展示该领域专利协同申请的变化趋势，可以看出该领域技术发展是趋向于合作发展、交流互通；还是趋向于独立自主研发。')
    huitu5()
    st.subheader("""专利类型构成""")
    st.write('展示专利类型的构成情况，各种类型专利的占比情况（授权发明为发明申请中已经授权的一部分），发明和实用新型是功能、结构上的创新，外观设计是对产品外观的创新。'
             '一般发明占比越高，则创新程度越高；实用新型侧重产品的小改进；产品种类多、更新换代快的行业外观设计偏多。')
    huitu7()
    st.subheader("""简单法律状态构成""")
    st.write('该图表通过专利有效/失效/审查中等状态的占比分析，帮助衡量该技术领域的专利活跃程度。'
             '通常情况下，审中状态的专利占比越大，反映该企业近期创新活力越高。')
    huitu8()
    st.subheader("""专利运营情况""")
    st.write('展示该领域专利转移、许可、质押的情况，反映出该领域专利技术运营活跃程度以及专利成果转化的发展趋势。')
    huitu9()
    st.subheader("""技术发展趋势""")
    st.write('展示该技术领域在主要技术分支的专利申请变化情况，申请趋势上升通常为该技术领域在当前技术分支上的技术研发热度较高。')
    huitu10()
#气球
st.balloons()
# #雪花
# st.snow()