#Python program to print the following pattern:
#1
#2 4
#3 6 9
#4 8 12 16
#5 10 15 20 25
#6 12 18 24 30 36

def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()

num_rows = 6
print_pattern(num_rows)
