import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
def giyuk(size):
	t1.fd(size)
	t1.right(90)
	t1.fd(size)
	t1.penup()
	t1.home()
	t1.pendown()
for turn in range(1,9):
    giyuk(100)
    t1.right(45*turn)
wn.exitonclick()
