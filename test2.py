user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]

# Create a new list without empty answers
# using filter with a lambda expression
empty_answ = list(filter(lambda x: x != "", user_answers))

# Display the cleaned list of answers
print(empty_answ)