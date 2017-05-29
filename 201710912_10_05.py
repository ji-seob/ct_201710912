import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

width = wn.window_width()

x1 = 0.0 - (width-60)/3
x2 = 0.0
x3 = 0.0 + (width-60)/3
def drawTriangleAT(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    t1.rt(60)
    t1.fd(size)
    t1.right(120)
    t1.fd(size)
    t1.rt(120)
    t1.fd(size)

def drawPentagon(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    t1.rt(108)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
def drawStarAT(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    t1.rt(36)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)

drawTriangleAT(100,x1)
drawPentagon(100,x2)
drawStarAT(100,x3)

win.exitonclick()
