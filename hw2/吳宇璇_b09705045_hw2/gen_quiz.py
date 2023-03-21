# gen_quiz.py
"""A program generating simple math problem."""

import random

problem_cnt = int(input('enter the number of problems: '))
correct_cnt = 0

for i in range(problem_cnt):
    print('\n*** Problem ' + str(i + 1) + ' of ' + str(problem_cnt) + ' ***')
    problem_type = random.randint(0, 2)
    n1 = random.randint(10, 100)
    n2 = random.randint(10, 100)
    if problem_type == 0:
        correct_ans = n1 + n2
        print(str(n1) + ' + ' + str(n2) + ' = ?')
    else:
        if n1 >= n2:
            correct_ans = n1 - n2
            print(str(n1) + ' - ' + str(n2) + ' = ?')
        else:
            correct_ans = n2 - n1
            print(str(n2) + ' - ' + str(n1) + ' = ?')
    if int(input()) == correct_ans:
        print('Good job!')
        correct_cnt += 1
    else:
        print('The answer should be ' + str(correct_ans))

print('\nYour final score is ' + str(100 * round(float(correct_cnt / problem_cnt), 3)))
