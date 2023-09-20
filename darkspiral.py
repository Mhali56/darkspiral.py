import turtle 

dist = 2
flag = 500
spiral = turtle.Turtle()
turtle.bgcolor("black")
spiral.speed(10)

while flag >0:
    spiral.forward(dist)
    spiral.color("aqua")
    spiral.left(120)
    spiral.left(3)
    dist += 3
    flag -= 3
turtle.done()

 