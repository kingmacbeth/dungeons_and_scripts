import os
import sys
from pprint import pprint

current_dir = os.path.dirname(__file__)
project_root = os.path.normpath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

from src.parser import parse_code


def debug_parser(filepath: str):
    print(f"Parsing do arquivo: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        ast = parse_code(code)
        print("\nAST gerada com sucesso:")
        pprint(ast, sort_dicts=False, indent=2, width=120)
    except SyntaxError as e:
        print(f"\n❌ Erro de parsing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python debug_parser.py <caminho_para_arquivo_msr>")
        sys.exit(1)

    debug_parser(sys.argv[1])
