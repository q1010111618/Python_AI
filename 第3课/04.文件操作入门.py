import os  # 用于拼接文件路径
# 读文件
# # 1. 打开文件
# # 注意：相对路径 "./resources/..." 是相对于"运行脚本的目录"解析的，
# # 从其他目录运行时容易找不到文件，所以这里用脚本所在目录拼接出绝对路径
# script_dir = os.path.dirname(__file__)  # 本脚本所在目录（第三课）
# file_path = os.path.join(script_dir, "resources", "望庐山瀑布.txt")
# f = open(file_path, "r", encoding="utf-8")
# # 2. 读取文件
# #content=f.read()  #读取全部内容
# #print(content)
# content=f.readlines()  #读取全部内容，返回列表
# for line in content:
#     print(line)
# # 3. 关闭文件
# f.close()


#写文件
# 1. 打开文件
# script_dir = os.path.dirname(__file__)  # 本脚本所在目录（第三课）
# file_path = os.path.join(script_dir, "resources", "静夜思.txt")
# f = open(file_path, "w", encoding="utf-8")
# # 2. 写入文件
# f.write("静夜思\n")
# f.write("李白\n")
# f.write("床前明月光，\n")
# f.write("疑是地上霜。\n")
# f.write("举头望明月，\n")
# f.write("低头思故乡。\n")
# # 3. 关闭文件
# f.close()


#====================================================
# try-finally 语句块，确保文件关闭,释放资源
#写文件
# 1. 打开文件
# script_dir = os.path.dirname(__file__)  # 本脚本所在目录（第三课）
# file_path = os.path.join(script_dir, "resources", "静夜思.txt")
# f = open(file_path, "w", encoding="utf-8")
# # 2. 写入文件
# try:
#     f.write("静夜思\n")
#     f.write("李白\n")
#     i=1/0
#     f.write("床前明月光，\n")
#     f.write("疑是地上霜。\n")
#     f.write("举头望明月，\n")
#     f.write("低头思故乡。\n")
# # 3. 关闭文件
# finally:
#     print("finally文件关闭")
#     f.close()

#====================================================
# with 语句块，确保文件关闭,释放资源（推荐写法）
#写文件
#1. 打开文件
script_dir = os.path.dirname(__file__)  # 本脚本所在目录（第三课）
file_path = os.path.join(script_dir, "resources", "静夜思.txt")
with open(file_path, "w", encoding="utf-8") as f:
    # 2. 写入文件
    f.write("静夜思\n")
    f.write("李白\n")
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
