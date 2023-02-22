from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0,0)
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.01

    def move_ball(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    def bounce_y(self):
        self.y_move *= -1
        self.xcor() + self.x_move
        self.ycor() + self.y_move
    
    def bounce_x(self):
        self.x_move *= -1
        self.xcor() + self.x_move
        self.ycor() + self.y_move
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.01
    