'''
Programa que mediante el uso de tkinter, muestra preguntas del examen PISA
07/10/2022
Diego Espejo
Gael 
'''
from tkinter import *
from tkinter import ttk
from preguntas_PISA import obtener_pregunta, posicion, keys

# Crear Ventana Principal
root = Tk() 
root.title("Examen PISA")
root.geometry('3000x1000')

# Primera Parte - Pantalla de Bienvenida
class pantallaInicio:
    # Pantalla de Inicio
    window = Frame(root, 
        height=1000,
        width=3000,
        bg="white",
        )
    window.pack()

    Button(window,
        text="Empezar Test",
        font="Arial 17",
        command=window.destroy
        ).place(x=1200,y=700) 

    Label(window,
        text="""Bienvenido a nuestra página para estudiar el examen PISA,
    
    Éxito!""",
        font="Arial 30",
        bg="white"
        ).place(x=300,y=200) 

# Segunda Parte - Preguntas PISA
class pantallaPreguntas:
    '''
    Se crea una clase en donde están definidos el texto,
    la imagen de las preguntas, y todo lo que se observa en la pantalla
    '''
    # Ventana Secundaria
    frm = Frame(root, 
        height=1000,
        width=3000,
        bg="white"
        )
    frm.pack()

    # Botón Enviar
    enviar = Button(frm, 
        text="Enviar",
        font="Arial 17",
        fg="black",
        #command=Poner función para que reciba lo ingresado por el usuario
        )
    enviar.place(x=990,y=700)

    # Botón Sig. Pregunta
    siguiente = Button(frm, 
        text="Siguiente Pregunta",
        font="Arial 17",
        fg="black",
        command=lambda:repetir() # Te lleva a la función repetir, la cual reinicia el valor de las variables, y así se generan las nuevas preguntas
        )
    siguiente.place(x=1100,y=700)

    # Botón Salir
    salir = Button(frm, 
        text="Salir",
        font="Arial 17", 
        fg="black",
        bg="white",
        command=root.destroy
        )
    salir.place(x=1300,y=700) 

    imagen_pregunta, texto_pregunta = obtener_pregunta() # Te da dos paths, uno a la imagen y otro al archivo txt
    imagen = PhotoImage(file=imagen_pregunta)

    # Posición de cada elemento de las preguntas
    xy_imagen, xy_texto, xy_respuesta = posicion() # Coordenadas preseleccionadas en otro archivo
    
    # Texto - Pregunta
    texto = Label(frm, 
        text=open(texto_pregunta).read(),
        font="Arial 20",
        fg="Black",
        bg="white"
        )
    texto.place(x=xy_texto[0],y=xy_texto[1]) # El valor recibido por la función "posicion()" es una lista con la coordenada x (índice = 0) y y (índice = 1)

    # Imagen - Pregunta
    photo = Label(frm, 
        image=imagen
        )
    photo.place(x=xy_imagen[0],y=xy_imagen[1])

    # Label - Respuesta
    respuesta = Label(frm, 
        text="Respuesta:",
        font="Arial 20",
        fg="black",
        bg="white"
        )
    respuesta.place(x=xy_respuesta[0],y=xy_respuesta[1]) 

    # Escribir Respuesta
    entrada_texto = Entry(frm, 
        textvariable=StringVar(),
        font="Arial 19"
        )
    entrada_texto.place(x=xy_respuesta[0]+130,y=xy_respuesta[1]) 

# Tercera Parte
class pantallaFinal:
    texto_salida = "./Final/salida.txt"
    foto_salida = "./Final/Screen Shot 2022-10-13 at 12.47.45.png"
    imagen = PhotoImage(file=foto_salida)
    imagen = imagen.subsample(2) # Significa que reduces la foto 1/2 de su tamaño

    # Pantalla de Inicio
    final = Frame(root, 
        height=1000,
        width=3000,
        bg="white",
        )
    final.pack()

    # Texto Final
    texto = Label(final, 
        text=open(texto_salida).read(),
        font="Arial 20",
        fg="Black",
        bg="white"
        )
    texto.place(x=400,y=600)
    
    # Imagen final
    photo = Label(final, 
        image=imagen
    )
    photo.place(x=440,y=150)
    
    # Finalizar
    Button(final,
        text="Finalizar",
        font="Arial 17",
        command=root.destroy
        ).place(x=1200,y=700)

# Funciones
def repetir():
    '''
    Elimina la pregunta pasada y manda a llamar una función para la nueva
    '''
    keys.pop(0) # Se elimina el primer índice de la lista de keys, para que así se cambie a otra pregunta
    if len(keys) > 0:
        # Se cambia el texto y la foto por el de otra pregunta
        texto, imagen = cambiar() 
        pantallaPreguntas.texto.config(text=texto) # Se edita y actualiza el valor de text por el nuevo tras usar la función
        pantallaPreguntas.photo.config(image=imagen) # Se edita y actualiza la imagen por la nueva tras usar la función

        # Se reasigna la posición de cada elemento de las preguntas
        xy_imagen, xy_texto, xy_respuesta = posicion()
        pantallaPreguntas.photo.place(x=xy_imagen[0],y=xy_imagen[1]) # Lo mismo que arriba, se actualiza el valor de las coordenadas x-y
        pantallaPreguntas.texto.place(x=xy_texto[0],y=xy_texto[1])
        pantallaPreguntas.respuesta.place(x=xy_respuesta[0],y=xy_respuesta[1])
        pantallaPreguntas.entrada_texto.place(x=xy_respuesta[0]+130,y=xy_respuesta[1])
    else:
        pantallaPreguntas.frm.destroy() # Se cierra la ventana secundaria

def cambiar():
    '''
    Cambia el texto y la imagen
    '''
    imagen_pregunta, texto_pregunta = obtener_pregunta()
    texto=open(texto_pregunta).read()
    imagen = PhotoImage(file=imagen_pregunta)
    pantallaPreguntas.photo.image = imagen # Se hace porque sino la imagen no se actualiza y se ve gris
    return texto, imagen

root.mainloop()
