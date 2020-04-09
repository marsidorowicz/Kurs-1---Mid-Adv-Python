import os
path = r"e:\1.txt"


if os.path.isfile(path) and open(path, "r", encoding="utf-8").read().split():
    text = open(path, "r", encoding="utf-8").read().split()
    print(len(text))

if os.path.isfile(path):
    print("Plik istnieje")
    text = open(path, "r", encoding="utf-8").read().split()
    print(text)
    print(len(text))
    open(path).close()
else:
    print("Brak pliku")
    open(path, "w", encoding="utf-8").close()
    text = open(path, "r", encoding="utf-8").read().split()
