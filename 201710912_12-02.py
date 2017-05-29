import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
width = wn.window_width()
height=wn.window_height()
w = (width-60)/3
h = height/3
x1 = 0.0 - w
x2 = 0.0
x3 = 0.0 + w

y1 = 0.0-h
y2 = 0.0
y3 = 0.0+h

size1 = 100
size2 = 100
size3 = 100

i=0

def drawSquareAT(x1,y1, size1):
    t1.penup()
    t1.goto(x1,y1)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    for i in range(0,4):
        t1.rt(90)
        t1.fd(size1)


def drawTriangleAT(x2,y2,size2):
    t1.penup()
    t1.goto(x2,y2)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    t1.rt(60)
    t1.fd(size2)
    for i in range(0,2):
        t1.rt(120)
        t1.fd(size2)


def drawStarAT(x3,y3,size3):
    t1.penup()
    t1.goto(x3,y3)
    t1.setheading(0)
    t1.pendown()
    t1. write(t1.pos())
    t1.rt(36)
    t1.fd(size3)
    for i in range(0,4):
        t1.rt(144)
        t1.fd(size3)


drawSquareAT(x1,y1,size1)

i=0
                   
drawTriangleAT(x2,y2,size2)

i=0
                   
drawStarAT(x3,y3,size3)

wn.exitonclick()
