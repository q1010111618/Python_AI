"""
案例1：根据输入的用户名密码执行登录操作：具体要求如下
1.正确的用户名和密码为admin/666888,zhaangsan/123456,taoge/888666
2.输入用户名和密码进行登录，直到登陆成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
3.输入的用户名和密码不能为空
4.登录成功：输出“登录成功，进入B站首页~！”
5.登录失败：输出“用户名或密码错误，请重新输入！”

关键字：
1.break：跳出循环
2.continue：跳过本次循环，继续下一次循环
"""

# while True:
#     user_name=input("请输入用户名：")
#     user_pwd=input("请输入密码：")

#     if(user_name=="" or user_pwd==""):
#         print("用户名或密码不能为空，请重新输入！")
#         continue
    
#     if user_name=="admin" and user_pwd=="666888":
#         print("登录成功，进入B站首页~！")
#         break
#     elif user_name=="zhaangsan" and user_pwd=="123456":
#         print("登录成功，进入B站首页~！")
#         break
#     elif user_name=="taoge" and user_pwd=="888666":
#         print("登录成功，进入B站首页~！")
#         break
#     else:
#         print("用户名或密码错误，请重新输入！")
        
#练习1: 用户名密码登录，正确的用户名和密码为admin/666888,5次登录机会，输入错误五次，不允许再操作
# failCount=0;
# while failCount<5:
#     user_name=input("请输入用户名：")
#     user_pwd=input("请输入密码：")
#     if user_name=="admin" and user_pwd=="666888":
#         print("登录成功，进入B站首页~！")
#         break
#     else:
#         failCount+=1
#         print(f"用户名或密码错误{failCount}次，请重新输入！")
        
# else:
#     print("用户名或密码错误次数过多，请稍后再试！")

