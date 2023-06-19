from collections import defaultdict
import streamlit as st
import pandas as pd
import utils

def build_upload_file():
    uploaded_file = st.file_uploader('excel文件',type=['xlsx'])

    if uploaded_file is None:
        st.stop()

    return uploaded_file

@st.cache_data
def load_data(file):
    print('执行加载数据')
    return pd.read_excel(file,None)

def build_sheet_select(dfs):
    names = list(dfs.keys())
    sheet_selects = st.multiselect('工作表',names,[])

    if len(sheet_selects)==0:
        st.stop()

    return sheet_selects

# 页签
def build_sheet_tabs(sheet_selects,dfs):
    filters = defaultdict(lambda :{})
    res_dfs = {}

    def record_filter(sheet_name,field,expr):
        filters[sheet_name][field]=expr

    tabs = st.tabs(sheet_selects)

    # 筛选区域
    def build_filters(sheet_name, df:pd.DataFrame):

        with st.expander('筛选'):
            for col,values in utils.get_cat_col_infos(df):
                select_values = st.multiselect(col,values,key=f'{sheet_name}_{col}')
                if select_values:
                    cond = df[col].isin(select_values)
                    df = df[cond]
                    record_filter(sheet_name,col,str(select_values))

            query = st.text_input('query 查询',key=sheet_name)
            if query:
                df = df.query(query)
                record_filter(sheet_name,'query',query)

        return df
    
    # 页签创建
    for tab,name in zip(tabs,sheet_selects):
        with tab:
            df = dfs[name]
            df = build_filters(name,df)
            st.dataframe(df)
            res_dfs[name] = df

    res_dfs['__filters__'] = pd.DataFrame(filters).T.reset_index()
    return res_dfs

def build_sidebar(df_infos):
    with st.sidebar:
        st.dataframe(df_infos['__filters__'])

        def onExport():
            file_path = 'exports.xlsx'
            with st.spinner('Wait for it...'):

                with pd.ExcelWriter(file_path) as ew:
                    for name,df in df_infos.items():
                        df.to_excel(ew,name,index=False)

            st.success(f'成功导出!查看[{file_path}]')

        st.button('导出',on_click=onExport)

file = build_upload_file()
dfs  = load_data(file)
sheets = build_sheet_select(dfs)
df_infos= build_sheet_tabs(sheets,dfs)

build_sidebar(df_infos)

