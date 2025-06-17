"""
Flag - mark a location
None - no value
is and is not - type, value, identity
id - Identity
"""

# v1 = "a"
# v2 = "b"
# print(id(v1))
# print(id(v2))

condition = False
passed_the_if = None

if condition:
    passed_the_if = True
    print("Do something.")
else:
    print("Don't do something")


if passed_the_if is None:
    print("Not passed the if")

if passed_the_if is not None:
    print("Passed the if")
