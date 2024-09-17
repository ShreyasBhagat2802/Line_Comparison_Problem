#UC 4
import math

class Line_Comparison:
    def calculate_lenghth(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
        length1 = math.sqrt(((self.line1[1][0]) - self.line1[0][0])**2 + ((self.line1[1][1]) - self.line1[0][1])**2)
        print(self.line1)
        print(length1)
        length2 = math.sqrt(((self.line2[1][0]) - self.line2[0][0])**2 + ((self.line2[1][1]) - self.line2[0][1])**2)
        print(self.line2)
        print(length2)

        if (line1 == line2) or (line1 == (line2[1], line2[0])):
            print("Equal lines")
        elif length1 > length2:
            print("Line1 is greater than Line2")
        else:
            print("Line1 is less than Line2")
                

print("Line 1")
l1_x1 = int(input("x1 = "))
l1_y1 = int(input("y1 = "))
l1_x2 = int(input("X2 = "))
l1_y2 = int(input("y2 = "))
l1_co = ((l1_x1,l1_y1),(l1_x2,l1_y2))

print("Line 2")
l2_x1 = int(input("x1 = "))
l2_y1 = int(input("y1 = "))
l2_x2 = int(input("X2 = "))
l2_y2 = int(input("y2 = "))
l2_co = ((l2_x1,l2_y1),(l2_x2,l2_y2))

cls_obj = Line_Comparison()
cls_obj.calculate_lenghth(l1_co, l2_co)

