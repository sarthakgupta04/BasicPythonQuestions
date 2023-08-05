#WAP that counts the occurrence of a character in string. (Do not use count function).
#Also it stats counting from specific location.

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
