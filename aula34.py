"""
Repetitions
while
performs an action while the condition is true
infinite loop -> when a code has no end
"""

condition = True

while True:
    name = input("What is your name?")
    print(f"Your name is {name}")

    if name == "out":
        break

print("End")
