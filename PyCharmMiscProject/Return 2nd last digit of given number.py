def second_last_digit():
    n = int(input("Enter the value:"))
    n = abs(n)
    if n<10:
        return -1
    return (abs(n) // 10 ) % 10

a = second_last_digit()
print(a)