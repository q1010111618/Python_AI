__all__ = ["PI", "NAME"]   #指定import * (*通配符指定导入哪些功能)


PI = 3.1415926
NAME = "LWH"

def log_separator():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)



#测试函数
#__name__: 内置变量，表示当前模块的名字
#如果当前模块是被其他模块导入，则__name__的值是导入模块的名字---->__name__=my_fun
#如果当前模块是被直接执行，则__name__的值是__main__
if __name__ == "__main__":
    print("我是被直接执行的")#当前页面独立测试，导入的情况就不会运行
else:
    print("我是被导入的")