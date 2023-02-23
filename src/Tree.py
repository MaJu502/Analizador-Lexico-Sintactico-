# Universidad del Valle de Guatemala
# Marco Jurado 20308
# basado en proyecto realizado para teoria de la computacion

class Tree:
    # constantes
    indice = 0
    simbolos = []
    letras = []

    def get_indice(self):
        return type(self).indice

    def set_indice(self,x):
        type(self).indice = x

    def reset_indice(self):
        self.set_indice(0)

    def get_simbolos(self):
        return type(self).simbolos

    def set_simbolos(self,x):
        type(self).simbolos.append(x)

    def reset_simbolos(self):
        type(self).simbolos = []

    def get_letras(self):
        return type(self).letras

    def set_letras(self, x):
        if x not in type(self).letras:
            type(self).letras.append(x)

    def reset_letras(self):
        type(self).letras = []

    def posicion_indice(self):
        ultimo = self.get_indice()
        self.set_indice(ultimo + 1)
        return ultimo

    i = property(get_indice, set_indice)
    simbols = property(get_simbolos, set_simbolos)
    letras = property(get_letras, set_letras)

    def __init__(self, exp) -> None:
        postfix = list(postfix) if type(postfix) == str else postfix

        # Si el postfix tiene 1 caracter
        self.root = postfix.pop()
        if len(postfix) == 0:
            self.set_letras(self.root)
            self.followposBucket = []
            self.position = self.__setPosition_i()
            self.set_s((self.position, self.root))
            self.leftChild = ''
            self.rightChild = ''
            if self.root == '#':
                self.reset_i()
            return

        if self.root in ['*', '+']:
            self.leftChild = ''
            self.rightChild = Tree(postfix)
            return

        # Hijo derecho
        self.rightChild = postfix.pop()

        if self.rightChild in ['.', '|', '*', '+', '?']:
            operators = 2 if self.rightChild in ['.', '|'] else 1

            while operators > 0:
                operators -= 1
                temp_char = postfix.pop()

                if temp_char in ['.', '|', '*', '+', '?']:
                    operators += 2 if self.rightChild in ['.', '|'] else 1

                self.rightChild = temp_char + self.rightChild

        # Hijo Izquierdo
        self.leftChild = Tree(postfix)
        self.rightChild = Tree(self.rightChild)

    def __repr__(self) -> str:
        if self.leftChild == '' and self.rightChild == '':
            return f'{self.root}-{self.position}'
        if self.root == '*':
            return f'Root: [{self.root}] child: [{self.rightChild}]'

        return f'Root: [{self.root}] rightChild: [\n{self.rightChild}\n] leftChild: [\n{self.leftChild}\n]'



# nullable -> usar e closure y si el e closure devuelve algo entonces si es nullable
def nullable(n: Tree) -> bool:

    raiz = n.root

    # Caso Epsilon
    if raiz == 'ε':
        return True

    # Caso or
    elif raiz == '|':
        if nullable(n.rightChild) is True or nullable(n.leftChild) is True:
            return True
        else:
            return False

    elif raiz == '.':
        if nullable(n.rightChild) is True and nullable(n.leftChild) is True:
            return True
        else:
            return False

    # Caso Kleen
    elif raiz == '*':
        return True

    elif raiz == '+':
        return False

    # caso ? ---> a|ε donde epsilon es nullable.
    elif raiz == '?':
        return True

    else:
        # caso base que es un elemento del alfabeto
        return False


def firstpos(n: Tree):

    raiz = n.root
    hijoIZQ = n.leftChild
    hijoDER = n.rightChild

    if raiz == 'ε':
        return []

    elif raiz == '.':
        if nullable(hijoIZQ):
            # la union de firstops de los hijos derecho e izquierdo
            return firstpos(hijoIZQ) + firstpos(hijoDER)
        else:
            # firspos de hijo izquierdo
            return firstpos(hijoIZQ)

    elif raiz == '|':
        return firstpos(hijoIZQ) + firstpos(hijoDER)

    elif raiz == 'ε':
        return firstpos(hijoDER)

    elif raiz == '*':
        return firstpos(hijoDER)

    elif raiz == '+':
        return firstpos(hijoDER)

    elif hijoIZQ == '' and hijoDER == '':
        # no tiene hijos
        return [n.position]


def lastpos(n: Tree):
    raiz = n.root
    hijoIZQ = n.leftChild
    hijoDER = n.rightChild

    if raiz == 'ε':
        return []

    elif raiz == '.':
        if nullable(hijoDER):
            # la union de firstops de los hijos derecho e izquierdo
            return lastpos(hijoIZQ) + lastpos(hijoDER)
        else:
            # firspos de hijo izquierdo
            return lastpos(hijoDER)

    elif raiz == '|':
        return lastpos(hijoIZQ) + lastpos(hijoDER)

    elif raiz == '*':
        return lastpos(hijoDER)

    elif raiz == '+':
        return lastpos(hijoDER)

    elif hijoIZQ == '' and hijoDER == '':
        # no tiene hijos
        return [n]


def followpos(n: Tree):
    raiz = n.root
    hijoDER = n.rightChild
    hijoIZQ = n.leftChild

    if hijoIZQ == '' and hijoDER == '':
        return

    if raiz == '.':
        izquierdo = lastpos(
            hijoIZQ
        )  # devuelve todos los arboles en el lastpos del hijo izq para añadirles el firstpos del hijo derecho de la root
        derecho = firstpos(hijoDER)  # este se agrega al followpos de 'izquierdo'

        for i in izquierdo:
            # recorrer todos los arboles del lastpos
            i.followposBucket = i.followposBucket + derecho

        # recursioooon programar es una fiesta yupi
        followpos(hijoDER)
        followpos(hijoIZQ)

    elif raiz == '*' or raiz == '+':
        # caso kleeen
        temp = lastpos(n)
        first = firstpos(n)

        for i in temp:
            i.followposBucket = i.followposBucket + first

        followpos(hijoDER)

    elif raiz == '|':
        followpos(hijoIZQ)
        followpos(hijoDER)

    else:
        return


def obtenerbuckets(n: Tree):
    hijoDER = n.rightChild
    hijoIZQ = n.leftChild
    retorno = []

    if hijoDER == '' and hijoIZQ == '':
        retorno.append(n.followposBucket)

    elif n.root == '.' or n.root == '|':
        left = obtenerbuckets(hijoIZQ)
        right = obtenerbuckets(hijoDER)
        retorno = retorno + [*left, *right]

    elif n.root == '*' or n.root == '+':
        right = obtenerbuckets(hijoDER)
        retorno = retorno + [*right]

    return retorno