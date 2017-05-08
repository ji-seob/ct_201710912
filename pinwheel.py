import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
turnBY=45
def giyuk(size):
	t1.fd(size)
	t1.right(90)
	t1.fd(size)
	t1.penup()
	t1.home()
	t1.pendown()
while turnBY <361:
    giyuk(100)
    t1.right(turnBY)
    turnBY = turnBY+45
wn.exitonclick()
