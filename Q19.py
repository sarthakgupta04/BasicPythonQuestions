#In a library, identical Python books are placed one over the other and form a layer of
#books. Students sequentially take the topmost book, whereas the students done with
#are again put back on top of the remained book layer. Write two functions for taking
#off and putting on the layer. Also, find out the number of books that remained in the
#layer after each taking off and putting on.

def take_book(layer):
    if layer:
        book = layer.pop(0)  # Remove the topmost book from the layer
        print("Student took book:", book)
    else:
        print("No books left in the layer.")

def put_book(layer, book):
    layer.insert(0, book)  # Put the book on top of the layer
    print("Book put back on top of the layer.")

# Example usage:
book_layer = ["Python Book 3", "Python Book 2", "Python Book 1"]

print("Initial book layer:", book_layer)

take_book(book_layer)
print("Books remaining:", len(book_layer))

put_book(book_layer, "Python Book 4")
print("Books remaining:", len(book_layer))
