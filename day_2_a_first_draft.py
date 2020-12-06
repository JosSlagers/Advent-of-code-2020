#!/usr/bin/env python

# first draft of advent of code 2020 day 2a

# Assignment, you're handed a list of password, the assignment requires you to count the number of passwords
# that meet the given password requirements.

# for instance:
# '6-10 s: snkscgszxsssscss' signifies that the password can only contain a minumum of 6 and a maximum of 10
# times the letter 's'. in this case it contains 9 times a 's', so it is in accordance with the policy.
# for the complete assignment see:


import numpy as np

csv_file = np.genfromtxt('password.csv', delimiter=',', dtype=str)
password_list = csv_file[:].tolist()
correct = 0

for x in password_list:
    digits_1 = 0
    digits_2 = -2

    for i in x:
        if i != '-':
            digits_1 += 1
        else:
            break

    for i in x[digits_1:]:
        if i != ':':
            digits_2 += 1
        else:
            break
    lower = int(x[0: digits_1])
    higher = int(x[digits_1:][1:digits_2])
    letter = x[digits_1:][digits_2 + 1]
    password = x[digits_1:][digits_2 + 1:][3:]

    count = 0

    for char in password:
        if char == letter:
            count += 1
    if count in range(lower, higher + 1):
        correct += 1
print(correct)

# The answer here is 414, which is correct, will rewrite the code in order for it be more readable.
