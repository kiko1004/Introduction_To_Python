def calculator():
    while True:
        num1 = float(input('Enter first number: '))
        op = input('Enter operator (+, -, *, /): ')
        num2 = float(input('Enter second number: '))
        if op == '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        elif op == '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        elif op == '*':
            print(f'{num1} * {num2} = {num1 * num2}')
        elif op == '/':
            print(f'{num1} / {num2} = {num1 / num2}')
        else:
            print('Invalid operator')
        again = input('Do you want to continue? (y/n) ').lower()
        if again != 'y':
            break
