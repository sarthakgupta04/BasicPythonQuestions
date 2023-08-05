#Define a function to find the sum of squares of numbers in a list using lambda
#function and map function. The function should take the list of numbers as input
#parameter and return the sum of squares. Call the function with user-defined list and
#print the sum of squares.

# Define the function using lambda and map
def sum_of_squares(numbers):
    square = lambda x: x**2
    squared_numbers = map(square, numbers)
    return sum(squared_numbers)

# Get user input for a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
user_list = list(map(float, user_input.split()))

# Calculate and print the sum of squares
result = sum_of_squares(user_list)
print("Sum of squares:", result)

