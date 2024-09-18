#UC 3

import math

def compare_lines(line1, line2):
    if line1.length() == line2.length():
        return "The two lines are equal in length."
    elif line1.length() > line2.length():
        return "The first line is greater than the second line."
    else:
        return "The first line is less than the second line."


if __name__ == "__main__":
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    point3 = Point(3, 5)
    point4 = Point(6, 9)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    
    result = compare_lines(line1,line2)
    print(result)

