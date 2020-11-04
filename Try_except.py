# https://airbrake.io/blog/python-exception-handling/class-hierarchy
# different type of exception in above list

try:
    num = int(input('Enter a number : '))
    print(num)
except ValueError as exception:
    print('Invalid input !!')
    print(exception)
