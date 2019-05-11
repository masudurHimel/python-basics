# list is like an array

x = [1, 2, 3, 'Himel', True]

print(x)

print(x[-1])
print(x[0])

# splice also works well as the strings

print(x[2:4])
print(x[::2])

# overwriting possible
x[0] = 'New Item'

print(x)

x.append('Khela hbe')
print(x)

# for  nested lists

x.append(['a', 'b', 'c'])
print(x)
print(x[6])
# for getting the nested  list's value

print(x[6][1])

# to make a nested list as a normal element

x.extend(['a', 'b', 'c'])
print(x)

# to remove the last item
item = x.pop()
print(x)

# to remove item with index position
item = x.pop(6)
print(x)

# reverse order

x.reverse()
print(x)
x.reverse()
print(x)

# for sorting
x = [5, 2, 1, 3]
x.sort()
print(x)

# matrix
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(x)
print(x[0])
print(x[0][0])

# matrix comprehensions

first_element = [row[0] for row in x]
print(first_element)

last_element = [row[2] for row in x]
print(last_element)

