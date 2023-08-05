#WAP to print the first word of a string.
def print_first_word(string):
    words = string.split()
    if len(words) > 0:
        print("First word:", words[0])
    else:
        print("No words found.")

input_string = "Hello, how are you today?"
print_first_word(input_string)
