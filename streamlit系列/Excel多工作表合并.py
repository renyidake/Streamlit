import streamlit as st
import pandas as pd
import tempfile

# 上传文件
def build_upload_file():
    uploaded_file = st.file_uploader('excel文件', type=['xlsx'])

    if uploaded_file is None:
        st.stop()

    return uploaded_file


@st.cache_data
def load_data(file):
    print('执行加载数据')
    return pd.read_excel(file, sheet_name=None)


def build_sheet_select(dfs):
    names = list(dfs.keys())  # 所有工作表名
    sheet_selects = st.multiselect('工作表', names, [])  # 选择的工作表名

    if len(sheet_selects) == 0:
        st.stop()

    return sheet_selects


def merge_selected_sheets(dfs, sheet_selects):
    combined_df = pd.DataFrame()  # 用于合并所有选定数据表的DataFrame

    for name in sheet_selects:
        df = dfs[name]
        # df = df.astype({'申请号': 'str'})
        df['表名'] = name
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    with st.expander('合并所有选定数据表'):
        st.dataframe(combined_df)

    return combined_df


# 主函数
def main():
    st.title("Excel文件工作表合并")

    file = build_upload_file()
    if file is not None:
        dfs = load_data(file)
        sheets = build_sheet_select(dfs)
        combined_df = merge_selected_sheets(dfs, sheets)

        # 导出合并后的文件
        if st.button('导出合并后的文件'):
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                file_path = temp_file.name

                with pd.ExcelWriter(file_path, engine='openpyxl') as ew:
                    combined_df.to_excel(ew, index=False)

            st.download_button('点击此处下载导出的文件', data=open(file_path, 'rb').read(), file_name='merged_data.xlsx')

if __name__ == "__main__":
    main()
