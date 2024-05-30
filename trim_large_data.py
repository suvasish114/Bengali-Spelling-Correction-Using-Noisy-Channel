import time
import re
import string
strip_chars = "".join([string.punctuation, "‘’"])
line_count = 0
bn_chars = [' ']
seconds = time.time()
init_time = time.ctime(seconds)

word_count = [0 for _ in range(100)]
sent_count = [0 for _ in range(200)]

# READ CHARACTERS
with open("bn_characters.txt", "r") as bnc:
	with open("bn_digits.txt", "r") as bnd:
		bn_chars.extend(bnc.read().split("\t")+bnd.read().split("\t"))

# REMOVE NON BEN CHARS
def remove_non_bn(sent):
	for ch in list(sent):
		for c in list(ch):
			if c not in bn_chars:
				return False
	return True

# DRIVING CODE
with open("bn1.txt", "w") as bn1:
	with open("bn.txt", "r") as bn:
		while bn.readline() != "":
			sentences = bn.readline()
			for sentence in re.split("\?|;|।|\n", sentences):
				if remove_non_bn(sentence) == False:
					continue
				sent = sentence.strip().translate(str.maketrans('', '', string.punctuation))

				if len(sent.split(" ")) < 200:
					sent_count[len(sent.split(" "))] += 1
				else:
					continue
				
				if len(sent.split(" ")) <= 2:
					continue
				
				for word in sent.split(" "):
					if len(word) < 100:
						word_count[len(word)] += 1
				
				if sent.strip() != "":
					bn1.write(sent.strip())
					bn1.write("\n")
					line_count += 1
					print("\033[H\033[J", end="")
					print(line_count)

# TEST
print(f"started at: {init_time}")
print(f"end at: {time.ctime(seconds)}")

with open("word_count.txt", "w") as wordc:
	for a in word_count:
		wordc.write(str(a))
		wordc.write("\n")
		
with open("sent_count.txt", "w") as sentc:
	for b in sent_count:
		sentc.write(str(b))
		sentc.write("\n")

