# Streamlit 入门示例
# 运行方式：在终端执行  streamlit run 02.streamlit入门.py
# 需要先安装：pip install streamlit

import os
import streamlit as st

# ========== 页面基本设置 ==========
# layout="wide" 表示页面宽度自适应
st.set_page_config(
    page_title="我的第一个 Streamlit 应用", 
    page_icon="🚀", 
    layout="wide",
    # 设置侧边栏默认状态为展开
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.baidu.com",
        "Report a bug": "https://www.baidu.com",
        "About": "https://www.baidu.com",
    }
)

# ========== 标题与文字 ==========
st.title("🎈 Streamlit 入门")
st.header("这是一级标题 header")
st.subheader("这是二级标题 subheader")
st.write("这是普通文本 write，支持 Markdown：**加粗**、*斜体*、`代码`")

# ========== 图片 ==========
# 用基于脚本目录的绝对路径，避免因启动目录不同而找不到图片
image_path = os.path.join(os.path.dirname(__file__), "resources", "img.jpeg")
st.image(image_path,width=300)

# ==========音频==========
audio_path = os.path.join(os.path.dirname(__file__), "resources", "audio.mp3")
st.audio(audio_path)

#==========视频==========
video_path = os.path.join(os.path.dirname(__file__), "resources", "video.mp4")
st.video(video_path)

# ========logo========
image_path2=os.path.join(os.path.dirname(__file__), "resources", "logo.png")
st.logo(image=image_path2)

# ========== 输入控件 ==========
name = st.text_input("请输入你的名字", placeholder="例如：张三")
age = st.slider("请选择年龄", min_value=0, max_value=100, value=18)
score = st.number_input("请输入成绩（0-100）", min_value=0.0, max_value=100.0, value=60.0)
hobby = st.selectbox("选择你的爱好", ["编程", "阅读", "运动", "音乐"])
like = st.checkbox("我同意以上操作")

# ========== 按钮 ==========
if st.button("点击提交"):
    st.success(f"提交成功！{name}，{age} 岁，爱好是 {hobby}，成绩 {score} 分")

# ========== 展示数据 ==========
if name:
    st.write(f"你好，**{name}**！欢迎来到 Streamlit 世界。")

# 用 DataFrame 展示数据
import pandas as pd

data = pd.DataFrame({
    "科目": ["语文", "数学", "英语"],
    "成绩": [score, 90, 85],
})
st.dataframe(data)
st.table(data)

student_data = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [18, 20, 22],
    "性别": ["男", "女", "男"],
})
st.table(student_data)

# ========== 侧边栏 ==========
with st.sidebar:
    st.markdown("## 📌 侧边栏")
    # ======= 单选按钮 ======
    theme = st.radio("选择主题色", ["蓝色", "绿色", "红色"],index=1)#index=1 表示默认选中第二个选项
    st.write(f"你选择了：{theme}")

# ========== 图表 ==========
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)

# ========== 状态展示 ==========
st.info("这是一条提示信息 info")
st.warning("这是一条警告 warning")
st.error("这是一条错误提示 error")

# ========== 进度条 ==========
import time

progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

st.balloons()
