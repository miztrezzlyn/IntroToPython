# arithmetic.py
"""Write a script that inputs three integers from the user. Display the sum,
average, product, smallest and largest of the numbers"""

number1 = int(input('Enter your first integer: '))
number2 = int(input('Enter your second integer: '))
number3 = int(input('Enter your third integer: '))

print(('Sum: '), (number1 + number2 + number3), '\n',
      ('Average: '), ((number1 + number2 + number3)/3), '\n',
      ('Product: '), (number1 * number2 * number3), '\n',
      ('Smallest: '), min(number1, number2, number3), '\n',
      ('Largest: '), max(number1, number2, number3), '\n')
