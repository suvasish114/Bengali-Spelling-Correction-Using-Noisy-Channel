# This module creates all confusion matrices needed for spelling correction

from lib.edit_distance import Editdistance
editdistance = Editdistance()

with open("datasets/bn_error_list.txt", "r") as error_file:
    error_words = error_file.read().split("\n")

with open("datasets/bn_characters.txt", "r") as _characters:
    characters = _characters.read().split("\t")

characters_index = dict(zip(characters, list(range(len(characters)))))

def get_char_index(character):
    if character == "#":
        return len(characters)
    return characters_index[character]


ins_mat = [[0 for _ in range(len(characters)+1)] for _ in range(len(characters))] # last col will be for #
del_mat = [[0 for _ in range(len(characters))] for _ in range(len(characters)+1)] # last row will be for #
sub_mat = [[0 for _ in range(len(characters))] for _ in range(len(characters))] # row == col
mat = [ins_mat, del_mat, sub_mat]
ttype = {'i':0, 'd':1, 's':2}

for error_word in error_words[:-1]:
    temp = error_word.split(":") # returns [original, typo]
    # print(temp)
    for sequence in editdistance.get_edit_sequence(temp[1], temp[0]): # passed [typo, original]
        if len(sequence) != 0:
            # print(sequence)
            try:
                mat[ttype[sequence[0]]][get_char_index(sequence[1])][get_char_index(sequence[2])] += 1
            except:
                print(f"escaping error for: {sequence}")

with open('datasets/bn_ins.txt', 'a') as bn_ins:
    for a in ins_mat:
        for b in a:
            bn_ins.write(str(b))
            bn_ins.write(" ")
        bn_ins.write("\n")
    bn_ins.close()

with open('datasets/bn_del.txt', 'a') as bn_del:
    for a in del_mat:
        for b in a:
            bn_del.write(str(b))
            bn_del.write(" ")
        bn_del.write("\n")

with open('datasets/bn_sub.txt', 'a') as bn_sub:
    for a in sub_mat:
        for b in a:
            bn_sub.write(str(b))
            bn_sub.write(" ")
        bn_sub.write("\n")