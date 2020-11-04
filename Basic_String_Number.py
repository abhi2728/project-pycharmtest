def function1():
    print('Hello')
    print('Bye')


def print_triangle():
    print("    /|")
    print("   / |")
    print("  /  |")
    print(" /   |")
    print("/____|")


def play_string():
    print("Play School")
    print("Play \nSchool")
    print("Play \"School\"")
    print("\"Play School\"")
    str1 = 'Movie is good'
    print('Lower : ' + str1.lower() + '\nUpper : ' + str1.upper() + '\nFirst Later Capital : ' + str1.capitalize())
    print(str1.replace('o', '$$', 2))


from math import *


def play_num():
    print(pow(5, 2))
    print(max(2, 6, 7, 8, 9, 4, 5, 78, 32, 67))
    print(max('Abhishek', 'Vinay', 'Rajesh'))
    print(round(3.64567, 2))
    print(floor(9.6456))
    print(ceil(9.0001))
    print(round(sqrt(9)))


print('This is outside function1')
# function1()
print_triangle()
# play_string()
#play_num()
