#WAP that creates a list of 10 random integers. Then creates two lists--- Odd list and
#Even list that has all odd and even values in the list respectively. (Import random )

import random

def split_odd_even(numbers):
    odd_list = []
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return odd_list, even_list

# Generate a list of 10 random integers
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Split the list into odd and even lists
odd_numbers, even_numbers = split_odd_even(random_numbers)

# Print the original list and the separated lists
print("Random Numbers:", random_numbers)
print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)
