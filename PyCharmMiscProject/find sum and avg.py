a = []
for i in range(10):
    num = int(input("Enter the num value"+str(i+1)))
    a.append(num)
print(a)

sum = 0
for i in a:
    sum += i
print(sum)

avg = sum / len(a)
print(avg)