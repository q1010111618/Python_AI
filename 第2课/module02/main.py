#导入模块
#import my_fun


#使用模块中功能
# print(my_fun.PI)
# print(my_fun.NAME)

# my_fun.log_separator()


#导入模块中的功能
#from  my_fun import PI,NAME,log_separator

#因为my_fun模块中__all__=["PI", "NAME"]，所以只能导入PI和NAME
from my_fun import *

#使用模块中功能
print(PI)
print(NAME)
#log_separator()