# function exercise

print("Problem 1\n")


def array_check(x):
    i = 0
    flag = False
    while i < len(x) - 2:
        if x[i] == 1:
            if x[i + 1] == 2:
                if x[i + 2] == 3:
                    flag = True
                    break
        i = i + 1
    return flag


x1 = [1, 1, 2, 3, 1]
x2 = [1, 1, 2, 4, 1]
x3 = [1, 1, 2, 1, 2, 3]

x = array_check(x1)
print(x)
x = array_check(x2)
print(x)
x = array_check(x3)
print(x)
print()

# problem 2
print("Problem 2\n")


def string_bits(x):
    result = x[::2]
    return result


x1 = "Hello"
x2 = "Hi"
x3 = "Heeololeo"

x = string_bits(x1)
print(x)
x = string_bits(x2)
print(x)
x = string_bits(x3)
print(x)
print()
# problem 3
print("Problem 3\n")


# we can do it with endswith method

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    if len(a) > len(b):
        x = a
        y = b
    else:
        x = b
        y = a

    temp = x[len(x) - len(y):]
    if temp == y:
        return True
    else:
        return False


x = "abc"
y = "abXabc"
result = end_other(x, y)
print(result)

# problem 4
print("\nProblem 4\n")


def double_char(x):
    result = ""
    for i in x:
        result += 2 * i

    print(result)


double_char("Hi-There")

# problem 5
print("\nproblem 5\n")


def no_teen_sum(a, b, c):
    x = fix_teen(a)
    y = fix_teen(b)
    z = fix_teen(c)

    return x + y + z


def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    else:
        return n


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))

# problem 6

print("\nproblem 6\n")


def count_evens(x):
    result = 0
    for i in x:
        if i % 2 == 0:
            result += 1

    return result


x = [1, 2, 3, 4, 5, 6]
y = [2, 2, 0]
z = [1, 3, 5]
print(count_evens(z))
