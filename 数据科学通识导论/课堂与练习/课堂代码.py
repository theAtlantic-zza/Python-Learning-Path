r=3
print(r)
s=3.14*r*r
print(s)

# r2 = int(input('请输入圆半径2:'))
# s= 3.14 * r2 * r2
# print(type(r))
# print(s)#s赋值更新

#练习 输入圆的半径,计算周长及面积
#
import math #导入数学模块，用于用Pi计算圆的周长和面积 math是python自带的数据库
#
# r = float(input("请输入圆的半径："))
# circumference = 2 * math.pi * r
# area = math.pi * r ** 2
# print("圆的周长是：", circumference)
# print("圆的面积是：", area)

def area_circle(r):
    return math.pi * r**2
r=2
area_circle(r)#定义完得调用
print(area_circle(r))


def triangle_area(a,h):
    s=1/2*a*h
    return s
tri_area= triangle_area(10,20)
print(tri_area)

import turtle
painter=turtle.Turtle()

painter.pencolor('blue')

for i in range(50):

    painter.forward(50)
    painter.left(123)

painter.pencolor('red')
for i in range(50):
    painter.forward(100)
    painter.left(123)

print(painter.pencolor())
