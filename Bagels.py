import random

# Generate a random three-digit number with no repeated digits
def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

# Check if the player's guess is correct
def is_guess_correct(guess, secret_number):
    return guess == secret_number

# Provide feedback on the player's guess
def provide_feedback(guess, secret_number):
    if is_guess_correct(guess, secret_number):
        return "You got it!"
    
    feedback = []
    for i in range(3):
        if guess[i] == secret_number[i]:
            feedback.append("Fermi")
        elif guess[i] in secret_number:
            feedback.append("Pico")
    
    if not feedback:
        return "Bagels"
    
    feedback.sort()
    return " ".join(feedback)

# Main game loop
print("Welcome to Bagels! Try to guess the secret 3-digit number.")
print("I'll give you some clues. Pico means one digit is correct but in the wrong position.")
print("Fermi means one digit is correct and in the right position. Bagels means no digit is correct.")

secret_number = generate_secret_number()

attempts = 0
while True:
    player_guess = input("Enter your guess: ")
    attempts += 1

    if len(player_guess) != 3 or not player_guess.isdigit():
        print("Please enter a valid 3-digit number.")
        continue

    player_guess = [int(digit) for digit in player_guess]

    feedback = provide_feedback(player_guess, secret_number)
    print(feedback)

    if is_guess_correct(player_guess, secret_number):
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        break