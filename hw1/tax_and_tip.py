# tax_and_tip.py
"""Calculate the tax, the tip, and the total cost of meal."""

cost = float(input('cost of meal: '))
tax = cost * 0.08
tip = cost * 0.18
total = cost + tax + tip
print('tax:     ' + str(tax))
print('tip:     ' + str(tip))
print('total:   ' + str(total))
