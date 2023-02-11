RATE = 0.05
INITIAL_BALANCE = 10000

numYears = int(input("Enter the number of years: "))

balance = INITIAL_BALANCE

print("%5s %12s" %("Year", "BALANCE"))
print("-" * 20)

for year in range(1, numYears+1):
    interest = balance * RATE
    balance = balance + interest
    print("%3d %15.2f" %(year, balance))
print("-" * 20)