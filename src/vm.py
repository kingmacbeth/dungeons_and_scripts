import os

from src.utils import slow_text


class VM:
    def __init__(self, game_data):
        self.game_data = game_data
        self.current_room = "start"
        self.max_hp = 10
        self.current_hp = 10
        self.enemy_name = ""

    def show_enemy_art(self, enemy_id: str) -> None:
        base_path = os.path.dirname(__file__)
        art_path = os.path.normpath(
            os.path.join(base_path, "..", f"ascii/{enemy_id}.txt")
        )

        if os.path.exists(art_path):
            with open(art_path, "r", encoding="utf-8") as f:
                art = f.read()
            slow_text(art, 0.01)
        else:
            slow_text(f"\n[ilustração não disponível para '{enemy_id}']")

    def run(self) -> None:
        while True:
            room = self.game_data.get(self.current_room)
            if not room:
                break

            next_room_set = False

            for stmt in room:
                if stmt[0] == "text":
                    slow_text(f"\n{stmt[1]}")
                elif stmt[0] == "enemy":
                    self.enemy_name = stmt[1]
                    self.max_hp = stmt[2]
                    slow_text(f"\nUm inimigo apareceu: {self.enemy_name}")
                    slow_text(f"\n(HP {self.max_hp})")
                    self.show_enemy_art(self.enemy_name.lower().replace(" ", "_"))
                elif stmt[0] == "attack":
                    self.handle_attack()
                elif stmt[0] == "choice":
                    choices = [s for s in room if s[0] == "choice"]
                    self.handle_choices(choices)
                    return
                elif stmt[0] == "goto":
                    self.current_room = stmt[1]
                    return

            if not next_room_set:
                self.current_room = None

    def handle_attack(self) -> None:
        slow_text("\nIniciando combate...")
        while self.current_hp > 0:
            input("\nPressione Enter para atacar!")
            self.current_hp -= 3
            slow_text(f"\nVocê causou 3 de dano. HP do inimigo: {self.current_hp}")
            if self.current_hp <= 0:
                slow_text("\nInimigo derrotado!")
                self.show_enemy_art(
                    self.enemy_name.lower().replace(" ", "_") + "_morto"
                )
            elif self.current_hp <= 0.6 * self.max_hp:
                self.show_enemy_art(
                    self.enemy_name.lower().replace(" ", "_") + "_machucado"
                )
            else:
                self.show_enemy_art(self.enemy_name.lower().replace(" ", "_"))

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
