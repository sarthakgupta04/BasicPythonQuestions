#WAP that has a list of numbers (both positive and negative). Make a new tuple that
#has only positive values from this list.

def extract_positive_numbers(numbers):
    positive_numbers = tuple(num for num in numbers if num > 0)
    return positive_numbers

number_list = [10, -5, 20, -3, 15, -8, 0, 7, -2]
positive_tuple = extract_positive_numbers(number_list)
print("Positive Numbers:", positive_tuple)
