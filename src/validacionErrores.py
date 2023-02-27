# Universidad del Valle de Guatemala
# Marco Jurado 20308
# https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Syntax_Errors

# devuelve 1 si es valida y 0 si tiene errores.
def validarErrores(exp):
    # verificar caracteres permitidos
    if any(not i.isalpha() and not i.isdigit() and i not in '*+|?()' for i in exp):
        print(' >> El ingreso contiene caracteres invalidos. Unicamente se aceptan letras y los simbolos permitidos.')
        return 0

    # verificar conteo de parentesis
    abre = exp.count('(')
    cierra = exp.count(')')
    if abre != cierra:
        print(' >> La cantidad de parentesis no es la correcta. Asegurate de ingresar una expresion valida.')
        return 0

    # no puede termianr con |
    if exp.endswith('|'):
        print(' >> La expresion no puede terminar con |. Asegurate de ingresar una expresion valida. ')
        return 0

    # no puede empezar con * + | ? .
    for operator in '*+|?.': # combine the two loops into one
        if exp.startswith(operator):
            print(f' >> La expresion no puede empezar con el operador {operator} , asegurate de ingresar una expresion valida.')
            return 0

    # verificar que lexicamente los operadores esten bien ubicados
    for i, (token1, token2) in enumerate(zip(list(exp), list(exp)[1:]), start=0):
        if (token1 == "|" and token2 in '*+|?.'):
            print(f'  >> Verifica que la posicion de los simbolos operadores sea correcta en el indice {i} y {i+1}.')
            return 0

    return 1