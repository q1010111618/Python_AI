#导入整个模块---->调用方式：模块名 / 别名.功能名
#import random
#import random as rd #别名

#for i in range(10):
#    print(rd.randint(1,100))

#导入模块中的功能---->调用方式：功能名
#from random import randint
#from random import randint as rd
from random import *

for i in range(10):
    print(randint(1,100))