#函数定义,函数必须先定义，后调用

# def out_line():
#     print("-" * 50)

# out_line()
# print("欢迎来到我的世界")


#哈啊按输的参数与返回值
#函数1：计算圆的面积
# def calc_area(radius):
#     area = 3.14 * radius ** 2
#     return area

# area2=calc_area(2)
# print(f"半径为2的圆的面积是：{area2}")

# #函数2：计算长方形的面积
# def calc_area(length,width):
#     area = length * width
#     return area

# area3=calc_area(3,4)
# print(f"长方形的面积是：{area3}")


# #函数3：计算圆的面积，周长 ---> 如果返回值有多个，多个返回值之间逗号分隔
# def circle_are_len(r):
#     """
#     该函数用于根据圆的半径计算圆的面积和周长
#     :param r: 圆的半径
#     :return: 圆的面积和周长
#     """
#     return round(3.14*r**2,2),round(3.14*r*2,2)

# help(circle_are_len)

# al=circle_are_len(r=3)
# print(f"半径为2的圆的面积是：{al[0]},周长是：{al[1]}")

# area,length=circle_are_len(r=3)
# print(f"半径为2的圆的面积是：{area},周长是：{length}")




#案例
#需求1：定义一个函数：根据传入的底和高计算三角形的面积的函数