from random import randint
from random import sample

# Lista donde dentro hay una lista de links de fotos y preguntas
preguntas_examen_PISA = {
    1: ["./Screen Shot 2022-10-11 at 10.30.27.png", "./pregunta.txt"],
    2: ["./Screen Shot 2022-10-11 at 18.29.55.png", "./pregunta (1).txt"]
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
