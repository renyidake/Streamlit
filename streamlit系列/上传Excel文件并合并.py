import pandas as pd
import streamlit as st
import tempfile


st.set_page_config(layout="wide")

st.title('Excel文件合并')

uploaded_files = st.file_uploader('上传多个Excel文件', accept_multiple_files=True, type='xlsx')
print(uploaded_files)
if not uploaded_files:
    st.warning('请上传至少一个Excel文件')
    st.stop()

# Start merging button
if st.button('开始合并'):
    dfs = []

    for file in uploaded_files:
        print(file)
        df = pd.read_excel(file)
        dfs.append(df)

    merged_df = pd.concat(dfs)
    merged_df = merged_df.drop_duplicates()
    # Save the merged DataFrame to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
        result_file = tmp.name
        merged_df.to_excel(result_file, index=False, engine='openpyxl')

    st.success('文件合并完成!')

    # Provide a download button for the merged result file
    with open(result_file, 'rb') as f:
        file_content = f.read()
    st.download_button(
        label='下载合并后的文件',
        data=file_content,
        file_name='result.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
