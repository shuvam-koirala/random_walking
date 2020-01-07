import turtle
import random
turtle.reset()
turtle.resetscreen()
turtle.screensize(400,400)
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.pensize(3)
turtle.delay(0.01)
a=10
for i in range(1000):
     step = random.choice(["n","s","e","w"])
     print (step)
     if step == "n":
          turtle.forward(a)
     elif step == "s":

          turtle.backward(a)
     elif step == "e":
          turtle.left(90)
          turtle.forward(a)
     elif step == "w":
          turtle.right(90)
          turtle.backward(a)
