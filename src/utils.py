import os
import random
import time

from src.parser import parse_code


def intro() -> None:
    print("Bem-vindo ao Dungeons and Scripts!")


def cartridge_menu() -> None:
    print("Digite o número do cartucho para jogar:")
    print("1 - Floresta Maldita")
    print("2 - Fortaleza do Demônio")
    print("3 - Morte no Espaço")
    print("4 - Castelo Sombrio")
    print("\n \n 0 - Sair do jogo")


def load_script(filename: str) -> dict:
    base_path = os.path.dirname(__file__)
    script_path = os.path.normpath(os.path.join(base_path, "..", filename))
    with open(script_path, "r", encoding="utf-8") as f:
        script_file = f.read()
    game_data = parse_code(script_file)
    return game_data


def loading(message: str) -> None:
    duration = random.uniform(3, 5)
    interval = 0.5
    steps = int(duration / interval)

    print(message, end="", flush=True)
    for _ in range(steps):
        print(".", end="", flush=True)
        time.sleep(interval)
    print("\n")
