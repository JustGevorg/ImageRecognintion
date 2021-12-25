class Point:

    def __init__(self, x, y: float):
        self.x = round(x, 4)
        self.y = round(y, 4)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
