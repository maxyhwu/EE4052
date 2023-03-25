# tortoise_and_hare.py
"""A program using random number to simulate the race of the tortoise and the hare."""

import time
import random
turtoise = 1
hare = 1
finish = False
elapse = 0

def turtoise_move():
    prob = random.randint(1, 10)
    if prob <= 5:
        return 3
    elif prob <= 7:
        return -6
    else:
        return 1

def hare_move():
    prob = random.randint(1, 10)
    if prob <= 2:
        return 0
    elif prob <= 4:
        return 9
    elif prob <=5:
        return -12
    elif prob <= 8:
        return 1
    else:
        return -2

print('ON YOUR MARK, GET SET\nBANG !!!!!\nAND THEY\'RE OFF !!!!!')
while finish == False:
    while turtoise < 70 and hare < 70:
        elapse += 1
        turtoise += turtoise_move()
        turtoise = min(70, max(turtoise, 1))
        hare += hare_move()
        hare = min(70, max(hare, 1))

        if hare == turtoise:
            print('OUCH!!!', end = '')
        else:
            for i in range(1,71):
                if i == turtoise:
                    print('T', end = '')
                elif i == hare:
                    print('H', end = '')
                else:
                    print(' ', end = '')
       # print(f'T = {turtoise}, H = {hare}')
        print('')
        #time.sleep(1)
    if turtoise >= 70:
        finish = True
        print('TORTOISE WINS!!! YAY!!!')
    elif hare >= 70:
        finish = True
        print('Hare wins. Yuch!')
    else:
        turtoise = 1
        hare = 1

print(f'TIME ELAPSED = {elapse} seconds')

