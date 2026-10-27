#if条件判断：如果分数超过680，我就去清华读书
# score = 682
# if score > 680:
#     print("我去清华读书")
#     print("恭喜你即将进入精彩的大学生活")
# else:
#     print("我去交大读书")


#if案例：模拟B站登录功能的实现（正确账号和密码为 1888888888/666888
# ok_account="1888888888"
# ok_password="666888"

# #1.接收用户输入的账号和密码
# account=input("请输入账号：")
# password=input("请输入密码：")

# #2.判断账号和密码是否全部正确，如果都正确则登陆成功，进入首页
# if ok_account==account and ok_password==password:
#     print("登录成功，进入首页")
# else:
#     print("登录失败，账号或密码错误")
#3.判断账号和密码是否有错误，如果有任何一个错误，则登录失败，提示错误信息


# 案例2：根据用户输入的年份，判断这一年是闰年还是平年（闰年：能被4整除，但不能被100整除；或者能被400整除）
# year=int(input("请输入一个年份："))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(f"{year}是闰年")       
# else:
#     print(f"{year}是平年")


#练习1：根据用户输入的数字，判断该数字是奇数还是偶数
# input_num=int(input("请输入一个数字："))
# if input_num%2==0:
#     print(f"{input_num}是偶数")
# else:
#     print(f"{input_num}是奇数")

#练习2：根据用户输入的年龄，判断该用户是否已经成年（>=18成年，否则未成年）
# age=int(input("请输入你的年龄："))
# if age>=18:
#     print(f"{age}岁，已成年")
# else:
#     print(f"{age}岁，未成年")

#练习3：根据用户输入的数字，判断该数字是正数还是负数（不考虑0）
# input_num=int(input("请输入一个数字："))
# if input_num>0:
#     print(f"{input_num}是正数")
# elif input_num<0:
#     print(f"{input_num}是负数")
# else:
#     print(f"{input_num}是0")

#练习4：根据用户输入的考试分数，判断该分数是否及格了（大于等于60就是及格）
# input_num=int(input("请输入你的考试分数："))
# if input_num>=60:
#     print(f"{input_num}你的分数及格了")
# else:
#     print(f"{input_num}你的分数不及格")

#需求1：根据输入用户名、密码进行登录系统
# username=input("请输入用户名：")
# password=input("请输入密码：")
# if username=="admin" and password=="666888":
#     print("登录成功")
# elif username=="root" and password=="547527":
#     print("登录成功")
# elif username=="guest" and password=="123456":
#     print("登录成功")
# else:
#     print("登录失败")

#练习5：根据输入的考试成绩，判断成绩等级
# score=int(input("请输入你的考试成绩："))
# if score>=85:
#     print("优秀")
# elif 60<=score<85:
#     print("及格")
# else:
#     print("不及格")

#练习6：购物折扣计算：根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
"""
totalPay=int(input("请输入你的购物车商品总额："))
if totalPay>=500:
    print(f"享受8折优惠，实际应付金额：{totalPay*0.8}")
elif totalPay>=300:
    print(f"享受9折优惠，实际应付金额：{totalPay*0.9}")
elif totalPay>=100:
    print(f"享受95折优惠，实际应付金额：{totalPay*0.95}")
else:
    print(f"不享受优惠，实际应付金额：{totalPay}")
"""

#“”“多行输出三引号
"""
案例：三角形类型判断：根据输入的三个边长（正整数），判断三角形的类型（等边三角形、等腰三角形、一般三角形，还是不能构成三角形）
 1.构成三角形的条件：两边之和大于第三边
 2.等边三角形：三边长度相等
 3.等腰三角形：两边长度相等，第三边长度不等
 4.一般三角形：三边长度不等
"""
"""
#1.接收输入的三角形的三个边的边长
a=int(input("请输入a边长："))
b=int(input("请输入b边长："))
c=int(input("请输入c边长："))  

#2.判断三角形的类型
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("等边三角形")
    elif a==b or a==c or b==c:
        print("等腰三角形")
    else:
        print("一般三角形")
else:
    print("不能构成三角形")t

"""

#练习：北京市居民年度用电电费计算：根据输入的用电度数，计算电费
electricity=float(input("请输入你的用电度数："))
if electricity<2880:
    print(f"第一档电费：{electricity*0.4883}元")
elif 2880<=electricity<=4800:
    print(f"第二档电费：{2880*0.4883+(electricity-2880)*0.5383}元")
else :
    print(f"第三档电费：{2880*0.4883+2080*0.5383+(electricity-4800)*0.7883}元")
