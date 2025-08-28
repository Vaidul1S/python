# Magic methods - dunder methods __init__, __str__, __eq__

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa > other.gpa

student1 = Student("Spongebob", 2.1)
student2 = Student("Larry", 3.5)
student3 = Student("Garry", 4.0)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __add__(self, other):
        return f"Total {self.pages + other.pages} pages."
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"Key '{key}' was not found!"


book1 = Book("A Game of Thrones", "G.R.R. Martin", 638)
book2 = Book("A Clash of Kings", "G.R.R. Martin", 756)
book3 = Book("A Storm of Swords", "G.R.R. Martin", 992)
book4 = Book("A Storm of Swords", "G.R.R. Martin", 1002)

print(book1)
print(book2)
print(book3)

print(book3 == book4)
print(book3 < book4)
print(book1 > book2)
print(book1 + book2)
print("Swords" in book3)
print(book1['title'])
print(book2['author'])
print(book3['pages'])
print(book4['year'])