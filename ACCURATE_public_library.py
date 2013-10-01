#!/usr/bin/env python

class Library(object): 
	def __init__(self, name):
		self.name = name
		self.inventory = {}
		self.shelves = []
		self.shelf_count = 0

class Shelf(object):
	def __init__(self, label):
		self.label = label
		self.books = []
		self.book_count = 0

class Book(object):
	def __init__(self, title):
		self.title = title

# adds shelves to library
def shelving(shelf, library):
	library.shelves.append(shelf)
	library.shelf_count = len(library.shelves)
	return "Shelf %s has been added to %s" % (shelf.label, public_library.name) 

# adds shelves to library
def enshelf(book, shelf, library):
	book_parts = {}
	book_parts[book.title] = book
	shelf.books.append(book_parts) 
	library.inventory[shelf.label] = shelf.books # {"shelf": [books]}
	return "%s has been shelved on Shelf %s" % (book.title, shelf.label)

# removes book from shelf
def unshelf(book, shelf, library):
	book_parts = {}
	book_parts[book.title] = book
	shelf.books.remove(book_parts)
	library.inventory[shelf.label] = shelf.books # {"shelf": [books]}
	shelf.book_count = len(shelf.books)
	return "%s has been removed from Shelf %s" % (book.title, shelf.label)

# lists all of the books in the library
def library_catalog(library):
	if library.inventory == {}:
		return "Oh my! This library has no books!"
	else:
		catalog = [i for i in library.inventory.values() if len(i) > 0]
		return catalog

# TESTING

# creating the library...
public_library = Library("The Public Library")

print library_catalog(public_library) # >>> Oh my! This library has no books!
print "%s has %s shelves." % (public_library.name, str(public_library.shelf_count)) # >>> The Public Library has 0 shelves.

# creating shelves... 
S1 = Shelf("ABCDE")
S2 = Shelf("FGHIJ")
S3 = Shelf("KLMNO")
S4 = Shelf("PQRST")
S5 = Shelf("UVWXYZ")

print shelving(S1, public_library) # >>> Shelf ABCDE has been added to The Public Library
print shelving(S2, public_library) # >>> Shelf FGHIJ has been added to The Public Library
print shelving(S3, public_library) # >>> Shelf KLMNO has been added to The Public Library
print shelving(S4, public_library) # >>> Shelf PQRST has been added to The Public Library
print shelving(S5, public_library) # >>> Shelf UVWXYZ has been added to The Public Library

print "%s has %s shelves." % (public_library.name, str(public_library.shelf_count)) # >>> The Public Library has 5 shelves.

# creating books... 
Bartleby_the_Scrivener = Book("Bartleby the Scrivener")
Harry_Potter1 = Book("Harry Potter1")
Harry_Potter2 = Book("Harry Potter2")

print enshelf(Bartleby_the_Scrivener, S3, public_library) # >>> Bartleby the Scrivener has been shelved on Shelf KLMNO
print enshelf(Harry_Potter1, S4, public_library) # >>> Harry Potter1 has been shelved on Shelf PQRST
print enshelf(Harry_Potter2, S4, public_library) # >>> Harry Potter2 has been shelved on Shelf PQRST

print "Shelf %s contains the following books: %s" % (S3.label, str(S3.books)) # >>> Shelf KLMNO contains the following books: [{'Bartleby the Scrivener': <__main__.Book object at 0x103151290>}]
print "Shelf %s contains the following books: %s" % (S4.label, str(S4.books)) # >>> Shelf PQRST contains the following books: [{'Harry Potter1': <__main__.Book object at 0x1031512d0>}, {'Harry Potter2': <__main__.Book object at 0x103151310>}]
print "Altogther, %s contains the following books: %s" % (public_library.name, str(library_catalog(public_library))) # >>> Altogther, The Public Library contains the following books: [[{'Harry Potter1': <__main__.Book object at 0x1031512d0>}, {'Harry Potter2': <__main__.Book object at 0x103151310>}], [{'Bartleby the Scrivener': <__main__.Book object at 0x103151290>}]]

print unshelf(Harry_Potter1, S4, public_library) # >>> Harry Potter1 has been removed from Shelf PQRST

print "Shelf %s contains the following books: %s" % (S4.label, str(S4.books)) # >>> Shelf PQRST contains the following books: [{'Harry Potter2': <__main__.Book object at 0x103151310>}]
print "Now, %s contains the following books: %s" % (public_library.name, str(library_catalog(public_library))) # >>> Now, The Public Library contains the following books: [[{'Harry Potter2': <__main__.Book object at 0x103151310>}], [{'Bartleby the Scrivener': <__main__.Book object at 0x103151290>}]]
