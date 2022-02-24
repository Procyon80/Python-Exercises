import random
pc_choice = random.choice(['rock','paper','scissors'])
user_choice = input("Do you want - rock, paper or scissors ?\n")

if pc_choice == user_choice:
    print("TIE!")
elif user_choice == 'rock' and pc_choice == 'scissors':
    print("WIN!")
elif user_choice == 'paper' and pc_choice == 'rock':
    print("WIN!")
elif user_choice == 'scissors' and pc_choice == 'paper':
    print("WIN!")
else:
    print("LOSE!")
