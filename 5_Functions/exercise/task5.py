import datetime
import sys
import csv


def temperatureConversion():
    while True:
        choice = input("Select 1 for fahrenheit\r\nSelect 2 for celsius\r\nEnter: ")
        if choice != "1" and choice != "2":
            return None
        try:
            date = datetime.datetime.now().strftime("%m/%d/%y %H:%M")
            if choice == "1":
                F = int(input("Enter Fahrenheit: "))
                to_celsius = str((5 / 9) * (F - 32))[:4]
                print(f"{date}| {to_celsius}C")
                toCSV(date, F, to_celsius)
            else:
                C = int(input("Enter Celsius: "))
                to_fahrenheit = str((9 / 5) * C + 32)[:4]
                print(f"{date}| {to_fahrenheit}F")
                toCSV(date, to_fahrenheit, C)
        except ValueError:
            print("Invalid value")
            continue
        else:
            again = input("Run again? y/n\r\nEnter: ").lower().strip()
            if again not in ["y", "n"]:
                sys.exit(0)
            elif again == "n":
                sys.exit(0)
            else:
                continue


def toCSV(date, fahrenheit, celsius):
    with open("temperature.csv", "a", newline="") as csvFile:
        writer = csv.writer(csvFile)
        if csvFile.tell() == 0:
            writer.writerow(["Date", "Fahrenheit", "Celsius"])
        writer.writerow([date, fahrenheit, celsius])


temperatureConversion()
