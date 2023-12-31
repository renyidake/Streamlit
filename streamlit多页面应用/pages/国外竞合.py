import streamlit as st
import pandas as pd
import time

st.markdown("# 国外企业竞合分析")
st.sidebar.markdown("# 装配式建筑重点技术专利概况分析")

def main():
    # 图片文件名列表
    image_files = [
        "streamlit多页面应用/images/20.png",
        "streamlit多页面应用/images/21.png",
        "streamlit多页面应用/images/22.png",
        "streamlit多页面应用/images/23.png",
        "streamlit多页面应用/images/24.png",
        "streamlit多页面应用/images/25.png",
    ]
    captions=['基于对国外装配式建筑技术相关专利信息统计，其中专利权人艾乐迈铁科公 司、鹿岛建设株式会社、及韩国建设技术研究院相关专利申请量排名靠前，在本 技术领域具有较好的专利技术基础，通过对此类相关权人的专利布局情况进行分 析，掌握其技术布局方向，同时能指引沛函建工在装配式建筑技术上的技术发展 及完善竞争能力布局体系。',
              '从 Elematic 公司相关专利的申请趋势及专利法律状态来看，该公司的相关技术成果产出具有 一定的阶段性，且目前约 64%的专利已经失效，有效专利量约占 26%，审中专 利不足 3%。从专利角度反映出目前该公司在预制构件混凝土脱模技术方向的技 术创新活跃度较低，专利维持度较低。',
              '日本鹿岛建设株式会社近二十年来在装配式建筑技术方面的专利申请量在 全球具有一定的专利领先优势，且目前大部分专利均处于有效状态，近十年其专 利技术成果也有一定的突破，可见其技术创新趋势较好。',
              '日本鹿岛建设株式会社在装配式市政预制构件技术及预制构件混凝土脱模 技术方向均有相应专利布局，其布局地域包括日本和新加坡，在本国每年都有相 关的技术创新成果，技术创新热度好。',
              '从分支技术相关专利的法律状态来看，日本鹿岛建设株式会社在预制构件混 凝土脱模技术上的专利维持性更好，装配式市政预制构件技术方面的相关专利现 已失效近一半。针对日本鹿岛建设株式会社的失效专利技术，沛函建工可在该失 效专利技术的基础上参考其技术进行迭代技术研发，以缩短自身研发周期及减少 研发投入。',
              '日本鹿岛建设株式会社在预制构件混凝土脱模技术方向的第一发明人包括 坂田昇、仲森稔晃等，在装配式市政预制构件技术方向的第一发明人包括加藤 康生、深澤哲也等',

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