from turtle import*
import random
for i in range(30):
  x = random.randrange(-500,500)
  y = random.randrange(-500,500)
  
#Yeni Kaledonya
a=Turtle()
a.fd(0)
a.fillcolor('blue')
a.begin_fill()
for i in range(2):
  a.forward(50)
  a.right(90)
  a.forward(100)
  a.right(90)
a.end_fill()

a.fd(50)

a.fillcolor('white')
a.begin_fill()
for i in range(2):
  a.forward(50)
  a.right(90)
  a.forward(100)
  a.right(90)
a.end_fill()

a.fd(50)

a.fillcolor('red')
a.begin_fill()
for i in range(2):
  a.forward(50)
  a.right(90)
  a.forward(100)
  a.right(90)
a.end_fill()

#ENDONEZYA
a=Turtle()
a.goto(0,-100)
a.fd(0)
a.fillcolor("red")
a.begin_fill()
a.forward(150)
a.right(90)
a.forward(50)
a.right(90)
a.forward(150)
a.end_fill()

a.fillcolor("white")
a.begin_fill()
a.left(90)
a.forward(50)
a.left(90)
a.forward(150)
a.left(90)
a.forward(50)
a.left(90)
a.forward(150)
a.pu()
a.end_fill()


hideturtle()

#YEMEN
a=Turtle()
a.setheading(-360)
a.goto(0,100)

a.fillcolor('red')
a.begin_fill()
for i in range(2):
  a.right(90)
  a.fd(34)
  a.right(90)
  a.fd(150)
a.end_fill()
a.right(90)
a.fd(34)
a.fillcolor('white')
a.begin_fill()
for i in range(2):
    a.fd(34)
    a.right(90)
    a.fd(150)
    a.right(90)
a.end_fill()
a.fd(34)
a.fillcolor('black')
a.begin_fill()
for i in range(2):
    a.fd(34)
    a.right(90)
    a.fd(150)
    a.right(90)
a.end_fill()

#YUNANİSTAN
a=Turtle()

a.color("blue") 

for i in range(4):
    a.begin_fill()
    for i in range(2):
        a.fd(150)
        a.left(90)
        a.fd(11.11)
        a.left(90)
    a.end_fill()

    a.pu()
    a.left(90)
    a.fd(22.22)
    a.right(90)
    a.pd()
    
a.begin_fill()
for i in range(2):
    a.fd(150)
    a.left(90)
    a.fd(11.11)
    a.left(90)
a.end_fill()

a.pu()
a.left(90)
a.fd(11.11)
a.right(90)
a.pd()

a.begin_fill()
for i in range(4):
    a.fd(55.55)
    a.right(90)
a.end_fill()

a.color("white")
a.pu()
a.fd(22.22)
a.pd()
a.begin_fill()
for i in range(2):
    a.fd(11.11)
    a.right(90)
    a.fd(56)
    a.right(90)
a.end_fill()

a.pu()
a.backward(22.22)
a.right(90)
a.fd(22.22)
a.left(90)
a.pd()

a.begin_fill()
for i in range(2):
    a.fd(56)
    a.right(90)
    a.fd(11.11)
    a.right(90)
a.end_fill()

a.home()
a.color("black")
for i in range(2):
    a.fd(150)
    a.left(90)
    a.fd(100)
    a.left(90)
    
#YUGOSLAVYA

from turtle import Turtle, Screen

WIDTH = 250
HEIGHT = WIDTH * 2 / 3
STAR = HEIGHT / 8
EXPAND = 1.2
TRANSLATION = STAR * EXPAND / 4
CURSOR_SIZE = 15

screen = Screen()

a = Turtle('square', visible=True)
a.penup()
a=Turtle()
a.fillcolor('blue')
a.begin_fill()
for i in range(2):
  a.right(90)
  a.fd(30)
  a.right(90)
  a.fd(150)
a.end_fill()
a.right(90)
a.fd(30)

a.fillcolor('white')
a.begin_fill()
for i in range(2):
    a.fd(30)
    a.right(90)
    a.fd(150)
    a.right(90)
a.end_fill()
a.fd(30)

a.fillcolor('red')
a.begin_fill()
for i in range(2):
    a.fd(30)
    a.right(90)
    a.fd(150)
    a.right(90)
a.end_fill()


a.shape('triangle')
a.shapesize(STAR * EXPAND / 2 / CURSOR_SIZE, STAR * EXPAND / CURSOR_SIZE)
a.pd()
a.fd(-15)
a.left(100)
a.color('red')
a.pu()
a.goto(-72, -42)
for _ in range(5):
    a.right(72)
    a.forward(TRANSLATION)
    a.stamp()
    a.backward(TRANSLATION)
    

screen.mainloop()





done()

