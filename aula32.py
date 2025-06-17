"""
Write a program that asks the user to type a integer and
informs whether this number is even or odd.
If the user does not type an integer, inform that it is not an integer.
"""

try:
    num = int(input("Please, type a integer: "))

    if num % 2 == 0:
        print(f"Your number ({num}) is even.")
    else:
        print(f"Your number ({num}) is odd")

except ValueError:
    print("Error!! check if the entered value is an integer.")

""" 
Write a program that asks the user for the time and, based on the time described, display the appropriate greeting. Ex.
Good morning (0-11), Good afternoon (12-17) and Good night (18-23)
"""

try:
    time = int(input("Please, what time is it? "))

    if time >= 0 and time <= 11:
        print("Good morning!")
    elif time >= 12 and time <= 17:
        print("Good afternoon!")
    elif time >= 18 and time <= 23:
        print("Good night!")
    elif time >= 24:
        print("The time entered does not exist")

except ValueError:
    print(
        "Error!! check if the value entered is an integer that can be used as the time on the clock."
    )

""" 
Write a program that asks for the user's first name. 
If the name has 4 letters or less, write "Your name is short"; 
If it has between 5 and 6 letters, write "Your name is normal"; 
If it has more than 6, write "Your name is very long".
"""

try:
    user_name = input("What is your name? ")
    num_name_letter = int(len(user_name))

    if num_name_letter >= 1 and num_name_letter <= 4:
        print("Your name is SHORT.")
    elif num_name_letter <= 6:
        print("Your name is NORMAL.")
    else:
        print("Your name is VERY LONG.")

except:
    print("Something went wrong!")
