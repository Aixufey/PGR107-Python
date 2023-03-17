"""
    Triangle can be classified based on the length of the sides
    Equilateral: All three sides are equal
    Isosceles: Two sides are equal
    Scalene: All three sides are different

    Algorithm analysis:
    1. Input from user for minimum 3 sides of a triangle
    2. Check if all sides are equal
    3. Else if any two sides are equal
    4. All sides are different
    5. Print the result accordingly
"""


def handle_triangle(**sides):
    triangle = {
        "Equilateral": sides["a"] == sides["b"] == sides["c"],
        "Isosceles": sides["a"] == sides["b"] or sides["a"] == sides["c"] or sides["b"] == sides["c"],
        "Scalene": sides["a"] != sides["b"] != sides["c"]
    }
    for T, sides in triangle.items():
        if sides:
            print(f"The triangle is {T}")
            break
    else:
        print("Invalid triangle")


def handle_input():
    try:
        a = int(input("Enter side 1: "))
        b = int(input("Enter side 2: "))
        c = int(input("Enter side 3: "))
        handle_triangle(a=a, b=b, c=c)
    except ValueError:
        print("Invalid input\r\nPlease enter a number e.g. '10'.")


handle_input()
