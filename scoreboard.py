from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hit_count = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()  # Initial display of score

    def update_score(self):
        self.write(f"Score: {self.hit_count}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment(self):
        self.hit_count += 1
        self.clear()  # Clear previous score display
        self.update_score()  # Update score display after incrementing