import requests
from lxml import html


# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求，获取数据
response = requests.get(target_url)

# 输出数据到控制台
#print(response.text)
document=html.fromstring(response.text)

#解析数据
#获取表格表头
#这个路径可以从网页按F12定位元素之后右键-》copy->copy xpath  //*[@id="top20"]/thead/tr/th[1]
t_head=document.xpath('//table[@id="top20"]/thead/tr/th/text()')
print(t_head)
#获取表格数据
t_body_tr=document.xpath('//table[@id="top20"]/tbody/tr')
#表格数据按行数组
t_body_list=[]
#将数据按行分组
for tr in t_body_tr:
    t_body_list.append(tr.xpath('td/text()'))
print(t_body_list) 