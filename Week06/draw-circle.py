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

x = turtle.Turtle()
y = 100
z = 5
a = 360.0 / y
 
for i in range(y):
    x.forward(z)
    x.right(a)
   
turtle.done()