class Animal:

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


class Cat(Animal):

    def __init__(self):
        print("CAT CREATED")

    def bark(self):
        print("WOOF")

# Method overidden
def eat(self):
    print("CAT EATING")

#Instatiate Animal class
# animal = Animal() # Create an Animal object
cat = Cat()
cat.whoAmI()
cat.eat()
cat.bark()
