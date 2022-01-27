from paddles import Paddle
from turtle import Turtle, Screen
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
from datetime import datetime

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()
game_on = True
screen.listen()
screen.onkey(paddle.paddle_1_up, "w")
screen.onkey(paddle.paddle_1_down, "s")
screen.update()
screen.onkey(paddle.paddle_2_up, "Up")
screen.onkey(paddle.paddle_2_down, "Down")
saved_time = datetime.now()

while game_on:
    sleep(0.035)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle.paddle1) < 24 or ball.distance(paddle.paddle2) < 24:
        ball.hit()
    if ball.xcor() > 500 or ball.xcor() < -500:
        scoreboard.game_over()
    if ball.distance(paddle.paddle1) < 40:
        scoreboard.score1_update()
    if ball.distance(paddle.paddle2) < 40:
        scoreboard.score2_update()

screen.exitonclick()
