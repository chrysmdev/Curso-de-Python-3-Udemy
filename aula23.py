# Logical Operator "not"
# Used to invert expressions
# not True  = False
# not False = True

password = input("Password: ")

if password == "12345":
    print("Logged")
else:
    print("Invalid Password")

# --------------------------

password = input("Password: ")

if password != "12345":
    print("Invalid Password")

# ---------------------------

password = input("Password: ")

if not password:
    print("You didn't type anything")

# ---------------------------

print(not 0)
print(not 1)

print(not True)  # False
print(not False)  # True
