# scoreboard
    # update score
# ball
    # make it move
    # detect collisions
    # detect when ball reaches edge of screen (goal)
# paddles
    # allow movement
    # detect collision with ball

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")


is_on = True
while is_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.move_speed)

    # detect collision with wall
    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -335 or ball.distance(r_paddle) < 50 and ball.xcor() > 335:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.restart()
        scoreboard.left_team_score()
        scoreboard.update_scoreboard()
            
    if ball.xcor() < -400:
        ball.restart()
        scoreboard.right_team_score()
        scoreboard.update_scoreboard()
            

screen.exitonclick()
