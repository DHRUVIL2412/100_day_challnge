from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')

    def move(self):
        self.penup()
        cordx = self.xcor()+10
        cordy = self.ycor()+10
        self.goto(cordx,cordy)
