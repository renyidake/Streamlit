import streamlit as st
import pandas as pd
import time

st.markdown("# 技术发展及专利功效矩阵分析")
st.sidebar.markdown("# 装配式建筑重点技术专利概况分析")

def main():
    # 图片文件名列表
    image_files = [
        "streamlit多页面应用/images/16.png",
        "streamlit多页面应用/images/17.png",
        "streamlit多页面应用/images/18.png",
        "streamlit多页面应用/images/19.png",
    ]
    captions=['从具体来看预制构件混凝土脱模技术的主要技术改进在于脱模方法/工艺，以及模具/脱模设备的改进，其技术创新热度较高，专利申请趋势较好。其次，脱模剂相比之下虽专利创新热度比较低，但其专利申请趋势整体依然是递增的，技术创新趋势较好。',
              '预制构件混凝土脱模技术的主要技术特征包括模具/脱模设备、脱模方法/工 艺、脱模剂，其主要的技术改进方向是为了使结构更简单、提高生产效率以及环 境友好等。',
              '装配式市政预制构件技术的技术创新包括预制道路板、预制生态护坡、预制 检查井及预制排水沟等，从其专利技术的分布情况来看，预制道路板技术的创新 成果较少，基本处于空白，预制生态护坡技术和预制排水沟技术相对来说技术创 新热度更高，且专利申请趋势较好，具有较好的技术研发基础及市场需求支撑。',
              '通过对几个分支技术的技术功效进行统计分析，其中预制排水沟的技术改进 方向在于使其结构简单以及提高其产品的多样性等，预制生态护坡技术的改进方 向主要在于提高施工效率及施工的便利性等。',

]

    # 轮播图容器
    carousel = st.empty()

    # 无限循环轮播
    while True:
        # for image_file in image_files:
        for i in range(0,len(captions)):
            # 显示当前图片
            carousel.image(image_files[i], caption=captions[i])

            # 等待一段时间
            time.sleep(3)

            # 清除当前图片
            carousel.empty()

if __name__ == '__main__':
    main()