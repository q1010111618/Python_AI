#while 循环：打印10遍
# i = 0
# while i < 10:
#     print("hello world")
#     i += 1
# else:
#     print("循环结束")

#案例，计算1-100之间所有偶数的累计之和
i=1
total=0
while i<=100:
    if i%2==0:
        print(f"{total}+{i}={total+i}")
        total+=i
    i+=1
else:
    print(f"1-100之间所有偶数的累计之和：{total}")