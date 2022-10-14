from random import randint
from random import sample

# Lista donde dentro hay una lista de links de fotos y preguntas
preguntas_examen_PISA = {
    1 : ["./Pregunta 1/Screen Shot 2022-10-11 at 10.30.27.png", "./Pregunta 1/pregunta.txt"],
    2 : ["./Pregunta 2/Copia de Screen Shot 2022-10-11 at 10.30.27.png", "./Pregunta 2/pregunta.txt"],
    3 : ["./Pregunta 3/Screen Shot 2022-10-11 at 17.58.57.png", "./Pregunta 3/pregunta.txt"],
    4 : ["", "./Pregunta 4/pregunta.txt"],
    5 : ["./Pregunta 5/Screen Shot 2022-10-11 at 18.03.33.png", "./Pregunta 5/pregunta.txt"],
    6 : ["./Pregunta 6/Screen Shot 2022-10-13 at 19.41.53 1.png", "./Pregunta 6/pregunta.txt"],
    7 : ["./Pregunta 8/Screen Shot 2022-10-11 at 18.29.55.png", "./Pregunta 8/pregunta.txt"],
    8 : ["./Pregunta 9/Screen Shot 2022-10-11 at 18.31.29.png", "./Pregunta 9/pregunta.txt"],
    9 : ["./Pregunta 10/Screen Shot 2022-10-11 at 18.33.51.png", "./Pregunta 10/pregunta.txt"]
}

# Lista de keys del diccionario en orden aleatorio sin repetir
keys = sample(range(1,len(preguntas_examen_PISA)+1),len(preguntas_examen_PISA))
    
def obtener_pregunta():
    '''
    Escoge una pregunta del diccionario de manera aleatoria
    ''' 
    pregunta = preguntas_examen_PISA[keys[0]]
    imagen = pregunta[0]
    texto = pregunta[1]
    keys.pop(0)
    return imagen, texto
