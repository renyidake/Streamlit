import pandas as pd
import streamlit as st
from pathlib import Path
import time
import openpyxl




folder = st.text_input('文件夹')

if not folder:
    st.stop()

# 文件夹不存在，需要提示并结束
folder=Path(folder)
if not folder.exists():
    st.warning(f'文件夹不存在呀[{folder}]')
    st.stop()



file_infos = pd.DataFrame([{
    '文件名':p.name,'是否合并':True
} for p in folder.glob('*.xlsx')])

editor_infos =  st.experimental_data_editor(file_infos)

# 没有勾选任何的文件，就结束
if editor_infos['是否合并'].sum()<=0:
    st.warning('至少选择一个文件呀')
    st.stop()


if st.button('开始合并'):
    
    files = list(editor_infos.query('是否合并')['文件名'])
    files = list(folder / f for f in files)

    pg = st.progress(0, text='开始合并...')
    pg_values = [1/n for n in range(len(files),0,-1)]

    dfs = []

    for file,pgv in zip(files,pg_values):
        pg.progress(pgv,f'处理 [{file.name}] 中')

        # 这句是模拟长时间任务(为了更好展示进度条而已)，正式环境记得去掉
        time.sleep(1)


        dfs.append(pd.read_excel(file))

    df =  pd.concat(dfs)

    result_file = 'result.xlsx'
    df.to_excel(result_file)
    st.info(f'合并完成，文件:[{result_file}]')