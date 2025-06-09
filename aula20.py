first_value = input("Enter a value: ")
second_value = input("Enter another value: ")

if first_value > second_value:
    print(f"{first_value} is greater than {second_value}")
elif first_value < second_value:
    print(f"{second_value} is greater than {first_value}")
elif first_value == second_value:
    print(f"{first_value} and {second_value} are egual!!")
else:
    print(f"{first_value=} and {second_value=} cannot be compared")
