# dog_years.py
"""A program converting from human years to dog years."""

dog_year = float(input("enter the dog years: "))
human_year = 0

if dog_year < 0:
    print("Error! Negative dog years.")
else:
    if dog_year <= 2:
        human_year = dog_year * 10.5
    else:
        human_year = 2 * 10.5 + (dog_year - 2) * 4

    print(str(dog_year) + " dog years = " + str(human_year) + " human years")
