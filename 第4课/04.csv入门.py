#csv操作 ---方式一：文件操作的原始方式


#写
# with open('csv_data/01.csv', 'w', encoding='utf-8') as csvfile:
#     csvfile.write("姓名,年龄,身高\n")
#     csvfile.write("tom,18,183\n")
#     csvfile.write("jack,18,178\n")
#     csvfile.write("rose,18,165\n")
#     csvfile.write("jerry,18,170\n")


#读
# with open('csv_data/01.csv', 'r', encoding='utf-8') as csvfile:
#     for row in csvfile:
#         print(row.strip())


#csv操作 ---方式二：csv模块
import csv

# newline='' 表示不换行
# with open('csv_data/02.csv', 'w', encoding='utf-8',newline='') as csvfile:
#     writer=csv.DictWriter(csvfile, fieldnames=['姓名', '年龄', '身高'])
#     writer.writeheader()#写入表头
#     #写入数据
#     writer.writerow({'姓名': 'tom', '年龄': '18', '身高': '183'})
#     writer.writerow({'姓名': 'jack', '年龄': '18', '身高': '178'})
#     writer.writerow({'姓名': 'rose', '年龄': '18', '身高': '165'})
#     writer.writerow({'姓名': 'jerry', '年龄': '18', '身高': '170'})

#读取csv文件
with open('csv_data/02.csv', 'r', encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)