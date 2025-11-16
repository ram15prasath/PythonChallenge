import random

print("Welcome to the Number Guessing Game!")

secret_number=random.randint(1,100)
attempts = 0

while True:
    user_input = int(input("Enter your guess (1–100): "))
    attempts += 1

    if user_input < 1 or user_input > 100:
        print("Invalid input! Please enter a number between 1 and 100.")
        continue

    if user_input > secret_number:
        print(f"The secret number is smaller than {user_input}. Try again!")
    elif user_input < secret_number:
        print(f"The secret number is greater than {user_input}. Try again!")
    else:
        print(f"🎉 Congrats! You guessed the number {secret_number} correctly!")
        print(f"🔢 Total attempts: {attempts}")
        break
