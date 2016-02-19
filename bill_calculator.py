bill = float(raw_input("How much did you spend?"))

def calculate_tip (bill_value, tip_value):
	return bill_value * tip_value 

def calculate_total_bill (bill, tip):
	return bill + tip

def calculate_split_bill (total_amount, people):
	return total_amount / people

menu_choice = int(raw_input("Dou you prefer number 1 or 2?"))

tip_percentage = float(raw_input("How much do you want to tip? Ex: 0.15 "))	

if menu_choice == 1:
	tip = calculate_tip(bill, tip_percentage)
	print tip
	
	total_amount = calculate_total_bill(bill, tip)
	print total_amount

	question = raw_input("Would you like to split the bill?")
	
	if question == "yes":
		people = int(raw_input("With how many people?"))
		print calculate_split_bill(total_amount, people)	

elif menu_choice == 2:
	people = int(raw_input("With how many people?"))
	tip = calculate_tip(bill, tip_percentage)
	total_amount = calculate_total_bill(bill, tip)
	print calculate_split_bill(total_amount, people)	
