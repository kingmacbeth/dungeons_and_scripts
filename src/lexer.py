from ply import lex

reserved = {
    "room": "ROOM",
    "text": "TEXT",
    "choice": "CHOICE",
    "goto": "GOTO",
    "enemy": "ENEMY",
    "attack": "ATTACK",
}

tokens = ["STRING", "ID", "NUMBER", "ARROW", "LBRACE", "RBRACE"] + list(
    reserved.values()
)

t_ARROW = r"->"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_STRING = r'"[^"]*"'
t_NUMBER = r"\d+"

t_ignore = " \t"


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()
