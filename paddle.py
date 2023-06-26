from turtle import Turtle


class Paddle(Turtle):

  def __init__(self, startpos):
    super().__init__()
    self.color("white")
    self.shape("square")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.goto(startpos)

  def move_paddle_upwards(self):
    xcoor = self.xcor()
    new_ycor = self.ycor()
    if new_ycor < 240:
      new_ycor += 20
      self.setpos(xcoor, new_ycor)

  def move_padddle_downwards(self):
    xcoor = self.xcor()
    new_ycor = self.ycor()
    if new_ycor > -240:
      new_ycor -= 20
      self.setpos(xcoor, new_ycor)
