# integer_sum.py
"""Calculate the sum of the first n positive integers."""

pos_int = input('enter a positive integer: ')
if pos_int == '1':
    print('1 = 1')
elif pos_int == '2':
    print('1 + 2 = 3')
elif pos_int == '3':
    print('1 + 2 + 3 = 6')
else:
    print('1 + 2 + ... + ' + pos_int + ' = ' + str(int(int(pos_int) * (int(pos_int) + 1) / 2)))
