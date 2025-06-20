import os
from parser import game_data, parser

from vm import VM


def load_script(filename: str) -> dict:
    base_path = os.path.dirname(__file__)
    script_path = os.path.join(base_path, filename)
    with open(script_path, "r") as f:
        code = f.read()
    parser.parse(code)
    return game_data


def main():
    print("🎮 Bem-vindo ao Dungeons and Scripts!")
    script = load_script("script.msr")
    print("Script carregado:", script.keys())
    vm = VM(script)
    while True:
        if vm.current_room not in vm.game_data:
            print("🏁 Fim do jogo.")
            break
        vm.run()


if __name__ == "__main__":
    main()
