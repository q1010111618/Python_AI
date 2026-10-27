#字典--- key 不能重复（如果重复，后面的值会覆盖前面的值），key必须得是不可变类型（int、float、str、tuple）
#定义字典
# dict1={"王林":670,"李慕婉":650,"张三":680,"韩立":543,"王林":400}
# print(dict1)
# print(type(dict1))

# #key 必须是不可变类型，不能是list,set,dict
# dict2={0:670,1.5:5200,(1,2):422,3:234}
# print(dict2)

# #访问
# print(dict1["王林"])
# dict1["李慕婉"]=688
# print(dict1)


# ----------------------------字典常见操作----------------------
# dict1={"王林":670,"李慕婉":650,"张三":680,"韩立":543,"王林":400}
# print(dict1)

# #添加 -key 不存在就是添加
# dict1["李飞宇"]=560
# print(dict1)

# #修改 - key 存在就是修改
# dict1["李飞宇"]=688
# print(dict1)

# #查询
# print(dict1["张三"])
# print(dict1.get("李慕婉"))

# print(dict1.keys()) #获取所有的key
# print(dict1.values()) #获取所有的value
# print(dict1.items()) #获取所有的key-value对


# #删除
# score=dict1.pop("李慕婉")
# print(score)
# print(dict1)

# del dict1["王林"]
# print(dict1)


# #遍历
# for key in dict1.keys():
#     print(f"{key}:{dict1[key]}")

# for item in dict1.items():
#     print(f"{item[0]}:{item[1]}")

# for k,v in dict1.items():
#     print(f"{k}:{v}")


#案例：开发一个购物车管理系统，实现商品信息的添加，修改，删除，查询。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下
#结构：shopping_cart={"Mate80":{"price":5999,"num":1 },"iPhone13":{"price":10999,"num":1}
#1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格，数量，输入完成后修改该商品信息。
#3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#4.查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx,商品价格：xxx,商品数量:xxx”。
#5.退出购物车

# shopping_cart={}

# #1.制作菜单
# print("欢迎使用购物车管理系统：")
# menu="""
# ######## 购物车系统 ########
# #      1. 添加购物车       #
# #      2. 修改购物车       #
# #      3. 删除购物车       #
# #      4. 查询购物车       #
# #      5. 退出购物车       #
# ############################
# """

# while True:
    
#     print(menu)
#     #2.执行的具体操作
#     choice=input("请输入您的选择：")
#     match choice:
#         case "1": #添加购物车
#             goods_name = input("请输入商品名称：")
#             goods_price = float(input("请输入商品价格："))
#             goods_num = int(input("请输入商品数量："))
            
#             #如果商品存在，则不执行添加，提示信息
#             if goods_name in shopping_cart:
#                 print(f"{goods_name}商品已存在，请重新选择~")
#             else:
#                 shopping_cart[goods_name]={"price":goods_price,"num":goods_num}
#                 print(f"{goods_name}商品添加成功")
#         case "2": #修改购物车
#             goods_name = input("请输入要修改的商品名称：")
#             #如果商品不存在，则提示错误信息，
#             if goods_name not in shopping_cart:
#                 print(f"{goods_name}商品不存在，请重新选择~")
#                 continue

#             goods_price = float(input("请输入商品最新价格："))
#             goods_num = int(input("请输入商品最新数量："))
#             shopping_cart[goods_name]={"price":goods_price,"num":goods_num}
#             print(f"{goods_name}商品修改成功")
#         case "3": #删除购物车
#             goods_name=input("请输入要删除的商品名称：")

#             #如果商品不存在，则提示错误
#             if goods_name not in shopping_cart:
#                 print(f"{goods_name}商品不存在，请重新选择~")
#             else:
#                 del shopping_cart[goods_name]
#                 print(f"{goods_name}商品删除成功")
#         case "4": #查询购物车
#             for goods_name in shopping_cart.keys():
#                 goods_info=shopping_cart[goods_name]
#                 print(f"商品名称：{goods_name},商品价格：{goods_info['price']},商品数量：{goods_info['num']}")
#         case "5": #退出购物车
#             print("欢迎下次光临~")
#             break
#         case _:  #匹配其他所有情况
#             print("输入有误，请重新输入")


#练习：开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下
#1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中
student_dict={}

