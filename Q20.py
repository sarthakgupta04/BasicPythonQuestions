#Write a program, which will find a list of all numbers between 1000 and 1999 such
#that each digit at odd place is an even number. Find sum of all odd places’ digits of
#every above such number and tell how many unique sum received using a suitable
#data structure.
#Example: one of the possible number is = [1206]
#sum of odd places’ digits = 8

def find_numbers():
    numbers = []
    unique_sums = set()

    for num in range(1000, 2000):
        num_str = str(num)

        if all(int(num_str[i]) % 2 == 0 for i in range(1, len(num_str), 2)):
            numbers.append(num)
            odd_sum = sum(int(num_str[i]) for i in range(1, len(num_str), 2))
            unique_sums.add(odd_sum)

    return numbers, unique_sums


numbers, unique_sums = find_numbers()
print("Numbers:", numbers)
print("Unique sums:", unique_sums)
print("Count of unique sums:", len(unique_sums))
