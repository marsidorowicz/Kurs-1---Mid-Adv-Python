import os

def Count(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        number = len(text.split())
        return number

path = r"e:\1.txt"
if os.path.isfile(path):
    print("Plik {} zawiera {} słów ".format(path, Count(path)))