import json
#写入JSON数据文件
# user={"name":"张三","age":20,"height":1.75,"weight":60.0}
# with open("./resources/user.json","w",encoding="utf-8") as f:
#     #ensure_ascii=False 默认是True 不转换成ascii编码
#     #indent 缩进(格式化)
#     json.dump(user,f,indent=2,ensure_ascii=False)


#读取JSON数据文件
with open("./resources/user.json","r",encoding="utf-8") as f:
    user=json.load(f)
    print(user)
    print(type(user))