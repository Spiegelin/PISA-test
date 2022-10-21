from random import randint
from random import sample

# Lista donde dentro hay una lista de links de fotos y preguntas
preguntas_examen_PISA = {
    1 : ["drive-download-20221014T003101Z-001/Pregunta 1/Screen Shot 2022-10-11 at 10.30.27.png", "drive-download-20221014T003101Z-001/Pregunta 1/pregunta.txt", "10 am"],
    2 : ["drive-download-20221014T003101Z-001/Pregunta 2/Copia de Screen Shot 2022-10-11 at 10.30.27.png", "drive-download-20221014T003101Z-001/Pregunta 2/pregunta.txt", "8-9, 16:30-23"],
    3 : ["drive-download-20221014T003101Z-001/Pregunta 3/Screen Shot 2022-10-11 at 17.58.57.png", "drive-download-20221014T003101Z-001/Pregunta 3/pregunta.txt", "23"],
    4 : ["", "drive-download-20221014T003101Z-001/Pregunta 4/pregunta.txt", "12,600"],
    5 : ["drive-download-20221014T003101Z-001/Pregunta 5/Screen Shot 2022-10-11 at 18.03.33.png", "drive-download-20221014T003101Z-001/Pregunta 5/pregunta.txt", "5"],
    6 : ["drive-download-20221014T003101Z-001/Pregunta 6/Screen Shot 2022-10-13 at 20.49.25.png", "drive-download-20221014T003101Z-001/Pregunta 6/pregunta.txt", "5"],
    7 : ["drive-download-20221014T003101Z-001/Pregunta 8/Screen Shot 2022-10-11 at 18.29.55.png", "drive-download-20221014T003101Z-001/Pregunta 8/pregunta.txt", "26"],
    8 : ["drive-download-20221014T003101Z-001/Pregunta 9/Screen Shot 2022-10-11 at 18.31.29.png", "drive-download-20221014T003101Z-001/Pregunta 9/pregunta.txt", ".5"],
    9 : ["drive-download-20221014T003101Z-001/Pregunta 10/Screen Shot 2022-10-11 at 18.33.51.png", "drive-download-20221014T003101Z-001/Pregunta 10/pregunta.txt", "32"]
}

iconos_respuestas = ["drive-download-20221014T003101Z-001/IconosRespuestas/Screen Shot 2022-10-19 at 21.54.31.png", "drive-download-20221014T003101Z-001/IconosRespuestas/Screen Shot 2022-10-19 at 21.57.25.png"]

# Lista de keys del diccionario en orden aleatorio sin repetir
keys = sample(range(1,len(preguntas_examen_PISA)+1),len(preguntas_examen_PISA))



def obtener_pregunta():
    '''
    Escoge una pregunta del diccionario de manera aleatoria
    ''' 
    pregunta = preguntas_examen_PISA[keys[0]]
    imagen = pregunta[0]
    texto = pregunta[1]
    respuesta = pregunta[2]
    return imagen, texto, respuesta

def posicion():
    '''
    Según cada pregunta acomoda de disntinta forma los labels
    '''
    if keys[0] == 1:
        xy_imagen = [150, 50]
        xy_texto = [400, 430]
        xy_respuesta = [400, 500]
        return xy_imagen, xy_texto, xy_respuesta
    elif keys[0] == 2:
        xy_imagen = [150, 50]
        xy_texto = [300, 430]
        xy_respuesta = [400, 650]
        return xy_imagen, xy_texto, xy_respuesta
    elif keys[0] == 3: 
        xy_imagen = [150, 50]
        xy_texto = [800, 250]
        xy_respuesta = [800, 450]
        return xy_imagen, xy_texto, xy_respuesta
    elif keys[0] == 4: 
        xy_imagen = [150, 50]
        xy_texto = [350, 300]
        xy_respuesta = [350, 550]
        return xy_imagen, xy_texto, xy_respuesta
    elif keys[0] == 5: 
        xy_imagen = [90, 50]
        xy_texto = [370, 550]
        xy_respuesta = [370, 650]
        return xy_imagen, xy_texto, xy_respuesta
    elif keys[0] == 6: 
        xy_imagen = [0, 50]
        xy_texto = [300, 600]
        xy_respuesta = [300, 700]
        return xy_imagen, xy_texto, xy_respuesta
    elif keys[0] == 7: 
        xy_imagen = [150, 20]
        xy_texto = [600, 200]
        xy_respuesta = [600, 300]
        return xy_imagen, xy_texto, xy_respuesta
    elif keys[0] == 8: 
        xy_imagen = [150, 50]
        xy_texto = [300, 430]
        xy_respuesta = [300, 650]
        return xy_imagen, xy_texto, xy_respuesta
    else: 
        xy_imagen = [80, 50]
        xy_texto = [900, 250]
        xy_respuesta = [900, 550]
        return xy_imagen, xy_texto, xy_respuesta