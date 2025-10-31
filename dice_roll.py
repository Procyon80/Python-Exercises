
import random
dice_roll = random.randint(1,6)
print("**************************************************************************")
print("> D I C E   v0.02 <")
print("**************************************************************************")
print("This is a guessing game based on a dice.")
print("The PC rolls a dice and you have to guess what number the computer rolled.")
print("Good luck!")
print("**************************************************************************")
try:
    guess = int(input("Guess the dice roll (1-6): "))
    while guess < 1 or guess > 6:
        print(f"Correct! The PC rolled a {dice_roll}")
        guess = int(input("Guess the dice roll (1-6): "))
    if guess == dice_roll:
        print(f"Correct the PC rolled a {dice_roll}")
    else:
        print(f"Wrong! The PC rolled a {dice_roll}.")
except ValueError:
    print("Invalid input! Please enter an integer between 1 and 6.")