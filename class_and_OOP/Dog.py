class Dog():

# Class object attribute
    species = "mammal"

    def __init__(self, breed, name):
        """
        Add attribute to Dog class
        """
        self.breed = breed
        self.name = name

myDog = Dog(breed = "Lab", name="bingo")
# otherDog = Dog(breed="Huskie")
print(myDog.breed)
print(myDog.name)
print(myDog.species )
