"""Calculator with while"""

answer = " "

while True:
    # Asking about operations
    operator = input("What type of operation do you want to do? [+ - x /]")
    num_1 = input("choose the first value: ")
    num_2 = input("choose the second value: ")

    # Validation of values
    valid_num = None
    float_num_1 = 0
    float_num_2 = 0

    try:
        float_num_1 = float(num_1)
        float_num_2 = float(num_2)
        valid_num = True
    except:
        valid_num = None

    if valid_num is None:
        print("ERROR!!! one or both of the values entered are invalid.")
        continue

    valid_operators = "+-x/"

    if operator not in valid_operators:
        print("ERROR!!! invalid operator.")
        continue

    if len(operator) > 1:
        print("ERROR!!! tpe only one operator!")
        continue

    # Calculation
    if operator == "+":
        result = float_num_1 + float_num_2
        print(f"Your result is: {result:.2f}")
    elif operator == "-":
        result = float_num_1 - float_num_2
        print(f"Your result is: {result:.2f}")
    elif operator == "x":
        result = float_num_1 * float_num_2
        print(f"Your result is: {result:.2f}")
    elif operator == "/":
        result = float_num_1 / float_num_2
        print(f"Your result is: {result:.2f}")
    else:
        print("We can't do that.")

    # Response to exit the loop
    answer = input("Do you want continue? [YES or NO]").upper().startswith("N")
    if answer is True:
        break

print("Goodbye")
