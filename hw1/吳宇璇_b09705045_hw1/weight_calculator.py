# weight_calculator.py
"""Calculate the total weight of Widgets and Gizmos."""

widget = int(input('enter widget count: '))
gizmo = int(input('enter gizmo count: '))
print('The total weight is ' + str(widget*75 + gizmo*112) + ' grams.')
