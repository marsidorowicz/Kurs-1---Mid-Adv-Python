path = r"e:\1.txt"

text = open(path, "r", encoding="utf-8").read().split()

print(text)
print(len(text))
