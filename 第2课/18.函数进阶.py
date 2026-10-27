#-----------------------------------函数--变量的作用域

#全局变量
# num=100

# #定义函数
# def circle_area(r):
#     #局部变量
#     pi=3.14
#     area=pi*r*r

#     #局部变量num，跟外部的num不是同一个
#     #num=1000
#     #print("num=",num)

#     #指定修改全局变量
#     global num
#     num=1000
#     print("num=",num)


#     return area

# #嗲敖勇函数
# c_area=circle_area(3)
# print(c_area)

# print("num=",num)


#----------------------------------函数 —— 传参方式-----------------------------
#定义函数
# def reg_stu(name,age,gender,city):
#     print(f"注册成功，姓名：{name},年龄：{age}，性别：{gender}，城市：{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}

# #传参方式一：位置参数
# stu=reg_stu("张三",18,"男","北京")
# print(stu)

# #传参方式二：关键字参数
# stu=reg_stu(name="李四",age=19,gender="女",city="上海")
# print(stu)

# stu = reg_stu(age=19,gender="女",city="上海",name="李四")
# print(stu)

# #传参方式三：位置参数+关键字参数-----》未知参数在前，关键字参数在后
# stu=reg_stu("王五",20,city="广州",gender="男")


#默认参数---默认参数要放在没设置默认值的参数后面
# def reg_stu(name,age,gender="男",city="北京"):
#     print(f"注册成功，姓名：{name},年龄：{age}，性别：{gender}，城市：{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}

# reg_stu("张三",18)
# reg_stu("李四",19,"女",)
# reg_stu("王五",20,"男","广州")

# reg_stu("韩丽",21,city="东莞")


#----------------------------------函数——可变参数-----------------------------
#定义函数
def calc_data(*args):
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)
    print(f"最小值：{min_data},最大值：{max_data},平均值：{avg_data}")
    print(args)
    print(type(args))

calc_data(1,2,3,4,5,6,7,8,9,10)


#----------------------------------函数——可变参数(关键字传递**kwargs）-----------------------------
#定义函数
def calc_data(*args,**kwargs):
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_data=round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最小值：{min_data},最大值：{max_data},平均值：{avg_data}")

    return min_data,max_data,avg_data

print(calc_data(1,2,3,42,5,6,7,81,9,10,print=True,round=2))
