import turtle


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(-40, 250)
        self.write(f"{self.l_score}", align="left", font=("Arial", 24, "normal"))
        self.goto(40, 250)
        self.write(f"{self.r_score}", align="left", font=("Arial", 24, "normal"))

    def left_team_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def right_team_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
    

    
