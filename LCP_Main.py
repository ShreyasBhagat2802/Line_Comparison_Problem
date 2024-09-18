import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)
    
    def equality(self, l2):
        if self.length() == l2.length():
            return "Same"
        else:
            return "Different"

    def compare_lines(self, l2):
        if line1.length() == line2.length():
            return "The two lines are equal in length."
        elif line1.length() > line2.length():
            return "The first line is greater than the second line."
        else:
            return "The first line is less than the second line."

if __name__ == "__main__":
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    line = Line(point1, point2)
    
    print(f"Length of the line: {line.length()}")

    point3 = Point(3, 5)
    point4 = Point(6, 4)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    
    print(line1.length())
    print(line2.length())

    equality_result = line1.equality(line2)
    print(equality_result)

    compare_lines_result = line1.compare_lines(line2)
    print(compare_lines_result)