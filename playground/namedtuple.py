from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'price'])

book1 = Book('Millenium', 'Steve larsson', 12000)

print("%s, %s, %s" % (book1.title, book1.author, book1.price))
print(book1)

Test = namedtuple('Test', ['name', 'description'])

challenge = Test('hongjinhyeok', 'cloud engineer')

print("%s %s" % (challenge.name, challenge.description))

