import re
import string
strip_chars = string.punctuation
sentences = set()

# REMOVE PUNCHUATION
def remove_punc(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))

# OPEN RAW DATAFRAME
with open("datasets/bn.txt", "r") as file:
    articles = file.read().split("\n")

# SPLIT SENTENCES
for article in articles:
    for sentence in re.split("\?|;|।|\n", article):
        sentences.add(remove_punc(sentence))

# WRITING FILE
with open("datasets/bn_sentences.txt", "w") as file:
    for sentence in list(sentences):
        file.write(sentence)
        file.write("\n")