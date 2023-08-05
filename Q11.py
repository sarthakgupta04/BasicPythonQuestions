#WAP that prints only those words that starts with a vowel.
def print_words_starting_with_vowel(string):
    words = string.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        if word[0].lower() in vowels:
            print(word)

input_string = "Hello, how are you today? Apple and orange are fruits."
print("Words starting with a vowel:")
print_words_starting_with_vowel(input_string)
