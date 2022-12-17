from turtle import Turtle


class States(Turtle):

    def __init__(self, name, location):
        """ name is an str,
            location is a tuple of coordinates,
        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(location)
        self.write(name)
