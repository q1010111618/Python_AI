# #1.导入模块
# import utils.my_fun

# #2.使用模块中的功能
# utils.my_fun.log_separator()


# from utils import my_fun

# my_fun.log_separator()


# #注意：如果要通过*导入，则必须在__init__.py中指定__all__=["my_fun"]
# from utils import *

# my_fun.log_separator2()


#2.导入模块中的功能
from utils.my_fun import log_separator

log_separator()