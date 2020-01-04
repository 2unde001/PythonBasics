class Circle():

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    # Create a method to calculate circle area
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Change the value of an attribute
    def set_radius(self, new_r):
        self.radius = new_r


myC1 = Circle(3)
myC1.set_radius(100)

print("Reset attribute by Changing radius value to: " +str(myC1.area()))
