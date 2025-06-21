import os
import sys
from pprint import pprint

current_dir = os.path.dirname(__file__)
project_root = os.path.normpath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

from src.lexer import initialize_lexer
from src.parser import parse_code


def debug_lexer(filepath: str):
    print(f"Lendo arquivo: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    lexer = initialize_lexer()
    lexer.input(code)

    print("\nTokens encontrados:")
    for token in lexer:
        print(f"{token.type:<10} | {token.value:<20} | linha {token.lineno}")


def debug_parser(filepath: str):
    print(f"\nRealizando parsing do arquivo: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        ast = parse_code(code)
        print("\nAST gerada com sucesso:")
        pprint(ast, sort_dicts=False, indent=2, width=120)
    except SyntaxError as e:
        print(f"\nErro de parsing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python debug_lexer.py <caminho_para_arquivo_msr>")
        sys.exit(1)

    filepath = sys.argv[1]

    debug_lexer(filepath)
    debug_parser(filepath)
