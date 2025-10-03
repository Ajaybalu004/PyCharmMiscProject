#python calculator
operator=input("enter an operator(+,-,*,/): ")
num1=float(input("Enter the value: "))
num2=float(input("Enter the value: "))

if operator=="+":
    result=(num1+num2)
    print(round(result,3))
elif operator=="-":
    result=(num1-num2)
    print(round(result,3))
elif operator=="*":
    result=(num1*num2)
    print(round(result,3))
elif operator=="/":
    result=(num1/num2)
    print(round(result,3))
else:
    print(f"you are enter invalid operator{operator}")
