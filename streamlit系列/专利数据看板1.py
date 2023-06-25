import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
import random
from pylab import mpl
from pyecharts import options as opts
from pyecharts.charts import Line, Grid,Bar,PictorialBar,Pie,Funnel,Scatter,Map,Geo,EffectScatter,Gauge,Polar,Radar,HeatMap,Graph,WordCloud
from matplotlib.ticker import MaxNLocator

from pandas.api.types import CategoricalDtype

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
st.set_page_config(initial_sidebar_state='collapsed',layout='centered')
# # 添加背景
# st.markdown(
#     """
#     <style>
#     body {
#         background-image: url('新不二LOGO.png');
#         background-repeat: no-repeat;
#         background-size: cover;
#         background-position: center center;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

#添加水印效果




# 缓存Excel数据到load-df
# @st.cache_data
def load_df():
    return pd.read_excel('AR眼镜.xlsx')  # streamlit系列/2020-2022中之信.xlsx


df = load_df()
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
st.sidebar.header('🎈筛选条件🎈：')
# 返回列的唯一值数组
market_values = df['受理局'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets = st.sidebar.multiselect('受理局', market_values_with_all, market_values_with_all[0])
if '全选' in markets:
    # Select all market values
    markets= market_values.tolist()
# # 多选择的部件
# markets = st.sidebar.multiselect('受理局', market_values, market_values)

market_values = df['专利类型'].unique()
# 多选择的部件
markets1 = st.sidebar.multiselect('专利类型', market_values, market_values)

# 返回列的唯一值数组
market_values = df['简单法律状态'].unique()
# 多选择的部件
markets2 = st.sidebar.multiselect('简单法律状态', market_values, market_values)

# 返回列的唯一值数组
market_values = df['申请年'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets3 = st.sidebar.multiselect('申请年', market_values_with_all, market_values_with_all[0])
if '全选' in markets3:
    # Select all market values
    markets3 = market_values.tolist()
# 返回列的唯一值数组
market_values = df['当前申请专利权人州省'].unique()
# 增加全选选项控制
market_values_with_all = ['全选'] + market_values.tolist()
# 多选择的部件
markets4 = st.sidebar.multiselect('当前申请专利权人州省', market_values_with_all, market_values_with_all[0])
if '全选' in markets4:
    # Select all market values
    markets4 = market_values.tolist()

# 做数据筛选 根据上面选择的类别
dfm = df.query('受理局 in @markets and 专利类型 in @markets1  and'
               ' 简单法律状态 in @markets2 and 申请年 in @markets3 and 当前申请专利权人州省 in @markets4')

st.image("新不二LOGO.png")  # streamlit系列/新不二LOGO.png
st.dataframe(dfm)

# 页面 标题
st.title('🎉专利数据看板🎉')

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
    print(df1)

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
    print(df2)

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
    print(df3)

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
    print(df4)

    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots(figsize=(6,4.5))  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.25)  # 图与画布四周距离
    plt.plot(df1['申请年'], df1['申请数量'], color="#F5616F", linestyle='-', linewidth=2, marker='o',markersize=5,
             mfc="#F5616F")  # X轴Y轴数据，颜色，线条样式，粗度，标记点，填充
    x = np.arange(len(df1['申请年']))
    wight=0.3
    plt.bar(x-wight, df2['申请数量'],width=wight, color="#3685fe")
    plt.bar(x, df3['申请数量'], width=wight,  color="#50c48f")
    plt.bar(x+wight, df4['申请数量'], width=wight,  color="#f7b13f")
    plt.ylabel('申请数量', fontdict={'size': 14})
    plt.xlabel('申请年', fontdict={'size': 14})
    plt.xticks(x,df1['申请年'], size=12,rotation=90)
    plt.yticks(size=12)
    # x,y轴整数刻度显示
    # plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    for a, b in zip(df1['申请年'], df1['申请数量']):
        plt.text(a, b, format(b), ha='center', va='center', fontsize=10, alpha=0.9)
    plt.legend(['综合申请','有效','失效','审中'], loc='lower center', frameon=False, prop={'size': 14},ncol=4, bbox_to_anchor=(0.5, -0.3), borderaxespad=0)  # 去掉图例边框
    st.pyplot(fig)

##五局流向图
def huitu2():
    dfmb=dfm
    df1 = dfmb.query('受理局 in %s ' % wuju)

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
    print(df_11)
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
    print(df_11)
    df_11=df_11.query('优先权国家 in %s ' % wuju)
    df_11=df_11.drop_duplicates()
    df_11 = df_11.groupby(['受理局', '优先权国家'], as_index=False)['公开公告号'].count()
    df_11 = df_11.sort_values(by=['受理局', '优先权国家'], ascending=True)
    df_11.columns = ['受理局', '优先权国家', '申请数量']
    df1=df_11

    xmax = max(df1['申请数量'])
    xmin = min(df1['申请数量'])
    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.2, right=0.95, top=0.95, bottom=0.15) #图与画布四周距离

    color = ["#3685fe", "#f5616f", "#50c48f", "#26ccd8", "#9977ef",
             "#f7b13f", "#f9e264", "#f47a75", "#009db2", "#024b51", ]
    for i in range(0, len(df1['申请数量'])):
        if len(df1['申请数量']) > i * 10:
            color.extend(color)
        if len(color) > len(df1['申请数量']):
            break

    color = random.sample(color, len(df1['申请数量']))
    plt.grid(ls='-.', lw=0.35)  # 增加栅格
    plt.scatter(df1['受理局'], df1['优先权国家'], df1['申请数量']/xmax*3000,c=color, alpha=0.7)
    plt.xlabel('技术目标国/地区',fontdict={ 'size':14})
    plt.ylabel('技术来源国/地区',fontdict={ 'size':14})
    plt.xticks(size=12)  # X轴刻度，标签，旋转度
    plt.yticks(size=12)
    for a, b, c in zip(df1['受理局'], df1['优先权国家'], df1['申请数量']):
        plt.text(a, b, c, ha='center', va='center', fontsize=10, alpha=0.9)
    st.pyplot(fig)

