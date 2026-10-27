#案例
#需求1：定义一个函数：根据传入的底和高计算三角形的面积的函数
# def triangle_area(b,h):
#     """
#     该函数用于根据三角形的底和高计算三角形的面积
#     :param b: 三角形的底
#     :param h: 三角形的高
#     :return: 三角形的面积
#     """
#     return b*h/2

# print("底长30，高度20的三角形面积：",triangle_area(20,30))

# #案例2：定义一个函数，计算传入的字符串中元音字幕的个数（元音字母为（aeiouAEIOU)
# def count_aeiou(s):
#     """
#     统计字符串中元音的个数
#     :paraaam s:字符串
#     :return: 元音字母的个数
#     """
#     num = 0
#     for w in s:
#         if w in "aeiouAEIOU":
#             num +=1
#     return num

# print(count_aeiou("Hello Python Hello World OK"))

# #案例3：定义一个函数：计算传入的班级成员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数),
# def calc_score(score_list):
#     """
#     计算成绩列表中的最高分、最低分、平均分
#     :param score_list: 成绩列表
#     :return: 最高分、最低分、平均分
#     """
#     max_s=max(score_list)
#     min_s=min(score_list)
#     avg_s=round(sum(score_list)/len(score_list),1)
#     return max_s,min_s,avg_s

# max_s,min_s,avg_s=calc_score([564,245,741,623,455,576,467])
# print(f"最高分：{max_s},最低分：{min_s},平均分：{avg_s}")



#练习1：定义一个函数，根据传入的分数，计算对应的分数等级并返回
def calc_level(score):
    """
    根据分数计算分数等级
    :param score: 分数
    :return: 分数等级
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"

print(calc_level(90))
print(calc_level(80))
print(calc_level(70))
print(calc_level(60))
print(calc_level(50))

#练习2：定义一个函数，用于判断一个字符串是否是回文串，返回bool值
def is_palindrome(s):
    """
    判断字符串是否是回文串
    :param s: 字符串
    :return: 是否是回文串
    """
    return s == s[::-1]

print(is_palindrome("level"))
print(is_palindrome("radar"))


#练习3：定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒的格式，并返回
def convert_time(seconds):
    """
    将秒转换为小时、分钟、秒的格式
    :param seconds: 秒
    :return: 小时、分钟、秒的格式
    """
    hours = seconds // 3600
    minutes = (seconds % 3600)//60
    seconds=seconds%60
    return hours,minutes,seconds

hours,minutes,seconds=convert_time(3661)
print(f"{hours}小时{minutes}分钟{seconds}秒")


#练习4：定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）
def is_triangle(a,b,c):
    """
    判断三角形的类型
    :param a: 三角形的边长
    :param b: 三角形的边长
    :param c: 三角形的边长
    :return: 三角形的类型
    """
    if a+b<=c or a+c<=b or b+c<=a:
        return "不能构成三角形"
    elif a==b==c:
        return "等边三角形"
    elif a==b or a==c or b==c:
        return "等腰三角形"
    else:
        return "普通三角形"

print(is_triangle(3,4,5))
print(is_triangle(3,3,3))
print(is_triangle(4,4,6))
print(is_triangle(1,2,3))