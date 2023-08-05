#WAP to extract each word from a string using a regular expression.
import re

def extract_words(string):
    words = re.findall(r'\b\w+\b', string)
    return words

input_string = "Hello, how are you today?"
word_list = extract_words(input_string)
print("Words:", word_list)
