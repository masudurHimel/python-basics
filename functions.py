# function


def my_function(x):
    """
    This is a docstring
    """

    print('my first value is = {}'.format(x))


def add_number(x, y):
    return x + y


my_function(5)

x = add_number(5, 2)
print(x)
print(type(x))

x = add_number('Masudur', ' Rahman')
print(x)
# for datatype
print(type(x))


# for type elaboration


def type_identifier(x, y):
    if type(x) == type(y) == type(5):
        return x + y
    else:
        return "Sorry man !! only integers"


print(type_identifier(5, 3))
print(type_identifier(5, 'Himel'))

# Lambda expression
# filter

myList = [1, 2, 3, 4, 5, 6, 7, 8]


def even_bool(x):
    return x % 2 == 0


x = filter(even_bool, myList)

print(x)
print(list(x))

# for lambda
# this is a lambda expression , generally used for one time function work , is exectable directly
lambda num: num % 2 == 0

x = filter(lambda num: num % 2 == 0,myList)
print(x)
print(list(x))

