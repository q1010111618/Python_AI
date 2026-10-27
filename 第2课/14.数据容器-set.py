#集合set---->是一种无序，不可重复，可修改的集合

#定义
# s1={5,3,2,1,0,12,9,22,52,5,0}

# print(s1)
# print(type(s1))

# #定义空集合
# s2=set()
# print(s2)
# print(type(s2))


#常见方法：
# s1={100,200,300,400,500,6500,21,12}
# print(s1)

# #add():添加元素s
# s1.add(234)
# print(s1)

# #remove():删除元素
# s1.remove(21)
# print(s1)

# #pop()：随机删除集合元素并返回
# e=s1.pop()
# print(e)
# print(s1)

# #clear():清空集合
# s1.clear()
# print(s1)

# s2={'A',"B","C","D","E","X","Y"}
# s3={'C',"E","Y","Z"}
# #difference():求两个集合的差集
# print(s2.difference(s3))
# print(s3.difference(s2))

# #union():求两个集合的并集
# print(s2.union(s3))

# #intersection():求两个集合的交集
# print(s2.intersection(s3))


"""
案例：根据提供的班级学生的选课情况，完成如下需求：
1.找出同时选修了法语和艺术的学生
2.找出同事选修了所有四门课程的学生
3.找出选修了足球，但是没有选修篮球的学生
4.统计每一个学生选修的课程数量
"""
#选修足球学生名单
football_set={"王林","曾牛","徐立国","通天","天运子","韩立","李飞宇","乌丑","紫灵"}
#选修篮球学生名单
basketball_set={"张铁","墨居仁","王林","姜老道","曾牛","王婵","韩立","天运子","李化元","李飞宇","云露"}
#选修法语学生名单
french_set={"许木","王卓","十三","虎炮","姜老道","天运子","红蝶","李飞宇","韩立","曾牛"}
#选修艺术学生名单
art_set={"通天","天运子","韩立","虎炮","姜老道","紫灵"}

#1.找出同时选修法语和艺术的学生
print(f"同时选修法语和艺术的学生：{french_set.intersection(art_set)}")
#方式2 &  --> 交集
print(f"同时选修法语和艺术的学生：{french_set & art_set}")

#2.找出同时选修所有四门课程的学生
print(f"同时选修所有四门课程的学生：{football_set.intersection(basketball_set,french_set,art_set)}")
#方式2
print(f"同时选修所有四门课程的学生：{football_set & basketball_set & french_set & art_set}")

#3.找出选修了足球，但是没有选修篮球的学生
print(f"选修乐足球，但没选修篮球的学生：{football_set.difference(basketball_set)}")
#方式2
print(f"选修乐足球，但没选修篮球的学生：{football_set - basketball_set}")
#方式3：集合推导式-->快速构建集合，语法：{妖王集合中添加的数据 for s in set1 if 条件}
print(f"选修乐足球，但没选修篮球的学生：{set(s for s in football_set if s not in basketball_set)}")

#4.统计每一个学生选修的课程数量
#4.1获取到学生名单
all_set=football_set.union(basketball_set).union(french_set).union(art_set)
#方式2：简化 |
all_set=football_set | basketball_set | french_set | art_set
print(f"学生名单：{all_set}")

#4.2获取每一个学生选修的课程数量
all_list = [*football_set,*basketball_set,*french_set,*art_set]

for s in all_set:
    print(f"{s} 选修了 {all_list.count(s)} 门课程")


