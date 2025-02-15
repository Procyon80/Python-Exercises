
import random
roll = random.randint(1,6)
print("**************************************************************************")
print("> D I C E   v0.01 <")
print("**************************************************************************")
print("This is a guessing game based on a dice.")
print("The PC rolls a dice and you have to guess what number the computer rolled.")
print("Good luck!")
print("**************************************************************************")
guess = int(input("Guess the dice roll:"))
if guess == roll:
    print("Correct the PC rolled a " + str(roll))
else:
    print("Wrong! The PC rolled a " + str(roll))