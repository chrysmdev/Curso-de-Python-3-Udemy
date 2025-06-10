"""
Exercise
Ask the user to enter their name
Ask the user to enter their age
if name and age was entered:
    Display:
        Your name is {name}
        Your name reversed is {name reversed}
        Your name contains (or not) spaces
        Your name has {n} letters
        Your name first letter is {letter}
        Your name last letter is {letter}
If nothing is entered for name or age:
    display "Sorry, you left empty fields."
"""

name = input("Enter your name: ")
age = input("Enter your age: ")

if name and age:
    print(f"Your name is {name}")
    print(f"Your name reversed is {name[::-1]}")

    if " " in name:
        print(f"Your name contains spaces!")
    else:
        print(f"Your name not contains spaces!")

    print(f"Your name has {len(name)} letters.")
    print(f"Your name first letter is {name[0]}")
    print(f"Your name last letter is {name[-1]}")

else:
    print("Sorry, you left empty fields.")
