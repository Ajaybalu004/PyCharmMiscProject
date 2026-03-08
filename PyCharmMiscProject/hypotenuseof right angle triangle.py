import math
#formula c=square root of a^2 +b^2

lenght_a = float(input("enter side A: "))
lenght_b = float(input("enter side B: "))

c=math.sqrt(pow(lenght_a,2)+pow(lenght_b,2))

print(f"Side c= {c}")