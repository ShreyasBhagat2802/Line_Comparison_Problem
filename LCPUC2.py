#UC 2
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def equality(self, l2):
        if self.length() == l2.length():
            return "Same" 
        else:
            return "Different"

if __name__ == "__main__":
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    point3 = Point(3, 5)
    point4 = Point(6, 9)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    
    print(line1.length())
    print(line2.length())

    equality_result = line1.equality(line2)
    print(equality_result)