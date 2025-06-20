from parser import game_data, parser

from vm import VM


def load_script(path):
    with open(path, "r") as f:
        code = f.read()
    parser.parse(code)
    return game_data


def main():
    print("🎮 Bem-vindo ao Dungeons and Scripts!")
    script = load_script("script.msr")
    vm = VM(script)
    while True:
        vm.run()


if __name__ == "__main__":
    main()
