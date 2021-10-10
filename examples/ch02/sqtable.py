# sqtable.py
"""Write a script to calculate the squares and cubes of the numbers 0-5
    and print the resulting values in table format."""

number = 0  # Assign an initial number
print('number\t', 'square\t', 'cube\n')

while number < 6:
    print(number, '\t', number ** 2, '\t', number ** 3, '\n')
    number = number + 1
