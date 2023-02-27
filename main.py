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
    print(' >> el AFN: ')
    print('     >> Estados: ',afnGENERADO[0])
    print('     >> estado inicial: ',afnGENERADO[1])
    print('     >> estados de aceptacion: ',afnGENERADO[2])
    print('     >> transiciones: ')
    for i in afnGENERADO[3]:
        print('         ->  ', i)
    print('\n')

    graficarAutom(afnGENERADO)

else: 
    # invalido. 
    pass