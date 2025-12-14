import turtle
screen = turtle.Screen()
screen.title("Basic turtle ==> square")
screen.bgcolor("white")
t = turtle.Turtle()
t.shape("circle")
t.speed(10)


t.pencolor("black")
t.fillcolor("grey")
t.pensize(5)

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.right(120)
    
t.end_fill

turtle.done()