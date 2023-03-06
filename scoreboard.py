from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 15, "normal")
MOVE = False

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.highest_score = self.get_highest_score()
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.color("white")
    self.update_scoreboard()


  def update_scoreboard(self):
    self.clear()
    self.color("white")
    self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", MOVE, ALIGN, FONT)
  
  def increase_score(self):  
    self.score += 1
    self.update_scoreboard()

  def reset_game(self):
    if self.score > self.highest_score:
      self.highest_score = self.score
      self.save_highest_score()
      self.score = 0
      self.update_scoreboard()

  def get_highest_score(self):
    with open("score.txt") as file:
      return int(file.read())

  def save_highest_score(self):
    with open("score.txt", mode="w") as file:
      file.write(f"{self.highest_score}")
    
  # def game_over(self):
  #   self.color("white")
  #   self.goto(0, 0)
  #   self.write("Game Over", MOVE, ALIGN, FONT)
    
    