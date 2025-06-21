import random


class Hero:
    def __init__(self, name: str, max_hp: int = 20):
        self.name = name
        self.hp = max_hp

    def attack(self) -> int:
        return random.randint(1, 7)

    def take_damage(self, damage: int):
        self.hp -= damage


class Enemy:
    def __init__(self, name: str, max_hp: int = 10):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp

    def attack(self) -> int:
        return random.randint(1, 7)

    def take_damage(self, damage: int):
        self.hp -= damage

    def get_ascii_filename(self, suffix="") -> str:
        base = self.name.lower().replace(" ", "_")
        return f"ascii/{base}{suffix}.txt"
