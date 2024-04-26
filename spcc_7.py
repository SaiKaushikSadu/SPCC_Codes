# Implementation of Code Optimization in Python

def code_opt(input_code):
    optimized_code=[]
    expressions={}
    line_replacement={}

    for line in input_code:
        left_side,exp =line.split(" = ")

        if exp in expressions:
            line_replacement[left_side]=expressions[exp]
        else:
            expressions[exp]=left_side
            optimized_code.append(line)

    final_code=[]
    for line in optimized_code:
        left_side,exp = line.split(" = ")
        for old,new in line_replacement.items():
            exp=exp.replace(old,new)
        final_code.append(f"{left_side} : {exp}")

    return final_code

input_code = [
    "t1 = -c",
    "t2 = a + b",
    "t3 = a + b",
    "t4 = a + b",
    "t5 = d + e",
    "t6 = a + b",
    "t7 = -c",
    "t8 = d + e",
    "t9 = 4 * t4"
]

optimized_code=code_opt(input_code)

for line in optimized_code:
    print(line)