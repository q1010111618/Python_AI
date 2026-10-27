"""
继承：子类继承父类，子类可以直接使用父类的方法和属性（不包括私有的）
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

if __name__ == "__main__":
    car = FuelCar("宝马", "X5", "黑色","张三")
    car.charge()
    car2 = ElectricCar("特斯拉", "Model S", "白色", "李四")
    car2.charge()
    #car.__control_fuel()

