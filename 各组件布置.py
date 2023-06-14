"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np



#创建数据表 自动识别数据并选择最好的形式展现 调用任何 Streamlit 方法的情况下写入您的应用程序。Streamlit 支持“魔术命令st.write()”，
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
st.write("自适应表格的展示:")
df


#创建数据表  将任何内容传递给st.write() Streamlit 会弄明白并以正确的方式呈现事物。
st.write("write表格的展示:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
#########使用 Numpy 生成随机样本，并使用方法st.dataframe()绘制交互式表格。
st.write("随机样本dataframe()绘制交互式表格:")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
######## PandasStyler对象突出显示交互式表格中的一些元素。
st.write("表格高亮设置:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
###Streamlit 也有静态表生成的方法： st.table().

import streamlit as st
import numpy as np
import pandas as pd
st.write("静态表生成的方法： st.table()")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

#将折线图添加到您的应用程序 st.line_chart()。
import streamlit as st
import numpy as np
import pandas as pd
st.write("折线图st.line_chart()")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#使用st.map()您可以在地图上显示数据点。
import streamlit as st
import numpy as np
import pandas as pd
st.write("地图st.map()")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#当您将数据或模型置于您想要探索的状态时，您可以添加小部件，例如st.slider(), st.button()或 st.selectbox()
##将小部件的当前状态分配给过程中的变量。
st.write("小部件st.slider()")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
##选择指定一个字符串用作小部件的唯一键，也可以通过键访问小部件  每个带有键的小部件都会自动添加到会话状态
st.write("小部件st.text_input")
st.text_input("Your name", key="name")
# 你可以使用以下命令在任意位置访问该值:
st.session_state.name
##使用复选框显示/隐藏数据
st.write("使用复选框显示/隐藏数据")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
##使用选择框作为选项
st.write("使用选择框作为选项")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    '你最喜欢哪个数字?',
     df['first column'])

'你的选择: ', option

##Streamlit 使用 st.sidebar. 传递给的每个元素都 st.sidebar固定在左侧，使用户可以专注于应用程序中的内容，同时仍然可以访问 UI 控件。
st.write("使用 st.sidebar. 传递给的每个元素都 st.sidebar固定在左侧")
##例如，如果要将选择框和滑块添加到侧边栏，请使用st.sidebar.sliderandst.sidebar.selectbox而不是st.sliderand st.selectbox：
st.write("将选择框和滑块添加到侧边栏使用st.sidebar.sliderandst.sidebar.selectbox")
# Add a selectbox to the sidebar:
st.write("向侧边栏添加一个选择框")
add_selectbox = st.sidebar.selectbox(
    '你希望我们怎样联系你?',
    ('邮箱', '固定电话', '移动电话')
)

# Add a slider to the sidebar:
st.write("向侧边栏添加一个滑块")
add_slider = st.sidebar.slider(
    '选择一个值范围',
    0.0, 100.0, (25.0, 75.0)
)
##除了侧边栏之外，Streamlit 还提供了几种其他方式来控制应用程序的布局。st.columns让您并排放置小部件，并 st.expander让您通过隐藏大内容来节省空间。
st.write("st.columns并排放置小部件")
st.write("st.expander让您通过隐藏大内容来节省空间")


import streamlit as st

left_column, right_column = st.columns(2)
# 您可以使用像st.sidebar这样的列:
left_column.button('按我!')

# 更好的是，在“with”块中调用Streamlit函数:
with right_column:
    chosen = st.radio(
        '分院帽',
        ("格兰芬多", " 拉文克劳", "赫奇帕奇", "斯莱特林"))
    st.write(f"你在 {chosen} 学院!")
##将长时间运行的计算添加到应用程序时，您可以使用它 st.progress()来实时显示状态。
import streamlit as st
import time

st.write("更新进度条")
'开始一个漫长的计算…'

# 添加一个占位符
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  # 在每次迭代中更新进度条。
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...现在我们做完了!'