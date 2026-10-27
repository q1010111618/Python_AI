s1 = "18809090000是我的手机号，你记住了吗？ 我的另一个手机号是18800008888， 两个QQ号分别是155998992 和 18809091293821 你记住了吗？"
s2 = "我的手机号是18809090000，你记住了吗？ 我的另一个手机号是18800008888， 两个QQ号分别是155998992 和 18809091293821 你记住了吗？"

import re

#match-匹配字符串的开始位置---->Match对象
# 匹配失败时返回 None，直接使用 .group() 会报错，需先判断
result=re.match(r"1[3-9]\d{9}",s1)
if result:
    print(result.group()) # 匹配成功时返回 Match 对象，使用 .group() 可以获取匹配的字符串
    print(result.span()) # 匹配成功时返回匹配的字符串范围，即 (起始位置, 结束位置)
    print(result.start()) # 匹配成功时返回匹配的字符串起始位置
    print(result.end()) # 匹配成功时返回匹配的字符串结束位置
else:
    print("未匹配到手机号")

#search-查找字符串的任意位置--->Match对象
result=re.search(r"1[3-9]\d{9}",s2)
if result:
    print(result.group()) # 匹配成功时返回 Match 对象，使用 .group() 可以获取匹配的字符串
    print(result.span()) # 匹配成功时返回匹配的字符串范围，即 (起始位置, 结束位置)
    print(result.start()) # 匹配成功时返回匹配的字符串起始位置
    print(result.end()) # 匹配成功时返回匹配的字符串结束位置
else:
    print("未匹配到手机号")

#findall-查找所有字符串，返回一个列表--->list
result=re.findall(r"1[3-9]\d{9}",s2)
print(result)
#sub-替换字符串
#split-切割字符串