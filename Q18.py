#Write a program that generates a four-digit random code and the user needs to guess
#the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong,
#the computer should print out “B”. If the digit is correct but at the wrong place, the
#computer should print “Y”. If both the digit and position are correct, the computer
#should print “R”.
#Example: Four-digit random code = “4583”
#User entered code = ”7536”
#Output = ”BRYB”

import random

def generate_random_code():
    digits = [str(i) for i in range(10)]  # List of digits from 0 to 9
    random.shuffle(digits)  # Shuffle the digits
    code = ''.join(digits[:4])  # Take the first four digits as the code
    return code

def get_guess():
    while True:
        guess = input("Enter your guess (four digits): ")
        if len(guess) == 4 and guess.isdigit():
            return guess
        else:
            print("Invalid guess! Please enter a four-digit number.")

def check_guess(code, guess):
    feedback = ""
    for i in range(4):
        if guess[i] == code[i]:
            feedback += "R"
        elif guess[i] in code:
            feedback += "Y"
        else:
            feedback += "B"
    return feedback

# Main game loop
code = generate_random_code()
tries = 10

print("Welcome to the Code Guessing Game!")
print("You have", tries, "tries to guess the four-digit code.")

while tries > 0:
    user_guess = get_guess()
    result = check_guess(code, user_guess)
    print("Result:", result)
    print()

    if result == "RRRR":
        print("Congratulations! You guessed the code correctly!")
        break

    tries -= 1
    print("Tries left:", tries)
    print()

if tries == 0:
    print("Game Over! You ran out of tries.")
    print("The correct code was:", code)
