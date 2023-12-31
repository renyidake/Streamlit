import streamlit as st
import pandas as pd
import time

st.markdown("# 全球装配式建筑重点技术竞争态势")
st.sidebar.markdown("# 装配式建筑重点技术专利概况分析")

def main():
    # 图片文件名列表
    image_files = [
        "streamlit多页面应用/images/1.png",
        "streamlit多页面应用/images/2.png",
        "streamlit多页面应用/images/3.png",
        "streamlit多页面应用/images/4.png",
        "streamlit多页面应用/images/5.png",
    ]
    captions=['基于全球装配式建筑重点技术近二十年在全球的相关专利申请统计，装配式 建筑技术近二十年来的专利申请量基本呈逐步上升态势，并从 2012 年开始步入 快速上升周期，但目前有效的专利总体仅占 36%左右，审中的专利占 26%左右，反映出该领域技术创新热度高但专利维持性相对不高。',
              '中国在该技术领域的专利申请量相比其他国家数量较多，可能在于近十年中 国建筑行业发展速度较快从而带动建筑行业相关技术快速创新。',
              '从主要的技术分布来看，中国在预制构件混凝土脱模技术上的专利申请量相 比其他国家超 10 倍以上，具有较大专利基础优势。相比韩国、美国、日本则主 要是发展装配式市政预制构件技术。基于各国建筑特色的不同，其技术发展存在 一定差异。',
              '从全球在该技术领域的主要申请人来看，专利申请量排名靠前的专利权人主 要为中国企业，但该领域不是技术密集型产业，专利技术与市场竞争能力不能完 全匹配，因此，上述专利申请量排名靠前的企业，其市场占有率并不一定呈正比 关系，但能一定程度反映企业的技术创新热度，故可以从侧面说明该技术在国内 技术创新热度高，且竞争激烈。',
              '全球装配式建筑技术中装配式市政预制构件技术及预制构件混凝土脱模技 术都存在较多的专利转移情况，诉讼事件各分支技术发生次数均未超 10 次，可 见该技术领域专利运营比较活跃，存在一定的技术竞争。针对应用型和基础型技 术还需通过全链条的专利布局保护，加大技术保护和竞争能力。',
]

    # 轮播图容器
    carousel = st.empty()
    carousel1 = st.empty()

    # 无限循环轮播
    while True:
        # for image_file in image_files:
        for i in range(0,len(captions)):

            # 显示当前图片
            carousel.image(image_files[i])
            #显示标题
            carousel1.markdown(f"<p style='text-align: left;'>{captions[i]}</p>", unsafe_allow_html=True)

            # 等待一段时间
            time.sleep(5)

            # 清除当前图片
            carousel.empty()
            carousel1.empty()

if __name__ == '__main__':
    main()