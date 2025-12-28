import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("Basic turtle ==> square")
screen.bgcolor("white")
t.shape("circle")
t.pensize(5)
t.fillcolor("grey")
t.pencolor("black")
t.speed(10)
t.begin_fill
for i in range (5):
    t.forward(100)
    t.right(72)
t.end_fill

