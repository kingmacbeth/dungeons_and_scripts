from lex import lex
import sys

# Primeiro passo: definir os tokens
tokens = ( "TIPO_DADO", "IDENTIFICADOR", "CONSTANTE_INTEIRA", "CONSTANTE_CHAR", "CONSTANTE_FLUTUANTE", "ABRE_PARENTESES", 
           "FECHA_PARENTESES", "ABRE_CHAVES", "FECHA_CHAVES", "FIM_COMANDO", "SEPARADOR", "OPERADOR_ATRIBUICAO", "OPERADOR_ARITMETICO")

t_TIPO_DADO = "int|float|char|double"
t_ABRE_PARENTESES = "\("
t_FECHA_PARENTESES = "\)"
t_ABRE_CHAVES = "\{"
t_FECHA_CHAVES = "\}"
t_FIM_COMANDO = "\;"
t_SEPARADOR = "\,"
t_OPERADOR_ATRIBUICAO = "\="
t_OPERADOR_ARITMETICO = "\+|\-|\*|\/|\%"
t_CONSTANTE_INTEIRA = "\d\d*"
t_CONSTANTE_CHAR = "\'[a-zA-Z]\'"
t_CONSTANTE_FLUTUANTE = "\d+\.\d+"
    
def t_MUDA_LINHA(t):
    r"\n"
    t.lexer.lineno += 1
# Esses tokens são pré-definidos e não precisam comparecer na tupla "tokens"
t_ignore = " "

# Definir como uma função

def t_error(t):
    print(t, "não foi reconhecido!")
    sys.exit(1)

def t_IDENTIFICADOR(t):
    "[a-zA-Z][a-zA-Z0-9]*" 
   
    if t.value in ('int', 'float', 'char', 'double'):
        t.type = 'TIPO_DADO'
    return t

def inicializaLexer(arquivo):
    # Terceiro passo: abrir o código fonte
    arquivo = open(arquivo)
    conteudo = arquivo.read()

    # Quarto passo: instanciar o lexer e carregar o conteúdo
    l = lex()
    l.input(conteudo)
    return l
