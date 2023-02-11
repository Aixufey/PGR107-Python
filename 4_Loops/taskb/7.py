ROWS = 5

for row in range(1, ROWS + 1):
    for col in range(1, ROWS + 1):
        if col == 1 or col == 2 or (row == 5):
            print("X", end=' ')
        else:
            print(" ", end=' ')
    print("\r")