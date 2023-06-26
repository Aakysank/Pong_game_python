from turtle import Turtle


class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.shapesize(stretch_wid=1, stretch_len=1)
    self.penup()
    self.setheading(45)
    self.speed(1)

  def move_ball(self):

    if self.ycor() > 280 and self.heading() == 45:
      self.setheading(315)
    elif self.ycor() < -280 and self.heading() == 315:
      self.setheading(45)
    elif self.ycor() > 280 and self.heading() == 135:
      self.setheading(225)
    elif self.ycor() < -280 and self.heading() == 225:
      self.setheading(135)

    self.forward(1)

  def reset_position(self):
    self.speed(1)
    self.goto(0, 0)
    self.setheading(self.heading() + 180)
