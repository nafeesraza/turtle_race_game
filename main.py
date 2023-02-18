import turtle as t
import random
src=t.Screen()
src.setup(500, 400)
is_race_on=False
user_bate=src.textinput(title="Make your bate", prompt="Which turtle will the race: ")
color=["green","red","pink","blue","purple","yellow"]
y_position=[-70, -40, -10, 20, 50, 80]
all_turtles=[]
for turtle_index in range(6):
    tim=t.Turtle(shape="turtle")
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(tim)


if user_bate:
    is_race_on=True

stop=False
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color==user_bate:
                print(f"You'hv won! The {winning_color} is the winner!")
            else:
                print(f"You'hv loss! The {winning_color} is the winner!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
src.exitonclick()