from lxml import html
import requests

# 获取页面内容
page = requests.get('https://www.tiobe.com/tiobe-index/')

# 解析页面内容，将其转换为一个html文档对象
tree = html.fromstring(page.text)

# 获取标题
# /html/head/title: 从根节点开始，找到head节点，然后找到title节点
# //html/head/title: 从任一位置开始匹配
title = tree.xpath('//title/text()')[0]
print(title)

# tr[2]: 匹配第2个tr标签
td_list = tree.xpath('//tr[2]/td/text()')
print(td_list)

# last(): 匹配最后一个元素
# 倒数第二个tr标签 last()-1
td_list = tree.xpath('//tr[last()]/td/text()')
print(td_list)

# p[@class]: 表示匹配有class属性的p标签
# p[@class='class-name']: 表示匹配有class属性为class-name的p标签
# p[@class='class-name']/text(): 表示匹配有class属性为class-name的p标签，然后获取其文本内容
#p_text = tree.xpath('//p[@class="class-name"]/text()')[0]
#print(p_text)


# @src: 表示元素上的src属性
# @*：表示获取元素上的所有属性
# <img src="",alt="123">