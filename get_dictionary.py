dictionary = []

# todo
def isbengali(word):
    ''' Returns wheather a word is in bengali or not
    Return: (boolean) '''
    return True

with open("datasets/bn.txt", "r") as file:
    sentences = file.read().split("\n")

for sentence in sentences:
    if len(sentence) > 0:
        for word in sentence.split(" "):
            if isbengali(word):
                dictionary.append(word)

with open("datasets/dict.txt", "a") as dictionary_file:
    for word in dictionary:
        dictionary_file.write(word)
        dictionary_file.write("\t")
    