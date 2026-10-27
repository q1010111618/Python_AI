#算术运算符：+ - * /  //  % **
# print("100+200=",100+200)
# print("100-50=",100-50)
# print("100*4=",100*4)
# print("100/4=",100/4)
# print("100//4=",100//4) #整除（结果为证整数）
# print("10%4=",10%4) #10除以4的余数
# print("10**4=",10**4) #10的4次方


#算数运算符的优先级---> ** ----> * / // % --->  + -
# print(10+20*30)
# print((10+20)*30)


#案例：输入两个数x和y，计算x+y和x-y的结果并输出
#键盘接收的数据都是字符串类型，需要转换为int类型
# x=float(input("请输入x的值："))
# y=float(input("请输入y的值："))
# print(f"x+y={x+y}")
# # 0.09999999999999998 ---> 精度损失：由于计算机底层是基于二进制存储的，所以会存在精度损失的问题
# print(f"x-y={x-y}")
# # 解决方案：使用round(...)函数进行四舍五入
# print(f"x-y={round(x-y,2)}")    #保留2位小数


#案例1：计算输入的三个整数的平均数
# num1=int(input("请输入第一个整数："))
# num2=int(input("请输入第二个整数："))
# num3=int(input("请输入第三个整数："))
# avg=(num1+num2+num3)/3
# print(f"三个数的平均数为：{avg}")

#案例2：要求输入梯形的上底、下底和高，计算梯形的面积
# bottom1=float(input("请输入梯形的上底："))
# bottom2=float(input("请输入梯形的下底："))
# height=float(input("请输入梯形的高："))
# area=(bottom1+bottom2)*height/2
# print(f"梯形的面积为：{area}")

#案例3：要求输入圆的半径，然后计算圆的周长和面积（周长：2πr,面积：πr²）
# from math import pi
# radius=float(input("请输入圆的半径："))
# perimeter=2*pi*radius
# area=pi*radius**2
# print(f"圆的周长为：{perimeter}")
# print(f"圆的面积为：{area}")

#案例4：身体质量指数BMI的计算（BMI=体重（kg）/身高（m）的平方）
# weight=float(input("请输入你的体重（kg）："))
# height=float(input("请输入你的身高（m）："))
# bmi=weight/height**2
# print(f"你的BMI指数为：{bmi}")


############  赋值运算符：= += -= *= /= %= //= **=   #########
# num=85
# num+=10
# print("num+=10:",num)
# num-=10
# print("num-=10:",num)
# num*=10
# print("num*=10:",num)
# num/=10
# print("num/=10:",num)
# num%=10
# print("num%=10:",num)
# num//=10
# print("num//=10:",num)
# num**=10
# print("num**=10:",num)

####  #####  比较运算符：== != > < >= <=   #############
# print("10==10吗：",10==10)
# print("10!=10吗：",10!=10)
# print(10>10)
# print(10<10)
# print(10>=10)
# print(10<=10)

##需求案例一，输入一个整数，判断这个数字是否在10-20之间
# num=int(input("请输入一个整数："))
# if num>=10 and num<=20:
#     print("这个数字在10-20之间")
# else:
#     print("这个数字不在10-20之间")

##需求案例二，输入一个整数，判断这个数字是否不在10-20之间
num:int=int(input("请输入一个整数："))
if not (10<=num<=20):
    print("这个数字不在10-20之间")
else:
    print("这个数字在10-20之间")