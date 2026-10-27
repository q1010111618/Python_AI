#字符串 基本操作--->不可变的（无法修改）、有序性、可迭代性
# s="hello world"
# print(s[4])
# print(s[-2])

# #不可修改，会报错
# #s[4]='X'

# for i in s:
#     print(i)

# #切片
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5])

# #省略就是默认末尾
# print(s[2::1])

# #步长为负数，反向输出
# print(s[::-1])

#-----------------字符串常用方法-----------------
# s="Hello-Python-Hello-World"

# #find():查找子串，返回子串的索引，如果不存在，返回-1
# print(s.find("Hello"))
# print(s.find("Java"))

# #count():统计子串出现的次数
# print(s.count("Hello"))

# #upper():转换为大写
# print(s.upper())

# #lower():转换为小写
# print(s.lower())

# #split():按照指定分隔符分割字符串，返回列表
# print(s.split("-"))

# #strip():去除字符串两端的指定字符，默认去除两端的空白字符
# print(s.strip())
# print(s.strip("-"))

# #replace():替换字符串中的指定字符串
# print(s.replace("-","_"))

# #startswith()/endswith()判断字符串是否以指定字符串开头/结尾
# print(s.startswith("Hello"))
# print(s.endswith("Hello"))


# print("------------------------------------")
# #一些列方法后，字符串并不会改变
# print(s)


#---------------------字符串案例----------------------
#案例1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），输出“邮箱格式正确”，否则输出"邮箱格式错误"
#方式一：
# email=input("请输入邮箱：")
# if email.count("@")==1 and email.count(".")>=1:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

#方式二：in运算符--->判断子串是否存在
# email=input("请输入邮箱：")
# if email.count("@")==1 and "." in email:
#     print(f"{email}邮箱格式正确")
# else:
#     print(f"{email}邮箱格式错误")


#--------------------------练习---------------------------
#练习1：输入一个字符串，判断该字符串是否是回文（回文：正着读和反着读是一样的）


# s=input("请输入一个字符串：")
# if s==s[::-1]:
#     print(f"{s}是回文")
# else:
#     print(f"{s}不是回文")

#练习2：将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来
s=[]
for i in range(10):
    str=input("请输入一个字符串：")
    new_str=str[::-1].upper()
    s.append(new_str)
print(s)