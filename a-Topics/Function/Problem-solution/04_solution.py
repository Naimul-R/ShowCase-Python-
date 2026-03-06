import math

def circle_stats(radius):
    area = round(math.pi * radius ** 2, 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference

a, c = circle_stats(4)
print("Area: ", a, "Circumferance: ", c)