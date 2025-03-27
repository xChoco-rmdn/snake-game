import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake")
screen.tracer(0)

snake = Snake()
score_display = Score()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score_display.increment()

    # Detect collision with wall
    if (snake.segments[0].xcor() > 280 or
            snake.segments[0].xcor() < -280 or
            snake.segments[0].ycor() > 280 or
            snake.segments[0].ycor() < -280):
        game_is_on = False
        score_display.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False

screen.exitonclick()
