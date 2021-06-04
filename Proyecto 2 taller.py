from tkinter import *
from random import *
import time
import threading 
from threading import Thread

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
        #Se define el boton para ir a la ventana "About"
        self.botona= Button(self.canvas,text="Pantalla About", command=self.ir)
        self.botona.place(x=265,y=450,width=100,height=30)
#Funcion que permite al boton de para ir a la pantalla about funcionar.
    def ir(self):
        if self.entrada.get()=="":
            self.About.correr()
  
#Pantalla about 
class About:
    def __init__(self):
        
        pass #permite pasar a la función run para ver todo el contenido de la ventana
    
#Funcion que permite ver la informacion requerida
    def correr(self):
        self.canvas = Canvas(width=600,height=600,highlightthickness=0,relief='ridge',bg="gray25")
        self.canvas.place(x=0,y=0)

        #Message with the information
        self.info=Message(self.canvas,justify=(CENTER),bg="gray25",fg="white",text="Hecho en Costa Rica.\n\n Tecnologico de Costa Rica.\n\n Ingenieria en Computadores.\n\n Taller de Programación.\n\n Año 2021.\n\n Grupo 04.\n\n Profesor: Luis Barboza Artavia.\n\n Instrucciones:\n Debe ingresar su nombre para poder comenzar el juego. \n Puede elegir el nivel donde desea comenzar.\n El boton Comenzar Juego lo envia de forma directa al nivel 1.",font=("Times New Roman",12))
        self.info.place(x=15,y=-23,width=500,height=500)

        #Button to return at the first window
        self.button_return=Button(self.canvas,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.correr)
        self.button_return.place(x=255,y=465,width=100,height=30)

#Clase pantalla del nivel 1  
class Pantalla_n1:
    def __init__(self,master):
        self.canvas=Canvas(self.window_1, width=700, height=500, bg="grey", bd=0, highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.pack()
        self.master=master
        #Se definen los gifs para mostrar las figuras
        self.gif1=PhotoImage(file='nave.gif')
        self.gif2=PhotoImage(file='figurra1.gif')
        self.gif3=PhotoImage(file='figurra2.gif')
        self.nave = self.canvas.create_image(317,350,image=self.gif1,ancho=NW)
        self.figuras1= self.canvas.create_image(307,100,image=self.gif2,ancho=NW)
        self.figuras2= self.canvas.create_image(307,100,image=self.gif3,ancho=NW)
        #Se definen los movimientos del jugaror y del los enemigos
        self.pantalla_n1.bind('<Up>', self.mover_nave_arriba)
        self.pantalla_n1.bind('<Down>', self.mover_nave_abajo)
        self.pantalla_n1.bind('<Left>', self.mover_nave_izquierda)
        self.pantalla_n1.bind('<Right>', self.mover_nave_derecha)
        movimiento_figura1 = Thread(target=self.movimiento_figura1,args=(self.figura1,25,2))
        movimiento_figura1.start()
        movimiento_figura2 = Thread(target=self.movimiento_figura2,args=(self.figura2,25,2))
        movimiento_figura2.start()
        
      

    

window=Tk()                       
var=IntVar()
ventana_principal = Ventana_inicio(window)
window.title("Juego_2")
window.minsize(600,600)
ventana_principal.correr()
window.mainloop()
