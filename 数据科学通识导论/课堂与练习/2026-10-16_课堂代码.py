# 练习 2：将姓名保存到列表，并查找姓名
names = []

while True:
    name = input("请输入同学姓名（直接回车结束）：")
    if name == "":
        break
    names.append(name)

target = input("请输入要查找的姓名：")
if target in names:
    print(f"{target} 已保存在列表中")
else:
    print(f"{target} 不在列表中")


# 练习 3：将姓名和身高保存到字典，并查找更高的同学
heights = {}

while True:
    name = input("请输入同学姓名（直接回车结束）：")
    if name == "":
        break
    height = float(input("请输入身高（厘米）："))
    heights[name] = height

target = input("请输入要查找的姓名：")
if target not in heights:
    print("没有找到这位同学")
else:
    target_height = heights[target]
    print(f"比 {target} 高的同学：")
    found = False
    for name, height in heights.items():
        if height > target_height:
            print(f"{name}：{height} 厘米")
            found = True
    if not found:
        print("没有更高的同学")
