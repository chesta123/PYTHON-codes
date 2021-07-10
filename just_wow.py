import turtle
a = turtle.Turtle()
a.getscreen().bgcolor("black")
a.penup()
a.goto(-200,100)
a.pendown()
a.color("yellow")
a.speed(25)
def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
for i in range(15):
        turtle.forward(6)
star(turtle,3)
turtle.left(216)
turtle.end_fill()
star(a,360)
turtle.done()
