from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Power
def power(n1, n2):
    return n1 ** n2

def calculator():
    # Define all operations
    operations = {'+' : add,
                  "-" : subtract,
                  '*' : multiply,
                  '/' : divide,
                  '**': power}

    # Ask for user input
    num1 = float(input('What\'s the first number?: '))

    # Print available operations
    for key in operations:
        print(key)

    should_continue = True
    while should_continue:
        # Ask for user input
        oper = input('Pick an operation: ')

        num2 = float(input('What\'s the next number?: '))

        # Define and function required for user-specified operation
        function = operations[oper]
        result = function(num1, num2)

        print(f'{num1} {oper} {num2} = {result}')
        cont = input(f'Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ')
        if cont == 'y':
            num1 = result
        else:
            calculator()

if __name__ == '__main__':
    print(logo)
    calculator()