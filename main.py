import turtle as turtle_module
import random
import time
screen = turtle_module.Screen()
screen.setup(800, 800)
ted = turtle_module.Turtle()
screen.bgcolor("black")

ted.shape("turtle")
ted.shapesize(20,20,20)

directions = [0, 90, 180, 270, 360]
colours = ['violet','indigo','blue','green','yellow','orange','red']

dancing = True

while dancing == True:
    ted.color(random.choice(colours))
    time.sleep(0.4)
    ted.setheading(random.choice(directions))

screen.exitonclick()
