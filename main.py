from src.infixTOpostfix import *
from src.validacionErrores import *
from src.DibujarAutomata import * 
from src.afn import *

regex = '(a|b)*a(a|b)(a|b)'

if validarErrores(regex) == 1:
    # ingreso valido
    postfixRegex = shunting_yard(regex)
    print(' >> la posti: ',postfixRegex)

    afnGENERADO = generadorAFN(postfixRegex)
    print(' >> el AFN: ', afnGENERADO)
    print('\n')

    graficarAutom(afnGENERADO)

else: 
    # invalido. 
    pass