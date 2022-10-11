from random import randint

preguntas_examen_PISA = {
    1 : ["/", "Hora: "],
    2 : "123",
    3 : "456"
}

def obtener_pregunta():
    '''
    Escoge una pregunta del diccionario de manera aleatoria
    '''
    index = randint(0, len(preguntas_examen_PISA))
    pregunta = preguntas_examen_PISA[index]
    return pregunta
