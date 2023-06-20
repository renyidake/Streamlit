import streamlit as st
import pandas as pd
import time

st.markdown("# 宜昌装配式建筑重点技术竞争态势")
st.sidebar.markdown("# 装配式建筑重点技术专利概况分析")

def main():
    # 图片文件名列表
    image_files = [
        "streamlit多页面应用/images/12.png",
        "streamlit多页面应用/images/13.png",
        "streamlit多页面应用/images/14.png",
        "streamlit多页面应用/images/15.png",
    ]
    captions=['结合宜昌市在本技术领域的专利申请趋势，其在装配式建筑技术领域的专利 申请始于近十年，且每年的专利申请量也仅个位数，专利创新成果较少，技术创 新活跃度不高，若该地计划在此领域进行技术布局需加大研发资源的投入，完善 技术链的研发储备。',
              '从宜昌市的地区分布来看，仅西陵区在此领域的专利布局数量相对多一点，但其数量也仅是偶有涉及，在布局强度及布局密度上均未能形成一定的竞争能力，其竞争优势还有待进一步加强。宜昌市虽在预制构件混凝土脱模技术及装配式市 政预制构件技术均有专利布局，但数量较少，各地区之间各自专利申请的独立性 较为明显，未形成全体系的专利布局体系。',
              '宜昌市在本技术领域的主要专利权人主要包括中国葛洲坝集团下属子公司，从专利申请的数量来看，各企业仅是偶有涉及，还未形成在本技术领域具有突出 影响的企业。',
              '宜昌市在本技术有相应专利申请的高校仅三峡大学有部分涉及。若 需在宜昌市进行本技术领域的技术研发布局，建议可依托本区域内龙头建筑企业，协同区域内企业资源，与三峡学院形成产学研用技术研发模式，强化本地企业研 发力量的不足，加快本区域内技术研发的布局',

]

    # 轮播图容器
    carousel = st.empty()
    carousel1 = st.empty()

    # 无限循环轮播
    while True:
        # for image_file in image_files:
        for i in range(0, len(captions)):
            # 显示当前图片
            carousel.image(image_files[i])
            # 显示标题
            carousel1.markdown(f"<p style='text-align: left;'>{captions[i]}</p>", unsafe_allow_html=True)

            # 等待一段时间
            time.sleep(5)

            # 清除当前图片
            carousel.empty()
            carousel1.empty()


if __name__ == '__main__':
    main()