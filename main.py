from src.infixTOpostfix import *

regex = 'ab*ab*'
print(regex)

postfixRegex = shunting_yard(regex)
print(postfixRegex)
