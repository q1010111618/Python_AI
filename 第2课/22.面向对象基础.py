#定义类 ------》 不推荐，动态的为对象添加属性
# class Car:
#     pass

# #创建对象
# c1=Car()

# #动态的为对象添加属性
# c1.color='red'
# c1.brand='BMW'
# c1.name="X5"
# c1.price=500000


# print(c1)
# print(c1.__dict__)#会将对象中的所有属性以字典的形式输出出来


#定义类
class Car:
    #类属性（所有实例对象共享的）
    wheel = 4 #轮的数量
    tax_rate=0.1 #购置税税率


    #__init__初始化方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
    #self:是第一个参数，表示四当前创建出来的实例对象
    def __init__(self,c_color,c_brand,c_name,c_price) -> None:
        self.color=c_color
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
        print("Car 类的对象初始化完毕，对象属性已添加完毕。")

    #定义实例方法
    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶中....")

    def total_cost(self,discount,rate):
        """
        计算提车的总费用，包含两个部分，车的价格，税费
        :param discount:折扣
        :param rage:税率
        :return:提车的总费用
        """
        total_cost=self.price*discount+rate*self.price
        return total_cost

    #魔法方法
    def __str__(self) :
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self, other) :
        return self.color==other.color and self.brand==other.brand and self.name==other.name and self.price==other.price

    def __lt__(self,other):
        return self.price < other.price
        

#创建对象
c1 = Car("red","BMW","X5",500000)
#调用对象中的方法
c1.running()

total=c1.total_cost(0.9,0.1)
print("提车的总费用为：",total)
# print(c1)
# print(c1.__dict__)

c2=Car("red","BMW","X5",500000)

#print(c1==c2)#地址比較

#使用魔法方法后
print(c1==c2)

print(c1 < c2)


#通过实例对象，查找属性时，会先找实例属性；实例属性不存在，再查找类属性
print(c1.wheel)

#通过类名访问类属性
print(Car.wheel)