##全球 地区分布分析
def huitu3():
    def cunchupng() -> map:
        dfmb=dfm
        df1 = dfmb[['受理局', '公开公告号']]
        df1 = df1.groupby('受理局', as_index=False)['公开公告号'].count()
        df1 = df1.sort_values(by='公开公告号', ascending=False)
        df1=df1.head(10)
        listx = list(df1['受理局'])
        listy = list(df1['公开公告号'])
        data_pair = [list(z) for z in zip(listx, listy)]
        xmin = min(listy)
        xmax = max(listy)
        map = (
            Map(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
                width="1000px",
                height="700px"
            ))
            .add(series_name="", data_pair=data_pair, maptype="world",  # world，china 省 市
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

        geo = (
            Geo(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
                width="1000px",
                height="700px"
            ))
            ## 新增坐标点
            .add_coordinate(
                name='中国',
                longitude=104,
                latitude=35,
            )
            .add_coordinate(
                name='日本',
                longitude=138,
                latitude=36,
            )
            .add_coordinate(
                name='韩国',
                longitude=128,
                latitude=36,
            )
            .add_coordinate(
                name='俄罗斯',
                longitude=87,
                latitude=64,
            )
            .add_coordinate(
                name='印度',
                longitude=78,
                latitude=20,
            )
            .add_coordinate(
                name='德国',
                longitude=10,
                latitude=51,
            )
            .add_coordinate(
                name='美国',
                longitude=-95,
                latitude=37,
            )
            .add_coordinate(
                name='加拿大',
                longitude=-106,
                latitude=56,
            )

            # .add_coordinate(
            #     name='欧洲专利局',
            #     longitude=5,
            #     latitude=52,
            # )
            # .add_coordinate(
            #     name='世界知识产权组织',
            #     longitude=8,
            #     latitude=46,
            # )
            .add_coordinate(
                name='欧洲专利局',
                longitude=38.4,
                latitude=-52,
            )
            .add_coordinate(
                name='世界知识产权组织',
                longitude=-26.7,
                latitude=-52.1,
            )
            .add_coordinate(
                name='泰国',
                longitude=101,
                latitude=15,
            )
            .add_coordinate(
                name='新加坡',
                longitude=103.8,
                latitude=1.3,
            )
            .add_coordinate(
                name='英国',
                longitude=-3.4,
                latitude=55.3,
            )
            .add_coordinate(
                name='法国',
                longitude=2,
                latitude=46,
            )
            .add_coordinate(
                name='西班牙',
                longitude=-3.7,
                latitude=40,
            )
            .add_coordinate(
                name='葡萄牙',
                longitude=-82,
                latitude=39.4,
            )
            .add_coordinate(
                name='墨西哥',
                longitude=-102.5,
                latitude=23.6,
            )
            .add_coordinate(
                name='丹麦',
                longitude=9.5,
                latitude=56.2,
            )
            .add_coordinate(
                name='南非',
                longitude=22.9,
                latitude=-30.6,
            )
            .add_coordinate(
                name='巴西',
                longitude=-51.9,
                latitude=-14.2,
            )
            .add_coordinate(
                name='波兰',
                longitude=19,
                latitude=52,
            )
            .add_coordinate(
                name='土耳其',
                longitude=35.2,
                latitude=38.9,
            )
            .add_coordinate(
                name='哈萨克斯坦',
                longitude=66.9,
                latitude=48,
            )
            .add_coordinate(
                name='澳大利亚',
                longitude=133.7,
                latitude=-25.3,
            )
            .add_coordinate(
                name='欧盟',
                longitude=4.3,
                latitude=50.8,
            )
            .add_coordinate(
                name='印度尼西亚',
                longitude=113.9,
                latitude=-0.8,
            )
            .add_coordinate(
                name='菲律宾',
                longitude=122.08,
                latitude=13.72,
            )
            .add_coordinate(
                name='马来西亚',
                longitude=102.2,
                latitude=4.8,
            )
            .add_coordinate(
                name='以色列',
                longitude=35.2,
                latitude=31.8,
            )

            .add_schema(maptype="world")  # 地图类型
            .add("geo", data_pair, symbol_size=20, )  # 名字 数据 尺寸
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    is_show=True,
                    position="inside",
                    formatter="{b}",
                    font_size=10,
                    font_style='normal',
                    font_weight='bold',
                    color='black'))
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    is_show=False, ), )
        )
        grid = (
            Grid(init_opts=opts.InitOpts(
                bg_color='#FFFFFF',
                width="1000px",
                height="700px"
            ))
            .add(map, grid_opts=opts.GridOpts(), )  # 地图叠加
            .add(geo, grid_opts=opts.GridOpts())
        )
        return grid

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
    # df_11 = df_11.head(30)
    print(df_11)


    df2 = dfmb.astype({'申请年': 'str'})
    df2 = df2.query('申请年 in %s ' % nianfen)
    # df2 = df2.loc[(df2['授权年'] != '-')]
    df2 = df2.loc[df2['法律状态事件'].str.contains('授权', na=False), :]
    df2 = df2[['公开公告号', '当前申请专利权人']]
    series = df2['当前申请专利权人'].str.split('|', expand=True)  # 按照 | 分隔符拆分字段，用以清楚多余空格，对比以|拆分字段
    df_z = df2[['公开公告号']]
    df_22 = pd.DataFrame()
    for i in range(0, series.columns.size):
        df_l = pd.concat([df_z, series[i]], axis=1)  ##公开号与拆分后的一列申请人数据结合成新表
        df_l.columns = ['公开公告号', '当前申请专利权人']
        df_22 = pd.concat([df_22, df_l])  ##所有新表叠加
    df_22.dropna(inplace=True)  # 删除空数据，获得有效数据
    df_22 = pd.concat([df_22['公开公告号'], df_22['当前申请专利权人'].str.strip()],
                      axis=1)  # 用strip（）删除字符串头尾多余空格
    df_22 = df_22.groupby('当前申请专利权人', as_index=False)['公开公告号'].count()
    df_22 = df_22.sort_values(by='公开公告号', ascending=False)
    df_22.columns = ['当前申请专利权人', '授权数量']
    # df_22 = df_22.head(30)
    print(df_22)
    df3=pd.merge(df_11,df_22,on='当前申请专利权人')
    df3.columns=['当前申请人','申请数量','授权数量']
    print(df3)
    df3=df3.head(10)
    df3 = df3.sort_values(by='申请数量', ascending=True)

    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.35, right=0.95, top=0.95, bottom=0.1)  # 图与画布四周距离
    plt.barh(df3['当前申请人'], df3['申请数量'], height=0.8, color="#50c48f",alpha=0.7)
    plt.barh(df3['当前申请人'], df3['授权数量'], height=0.5, color="#f5616f") #先后顺序影响色彩显示
    plt.xticks(size=12)
    plt.yticks(size=10)
    for a, b in zip(df3['申请数量'],df3['当前申请人'], ):
        plt.text(a, b, format(a), ha='left', va='center', fontsize=10, alpha=0.9)
    # for a, b in zip(df3['授权数量'],df3['当前申请人'], ):
    #     plt.text(a , b, format(a), ha='left', va='center', fontsize=10, alpha=0.9)
    plt.legend(['专利申请', '专利授权'], loc='lower center', frameon=False, prop={'size': 12}, ncol=2,
               bbox_to_anchor=(0.5, -0.15), borderaxespad=0)  # 去掉图例边框
    st.pyplot(fig)
