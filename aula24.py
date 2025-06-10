# Operators in and not in
# Strings are iterable
#  0 1 2 3 4 5 6 7 8
#  C h r y s t i a n
# -9-8-7-6-5-4-3-2-1

# name = "Chrystian"
# print(nome[2])
# print(nome[-4])

# print("y" in name)
# print("z" in name)
# print(10 * "-")
# print("tian" in name)
# print("sure" in name)

name = input("Enter your name: ")
find = input("Type what you want to find: ")

if find in name:
    print(f"{find} is in {name}")
else:
    print(f"{find} is not in {name}")
