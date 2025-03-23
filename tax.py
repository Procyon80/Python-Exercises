while True:
	try:
		tax = float(input("What is the tax? \n"))
		break
	except ValueError:
		print("Please enter a valid number for the tax.")

while True:
	try:
		amount = int(input("What is the amount? \n"))
		break
	except ValueError:
		print("Please enter a valid integer for the amount.")

total = amount + amount * tax
print("Total = " + str(total))
