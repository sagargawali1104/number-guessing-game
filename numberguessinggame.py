import random

print("================================")
print("   NUMBER GUESSING GAME")
print("================================")

# Generate random number
secret_number = random.randint(1, 20)

# Total attempts
attempts = 5

print("\nGuess a number between 1 and 20")
print("You have", attempts, "attempts")

# Game loop
while attempts > 0:

    # User input
    guess = int(input("\nEnter your guess: "))

    # Correct guess
    if guess == secret_number:
        print("\nCongratulations!")
        print("You guessed the correct number.")
        break

    # Hint for smaller number
    elif guess < secret_number:
        print("Too low! Try a bigger number.")

    # Hint for bigger number
    else:
        print("Too high! Try a smaller number.")

    # Reduce attempts
    attempts -= 1

    print("Remaining attempts:", attempts)

# Game over
if attempts == 0:
    print("\nGame Over!")
    print("The correct number was:", secret_number)

print("\nThanks for playing!")