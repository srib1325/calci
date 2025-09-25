import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Enter any number (1-10): "))

    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10.")
        continue  
    if guess == secret_number:
        print("You win!")
        break
    elif guess < secret_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
