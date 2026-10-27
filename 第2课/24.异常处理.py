#异常处理
# try:
#     print(1/0)
# except Exception as e:
#     print(f"异常错误：{e}")
# finally:
#     print("finally")


#异常的传递
def fun1():
    print("fun1.....runing....")
    fun2()

def fun2():
    print("fun2.....runing....")
    fun3()

def fun3():
    print("fun3.....runing....")
    print(my_color)

#测试
if __name__ == "__main__":
    try:
        fun1()
        print("main......runing....")
    except Exception as e:
        print(f"异常错误：{e}")