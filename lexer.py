import ply.lex as lex

tokens = (
    "ROOM",
    "TEXT",
    "CHOICE",
    "GOTO",
    "ENEMY",
    "ATTACK",
    "STRING",
    "ID",
    "NUMBER",
    "ARROW",
    "LBRACE",
    "RBRACE",
)

t_ignore = " \t"

t_ROOM = r"room"
t_TEXT = r"text"
t_CHOICE = r"choice"
t_GOTO = r"goto"
t_ENEMY = r"enemy"
t_ATTACK = r"attack"
t_ARROW = r"->"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_STRING = r'"[^"]*"'
t_ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
t_NUMBER = r"\d+"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
