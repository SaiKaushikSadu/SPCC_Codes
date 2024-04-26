def generate_three_address_code(expr):
    import re

    def new_temp():
        nonlocal temp_counter
        temp = f"t{temp_counter}"
        temp_counter += 1
        return temp

    tokens = re.findall(r'[\w\d]+|[()+\-*/:=]', expr)
    output = []  
    operators = []  
    temp_counter = 1
    code = []  

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, 'uminus': 3, '(': 0, ')': 0, '=': -1}
    associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', 'uminus': 'R', '=': 'R'}

    def handle_operator(op):
        while (operators and operators[-1] != '(' and
               (precedence[operators[-1]] > precedence[op] or
                (precedence[operators[-1]] == precedence[op] and associativity[op] == 'L'))):
            process_operator(operators.pop())
        operators.append(op)

    def process_operator(operator):
        if operator == 'uminus':  
            operand = output.pop()
            temp = new_temp()
            code.append(f"{temp} := -{operand}")
            output.append(temp)
        elif operator == '=':
            rhs = output.pop()
            lhs = output.pop()
            code.append(f"{lhs} := {rhs}")
        else: 
            right = output.pop()
            left = output.pop()
            temp = new_temp()
            code.append(f"{temp} := {left} {operator} {right}")
            output.append(temp)

    prev_token = None
    for token in tokens:
        if token.isalnum():  
            output.append(token)
        elif token in '+-*/':
            if token == '-' and (prev_token in {'(', None, '=', '+', '-', '*', '/'}):
                
                handle_operator('uminus')
            else:
                handle_operator(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                process_operator(operators.pop())
            operators.pop() 
        elif token == '=':
            operators.append(token)
        prev_token = token

    while operators:
        process_operator(operators.pop())

    return code

expr = "a := (-c * b) + (-c * d)"
tac_code = generate_three_address_code(expr)
for line in tac_code:
    print(line)
