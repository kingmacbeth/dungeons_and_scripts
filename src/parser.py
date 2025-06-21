import sys

from ply import yacc

from src.lexer import initialize_lexer, tokens


def p_script(p) -> None:
    """script : rooms"""
    p[0] = p[1]


def p_rooms_multiple(p) -> None:
    """rooms : rooms room"""
    p[0] = p[1]
    p[0][p[2]["name"]] = p[2]["stmts"]


def p_rooms_single(p) -> None:
    """rooms : room"""
    p[0] = {p[1]["name"]: p[1]["stmts"]}


def p_room(p) -> None:
    """room : ROOM ID LBRACE stmts RBRACE"""
    p[0] = {"name": p[2], "stmts": p[4]}


def p_stmts_multiple(p) -> None:
    """stmts : stmts stmt"""
    p[0] = p[1] + [p[2]]


def p_stmts_single(p) -> None:
    """stmts : stmt"""
    p[0] = [p[1]]


def p_stmt_text(p) -> None:
    """stmt : TEXT STRING"""
    p[0] = ("text", p[2].strip('"'))


def p_stmt_choice(p) -> None:
    """stmt : CHOICE STRING ARROW ID"""
    p[0] = ("choice", p[2].strip('"'), p[4])


def p_stmt_enemy(p) -> None:
    """stmt : ENEMY STRING ID NUMBER"""
    p[0] = ("enemy", p[2].strip('"'), int(p[4]))


def p_stmt_hero(p) -> None:
    """stmt : HERO STRING ID NUMBER"""
    p[0] = ("hero", p[2].strip('"'), int(p[4]))


def p_stmt_attack(p) -> None:
    """stmt : ATTACK"""
    p[0] = ("attack",)


def p_stmt_goto(p) -> None:
    """stmt : GOTO ID"""
    p[0] = ("goto", p[2])


def p_error(p) -> None:
    if p:
        print(f"\nErro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'.")
        sys.exit(1)
    else:
        print("\nErro de sintaxe no final do arquivo.")
        sys.exit(1)


parser = yacc.yacc()


def check_semantics(ast: dict) -> None:
    if "start" not in ast:
        raise ValueError("Erro semântico: sala 'start' não está definida.")

    for room_name, stmts in ast.items():
        for stmt in stmts:
            if stmt[0] in ("goto", "choice"):
                dest = stmt[-1]
                if dest not in ast:
                    raise ValueError(
                        f"Erro semântico: sala '{dest}' referenciada em '{room_name}' não existe."
                    )
            elif stmt[0] == "enemy":
                if len(stmt) < 3 or not isinstance(stmt[2], int) or stmt[2] <= 0:
                    raise ValueError(
                        f"Erro semântico: HP inválido do inimigo '{stmt[1]}' na sala '{room_name}'."
                    )
            elif stmt[0] == "attack":
                previous = [s for s in stmts if s[0] == "enemy"]
                if not previous:
                    raise ValueError(
                        f"Erro semântico: instrução 'attack' em '{room_name}' sem inimigo definido antes."
                    )


def parse_code(script_file: str) -> dict:
    lexer = initialize_lexer()
    ast = parser.parse(script_file, lexer=lexer)
    check_semantics(ast)
    return ast
