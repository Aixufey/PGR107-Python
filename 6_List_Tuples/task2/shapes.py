"""
    1. Determines a shape depending on the number of sides from given input.
    2. Application should support at least 3 sides and including 10 sides.
    3. Display error if beyond.
"""


def shape_collections(N):
    shapes = {
        1: "Sphere",
        2: "Cone",
        3: "Cylinder",
        4: "Tetrahedron",
        5: "Square Pyramid",
        6: "Cube",
        7: "Hexagonal Pyramid",
        8: "Octahedron",
        9: "Nonagon",
        10: "Decagon",
        60: "Triakis icosahedron "
    }
    if N in shapes.keys():
        for key, value in shapes.items():
            if N == key:
                # print(f"{value.capitalize()} has {N} sides.")
                return value

    return None


def geometric_collections(N):
    # list(figure.values()[0]) is a method to retrieve dictionaries with only one value at index 0
    # If a dictionary has multiple k,v pair
    # e.g. {fName: 'Duke', lName: 'Java'} it will be list(figure.values())[1]
    figures = [
        {1: 'Sphere'}, {2: 'Cone'}, {3: 'Cylinder'}, {4: 'Tetrahedron'},
        {5: 'Square Pyramid'}, {6: 'Cube'}, {7: 'Hexagonal Pyramid'}, {8: 'Octahedron'},
        {9: 'Nonagon'}, {10: 'Decagon'}
    ]

    for figure in figures:
        if N in figure:
            # print(f"{list(figure.values())[0]} has {N} sides.")
            return list(figure.values())[0]

    return None


def handle_input():
    N = int(input("Enter sides: "))
    # g = geometric_collections(N)
    s = shape_collections(N)

    if s is not None:
        print(f"{s} has {N} sides.")
    else:
        print(f"{N} is too abstract.")


handle_input()
