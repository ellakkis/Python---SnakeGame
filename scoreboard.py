from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 15, "normal")
MOVE = False

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.color("white")
    self.update_scoreboard()


  def update_scoreboard(self):
    self.clear()
    self.color("white")
    self.write(f"Score: {self.score}", MOVE, ALIGN, FONT)
  
  def increase_score(self):  
    self.score += 1
    self.update_scoreboard()

  def game_over(self):
    self.color("white")
    self.goto(0, 0)
    self.write("Game Over", MOVE, ALIGN, FONT)
    
    