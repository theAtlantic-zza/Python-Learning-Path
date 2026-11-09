import turtle
import 封装函数


radius = float(input('请输入圆的半径：'))
print('圆的面积：', 封装函数.circle_area(radius))

names = ()
while True:
    name = input('请输入同学姓名，直接回车结束：')
    if name == '':
        break
    names = names + (name,)

name = input('请输入要查找的姓名：')
print(封装函数.find_name(names, name))

heights = {}
while True:
    name = input('请输入同学姓名，直接回车结束：')
    if name == '':
        break
    height = float(input('请输入身高（厘米）：'))
    heights[name] = height

name = input('请输入要比较身高的同学姓名：')
封装函数.find_taller(heights, name)

print(封装函数.draw_blue_red())
print(封装函数.draw_spiral())
turtle.done()
