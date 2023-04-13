# sieve_of_eratosthenes.py
"""Implemented the Sieve of Eratosthenes method to find prime numbers."""

intList = [True] * 1000

for i in range(1, 999):
    for j in range(i + 1, 1000):
        if (j + 1)  % (i + 1) == 0:
            intList[j] = False

primeList = []
for i in range(1, 1000):
    if intList[i] == True:
        primeList.append(i + 1)

print(primeList)
