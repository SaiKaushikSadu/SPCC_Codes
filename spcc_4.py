# Implementation of Removal of Left Reursion in Python

def left_recur(grammar):
    new_grammar={}

    for non_terminal,productions in grammar.items():
        alpha_prods=[]
        beta_prods=[]

        for prod in productions:
            if(prod[0]==non_terminal):
                alpha_prods.append(prod[1:])
            else:
                beta_prods.append(prod)

        if alpha_prods:
            new_non_terminal = non_terminal + "'"
            new_beta_prods = []
            new_alpha_prods = []

            for beta in beta_prods:
                new_beta_prods.append(beta+[new_non_terminal])

            for alpha in alpha_prods:
                new_alpha_prods.append(alpha+[new_non_terminal])
            new_alpha_prods.append(["e"])

            new_grammar[non_terminal]=new_beta_prods
            new_grammar[new_non_terminal]=new_alpha_prods
        else:
            new_grammar[non_terminal]=productions

    return new_grammar


grammar = {
    "A": [["A", "a"], ["b"]]
}

new_grammar=left_recur(grammar)

for nt,productions in new_grammar.items():
    for prod in productions:
        print(f"{nt} -> {' '.join(prod)}")
