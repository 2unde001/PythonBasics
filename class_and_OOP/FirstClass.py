class FirstClass():

    def set_data(self, value):
        self.data = value

    def display(self):
        print(self.data)

# Instatiate FirstClass
a = FirstClass()
b = FirstClass()

# Set diff. data to set_data method
a.set_data("Harry Portal")
b.set_data(2344.5)

# Display a and b instance value
a.display()
b.display()

# Change the instance attribute.eg
a.data = "New data"
a.display()
b.anotherName = "new Name"
