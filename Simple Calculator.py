num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number : "))
op = input("Enter operation : ")


def operation(opr, a, b):
    if opr == '+' or opr == 'PLUS':
        return a + b
    elif opr == '-' or opr == 'MINUS':
        return a - b
    elif opr == '*' or opr == 'MULTIPLY':
        return a * b
    elif opr == '/' or opr == 'DIVIDE':
        return a / b
    else:
        return('Invalid operation')


ret = operation(op.upper(), num1, num2)
print(ret)
