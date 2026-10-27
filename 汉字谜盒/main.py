from datetime import datetime
import logging
import os
import re
from pathlib import Path
import json
from typing import Any
from dataclasses import dataclass
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from openai import OpenAI
# 消息参数的官方类型（TypedDict）：用它标注 messages 列表，
# 否则 list[dict[str, str]] 对不上 ChatCompletionMessageParam，basedpyright 会报类型错误
from openai.types.chat import ChatCompletionMessageParam

# 用 __file__ 定位目录，避免依赖启动时的工作目录（在哪运行都能找到 static）
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

# 日志记录
# 日志格式：时间 - 日志级别 -日志文件：行号 -日志内容
logging.basicConfig(
    level=logging.INFO, #日志级别
    format="%(asctime)s - %(levelname)s -%(filename)s:%(lineno)d- %(message)s"   #日志格式
    )

# 更新系统提示词
system_prompt = f"""
    你是一个专门玩猜字谜的AI助手，只进行字谜互动，不闲聊无关内容，全程纯文本交互。
    请严格遵守以下规则：
    
    一、出题规则
    1.开场先友好打招呼，并随机出一道常见、简单、适合大众的字谜，不生僻、不低俗、不使用网络烂梗。
    2.题目格式：“谜面”（打一字）。
    3.每次出题必须完全随机，禁止重复使用相同题目：你需要在对话上下文中主动记录已使用过的谜语，确保同一会话内绝对不重复。
    4.避免使用高频重复的经典老谜语，尽量选择多样化的中等常见谜语。

    二、【判断规则（最重要！）】
    1.判断题目时，只看用户输入中的核心汉字，忽略无关内容：
        -比如用户输入“江字”“江”“jiang”，都视为答案是[江]
        -用户输入“是江吗？”“应该是江”，也是为答案是[江]
    2.核心字与正确答案完全一致->判为正确，回复：“太棒了！答对了！就是‘XX’字！要不要再来一题？”
    3.核心字与正确答案完全不一致->判为错误，回复：“不对哦，再想想~给你个提示：[简短线索，不泄露答案]”
    4.用户说“不知道”“公布答案”：先揭晓谜底和解释，再问“要不要再来一题？”

    三、互动流程
    1.用户答对：夸奖+确认正确+询问“要不要再来一题？”
    2.用户答错：告知不对+简单提示+鼓励继续猜
    3.用户说“提示一下”：给出简短线索，不公布答案
    4.用户说“公布答案”或“不知道”：揭晓谜底和解释+询问“要不要再来一题？”
    5.用户说“换一题”“再来一题”：立即更换新字谜

    四、其他要求
    1.语气轻松有趣、简洁明快、不啰嗦。
    2.全程只围绕字谜，不回答其他问题，不聊无关话题。
    3.不适用多余表情符号，保持简洁。
    4.若用户答案与正确答案仅差一字或笔画，请仔细核对是否正确。

    请严格按照以上规则回复，优先保证谜语的随机性和多样性。
"""

# 初始化deepSeek大模型客户端
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)

# 创建一个FastAPI应用
app = FastAPI(title="汉字谜盒")

def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

# session_id 只允许“日期_时间”里出现的字符，挡住 ../../ 这类路径穿越
SESSION_ID_RE = re.compile(r"^[0-9\-_]+$")

# 会话历史最多保留多少条（一问一答算 2 条）：超出的从最早的开始丢，
# 避免长对话把上下文撑得越来越大、每轮耗时越来越久
MAX_HISTORY = 20


# 根据session_id获取会话数据：成功返回会话 dict，读不到（不存在/损坏/非法id）返回 None
# 注意：不要在这里返回 ApiResponse，否则函数会有“两种返回结构”，
# 调用方按会话 dict 取 ["message"] 时类型对不上（basedpyright 报 “int 不支持迭代”），
# 而且出错时会把错误信封当成会话数据继续往下走。
def get_session_data(session_id: str) -> dict[str, Any] | None:
    if not SESSION_ID_RE.match(session_id or ""):
        return None

    session_file = os.path.join(SESSION_DIR, f"{session_id}.json")
    if not os.path.exists(session_file):
        return None

    try:
        with open(session_file, "r", encoding="utf-8") as f:
            session_data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return None   # 文件损坏或无读取权限，统一当作“读不到”

    if not isinstance(session_data, dict):
        return None

    session_data.setdefault("message", [])   # 兼容旧文件，保证关键字段存在
    return session_data

