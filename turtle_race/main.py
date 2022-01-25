from turtle import Turtle, Screen
from random import randint

race_on = False
screen = Screen()
screen.setup(1000, 550)
colors = ["red", "blue", "green", "black", "brown"]
y_position = [212, 112, 12, -88, -188]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.hideturtle()
    new_turtle.shapesize(3)
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.setposition(-450, y_position[turtle_index])
    new_turtle.showturtle()
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 400:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                race_on = False
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                race_on = False
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()