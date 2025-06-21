import os
import sys
import time

from src.utils import cartridge_menu, intro, load_script, loading, slow_text
from src.vm import VM


def main():
    while True:
        os.system("clear")
        intro()
        cartridge_menu()

        choice = input("\nSeleção: ").strip()

        if choice == "0":
            print("\nObrigado por jogar!")
            loading("\nEncerrando")

            os.system("clear")
            sys.exit(0)

        elif choice == "1":
            loading("\nCarregando 'Castelo Sombrio'")
            script = load_script("scripts/castelo_sombrio.msr")
        elif choice == "2":
            loading("\nCarregando 'Floresta Maldita'")
            script = load_script("scripts/floresta_maldita.msr")
        elif choice == "3":
            loading("\nCarregando 'A Fortaleza do Demônio'")
            script = load_script("scripts/fortaleza_demonio.msr")
        elif choice == "4":
            loading("\nCarregando 'Morte no Espaço'")
            script = load_script("scripts/morte_espaco.msr")
        else:
            os.system("clear")
            slow_text("Escolha inválida. Por favor, tente novamente.")
            time.sleep(1)
            continue

        vm = VM(script)

        while vm.current_room:
            vm.run()

        time.sleep(1)
        print("\nFim do jogo.")
        input("\nPressione a tecla 'Enter' para retornar ao menu principal.\n")


if __name__ == "__main__":
    main()
