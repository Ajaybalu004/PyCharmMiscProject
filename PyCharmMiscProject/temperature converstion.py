unit = input ("Is this temperature in Celsius or Fahrenheit (C/F):")
temp = float(input("Enter the temperature:"))

if unit == "C": # converts fahrenheit to celsius
    temp = round((temp * 9) / 5  + 32,2)
    print(f"this is convert fahrenheit into celsius: {temp} F ")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9 + 32,2)
    print(f"this is convert celsius into fahrenheit: {temp} C ")

else:
    print(f"{unit} is an invalid unit of measurment.")

