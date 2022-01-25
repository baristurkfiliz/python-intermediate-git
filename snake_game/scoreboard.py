from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(-40, 280)
        self.write(f"My Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def score_add(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
