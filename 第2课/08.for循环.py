# for循环：遍历输入的字符串
# msg=input("请输入一个字符串：")
# for i in msg:
#     print(i)
# else:
#     print("遍历结束")


#案例1：计算1-100之间所有奇数之和
"""
range语句
用法1：range(end)->生成一个从0到end-1的整数序列,range(5)->0,1,2,3,4
用法2：range(start,end)->生成一个从start到end-1的整数序列,range(2,8)->2,3,4,5,6,7
用法3：range(start,end,step)->生成一个从start到end-1的step步长的整数序列,range(0,10,2)->0,2,4,6,8
"""
# total=0
# for i in range(1,101,2):
#     print(f"{total}+{i}={total+i}")
#     total+=i
# else:
#     print(f"1-100之间所有奇数之和：{total}")

#案例2：计算100-500之间所有3的倍数之和
# total=0
# for i in range(100,501):
#     if i%3==0:
#         print(f"{total}+{i}={total+i}")
#         total+=i
# else:
#     print(f"100-500之间所有3的倍数之和：{total}")


#循环嵌套：根据输入的长方形的长度m,宽度n，打印出长方形的形状

# m=int(input("请输入长方形的长度："))
# n=int(input("请输入长方形的宽度："))
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ") #print()默认输出后换行===>print(end="/n")，所以指定end=" "，不换行
#     print()


#案例：打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} X {i} = {i*j} ",end="\t")
#     print()

#需求1：根据输入的直角边的边长，打印等腰直角三角形
# n=int(input("请输入直角边的边长："))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#需求2：根据输入的数字，打印对应的数字金字塔
# n=int(input("请输入数字："))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#需求3：打印国际象棋棋盘
# for i in range(1,9):
#     for j in range(1,9):
#         if (i+j)%2==0:
#             print("■",end=" ")
#         else:
#             print("□",end=" ")
#     print()