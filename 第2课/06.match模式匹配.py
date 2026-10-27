#match....case 模式匹配：工作日程安排
"""
day=input("请输入今天的星期几(1-7)：")

match day:
    case "1":
        print("周一：工作会议日")
    case "2":
        print("周二：学习培训日")
    case "3":
        print("周三：项目开发日")
    case "4":
        print("周四：项目测试日")
    case "5":
        print("周五：项目发布日")
    case "6"|"7":
        print("周末休息日")
    case _:
        print("输入有误，请输入1-7")
"""

#案例：基于match...case实现一个简易的计算器，可以实现加减乘除四则运算
# num1=float(input("请输入第一个数字："))
# num2=float(input("请输入第二个数字："))
# op=input("请输入运算符(+ - * /)：")

# match op:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0:#if 条件成立，才匹配这个case
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("输入有误，请输入+ - * /")

#练习：请你编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应的动作（输出控制台）
op = input("请输入指令：")

match op:
    case "w"|"W"|"上":
        print("向上移动")
    case "s"|"S"|"下":
        print("向下移动")
    case "a"|"A"|"左":
        print("向左移动")
    case "d"|"D"|"右":
        print("向右移动")
    case "跳"|" ":
        print("角色跳跃")
    case "攻击"|"j"|"J":
        print("角色攻击")
    case "退出"|"esc"|"ESC":
        print("退出游戏")
    case _:
        print("输入有误，未匹配的指令操作。")
