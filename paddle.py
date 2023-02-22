from turtle import Turtle, width
UP = 90
DOWN = 270
 

class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto((location))
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=0.8)
    
    def move_up(self):
        new_y = self.ycor() + 15
        self.goto((self.xcor(), new_y))

    def move_down(self):
        new_y = self.ycor() - 15
        self.goto((self.xcor(), new_y))