from turtle import Turtle

UP = 90
DOWN = 270


class Paddle:

    def __init__(self):
        self.window_up = Turtle("square")
        self.window_down = Turtle("square")
        self.window_right = Turtle("square")
        self.window_left = Turtle("square")
        self.paddle1 = Turtle("square")
        self.paddle2 = Turtle("square")
        self.windows()
        self.paddle_1()
        self.paddle_2()

    def windows(self):
        # UP FRAME
        self.window_up.up()
        self.window_up.shapesize(0.1, 900)
        self.window_up.speed(0)
        self.window_up.color("white")
        self.window_up.goto(0, 297)
        # DOWN FRAME
        self.window_down.up()
        self.window_down.shapesize(0.1, 900)
        self.window_down.speed(0)
        self.window_down.color("white")
        self.window_down.goto(0, -290)
        # LEFT FRAME
        self.window_left.up()
        self.window_left.shapesize(600, 0.1)
        self.window_left.speed(0)
        self.window_left.color("white")
        self.window_left.goto(-497, 0)
        # RIGHT FRAME
        self.window_right.up()
        self.window_right.shapesize(600, 0.1)
        self.window_right.speed(0)
        self.window_right.color("white")
        self.window_right.goto(490, 0)

    def paddle_1(self):
        self.paddle1.up()
        self.paddle1.speed(0)
        self.paddle1.setheading(UP)
        self.paddle1.goto(-480, 0)
        self.paddle1.shapesize(0.6, 4.3)
        self.paddle1.color("white")
        self.paddle1.speed(0)

    def paddle_1_up(self):
        if self.paddle1.ycor() < 240:
            self.paddle1.setheading(UP)
            self.paddle1.forward(40)

    def paddle_1_down(self):
        if self.paddle1.ycor() > -210:
            self.paddle1.setheading(DOWN)
            self.paddle1.forward(40)

    def paddle_2(self):
        self.paddle2.up()
        self.paddle2.speed(0)
        self.paddle2.setheading(UP)
        self.paddle2.goto(470, 0)
        self.paddle2.shapesize(0.6, 4.3)
        self.paddle2.color("white")
        self.paddle2.speed(0)

    def paddle_2_up(self):
        if self.paddle2.ycor() < 240:
            self.paddle2.setheading(UP)
            self.paddle2.forward(40)

    def paddle_2_down(self):
        if self.paddle2.ycor() > -210:
            self.paddle2.setheading(DOWN)
            self.paddle2.forward(40)