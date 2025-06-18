"""
Assignment operators
= += -= *= /= //= **= %=
"""

line_counter = 0
plus_counter = 0
less_counter = 10
multiply_counter = 2
divide_counter = 1000

while plus_counter <= 10:
    line_counter += 1
    plus_counter += 1
    less_counter -= 1
    multiply_counter *= 2
    divide_counter /= 2

    print(f"-----{line_counter}-----")
    print(
        f"your plus_counter is {plus_counter}\n"
        f"your less_counter is {less_counter}\n"
        f"your multiply_counter is {multiply_counter}\n"
        f"your divide_counter is {divide_counter:.2f}\n"
    )

print("FINALLY OUT")
