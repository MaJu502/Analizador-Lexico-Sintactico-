from src.infixTOpostfix import *
from src.validacionErrores import *
from src.afn import *

regex = 'ab*ab*'
print(regex)

if validarErrores(regex) == 1:
    # ingreso valido
    postfixRegex = shunting_yard(regex)
    print(postfixRegex)

    afnGENERADO = generadorAFN(postfixRegex)
    print(afnGENERADO)
else: 
    # invalido. 
    pass