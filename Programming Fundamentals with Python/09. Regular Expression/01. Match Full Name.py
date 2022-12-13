import re

text = input()

matcher = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)

print(' '.join(matcher))
