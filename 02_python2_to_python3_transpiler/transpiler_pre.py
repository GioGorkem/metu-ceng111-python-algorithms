
def why_am_I_here(v2_code):
    each_v2_code = v2_code.split("\n")
    # ['print 'Processing data...'', 'value = input('Enter a number: ')', 'total = reduce(lambda x, y: x + y, [1, 2, 3, value])']
    each_v3_code = [make_v3(v2) for v2 in each_v2_code]
    control_reduce = [x for x in each_v2_code if "reduce" in x]
    if control_reduce:
        each_v3_code.insert(0, 'from functools import reduce') 
    
    exact_output = "\n".join(each_v3_code)
    return exact_output

def make_v3(v2):
    # 'print 'Processing data...''
    if v2[0] == "#":
        return v2
    elif "print" in v2:
        print_v3 = v2.replace(" ", "(", 1) + ")"
        # 'print('Processing data...')'
        if print_v3[-2] == ",":
            return print_v3.replace(",)", ", end=\" \")")
        else:
            return print_v3
    elif "raw_input" in v2:
        return v2.replace("raw_", "")
    elif "input" in v2:
        return v2.replace("input", "eval(input") + ")"
    else:
        for_numbers = v2.split(" ")
        for_numbers_wo_L = [x[::-1].replace("L", "", 1)[::-1] for x in for_numbers]
        y = " ".join(for_numbers_wo_L)
        return y 

