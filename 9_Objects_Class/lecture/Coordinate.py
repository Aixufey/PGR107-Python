class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __add__(self, other):
        # return the sum of both object's x & y
        x = self.x + other.x
        y = self.y + other.y
        return Coordinate(x, y)

    def distance(self, other):
        x = (self.x - other.x) ** 2
        y = (self.y - other.x) ** 2
        return (x + y) ** 0.5


c1 = Coordinate(3, 5)
c2 = Coordinate(6, 2)

print(c1)
print(c2)

# print(c1 + c2) can't add two objects, we need to define __add__
print(c1 + c2)

print(c2.distance(c1))
