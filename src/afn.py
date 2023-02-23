# Universidad del Valle de Guatemala
# Marco Jurado 20308
#

def generadorAFN(exp:str):
    exp = exp.replace('.#', '')
    bucket = exp.split('.')
    x = AFN(bucket[0])
    for element in bucket[-1]:
        x = agregarAFN(x, AFN(element))
    return x

def agregarAFN(q0, q1):
    offset = len(q0[0]) - 1

    #elementos del nuevo afn.
    transiciones = [(q[0] + offset, q[1] + offset, q[2]) for q in q1[3]]
    estados = list(range(offset + len(q1[0])))
    inicio = [q0[1][0]]
    aceptacion = [q1[2][0] + offset]

    return [estados, inicio, aceptacion, q0[3] + transiciones]

def AFN(Concat):
    estados = []
    inicial = []
    aceptacion = []
    transiciones = []

    # Cuando son caracteres
    if len(Concat) == 1:
        estados = [0, 1]
        inicial = [0]
        aceptacion = [1]
        transiciones = [(0, 1, Concat)]
    
    elif len(Concat) > 1:
        Concat = list(Concat)
        operador = Concat.pop()

        if operador == "|":
            a, b = "", ""

            # A y b son letras
            if len(Concat) == 2:
                a = AFN(Concat.pop())
                b = AFN(Concat.pop())

            # A es letra, b es operacion
            elif (
                abecedario.fullmatch(Concat[-1]) is not None
                and abecedario.fullmatch(Concat[-2]) is None
            ):
                a = AFN(Concat.pop())
                b = AFN("".join(Concat))

            # b es letra, a es operacion
            elif (
                abecedario.fullmatch(Concat[-1]) is None
                and abecedario.fullmatch(Concat[-2]) is not None
            ):
                # (Ejemplo) aba|
                b = AFN(Concat.pop(0))
                a = AFN("".join(Concat))

            # a y b son operciones
            else:
                a = AFN("".join(Concat))
                b = AFN("".join(Concat))

            suma = len(a[0]) + len(b[0])
            offset_a = 1

            for i in range(len(a[3])):
                transicion = a[3]
                transicion[i] = (
                    transicion[i][0] + offset_a,
                    transicion[i][1] + offset_a,
                    transicion[i][2],
                )

            offset_b = len(a[0]) + 1
            for i in range(len(b[3])):
                transicion = b[3]
                transicion[i] = (
                    transicion[i][0] + offset_b,
                    transicion[i][1] + offset_b,
                    transicion[i][2],
                )
            Estados = list(range(2 + suma))
            Inicio = [0]
            Aceptacion = [suma + 1]
            Transiciones = [
                (0, 1, "~"),
                (0, len(a[0]) + 1, "~"),
                *a[3],
                *b[3],
                (len(a[0]), suma + 1, "~"),
                (len(b[0]) + offset_b - 1, suma + 1, "~"),
            ]

        elif operador == "*":
            a = AFN("".join(Concat))
            offset = len(a[0])
            Estados = list(range(offset + 2))
            Inicio = [0]
            Aceptacion = [offset + 1]
            for i in range(len(a[3])):
                transicion = a[3]
                transicion[i] = (
                    transicion[i][0] + 1,
                    transicion[i][1] + 1,
                    transicion[i][2],
                )
            Transiciones = [
                (0, 1, "~"),
                *a[3],
                (offset, offset + 1, "~"),
                (0, offset + 1, "~"),
                (offset, 1, "~"),
            ]

        elif operador == "+":
            a = AFN("".join(Concat))
            offset = len(a[0])
            Estados = list(range(offset + 2))
            Inicio = [0]
            Aceptacion = [offset + 1]
            for i in range(len(a[3])):
                transicion = a[3]
                transicion[i] = (
                    transicion[i][0] + 1,
                    transicion[i][1] + 1,
                    transicion[i][2],
                )
            Transiciones = [
                (0, 1, "~"),
                *a[3],
                (offset, 1, "~"),
                (offset, offset + 1, "~"),
            ]

    stringEstados = "Estados: " + str(Estados)
    stringInicio = "Inicio: " + str(Inicio)
    stringAceptacion = "Aceptacion: " + str(Aceptacion)
    stringTransiciones = "Transiciones: " + str(Transiciones)
    titulo = "Thompson"

    stringFinal = (
        titulo
        + "\n"
        + stringEstados
        + "\n"
        + stringInicio
        + "\n"
        + stringAceptacion
        + "\n"
        + stringTransiciones
    )

    txt.EscribirTexto("Thompson", stringFinal)
    return [Estados, Inicio, Aceptacion, Transiciones]