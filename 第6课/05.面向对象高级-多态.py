"""
多态：
    一个事物多种形态
    多态的三个条件：
        1. 继承
        2. 重写
        3. 父类引用指向子类对象
"""

class Car:
    def __init__(self, brand, model, color, owner):
        self.brand = brand  #品牌
        self.model = model  #型号
        self.color = color  #颜色
        self.__owner = owner  #拥有者


    def start(self):
        print(f"{self.brand} {self.model} {self.color} 正在启动...")

    def run(self):
        print(f"{self.__owner} {self.brand} {self.model} {self.color} 正在行驶...")
        self.__control_fuel()

    def stop(self):
        print(f"{self.brand} {self.model} {self.color} 停止行驶...")

    def __control_fuel(self):
        print(f"{self.brand} {self.model} {self.color} 正在控制油门...")

    def get_owner(self):
        return self.__owner[0:1]+"**"

    def charge(self):
        print(f"{self.brand} {self.model} {self.color} 正在补充燃料...")

# 燃油车类，继承自Car类
class FuelCar(Car):
    def charge(self):
        #super().charge()#调用父类的方法，1
        #Car.charge(self)#调用父类的方法，2
        print(f"{self.brand} {self.model} {self.color} 正在加油...")



# 电动汽车类，继承自Car类
class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} {self.model} {self.color} 正在充电...")

#补充燃料函数
def charge(car:Car):
    car.charge()


#测试代码
if __name__ == "__main__":
    car = FuelCar("宝马", "X5", "黑色","张三")
    car2 = ElectricCar("特斯拉", "Model S", "白色", "李四")
    charge(car)
    charge(car2)