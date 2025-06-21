import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.normpath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

from src.utils import load_script
from src.vm import VM


def debug_vm(filepath: str):
    print(f"Executando jogo com script: {filepath}")
    game_data = load_script(filepath)
    vm = VM(game_data)

    while vm.current_room:
        print(f"\nEntrando na sala: {vm.current_room}")
        vm.run()
    print("\nFim da execução.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python debug_vm.py <caminho_para_arquivo_msr>")
        sys.exit(1)

    debug_vm(sys.argv[1])
