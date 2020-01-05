class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        Using special method to display
        Book string representation value
        """
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        #return length of the attribute
        return self.pages

    def __del__(self):
        print("a book is destroyed!")

book = Book("Fluent Python", "Smith Anderson", 32)
print(book)
print(len(book))
del book
