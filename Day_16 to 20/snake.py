from turtle import Turtle
SNAKE_POSITION = [(00, 00), (-20, 00), (-40, 00)]

class Snake:
    def __int__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for i in SNAKE_POSITION:
            t = Turtle()
            t.shape('square')
            t.color('green')
            t.penup()
            t.goto(i)
            self.segment.append(t)

    def move(self):
        composedSize = len(self.segment)-1
        for i in range(composedSize, 0, -1):
            xcord = self.segment[i - 1].xcor()
            ycord = self.segment[i - 1].ycor()
            self.segment[i].goto(xcord, ycord)
        self.segment[0].forward(10)

