# inheritence
# Special methods

class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_I(self):
        print("Animal")

    def eat(self):
        print("Eating")

    def __str__(self):
        return "Name : Animal"




# inheritance fact


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof")

    def eat(self):
        print("Dog eating")



myAnimal = Dog();
myAnimal.who_am_I()
myAnimal.eat()
myAnimal.bark()

# for string representation, we can change this by default using a str method which is built in

print(myAnimal)

