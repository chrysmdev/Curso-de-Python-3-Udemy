"""
String Slicing
 012345678910
 Hello World
-1110987654321
Slicing [i:f:p] [::]
i - inicial
f - final
p - pass
Obs: the function len returns the number of characters in the string
"""

var = "Hello World"

print(var[6:])
print(var[0:5])
print(var[::-1])
print(var[-1:-12:-1])

print(len(var))

print(var[0 : len(var) : 2])
