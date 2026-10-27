from 第2课.my_module.cicle_fun import circle_area


print("========= 计算披萨成本 =========")

# 披萨尺寸（半径，厘米）
s_radius=10 #小号
m_radis=15 #中号
l_radius=20 #大号

#计算面积
small_area=circle_area(s_radius)
middle_area=circle_area(m_radis)
large_area=circle_area(l_radius)

print(f"小号披萨面积：{small_area}")
print(f"中号披萨面积：{middle_area}")
print(f"大号披萨面积：{large_area}")

#成本计算
small_cost=small_area*0.25
middle_cost=middle_area*0.25
large_cost=large_area*0.25

print(f"小披萨面积：{small_cost} cm²，成本：{small_cost:.1f} 元")
print(f"中披萨面积：{middle_cost} cm²，成本：{middle_cost:.1f} 元")
print(f"大披萨面积：{large_cost} cm²，成本：{large_cost:.1f} 元")