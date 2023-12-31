import streamlit as st
import pandas as pd
import time

st.markdown("# 中国装配式建筑重点技术竞争态势")
st.sidebar.markdown("# 装配式建筑重点技术专利概况分析")

def main():
    # 图片文件名列表
    image_files = [
        "streamlit多页面应用/images/6.png",
        "streamlit多页面应用/images/7.png",
        "streamlit多页面应用/images/8.png",
        "streamlit多页面应用/images/9.png",
        "streamlit多页面应用/images/10.png",
        "streamlit多页面应用/images/11.png",
    ]
    captions=['国内装配式建筑技术的专利申请量近二十年基本呈快速上升态势，其中专 利有效率及审中专利占比较大，特别是在近十年由于建筑行业市场发展及政策驱 动，该技术的专利申请量急速上涨，专利技术创新热度高。',
              '从国内专利申请的区域分布来看，江苏、广东、浙江为主要的专利申请地区，其相关的专利创新热度较高，湖北地区在该技术领域的专利申请量与之相较存在 一定的差距。',
              '从技术分布来看，国内排名靠前的地区均主要发展预制构件混凝土脱模技术，在装配式市政预制构件技术方面的技术创新成果相对较少。湖北地区在该技术领 域的技术发展与之相比相同，也主要侧重于预制构件混凝土脱模技术的技术创新。',
              '在装配式建筑技术领域国内主要的专利权人企业包括江苏河海印务有限公 司、任丘市永基建筑安装工程有限公司、中国十七冶集团有限公司等，除江苏河 海印务有限公司外，大部分企业均以预制构件混凝土脱模技术创新为主，仅有部 分企业包括江苏河海印务有限公司、中交第二航务工程局、中交第一航务工程局 等对装配式市政预制构件技术进行了一定数量的技术创新。',
              '在本技术领域的国内高校/科研院所专利申请人主要有东南大学、交通运输 部天津水运工程科学研究院、同济大学等，在预制构件混凝土脱模技术方面主要 的专利权人包括东南大学、同济大学、华南理工大学、沈阳建筑大学等，在装配 式市政预制构件技术方面主要的专利权人包括交通运输部天津水运工程科学研 究院、东南大学、天津大学、大连理工大学等。',
              '国内在该技术领域的专利运营比较活跃，其中专利转让活动最多，其次包括 专利诉讼、许可、质押等专利运营活动时有发生，反映出该技术体现在专利上的 经济价值比较突出，并伴随一定的专利竞争。',
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