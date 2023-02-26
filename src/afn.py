# Universidad del Valle de Guatemala
# Marco Jurado 20308
#
from src.outPutTXT import *

def generadorAFN(exp:str):
    retorno = []
    exp = exp.replace('.#', '')
    exp = list(exp)
    print(exp)
    for element in exp:
        # se verifica que tipo de elemento es
        if element.isalpha() or element == 'ε':
            # caso base de letra o epsilon
            retorno.append(AFN(element,''))

        elif element in '|.':
            # caso or se tienen que sacar los ultimos dos construidos 
            a = retorno.pop()
            b = retorno.pop()
            retorno.append(binaryJoin(a,b, element))

        elif element in '*+?':
            # sacar el ultimo afn para agregarle la cerradura
            a = retorno.pop()
            retorno.append(AFN(a,element))

    return retorno
    
def AFN(element, operador):
    if operador == '':
        # es una letra o epsilon.
        estados = [0, 1]
        inicial = [0]
        aceptacion = [1]
        transiciones = [(0, 1, element)]
    
    elif operador == '*':
        estados = list(range(len(element[0]) + 2))
        inicial = [0]
        aceptacion = [len(element[0]) + 1]
        for i, (from_state, to_state, symbol) in enumerate(element[3]):
            element[3][i] = (from_state + 1, to_state + 1, symbol)
        transiciones = [
                (0, 1, "ε"),
                *element[3],
                (len(element[0]), len(element[0]) + 1, "ε"),
                (0, len(element[0]) + 1, "ε"),
                (len(element[0]), 1, "ε"),
            ]

    elif operador == '+':
        estados = list(range(len(element[0]) + 2))
        inicial = [0]
        aceptacion = [len(element[0]) + 1]
        for i, (from_state, to_state, symbol) in enumerate(element[3]):
            element[3][i] = (from_state + 1, to_state + 1, symbol)
        transiciones = [
                (0, 1, "ε"),
                *element[3],
                (len(element[0]), len(element[0]) + 1, "ε"),
                (len(element[0]), 1, "ε"),
            ]
        
    elif operador == '?':
        estados = list(range(len(element[0]) + 2))
        inicial = [0]
        aceptacion = [len(element[0]) + 1]
        for i, (from_state, to_state, symbol) in enumerate(element[3]):
            element[3][i] = (from_state + 1, to_state + 1, symbol)
        transiciones = [
                (0, 1, "ε"),
                *element[3],
                (len(element[0]), len(element[0]) + 1, "ε"),
                (0, len(element[0]) + 1, "ε"),
            ]

    return [estados, inicial, aceptacion, transiciones]


def binaryJoin(a,b,operador):
    if operador == '|':
        suma = len(a[0]) + len(b[0])
        estados = list(range(2 + suma))
        inicial = [0]
        aceptacion = [suma + 1]
        for i, (from_state, to_state, symbol) in enumerate(a[3]):
            a[3][i] = (from_state + 1, to_state + 1, symbol)
        for i, (from_state, to_state, symbol) in enumerate(b[3]):
            b[3][i] = (from_state + len(a[0]) + 1, to_state + len(a[0]) + 1, symbol)
        transiciones = [
                (0, 1, "ε"),
                (0, len(a[0]) + 1, "ε"),
                *a[3],
                *b[3],
                (len(a[0]), suma + 1, "ε"),
                (suma, suma + 1, "ε"),
            ]

    elif operador == '.':
        estados = list(range(len(a[0]) + len(b[0])))
        inicial = [0]
        aceptacion = [len(estados)-1]
        for i, (from_state, to_state, symbol) in enumerate(b[3]):
            b[3][i] = (from_state + len(a[0])-1, to_state + len(a[0])-1, symbol)

        transiciones = [
                *a[3],
                *b[3]
            ]
    return [estados, inicial, aceptacion, transiciones]

def describirAFN(x, nombre):
    titulo = f"Thompson_de_{nombre}"
    stringEstados = f"Estados: {x[0]}"
    stringInicio = f"Inicio: {x[1]}"
    stringAceptacion = f"Aceptacion: {x[2]}"
    stringTransiciones = f"Transiciones: {x[3]}"

    stringFinal = f"{titulo}\n{stringEstados}\n{stringInicio}\n{stringAceptacion}\n{stringTransiciones}"

    generarOUT(titulo, stringFinal)