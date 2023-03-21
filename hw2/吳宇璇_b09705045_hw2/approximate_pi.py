# approximate_pi.py
"""A program displays 15 approximations of pi."""

print("index    approximation")

curr_sum = 3
for i in range (15):
    if i == 0:
        print(str(i + 1) + "        " + str(curr_sum))
    elif i < 9:
        if i % 2 == 1:
            curr_sum += 4 / ((i * 2) * (i * 2 + 1) * (i * 2 + 2))
        else:
            curr_sum -= 4 / ((i * 2) * (i * 2 + 1) * (i * 2 + 2))
        print(str(i + 1) + "        " + str(curr_sum))
    else:
        if i % 2 == 1:
            curr_sum += 4 / ((i * 2) * (i * 2 + 1) * (i * 2 + 2))
        else:
            curr_sum -= 4 / ((i * 2) * (i * 2 + 1) * (i * 2 + 2))
        print(str(i + 1) + "       " + str(curr_sum))
