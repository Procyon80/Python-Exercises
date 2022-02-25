# loan details
money_owed = float(input("How much money do you owe ?\n")) # 5000EURO
apr = float(input("What is the APR (annual percentage rate) ?\n")) # 3%
payment = float(input("What is your monthly payment? \n")) # 300
months = int(input("How many months do you want to see results ?\n"))

# divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    # add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment <0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break
    
    # make payment
    money_owed = money_owed - payment

    # print the results after this month
    print("Paid", payment, "of which", interest_paid, "was interes", end=' ')
    print("Now I owe", money_owed)