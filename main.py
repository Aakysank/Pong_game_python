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

r_paddle_start_pos = (350, 0)
r_paddle_scoreboard_pos = (150,200)
r_paddle = Paddle(r_paddle_start_pos)
r_paddle_scoreboard = Scoreboard(r_paddle_scoreboard_pos)

l_paddle_start_pos = (-350,0)
l_paddle_scoreboard_pos = (-150,200)
l_paddle = Paddle(l_paddle_start_pos)
l_paddle_scoreboard = Scoreboard(l_paddle_scoreboard_pos)

pong_ball = Ball()

screen.listen()
screen.onkey(key="Up",   fun=r_paddle.move_paddle_upwards)
screen.onkey(key="Down", fun=r_paddle.move_padddle_downwards)
screen.onkey(key="w",   fun=l_paddle.move_paddle_upwards)
screen.onkey(key="s", fun=l_paddle.move_padddle_downwards)

speed = 1
is_game_over = False
while is_game_over == False:
  pong_ball.move_ball()
  if r_paddle.distance(pong_ball) < 50 and pong_ball.xcor() > 320 or l_paddle.distance(pong_ball) < 50 and pong_ball.xcor() < -320:
    if pong_ball.xcor() < -320:
      new_heading = pong_ball.heading() - 90
    else:
      new_heading = pong_ball.heading() + 90

    speed *= 5
    pong_ball.speed(speed)
      
    pong_ball.seth(new_heading)
  elif pong_ball.xcor() > 350:
    pong_ball.reset_position()
    l_paddle_scoreboard.update_score()
    speed = 1
  elif pong_ball.xcor() < -350:
    pong_ball.reset_position()
    r_paddle_scoreboard.update_score()
    speed =1

  time.sleep(0.005/speed)
  screen.update()
