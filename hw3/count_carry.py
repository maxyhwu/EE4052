# count_carry.py
"""A program asking the user to enter two positive integers and returns the exact number of carries if we add the two integers"""

n1 = int(input('enter n1: '))
n2 = int(input('enter n2: '))

if n1 == 0 or n2 == 0:
    print(0)
else:
    cnt = 0
    carry = 0
    while (n1 % 10 != 0 and n1 > 0) or (n2 % 10 != 0 and n2 > 0):
        carry = n1 % 10 + n2 % 10 + carry
        carry /= 10
        if int(carry) > 0:
            cnt += 1
        n1 = int(n1 / 10)
        n2 = int(n2 / 10)
    print(cnt)
