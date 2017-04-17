Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> wn = turtle.Screen()
>>> tutle.Turtle()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tutle.Turtle()
NameError: name 'tutle' is not defined
>>> t1 = turtle.Turtle()
>>> t1 = shape('turtle')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t1 = shape('turtle')
NameError: name 'shape' is not defined
>>> t1.shaple("turlte")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t1.shaple("turlte")
AttributeError: 'Turtle' object has no attribute 'shaple'
>>> t1.shape("turtle")
>>> wn.addshape("C:\Users\maple\Desktop\학교관련\컴사문\computing\99")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wn.addshape(99)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    wn.addshape(99)
  File "C:\Users\maple\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1132, in register_shape
    if name.lower().endswith(".gif"):
AttributeError: 'int' object has no attribute 'lower'
>>> wn.addshape("C:\\Users\\maple\\Desktop\\학교관련\\gg.gif")
>>> t1.shape("C:\\Users\\maple\\Desktop\\학교관련\\gg.gif")
>>> 
