# Universidad del Valle de Guatemala
# Marco Jurado 20308
import re
def agregarPuntos(exp):
    retorno = ''
    if len(exp) == 1:
        for i, X in enumerate(exp):
            retorno += X
    else:
        for i, X in enumerate(exp):
            if i > 0 and (re.match(r'\w|\(', X)) and (exp[i-1] not in '|(') and  (X not in '*+?'):
                retorno += '.'

            retorno += X
    
    return retorno