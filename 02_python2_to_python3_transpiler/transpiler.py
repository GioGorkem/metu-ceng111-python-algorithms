# """print ’Processing data...'
# value = input(’Enter a number: ')
# total = reduce(lambda x, y: x + y, [1, 2, 3, value])"""


def why_am_I_here(v2_code):
    code_list_v2 = split_codes(v2_code)
    code_list_v3 = [make_v3(x) for x in code_list_v2]
    if "reduce" in code_list_v3:
        code_list_v3.insert(0, "from functools import reduce")
        code_list_v3.remove("reduce")
    return "\n".join(code_list_v3)



def split_codes(v2_code):
    return v2_code.split("\n")
# code_list_v2: ['print ’Processing data...'', 'value = input(’Enter a number: ')', 'total = reduce(lambda x, y: x + y, [1, 2, 3, value])']

def make_v3(row_code_list_v2):
    if "print" in row_code_list_v2:
        return print_v3(row_code_list_v2)
    elif "raw_input" in row_code_list_v2:
        return input_v3(row_code_list_v2)
    elif "input" in row_code_list_v2:
        return eval_input_v3(row_code_list_v2)
    elif "=" in row_code_list_v2 and "L" in row_code_list_v2:
        return long_v3(row_code_list_v2) 
    elif "reduce" in row_code_list_v2:
        return ["reduce"]
    else:
        return row_code_list_v2
    
def print_v3(row_code_list_v2):
    if "'" in row_code_list_v2:
        split_row = row_code_list_v2.split("'")
        split_row[1] = f"('{split_row[1]}')"
        unspaced_row_1 = "".join(split_row)
        unspaced_row = " ".join(unspaced_row_1.split(" "))
        return unspaced_row
    elif row_code_list_v2[-1] == ",":
        split_row = row_code_list_v2.split(",")
        just_variable = split_row[0].split("print")
        just_variable[1] = "".join(just_variable[1].split(" "))
        just_variable[1] = f"print({just_variable[1]}, end=\" \")"
        unspaced_row_1 = "".join(just_variable)
        unspaced_row = "".join(unspaced_row_1.split(" "))
        return unspaced_row_1
def input_v3(row_code_list_v2):
    split_row = row_code_list_v2.split("raw_input")
    split_row[1] = f"input{split_row[1]}"
    return "".join(split_row)

def eval_input_v3(row_code_list_v2):
    split_row = row_code_list_v2.split("input")
    split_row[1] = f"eval(input{split_row[1]})"
    return "".join(split_row)

def long_v3(row_code_list_v2):
    split_row = list(row_code_list_v2)
    split_row.pop()
    no_L_split_row = "".join(split_row)
    return no_L_split_row
    





def control_reduce(code_list_v3):
    reduce_list = []
    reduce_list = [x for x in code_list_v3 if "reduce" in x]
    return reduce_list != []

    
print(why_am_I_here("""print 'Hello World'
print 'Python 2 is old'"""))