# 更新会话信息到json文件
def save_session_data(session_id: str, session_data: dict[str, Any]):
    session_file = os.path.join(SESSION_DIR, f"{session_id}.json")
    try:
        with open(session_file, "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        return ApiResponse(code=500, message=f"保存会话失败：{e}").to_dict()


# 统一返回格式的封装：所有接口都返回 {code, message, data}，前端只看 code 判断是否成功
@dataclass
class ApiResponse:
    code: int = 200        # 200 成功，非 200（400/500）失败
    message: str = "操作成功"
    data: Any = None       # 任意类型：字典/列表/字符串都行

    # data 没传时给空字典，避免前端拿到 null
    def __post_init__(self):
        if self.data is None:
            self.data = {}

    # 交给 FastAPI 前转成字典：不依赖框架对自定义对象的兜底序列化，接口文档也更清晰
    def to_dict(self):
        return {"code": self.code, "message": self.message, "data": self.data}

class ChatRequest(BaseModel):
    session_id: str
    message: str

# 统一处理异常信息
@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    logging.error(f"处理请求 {request.url} 时出错：{exc}")
    return JSONResponse(content={"code":500,"message":"服务器内部错误","data":{}})


# 定义路径
@app.get("/")
def root():
    logging.info("访问项目首页")
    return FileResponse(STATIC_DIR / "index.html")


# 创建会话存放的目录
SESSION_DIR = BASE_DIR / "sessions"
SESSION_DIR.mkdir(exist_ok=True)


# 新建会话
@app.post("/api/session")
def create_session():
    logging.info("创建会话")
    # 生成会话标识，日期+时间
    session_id =  generate_session_id()
    #组装会话信息，保存到文件
    session_data={
        "current_session":session_id,
        "message":[]
    }

    session_file = os.path.join(SESSION_DIR, f"{session_id}.json")
    try:
        with open(session_file, "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        # 写文件失败（目录不存在、磁盘满、权限不足等）也按统一格式返回，code 非 200
        return ApiResponse(code=500, message=f"创建会话失败：{e}").to_dict()

    # 返回会话ID：业务数据一律放进 data 里
    return ApiResponse(code=200, message="创建会话成功", data=session_id).to_dict()

# 获取会话列表
@app.get("/api/sessions")
def get_session_list():
    logging.info("获取会话列表")
    session_list = []
    for file in os.listdir(SESSION_DIR):
        if file.endswith(".json"):
            session_list.append(file[:-5])
    # 会话列表按日期时间排序
    session_list.sort(reverse=False)
    return ApiResponse(code=200, message="获取会话列表成功", data=session_list).to_dict()


# 会话详情：读取某个会话的完整消息，用于首页恢复历史会话
@app.get("/api/session/{session_id}")
def get_session(session_id: str):
    session_data = get_session_data(session_id)
    if session_data is None:
        return ApiResponse(code=404, message=f"会话不存在：{session_id}").to_dict()

    messages = session_data.get("message")
    return ApiResponse(code=200, message="查询会话成功", data={
        "session_id": session_id,
        "messages": messages if isinstance(messages, list) else [],
    }).to_dict()

# 删除会话
@app.delete("/api/session/{session_id}")
def delete_session(session_id: str):
    # 先用正则校验：直接拿用户输入拼路径会有路径穿越风险（../../xxx.json）
    if not SESSION_ID_RE.match(session_id or ""):
        return ApiResponse(code=400, message=f"会话ID不合法：{session_id}").to_dict()

    session_file = os.path.join(SESSION_DIR, f"{session_id}.json")
    if not os.path.exists(session_file):
        return ApiResponse(code=404, message=f"会话不存在：{session_id}").to_dict()

    try:
        os.remove(session_file)
    except OSError as e:
        # 删不掉（文件被占用、权限不足等）也按统一格式返回，code 非 200
        return ApiResponse(code=500, message=f"删除会话失败：{e}").to_dict()

    logging.info(f"删除会话：{session_id}")
    return ApiResponse(code=200, message="删除会话成功", data=session_id).to_dict()


#与AI交互
@app.post("/api/chat")
def chat(request:ChatRequest):
    logging.info(f"与AI交互:{request.session_id}:{request.message}")
    #逻辑实现---->调用deepSeek大模型
    #1.加载json文件中的会话数据
    session_data = get_session_data(request.session_id)
    if session_data is None:   # 会话不存在 / 文件损坏 / session_id 非法
        return ApiResponse(code=404, message=f"会话不存在：{request.session_id}").to_dict()

    #2.构建AI大模型交互的消息数据
    # 显式标注成 ChatCompletionMessageParam 列表：SDK 只接受这个类型，
    # 写成 list[dict[str, str]] 虽然运行时能跑，但类型检查过不了
    message_data: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": system_prompt}
    ]
    for message in session_data["message"]:
        # 历史消息来自 JSON 文件，可能是脏数据。这里做两件事：
        #   1) 运行时过滤：只保留 role/content 合法的消息，避免大模型接口报 400
        #   2) 按 role 分别用字面量构造：这样每条都能对上 ChatCompletionMessageParam 的对应分支，
        #      类型检查才过得去（直接 append 一个 dict[str, str] 是匹配不上的）
        if not isinstance(message, dict):
            continue
        role = message.get("role")
        content = message.get("content")
        if not isinstance(content, str):
            continue
        if role == "user":
            message_data.append({"role": "user", "content": content})
        elif role == "assistant":
            message_data.append({"role": "assistant", "content": content})
        elif role == "system":
            message_data.append({"role": "system", "content": content})
    message_data.append({"role": "user", "content": request.message})

    #3.调用deepSeek大模型
    # 必须显式给 timeout：SDK 默认等 600 秒，模型一慢，浏览器那边早就超时断开了，
    # 后端还占着连接傻等，前端表现就是“一直没反应”。这里 30 秒还没回来就按失败处理。
    try:
        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=message_data,
            stream=False,
            timeout=30,
        )
    except Exception as e:
        # 密钥无效、模型名写错、网络不通、超时……任何异常都在这里兜住，
        # 否则 FastAPI 只会回一个笼统的 500，前端看不到原因
        logging.info(f"[调用大模型失败] {type(e).__name__}: {e}")
        return ApiResponse(code=500, message=f"调用大模型失败：{type(e).__name__}: {e}").to_dict()

    #4.获取AI大模型返回的数据
    response_message = response.choices[0].message.content or ""
    logging.info(f"AI大模型返回的数据:{response_message}")

    #5.更新消息列表中的消息
    # 只把本轮这一问一答追加进历史：系统提示词每次请求都会单独带上，
    # 绝不能写进历史——否则每轮多存一份（实测 5 轮后历史里就有 5 条 system），
    # 请求体越来越大、响应越来越慢，最后必然超过前端的超时时间。
    history = session_data.get("message")
    if not isinstance(history, list):
        history = []
    history.append({"role": "user", "content": request.message})
    history.append({"role": "assistant", "content": response_message})
    # 历史只保留最近 MAX_HISTORY 条，防止长对话把上下文撑爆、每轮耗时线性上涨
    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]
    session_data["message"] = history

    #6.保存json文件中的会话数据
    save_session_data(request.session_id, session_data)

    #7.返回数据
    return ApiResponse(code=200, message="与AI交互成功", data=response_message).to_dict()


# 挂载静态资源目录：style.css / script.js / jquery.min.js
# 注意：必须挂载，否则浏览器请求 /style.css 等找不到路由，会返回 404 Not Found；
# 挂在 "/" 上是让 index.html 里的相对路径（style.css）能直接命中。
# 它必须放在【所有业务路由之后】：路由从上往下匹配，挂在前面会把 /api/session 挡住，
# 导致接口返回 405 Method Not Allowed（静态目录只接受 GET）。
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")


# 启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
