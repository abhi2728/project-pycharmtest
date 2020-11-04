from matplotlib import pyplot as plt1

x = [1, 2, 3]
y = [1, 4, 9]
z = [15, 2, 0]
a = [17, 21, 30]

plt1.plot(x, y)
plt1.plot(x, z)
plt1.plot(x, a)
plt1.title('Test Plot')
plt1.xlabel('X Values')
plt1.ylabel('Y Values')
plt1.legend(["This is Y", "This is Z", "This is A"])
plt1.show()


