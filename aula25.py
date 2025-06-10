# Basic String Interpolation
# s - string
# d e i - int
# f - float
# x and X - Hexadecimal (ABCDEF0123456789)
# """

name = "Luiz"
price = 1000.95897643
variable = "%s, the price is £%.2f" % (name, price)
print(variable)
print("The hexadecimal of %d is %04X" % (15, 15))
