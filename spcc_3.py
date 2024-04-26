# Implementation of Follow in Python

grammer={
    "E": ["TA"],
    "A": ["+TA", "e"],
    "T": ["FB"],
    "B": ["*FB", "e"],
    "F": ["(E)", "i"]
}

first={
    'E': ['(', 'i'],
    'A': ['+', 'e'],
    'T': ['(', 'i'],
    'B': ['*', 'e'],
    'F': ['(', 'i']
}

non_terminals = ['E', 'A', 'T', 'B', 'F']
terminals = ['+', '*', '(', ')', 'i', '$']
start_symbol=non_terminals[0]

def follow(nt,grammer,firsts,follows,visited):
    if(nt in visited):
        return follows[nt]
    visited.add(nt)

    if nt == start_symbol:
        follows[nt].add('$')

    for lhs,productions in grammer.items():
        for prod in productions:
            if nt in prod:
                nt_index=prod.index(nt)
                if nt_index+1<len(prod):
                    next_symbol=prod[nt_index+1]
                    if(next_symbol in non_terminals):
                        follows[nt].update(firsts[next_symbol]-{"e"})
                    else:
                        follows[nt].add(next_symbol)
                
                    if "e" in firsts.get(next_symbol,set()):
                        follows[nt].update(follow(lhs, grammer, firsts, follows, visited))
                else:
                    follows[nt].update(follow(lhs, grammer, firsts, follows, visited))
    return follows[nt]


first_sets={key: set(value) for key,value in first.items()}

follows={nt: set() for nt in non_terminals}

for nt in non_terminals:
    follow(nt,grammer,first_sets,follows,set())

for nt in non_terminals:
    print(f"Follow({nt}) : {follows[nt]}")
