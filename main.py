
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
#screen.onkey(key="c", fun=clear_screen)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    # detect collision with food using distance
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_scoreboard()
        snake.reset_snake()

    #detect collusion with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()



