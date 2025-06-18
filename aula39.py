"""
iterating strings with while
"""

#         012345678
# name = "Chrystian"  # iterable
#       - 987654321

name = input("What is your name? ")
name_size = len(name)
counter = 0

# My method

while counter != name_size:
    print(f"*{name[counter]}", end="")
    counter += 1

# comment method

while counter < len(name):
    print(name[counter], end="*")
    counter += 1

# teacher method

new_name = ""

while counter < len(name):
    letter = name[counter]
    new_name += f"*{letter}"
    counter += 1

new_name += "*"
print(new_name)
