import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
turnBY = 45
size = 100
def giyuk(size):
	t1.fd(size)
	t1.right(90)
	t1.fd(size)
oldPos = t1.pos()
oldHead = t1.heading()
giyuk(100)
t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBY)
t1.pendown()

giyuk(100)
t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBY*2)
t1.pendown()

giyuk(100)
t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBY*3)
t1.pendown()

giyuk(100)
t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBY*4)
t1.pendown()

giyuk(100)
t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBY*5)
t1.pendown()

giyuk(100)
t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBY*6)
t1.pendown()

giyuk(100)
t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBY*7)
t1.pendown()

giyuk(100)
t1.penup()
t1.setpos(oldPos)
t1.setheading(oldHead+turnBY*8)
t1.pendown()
wn.exitonclick()
