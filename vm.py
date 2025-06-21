import os


class VM:
    def __init__(self, game_data):
        self.game_data = game_data
        self.current_room = "start"
        self.hp = 10

    def show_enemy_art(self, enemy_id: str) -> None:
        base_path = os.path.dirname(__file__)
        art_path = os.path.join(base_path, "ascii_assets", f"{enemy_id}.txt")

        if os.path.exists(art_path):
            with open(art_path, "r", encoding="utf-8") as f:
                art = f.read()
            print(art)
        else:
            print(f"[ilustração não disponível para '{enemy_id}']")

    def run(self):
        while True:
            room = self.game_data.get(self.current_room)
            if not room:
                break

            next_room_set = False

            for stmt in room:
                if stmt[0] == "text":
                    print(f"\n📜 {stmt[1]}")
                elif stmt[0] == "enemy":
                    enemy_name = stmt[1]
                    enemy_hp = stmt[2]
                    print(f"\n👹 Um inimigo apareceu: {enemy_name} (HP {enemy_hp})")
                    self.enemy_hp = enemy_hp
                    self.show_enemy_art(enemy_name.lower().replace(" ", "_"))
                elif stmt[0] == "attack":
                    self.handle_attack()
                elif stmt[0] == "choice":
                    choices = [s for s in room if s[0] == "choice"]
                    self.handle_choices(choices)
                    return  # Sai do loop após escolha
                elif stmt[0] == "goto":
                    self.current_room = stmt[1]
                    return

            if not next_room_set:
                self.current_room = None

    def handle_attack(self):
        print("\n⚔ Iniciando combate...")
        while self.enemy_hp > 0:
            input("Pressione Enter para atacar!")
            self.enemy_hp -= 3
            print(f"👊 Você causou 3 de dano. HP do inimigo: {self.enemy_hp}")
            if self.enemy_hp <= 0:
                print("✅ Inimigo derrotado!")
                return

    def handle_choices(self, choices):
        print("\n🤔 Escolha uma opção:")
        for idx, choice in enumerate(choices):
            print(f"{idx + 1}. {choice[1]}")

        while True:
            try:
                opt = int(input("Sua escolha: "))
                if 1 <= opt <= len(choices):
                    self.current_room = choices[opt - 1][2]
                    return
                else:
                    print("Escolha inválida.")
            except ValueError:
                print("Digite um número válido.")
