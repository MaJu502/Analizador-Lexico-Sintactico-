# Universidad del Valle de Guatemala
# Marco Jurado 20308
#
# infixTOpostfix.py
# El proposito es transformar una expresión infix a postfix usando el algoritmo Shunting Yard

precedencia = {'?':3, '*': 3, '+': 2, '.': 1, '|': 0}


# precedencia añadida en ciclo de verificación de tokens
#   1. letra o epsilon
#   2. cerraduras (tomando en cuenta el caracter ?)
#   3. parentesis 
#   4. or
def shunting_yard(exp):
    retorno = []
    operadores = []
    
    tokens = list(exp)
    
    for i in tokens:

        # primero las verificaciones que interactuan unicamente con el stack de retorno
        # casi 'base'
        if i.isalpha() or i == 'ε':
            # si es letra o epsilon
            retorno.append(i)
        elif i in '+*?':
            # si es cerradura o ?
            retorno[-1] += i

        # verificaciones que interactuan con el stack de operadores 
        elif i == '(':
            # parentesis que abre --> solo agrega a operadores
            operadores.append(i)
        elif i == ')':
            # parentesis que cierra --> comienza a verificar contenido de parentesis 
            while operadores[-1] != '(':

                """ mientras el siguiente elemento del stack de operadores no 
                    sea el parentesis que completa va a continuar haciendo el
                    append al retorno."""

                retorno.append(operadores.pop())
            # saca nuevo elemento del stack de operadores
            operadores.pop()
        elif i in '|.':
            # si es un or --> ver ambos componentes (puede ser más de un solo elemento) del or ya que es operador binario
            while operadores and operadores[-1] != '(':
                # mientras hayan elementos en el stack de operadores y no sea un parentesis que abre
                while precedencia[i] <= precedencia[operadores[-1]]:
                    # verificar que la precedencia del token actual sea menor o igual a la del siguiente operador
                    retorno.append(operadores.pop())
            # caso base del or
            operadores.append(i)


    # Se evaluó todo se agregan operadores restantes.
    while operadores:
        # Mientras existan operadores
        retorno.append(operadores.pop())
    
    # Retornar todos los elementos de la expresión postfix generada.
    return ''.join(retorno)
