#字面量的写法
# print(100);
# print(3.14);
# print(True);
# print(False);
# print("hello world");
# print("--------------------");
# print(None);

# # 布尔类型本质上就是整数类型，0代表False，1代表True
# print(100 == True);
# print(0 == False);
# print(100 == False);
# print(1 == True);
# print(True+1);
# print(False-1);


#变量-----> Python是动态类型语言，一个变量可以存储不同类的数据（但是项目开发中，推荐变量固定一种类型）
# num = 1114.1
# print(num)

# num = num + 1
# print(num)

# num = "OK"
# print(num)

# num = True
# print(num)


# 案例
# base = 20.7 # 基础播放量
# incr = 50 # 每月新增播放量
# print("未来第一个月的播放总量：",base+incr)
# print("未来第二个月的播放总量：",base+2*incr)

# # 案例-升级： 一次性可以定义多个变量
# base,incr = 20.7,50
# print("未来第一个月的播放总量：",base+incr)
# print("未来第二个月的播放总量：",base+2*incr)

#案例1：变量交换,交换a和b
a=10
b=20
c=a
a=b
b=c
print(a,b)
