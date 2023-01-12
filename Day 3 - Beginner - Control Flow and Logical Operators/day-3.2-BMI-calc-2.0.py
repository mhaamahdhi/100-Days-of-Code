height = float(input("enter your height in m :"))
weight = float(input("enter your weight in kg:"))

bmi = weight/(height ** 2)

bmi_round = round(bmi,2)
print("\n")

if bmi_round <= 18.5:
    print(f"Your bmi is {bmi_round}, You are Under Weight")
elif bmi_round <= 25 :
    print(f"Your bmi is {bmi_round}, You are normal Weight")
elif bmi_round <= 30 :
    print(f"Your bmi is {bmi_round}, You are OverWeight")
elif bmi_round <= 35 :
    print(f"Your bmi is {bmi_round}, You are Obese")
else:
    print(f"Your bmi is {bmi_round}, You are Clinically Obese")


