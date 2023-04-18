class Car:
    def __init__(self, mpg):
        """
        gallons per 100 miles = 100 / MPG
        Combined driving: 100 / 35 = 2.86 gallons per 100 miles
        City driving: 100 / 30 = 3.33 gallons per 100 miles
        Highway driving: 100 / 43 = 2.33 gallons per 100 miles
        """
        self.miles_per_gallon = mpg
        self.fuel = 0

    def __str__(self):
        return f"This car's consumption is [100 miles / {self.miles_per_gallon}] = " + \
            f"{100 / self.miles_per_gallon:.2f} gallons per 100 miles."

    def add_fuel(self, gallon):
        """
        E.g. 2015 Volkswagen Golf 2015 full tank size 13.2 gallons = 50liters
        """
        if gallon <= 15:
            self.fuel += gallon
        else:
            print("Tank is full, max capacity is 15")

    def get_fuel_capacity(self):
        print(f"{self.fuel:.2f} gallon{'s' if self.fuel > 1 else ''} remaining.")

    def get_range(self):
        """
        Max range with current fuel: Total fuel * car's MPG
        """
        print(f"Can drive {self.fuel * self.miles_per_gallon} miles")
        return self.fuel * self.miles_per_gallon

    def drive(self, distance):
        """
        Can drive if fuel is not empty
        """
        if distance <= self.get_range():
            """
            Consumed = Distance / mpg i.e. 100miles / 35 = 2.85 gallons consumed
            Total fuel - consumed = Remaining fuel
            """
            self.fuel = self.fuel - (distance / self.miles_per_gallon)
        else:
            print("Not enough fuel.")


golf = Car(35)
golf.add_fuel(14.5)
golf.get_fuel_capacity()
print(golf)
golf.drive(100)
golf.get_fuel_capacity()
