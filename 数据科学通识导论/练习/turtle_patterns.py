import turtle


def draw_blue_red():
    painter = turtle.Turtle()
    painter.pencolor("blue")
    for _ in range(50):
        painter.forward(50)
        painter.left(123)

    painter.pencolor("red")
    for _ in range(50):
        painter.forward(100)
        painter.left(123)

    return "蓝红图案绘制完成"


def draw_spiral():
    spiral = turtle.Turtle()
    for i in range(20):
        spiral.forward(i * 10)
        spiral.right(144)

    return "螺旋图案绘制完成"
