weight= float(input("enter your weight:"))
unit = input("kilogram or pounds? or (K or L):")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is: {round(weight, 2)} {unit} ")

elif unit == "L":
    weight = weight/ 2.205
    unit = "Kgs."
    print(f"your weight is: {round(weight, 2)} {unit} ")
else:
    print(f"{unit} was not valid")

