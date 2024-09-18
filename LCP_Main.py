print("Welcome to Line Comparison Computation Program on Master Branch")

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    #UC1
    def length(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    #UC2
    def equality(self, l2):
        if self.length() == l2.length():
            return "Same" 
        else:
            return "Different"

if __name__ == "__main__":  
    print("Line 1")
    l1_x1 = int(input("x1 = "))
    l1_y1 = int(input("y1 = "))
    l1_x2 = int(input("X2 = "))
    l1_y2 = int(input("y2 = "))
    print("Line 1")
    l2_x1 = int(input("x1 = "))
    l2_y1 = int(input("y1 = "))
    l2_x2 = int(input("X2 = "))
    l2_y2 = int(input("y2 = "))
    
    point1 = Point(l1_x1, l1_y1)
    point2 = Point(l1_x2, l1_y2)
    point3 = Point(l2_x1,l2_y1)
    point4 = Point(l2_x2,l2_y2)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    
    print(line1.length())
    print(line2.length())

    equality_result = line1.equality(line2)
    print(equality_result)