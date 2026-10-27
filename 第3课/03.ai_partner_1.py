import streamlit as st

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# ========== 页面基本设置 ==========
# layout="wide" 表示页面宽度自适应
st.set_page_config(
    page_title="AI智能伴侣", 
    page_icon="🤖", 
    layout="wide",
    # 设置侧边栏默认状态为展开
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")

#Logo
st.logo(image="resources/logo.png")

# 系统提示词
system_prompt="你是一个优秀的AI助手"

# 初始化聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 遍历消息列表，输出消息
#deep_message=[]

for message in st.session_state.messages:
    st.chat_message(name=message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     deep_message.append({"role":"user","content":message["content"]})
    #     st.chat_message(name="user").write(message["content"])
    # else:
    #     deep_message.append({"role":"system","content":message["content"]})
    #     st.chat_message(name="assistant").write(message["content"])

# 消息输入框
# 输入框每次输入都会导致页面重新刷新渲染，如果想保留下面的输出，需要使用st.session_state.messages
prompt=st.chat_input("请输入您要问的问题：")
if prompt: #字符串会自动转换为bool值，如果不为空，则为True
    #st.write(f"问题：{prompt}")
    # name="user" 表示消息来自用户，"assistant" 表示消息来自机器人
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message(name="user").write(f"问题：{prompt}")
    print(f"------> 调用AI大模型，提示词：{prompt}")

    #调用AI大模型，返回回答
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages # 使用 * 运算符解包将列表展开为独立的元素
        ],
        stream=True,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # 输出大模型的结果（非流式输出的解析方式）
    #print("<------调用AI大模型，结果：",response.choices[0].message.content)
    #st.chat_message(name="assistant").write(response.choices[0].message.content)
    #st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    # 输出大模型的结果（流式输出的解析方式）
    response_message=st.empty()#创建一个空的组件，用于展示大模型返回的结果
    full_response=""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content=chunk.choices[0].delta.content
            full_response+=content
            response_message.chat_message("assistant").write(full_response) 
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})