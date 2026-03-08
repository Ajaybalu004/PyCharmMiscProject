class shape():
    def area(self):
        return 0
class rectangle():
    def area(self):
        l = int(input("enter the length of rectangle: "))
        b = int(input("enter the breath of rectangle: "))
        print(l*b)

r1 =rectangle()
r1.area()