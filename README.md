# Dungeons and Scripts

**Dungeons and Scripts** é uma aventura textual que utiliza
uma DSL chamada **MiniScriptRoom (.msr)** para definir salas, inimigos, escolhas e a progressão narrativa do jogo.
O projeto inclui um **lexer**, **parser**, **máquina virtual (VM)** e arte em ASCII para imersão visual no terminal.

---

## Instalação

Requisitos:
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (ou pip tradicional)

Clone o repositório e instale os pacotes:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

---

## Rodando o Jogo

Execute o jogo principal com:

```bash
python main.py
```

Você verá um menu com cartuchos de aventuras:

```
Digite o número do cartucho:
1. Floresta Maldita
2. Fortaleza do Demônio
3. Morte no Espaço
4. Castelo Sombrio
```

Para sair, digite `0`.

---

## Escrevendo Scripts .msr

Os arquivos `.msr` definem a lógica da aventura e seguem a linguagem MiniScriptRoom.
Veja um exemplo básico:

```msr
room start {
  text "Você está numa sala escura com duas saídas."

  choice "Ir para o corredor" -> corredor
  choice "Explorar a escuridão" -> morte
}

room corredor {
  text "Você entrou no corredor e ouviu passos."

  enemy "Goblin" goblin 10
  attack

  goto tesouro
}

room tesouro {
  text "Você encontrou um baú cheio de ouro. Parabéns!"
}

room morte {
  text "Você tropeçou e caiu num poço sem fundo. Fim de jogo."
}
```

### Tokens disponíveis

| Token      | Exemplo                                          | Descrição                                |
|------------|--------------------------------------------------|------------------------------------------|
| `room`     | `room corredor { ... }`                          | Define uma sala                          |
| `text`     | `text "Você vê uma sombra..."`                   | Mostra texto ao jogador                  |
| `choice`   | `choice "Ir à direita" -> direita`               | Cria uma escolha                         |
| `goto`     | `goto proxima_sala`                              | Salta diretamente para outra sala        |
| `enemy`    | `enemy "Goblin" HP 10`                           | Cria inimigo com nome, ID e HP           |
| `attack`   | `attack`                                         | Inicia o combate                         |
| `hero`     | `hero "Arthur" HP 20`                            | Define o nome e HP do herói *(opcional)* |

---

## Debug

Scripts auxiliares para análise de código `.msr`:

### Ver tokens e AST:
```bash
python debug/debug_lexer.py scripts/castelo_sombrio.msr
python debug/debug_parser.py scripts/castelo_sombrio.msr
```

### Executar jogo diretamente:
```bash
python debug/debug_vm.py scripts/castelo_sombrio.msr
```

---

## Arte ASCII

Os inimigos têm artes ASCII associadas. Coloque os arquivos em `ascii/` com nomes correspondentes:

```
ascii/
├── goblin.txt
├── goblin_machucado.txt
├── goblin_morto.txt
├── drone_de_seguranca.txt
├── espirito_antigo.txt
```

---

Projeto acadêmico da disciplina de Compiladores — FHO.

---
