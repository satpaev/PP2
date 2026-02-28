import re

s = input()

email = re.search(r"\S+@\S+\.\S+", s)

if email:
    print(email.group())
else:
    print("No email")