"""
Repetitions
while
performs an action while the condition is true
infinite loop -> when a code has no end
"""

num_row = 5
num_column = 5

row = 1
while row <= num_row:
    column = 1
    print(row)
    while column <= num_column:
        print(f"{row=}, {column=}")
        column += 1
    row += 1

print("OUT")
