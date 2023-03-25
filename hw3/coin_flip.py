# coin_flip.py
"""A program performing coin flip simulation."""

import random
total = 0
for i in range(10):
    flip = 0
    cnt = 1
    prev = -1
    while cnt < 3:
        flip += 1
        k = random.randint(0, 1)
        if k == 0:
            print('H ', end='')
        else:
            print('T ', end='')
        if k == prev:
            cnt += 1
        else:
            prev = k
            cnt = 1
    print(f'({flip} flips)')
    total += flip

total /= 10
print(f'On average, {total:.1f} flips were needed.')
