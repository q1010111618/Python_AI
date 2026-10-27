#函数的参数类型
#加
# def add(x,y):
#     return x+y

# #减
# def sub(x,y):
#     return x-y

# #乘
# def mul(x,y):
#     return x*y

# #除
# def div(x,y):
#     return x/y


# #计算
# def calc(x,y,op):
#     return op(x,y)

# print(calc(10,20,add))
# print(calc(10,20,sub))
# print(calc(10,20,mul))
# print(calc(10,20,div))


#定义函数
# def out_line():
#     print("-----------------------")

#匿名函数
# out_line=lambda : print("-----------------------")
# out_line()

# def add(x,y):
#     return x+y

# add_2=lambda x,y:x+y
# print(add_2(10,20))


# #需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序
# data_list = ["C++","C","Python","Java","JavaScript","PHP","Go","JavaScript","Rust"]
# print(data_list)

# data_list.sort()#这个是按照字符串的ASCII码（字母）排序
# print(data_list)


# data_list.sort(key=lambda item:len(item))
# #data_list.sort(key=len)#这个也是按照字符串的长度排序
# print(data_list)


#案例1：计算n的阶乘
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))



#案例：电商订单计算器
#定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
"""
具体规则如下：
    1、优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价
    2、积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且积分抵扣不能超过商品总价，积分只能整百抵扣）
"""
def calc_order_cost(*args:tuple[str,float,int],coupon=0,integral=0,freight=0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args:商品信息（商品名、价格、数量）--->如：("商品1",100,10),("商品2",200,20)
    :param coupon:优惠券金额
    :param integral:积分抵扣金额
    :param freight:运费金额
    :return:订单总金额
    """
    total_cost=0
    for item in args:
        total_cost+=item[1]*item[2]
    
    if total_cost>=5000 and coupon<=total_cost:
        total_cost-=coupon
    
    if total_cost>=5000 and integral//100<=total_cost:
        total_cost-=integral//100
    
    total_cost+=freight
    return total_cost

print("订单总金额：",calc_order_cost(("商品1",100,10),("商品2",200,20),coupon=500,integral=100,freight=10))


print("订单总金额：",calc_order_cost(("商品1","80",10),("商品2",80,20),freight=10))