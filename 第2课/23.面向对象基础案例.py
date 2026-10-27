"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
 1.1 输入学生姓名，语文成绩，数学成绩，英语成绩
 1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则不添加）
 1.3 验证成绩范围（0-100分）
 1.4 创建学生对象对象并添加到系统
2.修改学生成绩：根据输入的学生姓名，修改对应学生的语文成绩、数学成绩、英语成绩
 2.1 输入学生姓名
 2.2 检查学生姓名是否存在，如果存在，再修改（不存在则不修改）
 2.3 修改学生对象中的语文成绩、数学成绩、英语成绩
3.删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
 3.1 输入学生姓名
 3.2 检查学生姓名是否存在，如果存在，再删除（不存在则不删除）
 3.3 删除学生对象
4.查询学生成绩：根据输入的学生姓名，查询对应的学生成绩
 4.1 输入学生姓名
 4.2 检查学生姓名是否存在，如果存在，查询（不存在则不查询）
 4.3 查询学生对象中的语文成绩、数学成绩、英语成绩
5.查询所有学生成绩：查询系统中所有学生的成绩信息
"""

#学生类
class Student:
    def __init__(self,s_name:str,s_chinese:int,s_math:int,s_english:int):
        self.name=s_name
        self.chinese=s_chinese
        self.math=s_math
        self.english=s_english

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese+self.math+self.english}"

    #修改学生的成绩
    def update_score(self,s_chinese:int|None=None,s_math:int|None=None,s_english:int|None=None):
        if s_chinese is not None:
            self.chinese=s_chinese
        if s_math is not None:
            self.math=s_math
        if s_english is not None:
            self.english=s_english

#教务管理系统类
class EduManagement:
    system_version :str= "1.0"
    system_name:str= "教务管理系统"

    def __init__(self):
        self.students:list[Student]=[]  #列表，记录的是在校学生的成绩

    #添加学生成绩
    def add_student(self):
        name=input("请输入学生姓名：")

        #判断学生姓名是否存在
        for s in self.students:
            if s.name==name:
                print("学生姓名已存在，添加失败！")
                return

        chinese=int(input("请输入学生语文成绩："))
        math=int(input("请输入学生数学成绩："))
        english=int(input("请输入学生英语成绩："))


        #判断分数是否在0-100之间
        if 0 <=chinese <=100 and 0 <=math <=100 and 0 <=english <=100:
            stu=Student(name,chinese,math,english)
            self.students.append(stu)
            print("学生信息添加成功！")
        else:
            print("各科成绩必须在0 - 100之间！")

    #修改学生成绩
    def update_student(self):
        name=input("请输入要修改的学生姓名：")

        #判断学生姓名是否存在
        for s in self.students:
            if s.name==name:
                print(f"当前成绩：{s}")
                chinese=int(input("请输入修改后的语文成绩："))
                math=int(input("请输入修改后的数学成绩："))
                english=int(input("请输入修改后的英语成绩："))

                #判断分数是否在0-100之间
                if 0 <=chinese <=100 and 0 <=math <=100 and 0 <=english <=100:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功！")
                    print(f"修改后的成绩：{s}")
                    return
                else:
                    print("各科成绩必须在0 - 100之间！")
                    return

        print("未找到该学生，修改失败！")

    #删除学生成绩
    def delete_student(self):
        name=input("请输入要删除的学生姓名：")

        for s in self.students:
            if s.name==name:
                self.students.remove(s)
                print("学生信息删除成功！")
                return
        print("未找到该学生，删除失败！")
    #查询学生成绩
    def query_student(self):
        name=input("请输入要查询的学生姓名：")

        for s in self.students:
            if s.name==name:
                print(f"学生信息：{s}")
                return
        print("未找到该学生！")

    #查询所有学生成绩
    def list_students(self):
        for s in self.students:
            print(s)


    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")

        while True:
            print()
            print("# ########################################################################## #")
            print("# 1.添加学生  2.修改学生  3.删除学生  4.查询学生  5.查询所有学生  6.退出系统 #")
            print("# ########################################################################## #")
            print()

            choice=input("请输入要执行的操作,输入1-6：") 
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_students()
                    case "6":
                        print("退出系统！")
                        break
                    case _:
                        print("输入错误，请重新输入！") 
            except ValueError:
                print("输入的数据有问题：请检查，然后重新输入！！！")
            except Exception:
                print("程序运行出错，请重新选择~")

#测试
if __name__ == "__main__":
    edu=EduManagement()
    edu.run()


#测试
# if __name__ == "__main__":
#     s1=Student("张三",100,100,100)
#     print(s1)
#     s1.update_score(s_chinese=90)
#     print(s1)
