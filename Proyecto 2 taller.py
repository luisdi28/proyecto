from tkinter import *
from random import *
import time
from threading import Thread
import os
from PIL import ImageTk,Image

#Color de las figuras
chicle = "#FFBED2"
menta = "#B5EAD7"
azul = "#82B3FF"
amarrillo = "#FFFFD8"
salmon = "#FF9AA2"
purpura = "#B399D4"
rosado = "#E18AAA"

colors = [chicle, menta, azul, amarrillo, salmon, purpura, rosado]

def cargar_imagen(nombre):
    ruta=os.path.join('photos',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen

#Clase de la ventana de inicio
class Ventana_inicio:
    def __init__(self,master):
        self.master=master
		#Función para volver a la ventana inicial
        
    def regresar_ventana(self):
        ventana_principal.correr()
        
    #Funcion para correr lo que se tiene en la ventana    
    def correr(self):
        self.About=About()
        self.Pantalla_n1=Pantalla_n1()
        #Se define el canvas         
        self.canvas = Canvas(self.master,width=600,height=600,highlightthickness=0,relief='ridge',bg="black")
        self.canvas.place(x=0,y=0)
        #Titulo
        self.titulo=Label(self.canvas,text="Geometry Dodge",font=("Times New Roman",15),fg="white",bg="black")
        self.titulo.place(x=250,y=20)
        #Label del nombre
        self.nombre=Label(self.canvas,text="Inserte nombre")
        self.nombre.place(x=200,y=125,width=100,height=30)
        #Entrada de nombre
        self.entrada=Entry(self.canvas)
        self.entrada.place(x=355,y=125,width=100, height=30)
        #Recibimiento
        self.recibimiento=Label(self.canvas,text= "La geometria, de una forma nunca antes vista.")
        self.recibimiento.place(x=50,y=200,width=500,height=30)
        #Label para elegir el nivel
        self.nivel=Label(self.canvas,text="Elige el nivel: ",font=("Times New Roman",15),fg="white",bg="black")
        self.nivel.place(x=250,y=300)
        #Se definen los botones de radio para elegir el nivel
        self.rboton1=Radiobutton(self.canvas,text="Nivel 1",value=1,font=("Times New Roman",10),variable=var)                   
        self.rboton1.place(x=175,y=350)
        self.rboton2=Radiobutton(self.canvas,text="Nivel 2",value=2,font=("Times New Roman",10),variable=var)                   
        self.rboton2.place(x=275,y=350)
        self.rboton3=Radiobutton(self.canvas,text="Nivel 3",value=3,font=("Times New Roman",10),variable=var)                   
        self.rboton3.place(x=375,y=350)
        #Boton para empezar el juego.
        self.botone= Button(self.canvas,text="Empezar", command=self.ir_juego)
        self.botone.place(x=265,y=425,width=100,height=30)
        #Se define el boton para ir a la ventana "About"
        self.botona= Button(self.canvas,text="Pantalla About", command=self.ir_info)
        self.botona.place(x=265,y=450,width=100,height=30)

#Funcion que permite al boton de para ir a la pantalla about funcionar.
    def ir_info(self):
        if self.entrada.get()=="":
            self.About.correr()
    def ir_juego(self):
        if self.entrada.get()!="" and var.get()==1:
            self.Pantalla_n1.correr()
  
#Pantalla about 
class About:
    def __init__(self):
        
        pass #permite pasar a la función run para ver todo el contenido de la ventana
    
#Funcion que permite ver la informacion requerida
    def correr(self):
        self.canvas = Canvas(width=600,height=600,highlightthickness=0,relief='ridge',bg="gray25")
        self.canvas.place(x=0,y=0)

        #Mensaje con la información 
        self.info=Message(self.canvas,justify=(CENTER),bg="gray25",fg="white",text="Hecho en Costa Rica.\n\n Tecnologico de Costa Rica.\n\n Ingenieria en Computadores.\n\n Taller de Programación.\n\n Año 2021.\n\n Grupo 04.\n\n Profesor: Luis Barboza Artavia.\n\n Instrucciones:\n Debe ingresar su nombre para poder comenzar el juego. \n Puede elegir el nivel donde desea comenzar.\n El boton 'volver' lo retorna a la pantalla de inicio.",font=("Times New Roman",12))
        self.info.place(x=50,y=-23,width=500,height=500)

        #Boton para volver a la pantalla de inicio 
        self.button_return=Button(self.canvas,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.correr)
        self.button_return.place(x=255,y=465,width=100,height=30)

#Clase pantalla del nivel 1  
class Pantalla_n1:
    def __init__(self):

        pass

    def correr(self):
        self.canvas=Canvas(width=600, height=600, bg="snow", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.place(x=0,y=0)

        #Permite detectar cualquier boton que se asigne
        window.bind_all("<KeyRelease>",self.mover_cuadrado)
        
        #Se carga la imagen de la figura que usara el jugador
        self.cuadrado=cargar_imagen('cuadrado.png')
        self.cuadradoimg = self.canvas.create_image(300,540,image=self.cuadrado,ancho=NW)
        
        #Boton para retornar a la pantalla inicial
        self.button_return=Button(self.canvas,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.correr)
        self.button_return.place(x=15,y=565,width=100,height=30)

        #Se define el movimiento de la figura
    def mover_cuadrado(self,event):
        x,y=self.canvas.coords(self.cuadradoimg)
        if event.char=="s":
            if y+10<500-80:
                self.canvas.coords(self.cuadradoimg,x,y+10)
        elif event.char=="w":
            if y-10>0:
                self.canvas.coords(self.cuadradoimg,x,y-10)
        elif event.char=="d":
            if x+10<500-70:
                self.canvas.coords(self.cuadradoimg,x+10,y)
        elif event.char=="a":
            if x-10>0:
                self.canvas.coords(self.cuadradoimg,x-10,y)
        
        
      

    

window=Tk()                       
var=IntVar()
ventana_principal = Ventana_inicio(window)
window.title("Juego_2")
window.minsize(600,600)
ventana_principal.correr()
window.resizable(False,False)
window.mainloop()

