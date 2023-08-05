#WAP that accepts different number of arguments and returns sum of only the
#positive values passed to it.

def sum_positive_numbers(*args):
    positive_sum = sum(num for num in args if num > 0)
    return positive_sum

result1 = sum_positive_numbers(10, -5, 20, -3, 15)
result2 = sum_positive_numbers(5, 8, 0, -2)
result3 = sum_positive_numbers(-10, -7, -4)
print("Sum of Positive Numbers (Example 1):", result1)
print("Sum of Positive Numbers (Example 2):", result2)
print("Sum of Positive Numbers (Example 3):", result3)
