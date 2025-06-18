"""
https://docs.python.org/3.13/library/stdtypes.html
immutable that we saw: str, int, float, bool
"""

string = "chrystian Menezes"
another_var = f"{string[:3]}ABC{string[4:]}"
print(string)
print(another_var)
print(string.zfill(25))
