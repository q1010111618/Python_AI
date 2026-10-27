#猜数字游戏
# import random
# num=random.randint(1,100)
# while True:
#     guest_num=int(input("请输入猜测的数字："))
#     if guest_num==num:
#         print("猜对了！")
#         break
#     elif guest_num>num:
#         print("猜大了！")
#     else:
#         print("猜小了！")


#练习1：将1-1000之间（含1000）所有的5的倍数的数字累加起来
total=0
for i in range(1,10001):
    if i%5==0:
        total+=i
print(f"1-1000之间（含1000）所有的5的倍数的数字累加起来：{total}")

#练习2：统计字符串“aksdhjaoassdhakjskasahdoiaskjashjk”字符串中有多少个a和k
str="aksdhjaoassdhakjskasahdoiaskjashjk"
count_a=0
count_k=0
for i in str:
    if i=="a":
        count_a+=1
    elif i=="k":
        count_k+=1
print(f"字符串中a的个数：{count_a}")
print(f"字符串中k的个数：{count_k}")