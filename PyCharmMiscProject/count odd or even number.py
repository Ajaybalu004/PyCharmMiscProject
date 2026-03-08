o_count = 0
e_count = 0
for i in range(1,11):
    if (0 == i%2):
        e_count += 1
    else:
        o_count += 1
print(f"Even number={e_count}")
print (f"odd number={o_count}")