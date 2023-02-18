"""
The factorial of a number is the product of all the integers from 1 to that number. For example, the factorial
of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers, and the factorial of zero is one,
0! = 1. Write a function to find the factorial of a number passed to the function.
"""
import csv

"""
def factorial(n):
    result = 1
    for number in range(1, n+1):
        print(number, end=' ')
        result = result * number
        print(result)

factorial(5)
"""


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


with open('factorial.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["n!", "Factorize"])

    n = int(input("Enter number to factorize: "))
    for i in range(1, n + 1):
        result = factorial(i)
        writer.writerow([f"{i}", f" {result}"])
        print(f"%5s %15s" %(i, result))
