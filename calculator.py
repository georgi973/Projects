# take inputs
n1 = float(input('Enter first number: '))
n2 = float(input('Enter second number: '))
# choise operation
print('Operation: +, -, *, /')
command = input('Select operations: ')
# check operations and display result
# add(+) two numbers
if command == '+':
    print(n1, '+', n2, '=', n1 + n2)
# subtract(-) two numbers
elif command == '-':
    print(n1, '-', n2, '=', n1 - n2)
# multiplies(*) two numbers
elif command == '*':
    print(n1, '*', n2, '=', n1 * n2)
# devides(/) two numbers
elif command == '/':
    print(n1, '/', n2, '=', n1 / n2)
else:
    print('Invalid command!')