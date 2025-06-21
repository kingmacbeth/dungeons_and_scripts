import os
from parser import parse_code


def load_script(filename: str) -> dict:
    base_path = os.path.dirname(__file__)
    script_path = os.path.join(base_path, filename)
    with open(script_path, "r", encoding="utf-8") as f:
        code = f.read()
    game_data = parse_code(code)
    return game_data
