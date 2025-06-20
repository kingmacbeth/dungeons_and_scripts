from ply import yacc

from lexer import tokens

# Estrutura para guardar os dados do jogo
game_data = {}


def p_script(p):
    """script : rooms"""
    global game_data
    game_data = p[0]
    p[0] = p[1]


def p_rooms_multiple(p):
    """rooms : rooms room"""
    p[0] = p[1]
    p[0][p[2]["name"]] = p[2]["stmts"]


def p_rooms_single(p):
    """rooms : room"""
    p[0] = {p[1]["name"]: p[1]["stmts"]}


def p_room(p):
    """room : ROOM ID LBRACE stmts RBRACE"""
    p[0] = {"name": p[2], "stmts": p[4]}


def p_stmts_multiple(p):
    """stmts : stmts stmt"""
    p[0] = p[1] + [p[2]]


def p_stmts_single(p):
    """stmts : stmt"""
    p[0] = [p[1]]


def p_stmt_text(p):
    """stmt : TEXT STRING"""
    p[0] = ("text", p[2].strip('"'))


def p_stmt_choice(p):
    """stmt : CHOICE STRING ARROW ID"""
    p[0] = ("choice", p[2].strip('"'), p[4])


def p_stmt_enemy(p):
    """stmt : ENEMY STRING ID NUMBER"""
    p[0] = ("enemy", p[2].strip('"'), int(p[4]))


def p_stmt_attack(p):
    """stmt : ATTACK"""
    p[0] = ("attack",)


def p_stmt_goto(p):
    """stmt : GOTO ID"""
    p[0] = ("goto", p[2])


def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe no final do arquivo")


parser = yacc.yacc()
