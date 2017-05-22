import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

def giyukAt(size,x,y):
	t1.penup()
	t1.goto(x,y)
	t1.pendown()
	t1.fd(size)
	t1.rt(90)
	t1.fd(size)
	
def nieunAt(size,x,y):
	t1.penup()
	t1.goto(x,y)
	t1.pendown()
        t1.rt(90)
	t1.fd(size)
	t1.lt(90)
	t1.fd(size)

def mieumAt(size,x,y):
    giyukAt(size,x,y)
    t1.lt(90)
    nieunAt(size,x,y)

size = int(input("size"))
x= int(input("x"))
y= int(input("y"))

mieumAt(size,x,y)

wn.exitonclick()
