# problem 1
x = 'django'

print(x[0])
print(x[-1])
print(x[0:4])
print(x[1:4])
print(x[4:])

# reverse the string using indexing
print(x[::-1])

# problem 2

l = [3, 7, [1, 4, 'hello']]

l[2][2] = 'goodbye'

print(l)

# problem 3

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

# problem 4

mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

x = set(mylist)

print(x)

# problem 5

age = 4
name = "Sammy"

myString = "Hello my dog's name is {} and  he is 4 years old".format(name, age)
print(myString)
