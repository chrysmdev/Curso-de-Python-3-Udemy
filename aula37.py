"""
Repetitions
while
performs an action while the condition is true
infinite loop -> when a code has no end
"""

counter = 0

while counter <= 100:
    counter = counter + 1

    if counter % 2 == 0:
        print("I won't show the even")
        continue

    if counter >= 10 and counter <= 27:
        print("HEHE")
        continue

    print(f"your counter is {counter} ({id(counter)})")

    if counter == 40:
        break

print(f"Your counter now is {counter}")
print("out")
