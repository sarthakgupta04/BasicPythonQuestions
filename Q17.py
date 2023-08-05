#WAP that has a nested list to store toppers details. Edit the details and reprint the
#details.

def print_toppers_details(toppers):
    print("Toppers Details:")
    for student in toppers:
        print("Name:", student[0])
        print("Roll Number:", student[1])
        print("Grade:", student[2])
        print()

def edit_toppers_details(toppers, roll_number, new_name, new_grade):
    for student in toppers:
        if student[1] == roll_number:
            student[0] = new_name
            student[2] = new_grade
            break

# Initial Toppers Details
toppers = [
    ["Ram", 101, "A"],
    ["Mohan", 102, "A+"],
    ["Karan", 103, "B"],
]

# Print the initial details
print_toppers_details(toppers)

# Edit Toppers Details
roll_number = 102
new_name = "Mohan Kumar"
new_grade = "A"
edit_toppers_details(toppers, roll_number, new_name, new_grade)
# Print the updated details
print("\nAfter Editing:")
print_toppers_details(toppers)
