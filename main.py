import sys

from utils import cartridge_menu, intro, load_script, loading
from vm import VM


def main():
    while True:
        intro()
        cartridge_menu()

        choice = input("Seleção: ").strip()

        if choice == "0":
            print("Encerrando o jogo. Até logo!")
            sys.exit(0)

        elif choice == "1":
            loading("Carregando Floresta Maldita")
            script = load_script("scripts/floresta_maldita.msr")
        elif choice == "2":
            loading("Carregando Fortaleza do Demônio")
            script = load_script("scripts/fortaleza_demonio.msr")
        elif choice == "3":
            loading("Carregando Morte no Espaço")
            script = load_script("scripts/morte_espaco.msr")
        elif choice == "4":
            loading("Carregando Castelo Sombrio")
            script = load_script("scripts/castelo_sombrio.msr")
        else:
            print("Escolha inválida. Por favor, tente novamente.")
            continue

        vm = VM(script)

        while vm.current_room:
            vm.run()

        print("Fim do jogo.")
        input("\nPressione Enter para retornar ao menu principal...\n")


if __name__ == "__main__":
    main()
