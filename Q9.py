#WAP to print the last word of a string.
def print_last_word(string):
    words = string.split()
    if len(words) > 0:
        print("Last word:", words[-1])
    else:
        print("No words found.")

input_string = "Hello, how are you today?"
print_last_word(input_string)
