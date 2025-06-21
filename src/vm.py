import os

from src.entities import Enemy, Hero
from src.utils import slow_text


class VM:
    def __init__(self, game_data):
        self.game_data = game_data
        self.current_room = "start"
        self.hero = Hero("Jogador 1")
        self.enemy = None

    def show_enemy_art(self, filename: str) -> None:
        base_path = os.path.dirname(__file__)
        art_path = os.path.normpath(os.path.join(base_path, "..", filename))

        if os.path.exists(art_path):
            with open(art_path, "r", encoding="utf-8") as f:
                art = f.read()
            slow_text(art, 0.01)
        else:
            slow_text(f"\n[ilustração não disponível para '{filename}']")

    def run(self) -> None:
        while True:
            room = self.game_data.get(self.current_room)
            if not room:
                break

            next_room_set = False

            for stmt in room:
                match stmt[0]:
                    case "text":
                        slow_text(f"\n{stmt[1]}")
                    case "hero":
                        self.hero = Hero(stmt[1], stmt[2])
                    case "enemy":
                        self.enemy = Enemy(stmt[1], stmt[2])
                        slow_text("\nUm inimigo apareceu: ")
                        slow_text(f"\n{self.enemy.name}")
                        slow_text(f"\nHP {self.enemy.hp}")
                        self.show_enemy_art(self.enemy.get_ascii_filename())
                    case "attack":
                        self.handle_attack()
                    case "choice":
                        self.handle_choices([s for s in room if s[0] == "choice"])
                        return
                    case "goto":
                        self.current_room = stmt[1]
                        return

            if not next_room_set:
                self.current_room = None

    def handle_attack(self) -> None:
        slow_text("\nIniciando combate...")

        while self.enemy and self.enemy.hp > 0 and self.hero.hp > 0:
            input("\nPressione Enter para atacar!")

            hero_dmg = self.hero.attack()
            self.enemy.take_damage(hero_dmg)
            slow_text(
                f"\nVocê causou {hero_dmg} de dano. HP do inimigo: {self.enemy.hp}"
            )

            if self.enemy.hp <= 0:
                slow_text("\nInimigo derrotado!")
                self.show_enemy_art(self.enemy.get_ascii_filename("_morto"))
                break
            elif self.enemy.hp <= 0.6 * self.enemy.max_hp:
                self.show_enemy_art(self.enemy.get_ascii_filename("_machucado"))

            enemy_dmg = self.enemy.attack()
            self.hero.take_damage(enemy_dmg)
            slow_text(
                f"\n{self.enemy.name} contra-ataca e causa {enemy_dmg} de dano! Seu HP: {self.hero.hp}"
            )

            if self.hero.hp <= 0:
                slow_text("\nVocê foi derrotado... fim de jogo.")
                self.current_room = None
                return

    def handle_choices(self, choices) -> None:
        slow_text("\nEscolha uma opção:")
        for idx, choice in enumerate(choices):
            slow_text(f"{idx + 1}. {choice[1]}")

        while True:
            try:
                opt = int(input("\nSua escolha: "))
                if 1 <= opt <= len(choices):
                    self.current_room = choices[opt - 1][2]
                    return
                else:
                    slow_text("\nEscolha inválida.")
            except ValueError:
                slow_text("\nDigite um número válido.")
