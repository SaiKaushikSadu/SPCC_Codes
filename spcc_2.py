# Implementation of First in Python

grammer={
    "E" : ["TA"],
    "A" : ["+TA","e"],
    "T" : ["FB"],
    "B" : ["*FB","e"],
    "F" : ["(E)","i"]
}

terminals=["+","*","i","(",")"]
non_terminals=["E","A","T","B","F"]

def first(nt):
    productions=grammer[nt]
    first_set=[]
    
    for prod in productions:
        first_item=prod[0]

        for item in prod:
            if item in non_terminals:
                next_first=first(first_item)

                if "e" in next_first:
                    first_set.extend(next_first)
                else:
                    first_set.extend(next_first)
                    break
            else:
                first_set.append(item)
                break
            
    return list(set(first_set))

for nt in non_terminals:
    first_set=first(nt)
    print(f"First {nt} : {first_set}")
