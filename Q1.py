#WAP to enter a number and display its hex and octal equivalent and its square root.
def sum_of_squares(numbers):
    squares = map(lambda x: x**2, numbers)
    return sum(squares)

# Example usage
user_list = [1, 2, 3, 4, 5]
result = sum_of_squares(user_list)
print("Sum of squares:", result)
