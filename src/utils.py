import os
import random
import time

from src.parser import parse_code


def intro() -> None:
    slow_text("Bem-vindo ao Dungeons and Scripts!")
    time.sleep(1)


def cartridge_menu() -> None:
    slow_text("\nDigite o número do cartucho para jogar:")
    time.sleep(1)
    slow_text("1 - Floresta Maldita", 0.03)
    slow_text("2 - Fortaleza do Demônio", 0.03)
    slow_text("3 - Morte no Espaço", 0.03)
    slow_text("4 - Castelo Sombrio", 0.03)
    slow_text("\n \n0 - Sair do jogo", 0.03)
    time.sleep(1)


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

    slow_text(message)
    for _ in range(steps):
        print(".", end="", flush=True)
        time.sleep(interval)
    print("\n")


def slow_text(text: str, speed: float = 0.06):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()
