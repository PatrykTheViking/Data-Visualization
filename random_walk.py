from random import choice


class RandomWalk():
    """The class intended to generate the random walk"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Direction and distance calculation"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """ Generate all pin points for random walk"""
        while len(self.x_values) < self.num_points:

            # direction and distance set up
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # following x and y values set up
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
