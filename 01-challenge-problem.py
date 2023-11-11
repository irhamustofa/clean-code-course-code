class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, starting_point, width, height):
        self.starting_point = starting_point
        self.width = width
        self.height = height
        self.end_points(self)

    def area(self):
        return self.width * self.height

    def end_points(self):
        end_point_x = self.starting_point.x + self.width
        end_point_y = self.starting_point.y + self.height

    def print_points(self):
        print('Starting Point (X)): ' + str(self.starting_point.x))
        print('Starting Point (Y)): ' + str(self.starting_point.y))
        print('End Point X-Axis (Top Right): ' + str(end_point_x))
        print('End Point Y-Axis (Bottom Left): ' + str(end_point_y))


def create_rectangle():
    starting_point = Point(50, 100)
    rectange = Rectangle(starting_point, 90, 10)

    return rectangle


my_rect = create_rectangle()

print(my_rect.area())
my_rect.end_points()
