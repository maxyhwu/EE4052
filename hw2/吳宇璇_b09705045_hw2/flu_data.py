# flu_data.py
"""A program in which the user can input the number of reported infections per day over one week. and get the total, average, smallest, and largest of these values."""

patient = int(input('Enter the additional number of infected patients: '))
total_cnt = patient
patient_max = patient
patient_min = patient

for i in range(6):
    patient = int(input('Enter the additional number of infected patients: '))
    total_cnt += patient
    if patient > patient_max:
        patient_max = patient
    elif patient < patient_min:
        patient_min = patient

print('Total number of reported infected patients in one week: ' + str(total_cnt))
print('Average number of reported infected patients per day: ' + str(round(float(total_cnt / 7), 1)))
print('Smallest number of reported infected patients per day: ' + str(patient_min))
print('Largest number of reported infected patients per day: ' + str(patient_max))
