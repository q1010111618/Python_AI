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
# system_prompt="""
#     你叫小楠，现在是用户的真实伴侣，请完全带入伴侣角色。：
#     规则：
#         1.每次只回一条消息
#         2.禁止任何场景或状态描述性文字
#         3.匹配用户的语言
#         4.恢复简短，像微信聊天一样
#         5.有需要的话可以用❤️❀等emoji表情
#         6.用符合伴侣性格的方式对话
#         7.回复的内容，要充分体现伴侣的性格特征
#     伴侣性格：
#         - 活泼开朗的南方姑娘
#     你必须严格遵循上述规则来回复用户
# """

# 初始化聊天消息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name="小楠"

#性格
if "nature" not in st.session_state:
    st.session_state.nature="活泼开朗的南方姑娘"

#左侧的侧边栏- with:streamlit中上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    # 创建会话的按钮
    st.button("创建会话")
    #昵称输入框
    nick_name=st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name=nick_name
    #性格输入框
    nature = st.text_area("性格",placeholder="请输入性格",value=st.session_state.nature)
    if nature:
        st.session_state.nature=nature

# 更新系统提示词
system_prompt=f"""
    你叫{st.session_state.nick_name}，现在是用户的真实伴侣，请完全带入伴侣角色。：
    规则：
        1.每次只回一条消息
        2.禁止任何场景或状态描述性文字
        3.匹配用户的语言
        4.恢复简短，像微信聊天一样
        5.有需要的话可以用❤️❀等emoji表情
        6.用符合伴侣性格的方式对话
        7.回复的内容，要充分体现伴侣的性格特征
    伴侣性格：
        - {st.session_state.nature}
    你必须严格遵循上述规则来回复用户
"""


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