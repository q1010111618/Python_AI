from fileinput import filename
import json
import streamlit as st
from datetime import datetime
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)

# ========== 页面基本设置 ==========
# layout="wide" 表示页面宽度自适应
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    # 设置侧边栏默认状态为展开
    initial_sidebar_state="expanded",
    menu_items={},
)


# 保存会话信息函数
def save_session():
    # 保存当前会话到文件中
    if st.session_state.session_id:
        # 构建新的会话对象
        session_data = {
            "session_id": st.session_state.session_id,
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "messages": st.session_state.messages,
        }
        print(f"------> 保存会话信息：{session_data}")
        # 保存到文件中
        # 如果session目录不存在，则创建session目录
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
        else:
            # 如果session目录存在，则创建新的会话文件
            session_file = f"sessions/{st.session_state.session_id}.json"
            with open(session_file, "w", encoding="utf-8") as f:
                json.dump(session_data, f, indent=2, ensure_ascii=False)

# 生成会话标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 加载所有的会话列表信息
def load_sessions():
    session_list=[]
    # 加载sessions目录下的文件
    if os.path.exists("sessions"):
        # 遍历目录中的所有文件
        for file in os.listdir("sessions"):
            if file.endswith(".json"):
                session_list.append(file[:-5])# 步长截取去掉后缀名
    session_list.sort(reverse=True)# 倒序排列 不能直接return
    return session_list

# 加载会话信息并渲染在页面中
def load_session(session_id):
    try:
        # 加载会话文件
        session_file = f"sessions/{session_id}.json"
        with open(session_file, "r", encoding="utf-8") as f:
            session_data = json.load(f)
        st.session_state.messages = session_data["messages"]
        st.session_state.nick_name = session_data["nick_name"]
        st.session_state.nature = session_data["nature"]
        st.session_state.session_id = session_data["session_id"]
        #for message in st.session_state.messages:
        #    st.chat_message(name=message["role"]).write(message["content"])
    except Exception:
        st.error("加载会话信息失败")

# 删除会话信息
def del_session(session_id):
    try:
        # 删除会话文件
        session_file = f"sessions/{session_id}.json"
        os.remove(session_file)
        # 如果删除的是当前会话，则重置会话id和消息列表
        if st.session_state.session_id == session_id:
            st.session_state.session_id = generate_session_id()
            st.session_state.messages = []
    except Exception:
        st.error("删除会话信息失败")


# 大标题
st.title("AI智能伴侣")

# Logo
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
    st.session_state.nick_name = "小楠"

# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的南方姑娘"

# 会话标识
if "session_id" not in st.session_state:
    st.session_state.session_id = generate_session_id()

# 左侧的侧边栏- with:streamlit中上下文管理器
with st.sidebar:
    # AI控制面板
    st.subheader("AI控制面板")
    # 创建会话的按钮
    if st.button("新建会话", width="stretch", icon="✏️"):
        # 保存当前会话到文件中
        save_session()

        # 创建新的会话，重置会话id和消息列表
        # 如果消息列表不为空，则清空消息列表
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.session_id=generate_session_id()
            save_session()
            st.rerun()# 重新加载页面

        
    # 展示会话列表
    st.subheader("历史会话")
    # 获取会话列表
    session_list = load_sessions()
    # 展示会话列表
    for session in session_list:
        # 两个按钮放在一行
        col1,col2=st.columns([3,1])
        # 判断当前会话是否被选中
        is_active = session == st.session_state.session_id
        # 选中的会话显示 ▶ 标记，非选中显示普通空格占位
        label = f"▶ {session}" if is_active else f"  {session}"
        # 选中的会话用 type="primary" 高亮；否则用 "secondary" 普通样式
        btn_type = "primary" if is_active else "secondary"
        # 注意：多个会话时，若按钮参数完全相同（如删除按钮 label 都是空串），
        # Streamlit 会按“组件类型+参数”生成相同的内部 ID 而报 DuplicateElementId 错误，
        # 因此给每个按钮传入唯一的 key（用会话名区分）
        if col1.button(label, icon="📒", key=f"load_{session}",type=btn_type):
            # 加载会话信息
            load_session(session)
            st.rerun()
        if col2.button("", icon="❌", key=f"del_{session}"):
            del_session(session)
            st.rerun()
        
    
    # 分割线
    st.divider()
    # ==============================
    st.subheader("伴侣信息")
    # 昵称输入框
    nick_name = st.text_input(
        "昵称", placeholder="请输入昵称", value=st.session_state.nick_name
    )
    if nick_name:
        st.session_state.nick_name = nick_name
    # 性格输入框
    nature = st.text_area(
        "性格", placeholder="请输入性格", value=st.session_state.nature
    )
    if nature:
        st.session_state.nature = nature

# 更新系统提示词
system_prompt = f"""
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
# deep_message=[]
st.text(f"当前会话名称：{st.session_state.session_id}")
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
prompt = st.chat_input("请输入您要问的问题：")
if prompt:  # 字符串会自动转换为bool值，如果不为空，则为True
    # st.write(f"问题：{prompt}")
    # name="user" 表示消息来自用户，"assistant" 表示消息来自机器人
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message(name="user").write(f"问题：{prompt}")
    print(f"------> 调用AI大模型，提示词：{prompt}")

    # 调用AI大模型，返回回答
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages,  # 使用 * 运算符解包将列表展开为独立的元素
        ],
        stream=True,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "enabled"}},
    )
    # 输出大模型的结果（非流式输出的解析方式）
    # print("<------调用AI大模型，结果：",response.choices[0].message.content)
    # st.chat_message(name="assistant").write(response.choices[0].message.content)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    # 输出大模型的结果（流式输出的解析方式）
    response_message = st.empty()  # 创建一个空的组件，用于展示大模型返回的结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    # 保存会话到文件中
    save_session()