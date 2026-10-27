from fastapi import FastAPI


# 创建一个FastAPI应用
app = FastAPI()

# 定义一个路由
@app.get("/")
def read_root():
    return {"message": "Hello World"}

#
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "张三"},
        {"id": 2, "name": "李四"},
        {"id": 3, "name": "王五"},
    ]


# 启动服务 ---> uvicorn : Python 内置的 轻量级web 服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("08_FastAPI入门:app", host="127.0.0.1", port=8000, reload=True)