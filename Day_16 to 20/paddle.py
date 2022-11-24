from turtle import Turtle , Screen ,exitonclick
class Paddle(Turtle):
    def __init__(self,cordx,cordy):
        super().__init__()
        paddle = Turtle()
        self.shape('square')
        self.penup()
        self.shapesize(5, 1)
        self.color('white')
        self.goto(cordx, cordy)

    def go_down(self):
        new_cordx = self.ycor() +20
        self.goto(self.xcor(),new_cordx)
    def go_up(self):
        new_cordy = self.ycor() -20
        self.goto(self.xcor(),new_cordy)


