inp = 'This should(<></>) also be <reverse>dedoced</reverse> properly.'"These people believe in <reverse>em</reverse>."
start_point = inp.find("<reverse>")
end_point = inp.find("</reverse>")
encoded_inp = inp[:start_point]
encoded_inp_2 = inp[start_point + len("<reverse>"):end_point:] 
encoded_inp_3 = inp[end_point + len("</reverse>"):] 
print(encoded_inp +encoded_inp_2[::-1] +encoded_inp_3)
