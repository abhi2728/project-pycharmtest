# Get users input

def input_str():
    name = input("Whats your name :")
    print('Hi ' + name + '\n' + 'how are you ' + name)


def input_num():
    num1 = input('Enter a number : ')
    num2 = input('Enter another number : ')
    #ret1 = int(num1) + int(num2)
    #print(ret1)
    ret1 = float(num1) + float(num2)
    print(ret1)

#input_str()
input_num()
