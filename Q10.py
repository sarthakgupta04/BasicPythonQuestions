#WAP to print only the first two characters of every word.
def print_first_two_chars(string):
    words = string.split()
    for word in words:
        if len(word) >= 2:
            print(word[:2])
        else:
            print(word)

input_string = "Hello, how are you today?"
print_first_two_chars(input_string)
