inp = input()
inp_1 = inp[0:inp.index(" ")]
inp_2_3 = inp[inp.index(" ")+1:]
inp_2 = inp_2_3[0:inp_2_3.index(" ")]
inp_3 = inp_2_3[inp_2_3.index(" ")+1:]
print(inp_1)
print(inp_2)
print(inp_3)
