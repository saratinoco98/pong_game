from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)
        ycor = self.ycor()

    def move_up(self):
        x = self.xcor()
        new_y = self.ycor()
        self.setpos(x, new_y + 20)

    def move_down(self):
        x = self.xcor()
        new_y = self.ycor()
        self.setpos(x, new_y - 20)