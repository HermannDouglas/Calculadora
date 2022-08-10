def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction 
    * for multiplication
    / for divisio
    ''')

    number_1 = int(input('Enter your first number:'))
    number_2 = int(input('Enter your second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('You have not type a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
                do you want to calculate again?
                Please type Y for YES ir N for NO.
                ''')

    if calc_again.upper() == 'Y':   
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()