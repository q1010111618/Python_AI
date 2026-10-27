# #常见数据类型---->type()获取指定的字面量和变量的类型
# print(type(10))
# print(type(3.14))
# print(type('hello'))
# print(type(True))
# print(type(None))

# num = -100
# print(type(num))

# #isinstance()检查数据是否属于指定的类型--->返回结果是个Bool值
# print(isinstance(num,int))
# print(isinstance(num,float))


#字符串
#定义字符串的三种方式
# s1 = "Hello"  #双引号定义
# s2 = 'Python' #单引号定义
# s3 = """
# Hello:
#     三引号支持换行定义！
#     2026年4月28日
# """  #三引号定义（多行字符串，保留定义格式）
# print(s1)
# print(s2)
# print(s3)

# print(type(s1))
# print(type(s2))
# print(type(s3))

# #定义字符串----> \转义    \n换行符，\t制表符
# msg = 'It\'s very good'
# msg1 = "It's very good"
# print(msg)
# print(msg1)

# #\n换行，\t缩进
# print("\t欢迎大家进入到Pyhon学习！\n\t大家可以一起交流学习！")


#字符串拼接
s1 = "人生苦短" "我用Python"     ",OK"
print(s1)

msg1 = "人生苦短"
msg2 = "我用Python"
print("鬼叔说："+msg1 +","+ msg2)

# ---> str(int数字)--->将int类型的数字转为字符串类型
age1 = 30
print("鬼叔今年"+str(age1)+"岁！")

name="鬼叔"
age="30"
job="程序员"
like="编程"
print("大家好，我是"+name+"，今年"+age+"岁，是一名"+job+"，喜欢"+like+"！")

#通过%s占位符格式化字符串
print("大家好，我是%s，今年%s岁，是一名%s，喜欢%s！"%(name,age1,job,like))
#通过f"..{变量名/表达式}.."格式化字符串  ---> 推荐使用
print(f"大家好，我是{name}，今年{age1}岁，是一名{job}，喜欢{like}！")