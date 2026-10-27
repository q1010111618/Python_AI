# 类型注解---->类型推断
# names=['A','B','C']

# # 变量定义
# a2:int=598
# score2:float=98.5
# name2:str="zs"
# is_ok2:bool=True
# pic2:None=None

# names2:list[str|int]=["A","B","C"]
# phones2:set[str]={"138","139","159"}
# scores2:dict[str,float]={"zs":99.5,"ls":88.5,"ww":77.5}
# goods2:tuple[str,float,int]=("Python",99.8,10)

# names2.append(100)

# #只是提示，不是强制性约束,不影响执行
# names2.append(100.5)

# print(names2)



#函数类型注解
def add(x:int,y:int)->int:
    return x+y

print(add(10,20))
print(add("10",20))