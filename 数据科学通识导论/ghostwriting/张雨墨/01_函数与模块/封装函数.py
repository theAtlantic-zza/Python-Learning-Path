import math
import turtle


def circle_area(radius):
    area = math.pi * radius * radius
    return area


def find_name(names, name):
    if name in names:
        return '这个姓名已保存在元组中'
    else:
        return '元组中没有这个姓名'


def find_taller(heights, name):
    if name not in heights:
        print('没有找到这位同学')
        return

    found = False
    for student in heights:
        if heights[student] > heights[name]:
            print(student, heights[student], '厘米')
            found = True
    if found == False:
        print('没有比这位同学更高的人')


def draw_blue_red():
    pen = turtle.Turtle()
    pen.pencolor('blue')
    for i in range(50):
        pen.forward(50)
        pen.left(123)

    pen.pencolor('red')
    for i in range(50):
        pen.forward(100)
        pen.left(123)
    return '蓝红图案绘制完成'


def draw_spiral():
    pen = turtle.Turtle()
    for i in range(20):
        pen.forward(i * 10)
        pen.right(144)
    return '螺旋图案绘制完成'
