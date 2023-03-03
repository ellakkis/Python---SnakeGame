from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

  def __init__(self):
    self.snakes_list = []
    self.create_snake()
    self.head = self.snakes_list[0]

  def create_snake(self):
    for start_pos in STARTING_POSITION:
      self.add_snake(start_pos)
      
  def add_snake(self, position):
    snake = Turtle()
    snake.penup()
    snake.shape("square")
    snake.color("white")
    snake.goto(position)
    self.snakes_list.append(snake)
  
  def extend_snake(self):
    self.add_snake(self.snakes_list[-1].position())

  def move(self):
    for snake_num in range(len(self.snakes_list)-1, 0, -1):
      xcor_snake = self.snakes_list[snake_num - 1].xcor()
      ycor_snake = self.snakes_list[snake_num - 1].ycor()
      self.snakes_list[snake_num].goto(xcor_snake, ycor_snake)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.seth(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.seth(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.seth(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.seth(RIGHT)

  
    