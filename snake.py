from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_squares = []
        self.create_snakes()
        self.head = self.all_squares[0]

    def create_snakes(self):

        for i in STARTING_POSITIONS:
            self.add_square(i)

    def add_square(self, i):
        single_square = Turtle(shape="square")
        single_square.color("white")
        single_square.penup()
        single_square.setposition(i)
        self.all_squares.append(single_square)

    def extend(self):

        self.add_square(self.all_squares[-1].position())

    def move(self):

        for square_now in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[square_now - 1].xcor()
            new_y = self.all_squares[square_now - 1].ycor()
            self.all_squares[square_now].setposition(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(0)
