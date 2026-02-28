import re

text = input()

pattern = re.compile(r'\b\w+\b')

matches = pattern.findall(text)

print(len(matches))