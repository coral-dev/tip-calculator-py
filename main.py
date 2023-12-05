print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
num_of_people = int(input("How many people to split the bill?"))

total_payment = total_bill + (total_bill * (tip_percentage/100))
each_payment = round(total_payment / num_of_people, 2)
final_amount = "{:.2f}".format(each_payment)

print(f"Each person should pay: ${final_amount}")
