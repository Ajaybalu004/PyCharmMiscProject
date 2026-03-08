s_username="Ajay"
s_password="1234567890"

username = input("Enter the valid username: ")
password = input("Enter the valid password: ")

def validate():
    if (s_username == username and s_password == password):
        return "valid"
    else:
        return "invalid"

a = validate()
print(a)