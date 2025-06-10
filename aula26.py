"""
String basic formatting
s - string
d - int
f - float
.<number of digits>f
x or X - Hexadecimal
(Character)(><^)(quantity)
> - Left
< - Right
^ - Center
= - Forces the number to appear before the zeros
+ or - signs
Ex.: 0>-100,.1f
Conversion flags - !r !s !a  __repr__  __str__  ascii
"""

var = "ABC"
print(f"{var}")
print(f"{var: >10}")
print(f"{var: <10}")
print(f"{var: ^10}")
print(f"{var:~^10}")

print(f"{1000.4873648123746:,.1f}")
print(f"{-1000.4873648123746:,.1f}")  # show the minus sign by default
print(f"{1000.4873648123746:+,.1f}")  # show the plus sign when the number is positive

print(f"{1000.4873648123746:0>+10,.1f}")
print(f"{1000.4873648123746:0=+10,.1f}")

print(f"The hexadecimal of 1500 is {1500:08X}")

print(f"{var!r}")