#1.制作菜单
print("欢迎使用教务管理系统：")
menu="""
################################### 教务管理系统 ################################################
#1. 添加学生信息   2. 修改学生信息  3. 删除学生信息  4. 查询学生信息  5. 列出所有学生  6. 统计班级成绩  7. 退出系统          #
################################################################################################
"""
while True:
    print(menu)
    choice=input("请输出你的选择：")
    match choice:
        case "1": #添加学生信息
            student_name=input("请输入学生姓名：")
            if student_name in student_dict:
                print(f"{student_name}学生已存在，请重新选择")
                continue

            student_chinese=int(input("请输入学生语文成绩："))
            student_math=int(input("请输入学生数学成绩："))
            student_english=int(input("请输入学生英语成绩："))
            student_dict[student_name]={"chinese":student_chinese,"math":student_math,"english":student_english}
            print(f"{student_name}学生信息添加成功")
        case "2": #修改学生信息
            student_name = input("请输入学生姓名：")
            if student_name not in student_dict:
                print(f"{student_name}学生不存在，请重新选择")
                continue

            student_chinese=int(input("请输入学生语文成绩："))
            student_math=int(input("请输入学生数学成绩："))
            student_english=int(input("请输入学生英语成绩："))
            student_dict[student_name]={"chinese":student_chinese,"math":student_math,"english":student_english}
            print(f"{student_name}学生信息添加成功")
        case "3": #删除学生信息
            student_name = input("请输入学生姓名：")
            if student_name not in student_dict:
                print(f"{student_name}学生不存在，请重新选择")
                continue
            del student_dict[student_name]
            print(f"{student_name}学生信息删除成功")
        case "4": #查询学生信息
            student_name=input("请输入学生姓名：")
            if student_name not in student_dict:
                print(f"{student_name}学生不存在，请重新选择")
                continue
            student_info=student_dict[student_name]
            print(f"学生姓名：{student_name},语文成绩：{student_info['chinese']},数学成绩：{student_info['math']},英语成绩：{student_info['english']}")
        case "5": #列出所有学生
            for name in student_dict.keys():
                student_score=student_dict[name]
                print(f"学生姓名：{name},语文成绩：{student_score['chinese']}，数学成绩：{student_score['math']},英语成绩：{student_score['english']}")
        case "6": #统计班级成绩
            #统计班级语文、数学、英语成绩的最高分，最低分，平均分，以及语文，数学，英语最高分和最低分的同学姓名
            chinese_scores=[]
            math_scores=[]
            english_scores=[]
            for name in student_dict.keys():
                student_score=student_dict[name]
                chinese_scores.append(student_score['chinese'])
                math_scores.append(student_score['math'])
                english_scores.append(student_score['english'])

            max_chinese=max(chinese_scores)
            min_chinese=min(chinese_scores)
            max_math=max(math_scores)
            min_math=min(math_scores)
            max_english=max(english_scores)
            min_english=min(english_scores)
            print(f"语文所有分数：{chinese_scores}")
            print(f"语文最高分：{max_chinese},最低分：{min_chinese},平均分：{sum(chinese_scores)/len(chinese_scores):.1f}")
            print(f"数学所有分数：{math_scores}")
            print(f"数学最高分：{max_math},最低分：{min_math},平均分：{sum(math_scores)/len(math_scores):.1f}")
            print(f"英语所有分数：{english_scores}")
            print(f"英语最高分：{max_english},最低分：{min_english},平均分：{sum(english_scores)/len(english_scores):.1f}") 

            #找出各科成绩最低分，最高分的同学
            top_student = {"chinese_max": "", "chinese_min": "", "math_max": "", "math_min": "", "english_max": "", "english_min": ""}
            for name, score in student_dict.items():
                if score["chinese"] == max_chinese: top_student["chinese_max"] += name + " "
                if score["chinese"] == min_chinese: top_student["chinese_min"] += name + " "
                if score["math"] == max_math: top_student["math_max"] += name + " "
                if score["math"] == min_math: top_student["math_min"] += name + " "
                if score["english"] == max_english: top_student["english_max"] += name + " "
                if score["english"] == min_english: top_student["english_min"] += name + " "

            print(f"语文最高分同学：{top_student['chinese_max'].strip()}，最低分同学：{top_student['chinese_min'].strip()}")
            print(f"数学最高分同学：{top_student['math_max'].strip()}，最低分同学：{top_student['math_min'].strip()}")
            print(f"英语最高分同学：{top_student['english_max'].strip()}，最低分同学：{top_student['english_min'].strip()}")
            
        case "7": #退出系统
            print("欢迎下次光临~")
            break
        case _:  #匹配其他所有情况
            print("输入有误，请重新输入")
