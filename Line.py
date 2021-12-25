from Point import Point
import operator
import math


class Line:

    def __init__(self, point0, point1: Point):
        self.start = sorted([point0, point1],
                            key=operator.attrgetter('x'))[0]
        self.end = sorted([point0, point1],
                          key=operator.attrgetter('x'))[1]
        self.a = round((self.start.y - self.end.y) / (self.start.x - self.end.x), 4)
        self.b = round(self.start.y - self.a * self.start.x, 4)
        self.lenght = math.sqrt(math.pow(self.start.x - self.end.x, 2) + math.pow(self.start.y - self.end.y, 2))

    def get_value(self, x):
        return round(self.a * x + self.b, 4)

    def get_points(self):
        return self.start, self.end

    def own_line(self, point):
        len_to_end = math.sqrt(math.pow((self.end.x - point.x), 2) + math.pow((self.end.y - point.y), 2))
        len_to_start = math.sqrt(math.pow((self.start.x - point.x), 2) + math.pow((self.start.y - point.y), 2))
        return len_to_start + len_to_end == self.lenght

    def intersection(self, line):
        if self.a - line.a != 0:
            i_x = round((line.b - self.b) / (self.a - line.a), 4)
            i_y = round(self.get_value(i_x), 4)
            intersection_point = Point(i_x, i_y)
            if line.own_line(intersection_point) and self.own_line(intersection_point):
                return intersection_point
            else:
                return -1.0
        else:
            return -1.0