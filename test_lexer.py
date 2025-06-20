from lexer import lexer

with open("script.msr") as f:
    code = f.read()

lexer.input(code)

for tok in lexer:
    print(tok)
