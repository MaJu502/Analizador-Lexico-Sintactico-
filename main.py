from src.infixTOpostfix import *
from src.afn import *

regex = 'ab*ab*'
print(regex)

postfixRegex = shunting_yard(regex)
print(postfixRegex)

afnGENERADO = generadorAFN(postfixRegex)
print(afnGENERADO)