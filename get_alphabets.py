alphabets = list()
with open("datasets/unicode.txt") as file:
    codes = file.read().split("\n")

print(codes)

for code in codes[:-1]: 
    alphabets.append(chr(int(hex(int(code, 16)), 16)))

with open("datasets/characters.txt", "a") as characters:
    for alphabet in alphabets:
        characters.write(alphabet)
        characters.write("\t")