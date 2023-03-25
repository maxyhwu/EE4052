# square_root.py
"""A program computing square roots using Newton’s method."""

x = float(input('enter a positive integer: '))
temp = x / 2
print('guess 0: ' + str("%.10f" % temp))

i = 1
while abs(temp ** 2 - x) >= 10 ** (-8):
    temp = (temp + x / temp) / 2
    print('guess ' + str(i) + ':', str("%.10f" % round(temp, 10)))
    i += 1
print('error = ', "%.2e" % abs(temp ** 2 - x))
