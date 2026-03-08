class usermaincode(object):
    @classmethod
    def lastdigit(cls):
        input1 = (int(input("Enter the digit value: ")))
        return abs(input1) % 10

print(usermaincode.lastdigit())