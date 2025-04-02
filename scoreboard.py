from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as highscore:
            self.high_score = int(highscore.read())
        self.hit_count = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()  # Initial display of score

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.hit_count} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.hit_count > self.high_score:
            self.high_score = self.hit_count
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.hit_count = 0
        self.update_score()

    def increment(self):
        self.hit_count += 1
        self.clear()  # Clear previous score display
        self.update_score()  # Update score display after incrementing