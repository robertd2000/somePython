import matplotlib.pyplot as plt
from random import choice


class Random_walk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walK(self):
        while len(self.x_values) < self.num_points:
            # x_direction = choice([1, -1])
            # x_distance = choice([0, 1, 2, 3, 4])
            x_step = self.get_step()

            # y_direction = choice([1, -1])
            # y_distance = choice([0, 1, 2, 3, 4])
            y_step = self.get_step()

            if y_step == 0 and x_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


while True:
    rw = Random_walk(5000)
    rw.fill_walK()
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=5)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
