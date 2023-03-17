from math import *


def DistanceTwoPoints(x1, y1, x2, y2):
    result = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return result


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

distance = DistanceTwoPoints(x1, y1, x2, y2)
print(f"The distance between the two points is {distance}")
