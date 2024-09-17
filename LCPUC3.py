#UC 3
import math
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


print(l1_co)
length1 = math.sqrt((l1_x2 - l1_x1)**2 + (l1_y2 - l1_y1)**2)
print(length1)
print(l2_co)
length2 = math.sqrt((l2_x2 - l2_x1)**2 + (l2_y2 - l2_y1)**2)
print(length2)

if (l1_co == l2_co) or (l1_co == (l2_co[1], l2_co[0])):
    print("Equal lines")
elif length1 > length2:
    print("Line1 is greater than Line2")
else:
    print("Line1 is less than Line2")