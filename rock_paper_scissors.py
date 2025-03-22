import random
pc_choice = random.choice(['rock','paper','scissors'])
try:
    user_choice = input("Do you want - rock, paper or scissors ? \n")
except Exception as e:
    print(f"An error occurred: {e}")
    user_choice = None

winning_combinations = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

if pc_choice == user_choice:
    print("TIE!")
elif user_choice in winning_combinations and winning_combinations[user_choice] == pc_choice:
    print("WIN!")
else:
    print("LOSE!")
