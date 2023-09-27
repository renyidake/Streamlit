from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
#设置对象居中、对齐等
from docx.enum.text import WD_TAB_ALIGNMENT,WD_TAB_LEADER
#设置制表符等
from docx.shared import Inches
#设置图像大小
from docx.shared import Pt, RGBColor
# 字号，颜色
from docx.oxml.ns import qn
# 中文字体
from docx.shared import Length
#设置宽度
import re #正则表达式
from docx.enum.style import WD_STYLE_TYPE #读取各部分名称
import tempfile
import os
import streamlit as st

path='D:\工具'
name='自动化产出'
isExists=os.path.exists(path+name)
if not isExists:
    os.makedirs(path+name)

# 创建一个临时文件夹用于存储上传的文件
temp_dir = tempfile.TemporaryDirectory()
uploaded_files = st.file_uploader('上传需要更改格式的Word文件！', accept_multiple_files=True, type='docx')

if not uploaded_files:
    wd=Document('streamlit系列/练习原.docx')  # streamlit系列/2020-2022中之信.xlsx
else:
    for file in uploaded_files:
        # 将上传的文件保存到临时文件夹中
        with open(f"{temp_dir.name}/{file.name}", "wb") as f:
            f.write(file.getbuffer())
        # 获取临时文件的完整路径
        excel_file_path = f"{temp_dir.name}/{file.name}"
    wd = Document(excel_file_path)

    st.write("请输入各部分的字体字号")
    ziti1=st.text_input("一级标题字体", value='黑体',key="ziti1")
    zihao1 = st.text_input("一级标题字号", value=18, key="zihao1")
    zihao1 = int(zihao1)

    ziti2 = st.text_input("二级标题字体", value='方正仿宋_GB2312', key="ziti2")
    zihao2 = st.text_input("二级标题字号", value=16, key="zihao2")
    zihao2 = int(zihao2)

    ziti3 = st.text_input("三级标题字体", value='宋体', key="ziti3")
    zihao3 = st.text_input("三级标题字号", value=14, key="zihao3")
    zihao3=int(zihao3)

    ziti4 = st.text_input("四级标题字体", value='楷体', key="ziti4")
    zihao4 = st.text_input("四级标题字号", value=12, key="zihao4")
    zihao4 = int(zihao4)

    ziti5 = st.text_input("正文字体", value='仿宋', key="ziti5")
    zihao5 = st.text_input("正文字号", value=12, key="zihao5")
    zihao5 = int(zihao5)

    ziti6 = st.text_input("题注字体", value='微软雅黑', key="ziti6")
    zihao6 = st.text_input("题注字号", value=8, key="zihao6")
    zihao6 = int(zihao6)

    st.write('一级标题:',ziti1,zihao1,'二级标题:',ziti2,zihao2,'三级标题:',ziti3,zihao3,'四级标题:',ziti4,zihao4,'正文:',ziti5,zihao5,'题注:',ziti6,zihao6)

    print('读取一级标题：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'Heading 1':
            print(段落.text)
    print('读取二级标题：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'Heading 2':
            print(段落.text)
    print('读取所有标题：')
    for 段落 in wd.paragraphs:
        if re.match("^Heading \d+$",段落.style.name):
            print(段落.text)

    print('读取标题名称：')
    标题 = wd.styles
    for i in 标题:
        if i.type==WD_STYLE_TYPE.PARAGRAPH:
            print(i.name)
    print('Caption：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'Caption':
            print(段落.text)
    print('annotation text：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'annotation text':
            print(段落.text)
    print('toc 3：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'toc 3':
            print(段落.text)
    print('Footer：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'Footer':
            print(段落.text)
    print('Header：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'Header':
            print(段落.text)

    print('toc 2：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'toc 2':
            print(段落.text)
    print('Normal (Web)：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'Normal (Web)':
            print(段落.text)
    print('TOC Heading：')
    for 段落 in wd.paragraphs:
        if 段落.style.name == 'TOC Heading':
            print(段落.text)

    for 段落 in wd.paragraphs:
        if 段落.style.name =='Heading 1':
            for 块 in 段落.runs:
                块.font.bold = True  # 加粗
                块.font.italic = False  # 斜体
                块.font.underline = False  # 下划线
                块.font.strike = False # 删除线
                块.font.shadow = False # 阴影
                块.font.size = Pt(zihao1)
                块.font.color.rgb = RGBColor(0,0,0)
                # 颜色
                块.font.name = 'Arial'
                # 英文字体设置
                块._element.rPr.rFonts.set(qn('w:eastAsia'),ziti1)
                # 设置中文字体
    for 段落 in wd.paragraphs:
        if 段落.style.name =='Heading 2':
            for 块 in 段落.runs:
                块.font.bold = True  # 加粗
                块.font.italic = False  # 斜体
                块.font.underline = False  # 下划线
                块.font.strike = False # 删除线
                块.font.shadow = False # 阴影
                块.font.size = Pt(zihao2)
                块.font.color.rgb = RGBColor(0,0,0)
                # 颜色
                块.font.name = 'Arial'
                # 英文字体设置
                块._element.rPr.rFonts.set(qn('w:eastAsia'),ziti2)
                # 设置中文字体
    for 段落 in wd.paragraphs:
        if 段落.style.name =='Heading 3':
            for 块 in 段落.runs:
                块.font.bold = True  # 加粗
                块.font.italic = False  # 斜体
                块.font.underline = False  # 下划线
                块.font.strike = False # 删除线
                块.font.shadow = False # 阴影
                块.font.size = Pt(zihao3)
                块.font.color.rgb = RGBColor(0,0,0)
                # 颜色
                块.font.name = 'Arial'
                # 英文字体设置
                块._element.rPr.rFonts.set(qn('w:eastAsia'),ziti3)
                # 设置中文字体
    for 段落 in wd.paragraphs:
        if 段落.style.name =='Heading 4':
            for 块 in 段落.runs:
                块.font.bold = True  # 加粗
                块.font.italic = False  # 斜体
                块.font.underline = False  # 下划线
                块.font.strike = False # 删除线
                块.font.shadow = False # 阴影
                块.font.size = Pt(zihao4)
                块.font.color.rgb = RGBColor(0,0,0)
                # 颜色
                块.font.name = 'Arial'
                # 英文字体设置
                块._element.rPr.rFonts.set(qn('w:eastAsia'),ziti4)
                # 设置中文字体
    for 段落 in wd.paragraphs:
        if 段落.style.name =='Normal':
            for 块 in 段落.runs:
                块.font.bold = False  # 加粗
                块.font.italic = False  # 斜体
                块.font.underline = False  # 下划线
                块.font.strike = False # 删除线
                块.font.shadow = False # 阴影
                块.font.size = Pt(zihao5)
                块.font.color.rgb = RGBColor(0,0,0)
                # 颜色
                块.font.name = 'Arial'
                # 英文字体设置
                块._element.rPr.rFonts.set(qn('w:eastAsia'),ziti5)
                # 设置中文字体
    for 段落 in wd.paragraphs:
        if 段落.style.name =='TOC Heading':
            for 块 in 段落.runs:
                块.font.bold = True  # 加粗
                块.font.italic = True  # 斜体
                块.font.underline = False  # 下划线
                块.font.strike = False # 删除线
                块.font.shadow = False # 阴影
                块.font.size = Pt(16)
                块.font.color.rgb = RGBColor(0,0,0)
                # 颜色
                块.font.name = 'Arial'
                # 英文字体设置
                块._element.rPr.rFonts.set(qn('w:eastAsia'),'黑体')
                # 设置中文字体
    for 段落 in wd.paragraphs:
        if 段落.style.name =='Caption':
            for 块 in 段落.runs:
                块.font.bold = True  # 加粗
                块.font.italic = True  # 斜体
                块.font.underline = False  # 下划线
                块.font.strike = False # 删除线
                块.font.shadow = False # 阴影
                块.font.size = Pt(zihao6)
                块.font.color.rgb = RGBColor(0,0,255)
                # 颜色
                块.font.name = 'Arial'
                # 英文字体设置
                块._element.rPr.rFonts.set(qn('w:eastAsia'),ziti6)

    # #修改正文文字样式
    # Normal  正文
    # Heading 1 一级标题
    # Heading 2  二级
    # Heading 3  三级
    # Heading 4  四级
    # Caption  图注 表注
    # annotation text
    # toc 3
    # Footer
    # Header
    # toc 2
    # Normal (Web)
    # TOC Heading  标题 自定义？

    wd.save(r'D:\工具自动化产出\word文档格式调整.docx')
    # st.write('Word文档已存储于：D:\工具自动化绘图\word文档格式调整.docx')
    st.markdown("<span style='color:red'>Word文档已存储于：D:\工具自动化产出\word文档格式调整.docx</span>", unsafe_allow_html=True)
temp_dir.cleanup()

