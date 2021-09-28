# import random
# from turtle import Turtle,Screen,colormode

# t=Turtle()

# colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color


# directions = [0,90,180,270]
# t.pensize(15)
# t.speed("fastest")

# for i in range(200):
#     t.color(random_color())
#     t.forward(30)
#     t.setheading(random.choice(directions))

# # def sides_shape(num_of_sides):
# #   for i in range (num_of_sides):
# #     angle=360/num_of_sides
# #     t.forward(100)
# #     t.right(angle)
    

# # for i in range(3,11):
# #     t.color(random.choice(colours))
# #     sides_shape(i)




# scr=Screen()
# scr.exitonclick()



# import turtle as turtle_module
# import random

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)









# screen = turtle_module.Screen()
# screen.exitonclick()
# import turtle as t
# import random



# t.colormode(255)
# # tim = t.Turtle()
# t.speed("fastest")
# t.penup()
# t.hideturtle()
# color_list = [(202, 164, 164), (240, 245, 245), (236, 239, 239), (149, 75, 75), (222, 201, 201), (53, 93, 93), (170, 154, 154), (138, 31, 31), (134, 163, 163), (197, 92, 92), (47, 121, 121), (73, 43, 43), (145, 178, 178), (14, 98, 98), (232, 176, 176), (160, 142, 142), (54, 45, 45), (101, 75, 75), (183, 205, 205), (36, 60, 60), (19, 86, 86), (82, 148, 148), (147, 17, 17), (27, 68, 68), (12, 70, 70), (107, 127, 127), (176, 192, 192), (168, 99, 99)]

# t.setheading(225)
# t.forward(300)
# t.setheading(0)
# num_of_dots = 100

# for i in range(1,num_of_dots+1):
#     t.dot(20,random.choice(color_list))
#     t.forward(50)
#     if i %10 == 0:
#         t.setheading(90)
#         t.forward(50)
#         t.setheading(180)
#         t.forward(500)
#         t.setheading(0)

# screen = t.Screen()
# screen.exitonclick()

# from turtle import *
# import turtle as t
# import random
# t.speed("fastest")
# penup()
# hideturtle()
# for i in range(15):
#     color("Black")
#     write(i,align="center")
#     right(90)
#     penup()
#     forward(10)
#     pendown()
#     forward(150)
#     penup()
#     backward(160)
#     left(90)
#     forward(20)
# akshay=Turtle()
# akshay.color("Red")
# akshay.shape("turtle")
# akshay.penup()
# akshay.goto(0,-30)
# akshay.pendown()

# aks=Turtle()
# aks.color("Blue")
# aks.shape("turtle")
# aks.penup()
# aks.goto(0,-60)
# aks.pendown()

# gaurav=Turtle()
# gaurav.color("Black")
# gaurav.shape("turtle")
# gaurav.penup()
# gaurav.goto(0,-90)
# gaurav.pendown()
# saurabh=Turtle()
# saurabh.color("Green")
# saurabh.shape("turtle")
# saurabh.penup()
# saurabh.goto(0,-120)
# saurabh.pendown()
# for i in range(100):
#     akshay.forward(random.randint(1, 5))
#     aks.forward(random.randint(1, 5))
#     gaurav.forward(random.randint(1, 5))
#     saurabh.forward(random.randint(1, 5))
#     if aks.position()>=(280,-60):
#         print("aks win")
#         break
#     if akshay.position()>=(280,-30):
