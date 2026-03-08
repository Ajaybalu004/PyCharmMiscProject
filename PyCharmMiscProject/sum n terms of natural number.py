n =int(input("enter the natural number:"))
print("The Sum of the first",n,"Natural number:")
a =[]
for i in range(n):
    a.append(i+1)
print(a)

sum = 0
for i in a:
    sum += i
    avg = sum / len(a)
print("sum =",sum)
print("Average value",avg)