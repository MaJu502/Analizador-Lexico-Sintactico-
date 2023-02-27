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
    # Open the file in write mode
    with open('afn.txt', 'w',encoding='utf-8') as f:
        f.write(' >> el AFN: \n')
        f.write('     >> Estados: {}\n'.format(afnGENERADO[0]))
        f.write('     >> estado inicial: {}\n'.format(afnGENERADO[1]))
        f.write('     >> estados de aceptacion: {}\n'.format(afnGENERADO[2]))
        f.write('     >> transiciones: \n')
        for i in afnGENERADO[3]:
            f.write('         ->  ')
            for j in i:
                f.write('{} '.format(j))
            f.write('\n')
        f.write('\n')

    graficarAutom(afnGENERADO)

else: 
    # invalido. 
    pass