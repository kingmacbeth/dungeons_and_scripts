from src.lexer import lexer

with open("scripts/castelo_sombrio.msr") as f:
    code = f.read()

lexer.input(code)

for tok in lexer:
    print(tok)
