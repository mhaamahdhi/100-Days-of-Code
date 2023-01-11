height = float(input("enter your height in m :"))
weight = float(input("enter your weight in kg:"))

bmi = weight/(height ** 2)

bmi_round = round(bmi)

print(bmi)
print(bmi_round)