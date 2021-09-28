from turtle import Turtle , Screen

tim = Turtle()

scr = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


scr.listen() 
scr.onkey(move_forward,"s")
scr.onkey(move_backward,"w")
scr.onkey(turn_left,"a")
scr.onkey(turn_right,"d")
scr.onkey(clear,"c")

scr.exitonclick()