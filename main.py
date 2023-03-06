from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

TOP_WALL = 280
RIGHT_WALL = 280
BOTTOM_WALL = -280
LEFT_WALL = -280

screen = Screen()
screen.setup(600, 600)
screen.screensize(600, 600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


  
# moving the snake
end_of_game = False

while not end_of_game:
  screen.update()
  time.sleep(0.1)

  snake.move()

  # detect collision with food
  if snake.head.distance(food) < 15:
    food.move()
    score.increase_score()
    snake.extend_snake()

  # detect collision with wall
  if snake.head.xcor() > RIGHT_WALL or snake.head.xcor() < LEFT_WALL or snake.head.ycor() < BOTTOM_WALL or snake.head.ycor() > TOP_WALL:
    score.reset_game()
    snake.reset_snake()
    
    
  # detect collision with tail
  for segment in snake.snakes_list[1:]:
   if snake.head.distance(segment) < 10:
      score.reset_game()
      snake.reset_snake()
