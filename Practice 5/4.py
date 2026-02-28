import re

s = input()

numbers = re.findall(r"\d", s)

if numbers:
    print(" ".join(numbers))
else:
    print('')