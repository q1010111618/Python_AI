# 描述包信息
__version__ = "0.0.1"
__author__ = "LWH"

# 显式导入子模块（否则 __all__ 中的模块不会被加载到包命名空间）
from . import my_fun
from . import my_var

__all__ = ["my_fun", "my_var"]
