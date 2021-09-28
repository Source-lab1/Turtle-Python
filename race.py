from turtle import Turtle , Screen
import random
import turtle

is_race_on = False
scr = Screen()
scr.setup(500,400)
user_bet = scr.textinput(title="Make your bet",prompt= "Which turtle will win the race ? Enter the Color : ")
# print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for i in range(6):
    n_tim = Turtle(shape="turtle")
    n_tim.color(colors[i])
    n_tim.penup()
    n_tim.goto(x=-230,y=y_positions[i])
    all_turtles.append(n_tim)

if user_bet:
    is_race_on= True

while is_race_on:
    for turt in all_turtles:
        if turt.xcor() > 230:
            is_race_on=False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print("You've won! The {} turtle is the winner! ".format(winning_color))
            else:
                print("You've lost! The {} turtle is the winner! ".format(winning_color))
        rand_dis = random.randint(1,11)
        turt.forward(rand_dis)

scr.exitonclick()