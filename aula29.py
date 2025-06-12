"""
Introduction to try/except
try -> try to run the code
except -> an error occurred while trying to run the code
"""

num_str = input("I will double the number you enter: ")

try:
    print("STR:", num_str)
    num_float = float(num_str)
    print("FLOAT:", num_float)
    print(f"Twice {num_str} is {num_float * 2:.2f}")
except:
    print("This is not a number!")

# if num_str.isdigit():
#     num_float = float(num_str)
#     print(f"Twice {num_str} is {num_float * 2:.2f}")
# else:
#     print("This is not a number!")
