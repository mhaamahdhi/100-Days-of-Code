welcome_message = "Welcome to the tip calculator"
print(welcome_message)
bill_amount = float(input("what was the total bill : "))
tips = int(input("What percentage tip would you like to give: "))
add_tips_percentage = tips /100
add_tips_amount = bill_amount * add_tips_percentage
final_tips_with_amount = bill_amount + add_tips_amount
split_the_bill = int(input("How many people to split the bill: "))
splitted_amount_for_each_person = round((final_tips_with_amount /split_the_bill),2)
print(f"Each person should pay {splitted_amount_for_each_person}")

