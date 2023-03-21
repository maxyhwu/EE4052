# change_calculator.py
"""Calculate the minimum number of bills and coins needed to make change for a person."""

cost = float(input('How much did the item cost: '))
give = float(input('How much did the person give you: '))
change = round(give - cost, 2)
print("The person\'s change is $" + str(change))
twenties = int(change / 20)
change -= twenties * 20
tens = int(change / 10)
change -= tens * 10
fives = int(change / 5)
change -= fives * 5
ones = int(change / 1)
change -= ones / 1
quarters = int(change * 4)
change -= quarters * 0.25
dimes = int(change * 10)
change -= dimes * 0.1
nickels = int(change * 20)
change -= nickels * 0.05
pennies = round(change * 100)
print(str(twenties) + ' twenties')
print(str(tens) + ' tens')
print(str(fives) + ' fives')
print(str(ones) + ' ones')
print(str(quarters) + ' quarters')
print(str(dimes) + ' dimes')
print(str(nickels) + ' nickels')
print(str(pennies) + ' pennies')

