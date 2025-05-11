import pandas as pd
import streamlit as st
#
# data = pd.read_csv("sales.csv")
# st.header("销售数据筛选器")
# id = st.selectbox("选择用户", data["user_id"].unique())
# filtered_data = data[data["user_id"] == id]
# st.bar_chart(filtered_data.set_index("user_id")["recency"])
# import time
#
# progress_bar = st.progress(0)
# for i in range(100):
#     progress_bar.progress(i + 1)
#     time.sleep(0.1)
# st.success("处理完成！")

import streamlit as st

st.set_page_config(page_title="新闻展示", layout="wide")
st.title("📰 新闻信息展示平台")

# 示例数据（你可以替换为自己的内容）
news_data = {
    "国内": [
        {"title": "全国人大召开会议", "time": "2025-05-11", "summary": "会议就2025年经济发展展开讨论。", "content": "会议内容包括......"},
        {"title": "教育部发布新规", "time": "2025-05-10", "summary": "教育部对高校课程改革提出新要求。", "content": "据悉，新规强调......"}
    ],
    "国际": [
        {"title": "联合国召开气候峰会", "time": "2025-05-11", "summary": "各国代表就碳减排目标展开讨论。", "content": "本次会议聚焦......"},
        {"title": "美欧关系趋于紧张", "time": "2025-05-09", "summary": "因贸易政策分歧引发新一轮争议。", "content": "专家认为这将对......"}
    ],
    "科技": [
        {"title": "国产AI芯片再突破", "time": "2025-05-10", "summary": "新一代芯片性能提升30%。", "content": "新发布的芯片X9000采用......"},
        {"title": "智能汽车进入量产阶段", "time": "2025-05-08", "summary": "多家车企宣布将在年底交付。", "content": "业内人士表示......"}
    ]
}

# 选择新闻类别
category = st.selectbox("请选择新闻类别", list(news_data.keys()))

st.subheader(f"📚 {category}新闻")

# 展示对应类别的新闻
for item in news_data[category]:
    with st.expander(f"{item['title']}  🕒 {item['time']}"):
        st.write("📝 摘要：", item['summary'])
        st.write("📄 正文：", item['content'])
