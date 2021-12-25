from Line import Line

class Figure:

    def __init__(self, *lines: Line):
        self.all_lines = []
        for line in lines:
            self.all_lines.append(line)

    def get_lines(self):
        return self.all_lines