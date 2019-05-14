# class name should start with capital
# function name should start with small


class Dog():

    # more like a constructor
    def __init__(self, name, breed):
        self.breed = breed
        self.name = name


myDog = Dog("Doraemon", "Splitz")

print(myDog.name, "-", myDog.breed)