##协同申请趋势
def huitu5():

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

    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()  # 去除多余边框
    ax.spines['right'].set_visible(False)  # 右边框
    ax.spines['top'].set_visible(False)  # 上边框
    ax.spines['left'].set_visible(False)  # 右边框
    ax.spines['bottom'].set_visible(False)  # 上边框
    plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.15)  # 图与画布四周距离
    plt.plot(df1['申请年'], df1['申请数量'], color="#F5616F", linestyle='-', linewidth=2,marker='o',markersize=5,mfc="#F5616F"
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
##专利类型构成
def huitu7():

    dfmb = dfm
    df1 = dfmb[['专利类型', '公开公告号']]
    df1 = df1.loc[(df1['专利类型'] != '-')]
    df1 = df1.groupby('专利类型', as_index=False)['公开公告号'].count()
    df1 = df1.sort_values(by='公开公告号', ascending=False)
    df1.columns = ['专利类型', '申请数量']
    df1 = df1.head(5)

    plt.figure(dpi=720)  # 配置画布大小，分辨率
    fig, ax = plt.subplots()
    colors = ["#50C48F", "#F5616F", "#3685FE", "#26CCD8", "#9977EF",
              "#F7B13F", "#F9E264", "#F47A75", "#009DB2", "#024B51"]
    plt.pie(x=df1['申请数量'],
            labels=df1['专利类型'],
            colors=colors,
            autopct='%.1f%%',
            pctdistance=0.7,  # 标签距离圆心位置
            textprops={'fontsize': 12, 'color': 'k'},  # 标签字体大小 颜色

            )
    plt.subplots_adjust(bottom=0.2)  # 图与画布四周距离
    st.pyplot(fig)
##简单法律状态构成
def huitu8():
    global document
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


    colors = ["#50C48F", "#F5616F", "#3685FE", "#26CCD8", "#9977EF",
              "#F7B13F", "#F9E264", "#F47A75", "#009DB2", "#024B51"]
    plt.figure(dpi=720)
    fig, ax = plt.subplots()  # 去除多余边框
    plt.pie(x=df1['申请数量'],
            labels=df1['简单法律状态'],
            colors=colors,
            autopct='%.1f%%',
            pctdistance=0.7,
            textprops={'fontsize': 12, 'color': 'k'},
            wedgeprops={'width': 0.5, 'edgecolor': 'w'},
            )
    plt.subplots_adjust(bottom=0.2)  # 图与画布四周距离
    st.pyplot(fig)
##专利运营情况
def huitu9():
    global document
    dfmb=dfm
    df1 = dfmb[['法律状态事件','申请年', '公开公告号' ]]
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
#基础功效 ipc 申请趋势
def huitu10():
    global document
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
huitu1()
huitu2()
huitu3()
huitu4()
huitu5()
huitu7()
huitu8()
huitu9()
huitu10()