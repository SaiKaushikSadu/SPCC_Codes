# Implementation of Lexical Analyzer in Python

import re

def isKeyword(token):
    if(token in ["if","else","int","main","try","catch","for","while","do"]):
        print(f"\n{token} is a keyword")
        return True
    return False

def isIdentifier(token):
    id_regex=r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if re.match(id_regex,token):
        print(f"\n{token} is a identifier")
        return True
    return False

def isConstant(token):
    const_regex=r'^[0-9]*$'
    if re.match(const_regex,token):
        print(f"\n{token} is a constant")
        return True
    return False

def isPunctuation(token):
    if(token in ["{","}","(",")","[","]",";"]):
        print(f"\n{token} is a punctuation")
        return True
    return False
    
def isOperator(token):
    if(token in ["+","-","*","/","%","=","=="]):
        print(f"\n{token} is a operator")
        return True
    return False

code = input("Enter a valid code: ").split()
print(code)

print(f"The number of tokens in the code is : {len(code)}")

for token in code:
    if(isKeyword(token)):
        continue
    elif(isIdentifier(token)):
        continue
    elif(isConstant(token)):
        continue
    elif(isPunctuation(token)):
        continue
    elif(isOperator(token)):
        continue


