# Logical Operators
# and - or - not
# and - All conditions need to be true
# if any value is considered false, the entire expression will be evalueted at that value
# They are considered falsy (which you have already seen)
# 0 0.0 '' False
# There is also the type None which is used to represent a non-value

Enter = input("[L]og [O]ut: ")
password_entered = input("Password: ")

password_allowed = "12345"

if (Enter == "L" or Enter == "l") and password_entered == password_allowed:
    print("Logged")
else:
    print("Out")

# Short circuit assessment
print(True and True and True)
print(True and 0 and True)

password = input("Password: ") or "No Password"
print(password)
