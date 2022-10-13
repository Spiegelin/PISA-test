from random import randint

preguntas_examen_PISA = {
    1 : ["Path Foto", "Path Texto"],
    2 : ["Path Foto", "Path Texto"]
}

def obtener_pregunta():
    '''
    Escoge una pregunta del diccionario de manera aleatoria
    '''
    index = randint(1, len(preguntas_examen_PISA))
    pregunta = preguntas_examen_PISA[index]
    imagen = pregunta[0]
    texto = pregunta[1]
    return imagen, texto

