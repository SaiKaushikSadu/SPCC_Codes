# Implementation of LL(1) parser in Python

nonterm_userdef = ['S', 'A', 'B']
term_userdef = ['a', 'b', 'c', 'd', '$']  # Assuming 'b' and '$' are terminals

firsts = {
    'S': {'a'},
    'A': {'c', 'e'},
    'B': {'d', 'e'}
}

follows = {
    'S': {'$'},
    'A': {'d', 'b'},
    'B': {'b'}
}

diction = {
    'S': [['a', 'A', 'B', 'b']],
    'A': [['c'], ['e']],
    'B': [['d'], ['e']]
}

def createParseTable():
    parse_table={nt: {t: '' for t in term_userdef} for nt in nonterm_userdef}

    for nt in nonterm_userdef:
        for production in diction[nt]:
            first_of_production=set()
            if production[0] in term_userdef:
                first_of_production.add(production[0])
            elif production[0] =='e':
                first_of_production=follows[nt]
            else:
                first_of_production=firsts[production[0]]

            for terminal in first_of_production:
                if terminal!="e":
                    parse_table[nt][terminal]=' '.join(production)
                else:
                    for follow in follows:
                        parse_table[nt][follow]=' '.join(production)
            
    return parse_table

def displayParseTable(parse_table):
    headers=["Non-T"]+term_userdef
    header_format="{:>15}"*(len(term_userdef)+1)
    row_format="{:>15}"*(len(term_userdef)+1)

    print(header_format.format(*headers))

    for non_terminal in parse_table:
        row=[non_terminal]
        for terminal in term_userdef:
            production=parse_table[non_terminal].get(terminal)
            if production:
                row.append(f"{non_terminal} -> {production}")
            else:
                row.append("")
        print(row_format.format(*row))


parse_table = createParseTable()

print(parse_table)

displayParseTable(parse_table)