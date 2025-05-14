import random

4
secret = random.randint(1,10)
guess = 0
score = 100
attempts = 0

print(" Welcome to Python Casino!")
print("Guess the number between 1 and 10")
print("You start with 100 points. Each wrong guess costs 10 points.\n")

while guess != secret:
    guess = int(input("Your guess: "))
    attemps += 1

    if guess < secret:
        print( "up")
        score -=10
    elif guess > secret:
        print("down")
        score -=10
    else:
        print("Correct! You win!")
        print(f"Attempts: {attempts}")
        print(f"Final score: {score}")



        