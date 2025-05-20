from lexerFHO import inicializaLexer
import sys
lexer = inicializaLexer("main.cpp")

lookAhead = lexer.token() # Inicializando o lookAhead

# tabela de símbolos
simbolos = {}

def analisaVariavel(identificador, tipo, linha):
    # Agora vou procurar na tabela de símbolos
    if verificaExistencia(identificador):
        print("Erro semântico(" + str(linha) +"):",
               identificador,"já previamente declarado")
        sys.exit(1)
    else:
        adicionarVariavel(identificador, tipo)

def verificaVariavelNaoDeclarada(identificador,  linha):
    global simbolos
    if not verificaExistencia(identificador):
        print("Erro semântico(" + str(linha) +"):",
               identificador,"não declarado")
        sys.exit(1)
    return simbolos[identificador]

def atualizaVariavel(identificador, valor):
    global simbolos
    simbolos[identificador]["valor"] = valor

def verificaExistencia(lexema):
    global simbolos
    return lexema in simbolos

def adicionarVariavel(lexema, tipo):
    global simbolos
    simbolos[lexema] = {
            "tipo" : tipo,
            "valor": ""
        } 

def match(esperado):
    global lookAhead
    if lookAhead != None and esperado == lookAhead.type:
        lookAhead = lexer.token() # continua o processo. 
        return
    
    print("Erro sintático na linha", lookAhead.lineno, "Esperado", esperado, "lido", lookAhead)
    sys.exit(1)


#Fator -> id | cte | ( ExpressaoInicial )
def fator(valor):
    if lookAhead.type == "IDENTIFICADOR":
        identificador = verificaVariavelNaoDeclarada(lookAhead.value, lookAhead.lineno)
        match("IDENTIFICADOR")
        return identificador["valor"]
    elif lookAhead.type == "CONSTANTE_INTEIRA":
        valor = lookAhead.value
        match("CONSTANTE_INTEIRA")
        return int(valor)
    elif lookAhead.type == "CONSTANTE_FLUTUANTE":
        valor = lookAhead.value
        match("CONSTANTE_FLUTUANTE")
        return float(valor)
    else:
        match("ABRE_PARENTESES")
        valor = expressaoInicial(valor)
        match("FECHA_PARENTESES")
        return valor
    return valor
    
#Termo -> * Fator Termo | / Fator Termo | $
def termo(valor):
    if lookAhead.type == "OPERADOR_ARITMETICO" and (lookAhead.value == "*" or lookAhead.value == "/"):
        operador = lookAhead.value
        match("OPERADOR_ARITMETICO")
        valor2 = fator(valor)
        if operador == "*":
            resultado = valor * valor2
        else:
            resultado = valor / valor2
        valor3 = termo(resultado)
        return valor3
    return valor
    
#Termo_Inicial -> Fator Termo
def termoInicial(valor):
    valor2 = fator(valor)
    valor3 = termo(valor2)
    return valor3

#Expressao -> + Termo_Inicial Expressao | - Termo_Inicial Expressao | $
def expressao(valor):
    if lookAhead.type == "OPERADOR_ARITMETICO" and (lookAhead.value == "+" or lookAhead.value == "-"):
        operador = lookAhead.value
        match("OPERADOR_ARITMETICO")
        valor2 = termoInicial(valor)
        if operador == "+":
            resultado = valor + valor2
        else:
            resultado = valor - valor2
        valor3 = expressao(resultado)
        return valor3
    return valor

# Expressao_Inicial -> Termo_Inicial Expressao
def expressaoInicial(valor):
    valor2 = termoInicial(valor)
    valor3 = expressao(valor2)
    return valor3

#CorpoCMD -> id = Expressao_Inicial ; CorpoCMD | $
def corpoCMD():
    if lookAhead.type == "IDENTIFICADOR":
        identificador = verificaVariavelNaoDeclarada(lookAhead.value, lookAhead.lineno)
        match("IDENTIFICADOR")
        match("OPERADOR_ATRIBUICAO")
        valor = expressaoInicial(0)
        identificador["valor"] = valor
        match("FIM_COMANDO")
        corpoCMD()

# ; Declaração | , id ListaVar
def listaVar(tipo):
    global lookAhead
    if lookAhead.type == "FIM_COMANDO":
        match("FIM_COMANDO")
        declaracao()
    elif lookAhead.type == "SEPARADOR":
        match("SEPARADOR")
        identificador = lookAhead.value
        match("IDENTIFICADOR")
        # Ação semântica de verificação de variável previamente declarada.
        analisaVariavel(identificador, tipo, lookAhead.lineno)
        listaVar(tipo)
  
# tipo id ListaVar | $
def declaracao():
    global lookAhead
    if lookAhead.type == "TIPO_DADO":
        tipo = lookAhead.value
        match("TIPO_DADO")
        identificador = lookAhead.value
        match("IDENTIFICADOR")
        # Ação semântica de verificação de variável previamente declarada.
        analisaVariavel(identificador, tipo, lookAhead.lineno)
        listaVar(tipo)

# Declaração CorpoCMD
def corpo():
    declaracao()
    corpoCMD()

# int main  () { Corpo }
def programa():
    match("TIPO_DADO")
    match("IDENTIFICADOR")
    match("ABRE_PARENTESES")
    match("FECHA_PARENTESES")
    match("ABRE_CHAVES")
    corpo()
    match("FECHA_CHAVES")

programa()
print("Sintaticamente correto!")
for s in simbolos:
    print(s,":",simbolos[s])
    