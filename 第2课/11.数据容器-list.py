#列表操作
#定义
# s=[56,90,88,65,90,"A","Hello",True]

# print(type(s))

# #访问列表元素
# #获取
# print(s[0]) #获取第一个元素，正向索引从0开始
# print(s[-1]) #获取最后一个元素，反向索引，从-1开始

# print(s[2])
# print(s[-6])

# #修改
# s[5]="Python"
# print(s)

# #删除
# del s[5]
# print(s)

# #遍历
# for i in s:
#     print(i)

#列表操作
#定义
# s=[56,90,88,65,90,"A","Hello",True]

# #切片操作 s[开始索引：结束索引：步长]
# print(s[0:5:1])
# print(s[:5:])#默认开始索引0，步长为1，简写方案
# print(s[:5]) #还可以再简写如下

# print(s[0:6:2])
# print(s[:6:2])
# print(s[:-2:2])
# print(s[::-1]) #反向输出列表元素


#-----------------------列表list常用方法------------------------------
#列表定义
# s=[56,90,88,64,489,90,208,11,45]
# print(s)

# #append():在列表末尾添加元素
# s.append(100)
# print(s)

# #insert():在指定索引位置插入元素
# s.insert(2,1000)
# print(s)

# #remove():删除列表中第一个匹配到的元素
# s.remove(90)
# print(s)

# #pop():删除指定索引位置的元素，默认删除最后一个元素
# e=s.pop(2)
# print(e)

# e=s.pop()
# print(e)

# print(s)

# #sort():排序
# s.sort()
# print(s)

# #reverse():反转
# s.reverse()
# print(s)


#案例：将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值，最大值和平均值

#1.定义列表
# num_list=[]

# #2.将用户输入的10个数字存储到列表中
# for i in range(10):
#     num=int(input("请输入数字："))
#     num_list.append(num)

# #3.排序
# num_list.sort()
# print("排序后的列表：",num_list)

# #4.输出最小值，最大值和平均值
# print(f"最小值：{num_list[0]}")
# print(f"最大值：{num_list[-1]}")
# print(f"平均值：{sum(num_list)/len(num_list)}")


#案例2：合并两个列表中的元素，并对合并的结果进行去重处理
# num_list1=[19,23,45,56,222,23,41,24,523,12]
# num_list2=[23,4556,21,34,64,12,34]

# #1.合并列表
# #使用+运算符直接合并
# #num_list3=num_list1+num_list2
# #使用*进行解包操作
# num_list3=[*num_list1,*num_list2]
# print("合并后列表：",num_list3)


# #2.去重
# new_list=[]
# for i in num_list3:
#     if i not in new_list:
#         new_list.append(i)
# #简化
# #new_list=list(set(num_list3))
# print("去重后列表：",new_list)


#案例3：生成1-20的平方列表
#方式一：传统方式
# num_list=[]
# for i in range(1,21):
#      num_list.append(i**2)
# print(num_list)

#方式二：列表推导式
# num_list=[i**2 for i in range(1,21)]
# print(num_list)

#案例4：从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表

# num_list=[12,34,21,33,55,66,77,88]
# new_list=[]

# #方式1：
# # for i in num_list:
# #     if i%2==0:
# #         new_list.append(i**2)

# #方式2：
# #[要插入的值 for 变量 in 序列/列表 if 条件]
# new_list=[i**2 for i in num_list if i%2==0]
# print(new_list)

#练习1：将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台
list1=['a','b','c','d']
list2=['x','y','a','b']
list3=['w','a','d']

new_list=list1+list2+list3
print('合并列表后：',new_list)

new_list=list(set(new_list))
new_list.sort()
print('去重排序后：',new_list)

#练习2：将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
new_list=[i**2 for i in list1 if i%3==0 or i%5==0]
print(new_list)

#练习3：将如下列表中的正数提取出来，封装为一个新的列表
list1=[11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
new_list=[i for i in list1 if i>0]
print(new_list)