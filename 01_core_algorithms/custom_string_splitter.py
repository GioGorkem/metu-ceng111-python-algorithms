delm = input()
inp = input()
space_1 = inp.find(delm)
space_2 = inp.find(delm, space_1 + len(delm))
word_1 = inp[:space_1]
word_2 = inp[space_1 + len(delm): space_2]
word_3 = inp[space_2 + len(delm):]
print(word_1)
print(word_2)
print(word_3)