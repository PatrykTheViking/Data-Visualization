from random import choice


class RandomWalk():
    """The class intended to generate the random walk"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]