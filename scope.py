# local and global variable

# in order to change a global variable inside a function
x = 25


def global_change():
    # in order to reach he global variable
    global x
    x = 1000


print(x)
global_change()
print(x)
