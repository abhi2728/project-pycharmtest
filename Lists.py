# list

def fun_list():
    friends = ['Abhi', 'Vinay', 'Gulla', 'Rajesh', 'Raman', 'Rahul', 'Aniesh']
    # return friends[0][2]
    return friends[1:-1]


def unique_elements():
    friends = ['Abhi', 'Vinay', 'Gulla', 'Rajesh', 'Raman', 'Rahul', 'Aniesh', 'Vinay', 'Abhi', 'Gulla']
    set1 = set(friends)
    return set1


def extend_list():
    friends = ['Abhi', 'Vinay', 'Gulla']
    friends.extend([1, 4, 6, 90])
    friends.reverse()
    return friends


ret = extend_list()
print(ret)
