from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(0, 250)
        self.write(f"{self.score_1}   :   {self.score_2}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def score1_update(self):
        self.score_1 += 1
        self.clear()
        self.update_scoreboard()

    def score2_update(self):
        self.score_2 += 1
        self.clear()
        self.update_scoreboard()