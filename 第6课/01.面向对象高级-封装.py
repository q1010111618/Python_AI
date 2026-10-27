"""
封装：将数据（属性）和方法封装到一个类中，对外提供访问接口
 1.私有属性：在属性名称前加__，表示私有属性，只能在当前类中被访问
 2.私有方法：在方法名称前加__，表示私有方法，只能在当前类中被访问
 3.私有属性/方法的访问：在类外部，不能直接访问私有属性/方法，需要提供公有方法来访问
 4.私有属性/方法的访问：在类内部，可以直接访问私有属性/方法
 注意事项：Python中没有真正的私有属性/方法，只是一个命名规范，表示私有属性/方法，不应该被外部访问
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
        print(f"{self.brand} {self.model} {self.color} 正在控制油量...")

    def get_owner(self):
        return self.__owner[0:1]+"**"

if __name__ == "__main__":
    car = Car("宝马", "X5", "黑色","张三")
    print(car.brand)
    print(car.model)
    print(car.color)

    #print(car.__owner)
    #print(car._Car__owner) #如果想访问私有属性，可以使用_类名__属性名称
    car._Car__control_fuel() # 如果想访问私有方法，可以使用_类名__方法名称

    car.start()
    car.run()
    car.stop()
    print(car.get_owner())