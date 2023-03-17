def pyramidVolume(height, length):
    base = height * length
    volume = 1 / 3 * height * base
    return volume


heightInput = float(input("Enter the height: "))
lenInput = float(input("Enter the length: "))

result = pyramidVolume(heightInput, lenInput)
print("%50.2f" % result)
