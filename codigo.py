'''
Programa que mediante el uso de tkinter, muestra preguntas del examen PISA

07/10/2022
Diego Espejo
Gael 
'''
from preguntas import obtener_pregunta
from tkinter import *
from tkinter import ttk

# Crear Ventana Principal
root = Tk() 
root.title("Examen PISA")
root.geometry('3000x1000')

def repetir():
    '''
    Elimina la pregunta pasada y manda a llamar una función para la nueva
    ''' 
    preguntas.texto.config(text=cambiar_texto())
    preguntas.photo.config(image=cambiar_imagen())
    pantallaPreguntas.frm.update()
    pantallaPreguntas.frm.update()

def cambiar_texto():
    '''
    Cambia el texto
    '''
    imagen_pregunta, texto_pregunta = obtener_pregunta()
    texto=open(texto_pregunta).read()
    return texto

def cambiar_imagen():
    '''
    Cambia la imagen
    '''
    imagen_pregunta, texto_pregunta = obtener_pregunta()
    imagen = PhotoImage(file=imagen_pregunta)
    return imagen

class pantallaInicio:
    # Pantalla de Inicio
    window = Frame(root, 
        height=1000,
        width=3000,
        bg="white",
        )
    window.pack()

    Button(root,
        text="Empezar Test",
        font="Arial 17",
        command=window.destroy
        ).place(x=1200,y=700) 

    Label(root,
        text="""Bienvenido a nuestra página para estudiar el examen PISA,
    
    Éxito!""",
        font="Arial 30",
        bg="white"
        ).place(x=300,y=200) 
    
class pantallaPreguntas:
    # Pantalla Preguntas
    frm = Frame(root, 
        height=1000,
        width=3000,
        bg="white"
        )
    frm.pack()

    # Botón Salir
    salir = Button(frm, 
        text="Salir",
        font="Arial 17", 
        fg="black",
        bg="white",
        command=root.destroy
        )
    salir.place(x=1300,y=700) 

    # Botón Enviar
    enviar = Button(frm, 
        text="Enviar",
        font="Arial 17",
        fg="black",
        command=lambda:repetir()
        )
    enviar.place(x=1100,y=700)

class preguntas:
    '''
    Se crea una clase en donde están definidos el texto y
    la imagen de las preguntas
    '''
    imagen_pregunta, texto_pregunta = obtener_pregunta()
    imagen = PhotoImage(file=imagen_pregunta)

    texto = Label(pantallaPreguntas.frm, 
        text=open(texto_pregunta).read(),
        font="Arial 20",
        fg="Black",
        bg="white"
        )
    texto.place(x=400,y=400) 

    # Imagen - Pregunta
    photo = Label(pantallaPreguntas.frm, 
        image=imagen
        )
    photo.place(x=50,y=50) 

    # Label - Respuesta
    Label(pantallaPreguntas.frm, 
        text="Respuesta:",
        font="Arial 17",
        fg="black",
        bg="white"
        ).place(x=500,y=500) 

    # Escribir Respuesta
    Entry(pantallaPreguntas.frm, 
        textvariable=StringVar()
        ).place(x=600,y=500)  

root.mainloop()
