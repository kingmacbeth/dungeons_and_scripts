from utils import load_script
from vm import VM


def main():
    print("Bem-vindo ao Dungeons and Scripts!")
    print("Cartuchos para jogar: ")
    print("1. Floresta Maldita")
    print("2. Fortaleza do Demônio")
    print("3. Morte no Espaço")
    print("4. Teste")

    choice = input("Digite o número do cartucho: ")
    if choice not in ["1", "2", "3", "4"]:
        print("Escolha inválida. Encerrando o jogo.")
        return
    print(f"Você escolheu o cartucho {choice}. Carregando o jogo...")

    if choice == "1":
        print("Carregando Floresta Maldita...")
        script = load_script("scripts/floresta_maldita.msr")
    elif choice == "2":
        print("Carregando Fortaleza do Demônio...")
        script = load_script("scripts/fortaleza_demonio.msr")
    elif choice == "3":
        print("Carregando Morte no Espaço...")
        script = load_script("scripts/morte_espaco.msr")
    elif choice == "4":
        print("Carregando Teste...")
        script = load_script("scripts/example.msr")
    vm = VM(script)

    while vm.current_room:
        vm.run()

    print("Fim do jogo.")


if __name__ == "__main__":
    main()
