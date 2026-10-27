"""
多继承:一个类可以同时继承多个父类
    多个父类时，默认使用第一个父类的同名属性
    如果需要使用其他父类的同名属性，需要使用父类名.属性名
    如果多个父类中有同名方法，默认使用第一个父类的同名方法
    如果需要使用其他父类的同名方法，需要使用父类名.方法名
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
        #self.__control_fuel()

    def stop(self):
        print(f"{self.brand} {self.model} {self.color} 停止行驶...")

    def __control_fuel(self):
        print(f"{self.brand} {self.model} {self.color} 正在控制油门...")

    def get_owner(self):
        return self.__owner[0:1]+"**"

    def charge(self):
        print(f"{self.brand} {self.model} {self.color} 正在补充燃料...")

# 华为AI驾驶
class HuaweiAiDriving:
    def __init__(self,version="V1.0"):
        self.version = version
    
    def run(self):
        print(f'使用华为AI驾驶，版本号：{self.version}')

# 问界汽车
class WenJieCar(Car,HuaweiAiDriving):
    def __init__(self, brand, model, color, owner,version="V1.0"):
        super().__init__(brand, model, color, owner)
        HuaweiAiDriving.__init__(self,version)

    def run(self):
        super().run()
        HuaweiAiDriving.run(self)

if __name__ == "__main__":
    car = WenJieCar("问界","M5","白色","张三","V2.0")

    #print(car.__dict__) #查看对象的属性

    #print(WenJieCar.__mro__) #查看方法解析顺序
    #print(WenJieCar.mro()) #查看方法解析顺序

    car.run()