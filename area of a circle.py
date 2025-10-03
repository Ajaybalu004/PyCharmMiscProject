import math
# formula area of a circle is a=pi * r^2
radius = float(input(f"Enter the radius value: "))

area= math.pi * pow(radius,2)

print(f"The area of the circle is: {area}")
print(f"The area of the circle is: {round(area,2)}cm^2")