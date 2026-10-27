class Duck:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def swimming(self):
        print(f'Duck:{self.age}岁的{self.name}在游泳')

class Dog:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def swimming(self):
        print(f'Dog:{self.age}岁的{self.name}在游泳')

class Pig:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def swimming(self):
        print(f'Pig:{self.age}岁的{self.name}在游泳')

#在鸭子类型中，我们关注的是对象的行为，而不是对象的类型
#鸭子类型的优势是不需要存在继承关系，只要对象有相应的方法就可以使用
def go_swimming(duck):
    duck.swimming()

#测试代码
if __name__ == "__main__":
    duck = Duck("鸭子",10)
    dog = Dog("狗子",10)
    pig = Pig("猪子",10)
    go_swimming(duck)
    go_swimming(dog)
    go_swimming(pig)