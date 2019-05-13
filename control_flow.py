print(1 == '1')
print((2 > 3) or (5 > 2))

# important things to remember that , there is no bracket for condition and whitespace defines the scopes

if 2 > 3:
    print("hello")
    print("again")
elif 2 == 2:
    print("its true")

# loops
# for loops
# i is the iteration term here

x = [1, 2, 3, 4, 5, 6]

for i in x:
    print(i)
print(x)

dictionary = {'key1': 1, "key2": 2}

for i in dictionary:
    print(i)
    print(dictionary[i])

tuple = [(1, 2), (3, 5)]

for i in tuple:
    print(i)

for i, j in tuple:
    print(i)
    print(j)

# while loop
i = 0
while i < 5:
    print("i is {}".format(i))
    i = i + 1

# range
x = range(5)
print(x)

print(list(range(5)))
print(list(range(0, 5)))
print(list(range(0, 5, 2)))

for i in list(range(5)):
    print(i)

# comprehension
x = [1, 2, 3, 4]
out = []

for i in x:
    out.append(i ** 2)

print(x)
print(out)

# another way

x = [1, 2, 3, 4]

out = [i**2 for i in x]

print(x)
print(out)
