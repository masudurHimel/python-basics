# Dictionary
# dictionary has no order inside it
myDictionary = {'key 1': 'value 1 ', 'key 2': 'value 2'}

print(myDictionary)
print(myDictionary['key 1'])

# nested dictionary

myDictionary = {'key 1': 'value 1 ', 'key 2': 'value 2', 'key3': {'pseudo 1': 123, 'pseudo 2': [1, 2, 'Grab me']}}

print(myDictionary)
print(myDictionary['key3']['pseudo 2'][2])

#to replace dictionary
myDictionary['key 1'] = 'tempvalue'
print(myDictionary)

#to add
myDictionary['key4'] = 'Another key'
print(myDictionary)
