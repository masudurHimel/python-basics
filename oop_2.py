class Circle():

    pi = 3.14

    # for default value we can set up in this way
    def __init__(self,radius=1):
        self.radius = radius

    def get_area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self,radius):
        self.radius = radius

myCircle = Circle(5)

print(myCircle.radius)
print(myCircle.get_area())
myCircle.set_radius(2)
print(myCircle.radius)
print(myCircle.get_area())



