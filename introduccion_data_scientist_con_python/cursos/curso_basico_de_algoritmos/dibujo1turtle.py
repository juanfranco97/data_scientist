import turtle


myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def draw(myTurtle, lenght):
    if lenght > 0:
        myTurtle.forward(lenght)
        myTurtle.left(90 - lenght/7)
        draw(myTurtle, lenght - 5)

draw (myTurtle, 120)
myWin.exitonclick()