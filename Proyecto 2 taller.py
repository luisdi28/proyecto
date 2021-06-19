from tkinter import *
from random import *
import time
from threading import Thread
import os
from PIL import ImageTk,Image
import vlc

player = vlc.MediaPlayer("play_music/pantalla.mp3")
player1 = vlc.MediaPlayer("play_music/nivel_1.mp3")
player2 = vlc.MediaPlayer("play_music/nivel_2.mp3")
player3 = vlc.MediaPlayer("play_music/nivel_3.mp3")
player4 = vlc.MediaPlayer("play_music/boom.mp3")

#Globales
global reset
reset=False
global vidanave
vidanave=3
global puntaje
puntaje=0
global progreso
progreso=0
global mi
mi = 0
global seg
seg=0
global cerrarthread
cerrarthread=False
global sihaycolision
sihaycolision=False

#Funcion para obtener los mejores puntajes

def division(lista):
    #lista=list(map(int,lista))
    pivote=lista[0]
    menores=[]
    mayores=[]

    for i in range(1,len(lista)):
        var=lista[i].split("-")
        var2=pivote.split("-")
        if int(var[1]) < int(var2[1]):
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
            
    return menores,pivote,mayores

def quicksort(lista):
    
    if len(lista) < 2:
        
        return lista
    
    mayores,pivote,menores = division(lista)

    return quicksort(menores) + [pivote] + quicksort(mayores)


#Función para leer el .txt
def read():
        try:
            archivo = open ("Puntuacion.txt","r")
            return (archivo.readlines())
        finally:
            archivo.close()

#Función para escribir en el archivo txt
def archivo(texto):
    archivo = open ("Puntuacion.txt","a")
    archivo.write(texto)
    archivo.close()

#Función para cargar imagen
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
        global cerrarthread
        cerrarthread=True
        global reset
        reset=False
        ventana_principal.correr()
        player1.stop()
        player2.stop()
        player3.stop()
        
    #Funcion para correr lo que se tiene en la ventana    
    def correr(self):
        player.play()
        global cerrarthread
        cerrarthread=False
        self.About=About()
        self.Pantalla_n1=Pantalla_n1()
        self.Pantalla_n2=Pantalla_n2()
        self.Pantalla_n3=Pantalla_n3()
        self.Pantalla_ganadores=Pantalla_ganadores()
        self.Pantalla_ganadores=Pantalla_ganadores()

        #Se define el canvas         
        self.canvas = Canvas(self.master,width=600,height=600,highlightthickness=0,relief='ridge',bg="black")
        self.canvas.place(x=0,y=0)
        #Imagen de fondo
        self.fondo=cargar_imagen('ventana.png')
        self.fondoimg = self.canvas.create_image(0,0,image=self.fondo,ancho=NW)
        #Titulo
        self.titulo=Label(self.canvas,text="Geometry Dodge",font=("Times New Roman",15),fg="white",bg="black")
        self.titulo.place(x=250,y=20)
        #Label de Bienvenida
        self.bienvenida=Label(self.canvas,text="Bienvenid@",font=("Times New Roman",15),fg="white",bg="black")
        self.bienvenida.place(x=270,y=75)
        #Label del nombre
        self.nombre=Label(self.canvas,text="Inserte nombre",font=("Times New Roman",12),fg="white",bg="black")
        self.nombre.place(x=200,y=150,width=100,height=30)
        #Entrada de nombre
        self.entrada=Entry(self.canvas,relief='raised',highlightbackground="black",highlightcolor="black")
        self.entrada.place(x=355,y=150,width=100, height=30)
        #Recibimiento
        self.recibimiento=Label(self.canvas,text= "La geometria, de una forma nunca antes vista.",font=("Times New Roman",14),fg="white",bg="black")
        self.recibimiento.place(x=150,y=225,width=350,height=30)
        #Label para elegir el nivel
        self.nivel=Label(self.canvas,text="Elige el nivel: ",font=("Times New Roman",15),fg="white",bg="black")
        self.nivel.place(x=250,y=300)
        #Se definen los botones de radio para elegir el nivel
        self.rboton1=Radiobutton(self.canvas,text="Nivel 1",value=1,font=("Times New Roman",10),variable=var,fg="white",bg="black")                   
        self.rboton1.place(x=175,y=350)
        self.rboton2=Radiobutton(self.canvas,text="Nivel 2",value=2,font=("Times New Roman",10),variable=var,fg="white",bg="black")                   
        self.rboton2.place(x=275,y=350)
        self.rboton3=Radiobutton(self.canvas,text="Nivel 3",value=3,font=("Times New Roman",10),variable=var,fg="white",bg="black")                   
        self.rboton3.place(x=375,y=350)
        #Boton para empezar el juego.
        self.botone= Button(self.canvas,text="Empezar",fg="white",bg="black",command=self.ir_juego)
        self.botone.place(x=265,y=425,width=100,height=30)
        #Se define el boton para ir a la ventana "About"
        self.botona= Button(self.canvas,text="Pantalla About",fg="white",bg="black",command=self.ir_info)
        self.botona.place(x=265,y=475,width=100,height=30)
        #Se define el boton para ir a la ventana "Ganadores"
        self.botong= Button(self.canvas,text="Pantalla de Ganadores",fg="white",bg="black",command=self.ganadores)
        self.botong.place(x=253,y=525,width=125,height=30)

#Funcion que permite al boton de para ir a la pantalla about funcionar.
    def ir_info(self):
        if self.entrada.get()=="":
            self.About.correr()
            player.play()
            
    def ir_juego(self):
        if self.entrada.get()!="" and var.get()==1:
            self.Pantalla_n1.correr(self.entrada.get(),Pantalla_n2(),Pantalla_n3())
            player.stop()
        elif self.entrada.get()!="" and var.get()==2:
            self.Pantalla_n2.correr(self.entrada.get(),Pantalla_n3())
            player.stop()
        elif self.entrada.get()!="" and var.get()==3:
            self.Pantalla_n3.correr(self.entrada.get())
            player.stop()
            
    def ganadores(self):
        self.Pantalla_ganadores.correr()
        player.play()
        
#Pantalla about 
class About:
    def __init__(self):
        
        pass #permite pasar a la función run para ver todo el contenido de la ventana
    
#Funcion que permite ver la informacion requerida
    def correr(self):
        self.canvas = Canvas(width=600,height=600,highlightthickness=0,relief='ridge',bg="gray25")
        self.canvas.place(x=0,y=0)

        #Mensaje con la información 
        self.info=Message(self.canvas,justify=(CENTER),bg="gray25",fg="white",text="Hecho en Costa Rica.\n\n Tecnologico de Costa Rica.\n\n Ingenieria en Computadores.\n\n Taller de Programación.\n\n Año 2021.\n\n Grupo 04.\n\n Profesor: Luis Barboza Artavia.\n\n Estudiantes: Luis Diego Araya y Carlos Contreras. \n\n Autores: Luis Diego Araya y Carlos Contreras. \n\n Instrucciones:\n Debe ingresar su nombre para poder comenzar el juego. \n Puede elegir el nivel donde desea comenzar.\n El boton 'volver' lo retorna a la pantalla de inicio.",font=("Times New Roman",12))
        self.info.place(x=50,y=-23,width=500,height=500)

        #Boton para volver a la pantalla de inicio 
        self.button_return=Button(self.canvas,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.correr)
        self.button_return.place(x=255,y=465,width=100,height=30)

#Clase pantalla del nivel 1  
class Pantalla_n1:
    def __init__(self):

        pass

    def correr(self,nombre,pantalla2,pantalla3):
        player1.play()
        self.nombre=nombre
        self.pantalla2=pantalla2
        self.pantalla3=pantalla3
        global vidanave
        vidanave=3
        global puntaje
        puntaje=0
        global seg
        seg=0
        global mi
        mi=0
        global cerrarthread
        cerrarthread=True
        
        WIDTH, HEIGHT = 600, 600
        self.canvas=Canvas(width=WIDTH, height=HEIGHT, bg="snow", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.place(x=0,y=0)

        #Permite detectar cualquier boton que se asigne
        window.bind_all("<KeyRelease>",self.mover_cuadrado)

        #Imagen de fondo
        self.fondo=cargar_imagen('fondo1.png')
        self.fondoimg = self.canvas.create_image(0,0,image=self.fondo,ancho=NW)
        
        #Se carga la imagen de la figura que usara el jugador y el enemigo
        self.cuadrado=cargar_imagen('cuadrado.png')
        self.cuadradoimg = self.canvas.create_image(300,540,image=self.cuadrado,ancho=NW)

        self.triangulo=cargar_imagen('triangulo.png')
        self.trianguloimg = self.canvas.create_image(randint(0,300),randint(0,300),image=self.triangulo,ancho=NW)

        self.circulo=cargar_imagen('circulo.png')
        self.circuloimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.circulo,ancho=NW)

        self.estrella=cargar_imagen('estrella.png')
        self.estrellaimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.estrella,ancho=NW)
        
        #Boton para retornar a la pantalla inicial
        self.button_return=Button(self.canvas,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.regresar_ventana)
        self.button_return.place(x=15,y=565,width=100,height=30)

        #Label que muestra la puntuacion, la vida y el nombre del jugador 
        self.puntuacion= Label(self.canvas,text= "Puntaje: " + str(puntaje), font=("Times New Roman",9), fg="snow", bg="grey")
        self.puntuacion.place(x=425,y=575,width=65, height=20)
        self.vida=Label(self.canvas,text= "Vidas: " + str(vidanave), font=("Times New Roman",9), fg="snow", bg="grey")
        self.vida.place(x=525,y=575,width=65, height=20)
        
        #Label con el Nombre
        self.mostrar= Label(self.canvas,text=""+self.nombre, font=("Times New Roman",9), fg="snow", bg="grey")
        self.mostrar.place(x=320,y=575,width=65, height=20)

        #Canvas de ganar
        self.win=Canvas(width=600, height=600, bg="white", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.boton_nivel=Button(self.win,text="Siguiente", command=self.siguiente)
        self.boton_nivel.place(x=75,y=540)

        #Labels de ganador
        label1 = Label(self.win, text="Felicidades", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label1.place(x=150, y=45)
        label2 = Label(self.win, text="por", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label2.place(x=170, y=85)
        label3 = Label(self.win, text="la victoria", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label3.place(x=200, y=125)
        label4 = Label(self.win, text="presiona", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label4.place(x=230, y=165)
        label5 = Label(self.win, text="el boton para continuar", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label5.place(x=260, y=205)

        #Canvas de perder
        self.lose=Canvas(width=600, height=600, bg="black", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.button_return=Button(self.lose,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.regresar_ventana)
        self.button_return.place(x=15,y=565,width=100,height=30)

        #Labels de perdedor
        label6 = Label(self.lose, text="Game", font=("Haettenschweiler", 40), bg="black", fg="red")
        label6.place(x=253,y=50)
        label7 = Label(self.lose, text="Over", font=("Haettenschweiler", 40), bg="black", fg="red")
        label7.place(x=259,y=120)

        #Cronometro
        self.minuto=Label(self.canvas,text="",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.minuto.place(x=5,y=3)
        self.segundo=Label(self.canvas,text="",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.segundo.place(x=65,y=3)
        self.dos_puntos=Label(self.canvas,text=":",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.dos_puntos.place(x=35,y=3)

        #Thread del cronometro (lo inicia)
        self.reloj=Thread(target=self.tiempo,args=[])
        self.reloj.start()

        #Thread de la animacion
        animacion = Thread(target = self.Animacion, args = (self.trianguloimg,self.circuloimg,self.estrellaimg,self.canvas))
        animacion.start()
        
#Función para guardar los puntajes
    def prueba(self):
        global vidanave
        global seg
        if vidanave<=0:
            textop=str(self.nombre) + "-" + str(puntaje)+"\n"
            archivo(textop)

#Funcion para ir a la pantalla de victoria
    def ventana_win(self):
        global seg
        global cerrarthread
        if seg==20:
            player1.stop()
            cerrarthread=False
            self.canvas.place_forget()
            return self.win.place(x=0,y=0)

#Funcion que lo envia al siguiente nivel
    def siguiente(self):
        global reset
        reset=True
        self.pantalla2.correr(self.nombre,self.pantalla3)

#Funcion para ir a la pantalla de derrota
    def ventana_lose(self):
        #player1.stop()
        global vidanave
        global cerrarthread
        if vidanave==0:
            player1.stop()
            cerrarthread=False
            self.canvas.place_forget()
            return self.lose.place(x=0,y=0)

        #Imagen estrella
        self.trofeo=cargar_imagen('trofeo.png')
        self.trofeoimg = self.win.create_image(250,300,image=self.trofeo,ancho=NW)

        #Imagen calabera
        self.calabera=cargar_imagen('calabera.png')
        self.calaberaimg = self.lose.create_image(185,300,image=self.calabera,ancho=NW)
        
#Funcion del cronometro
    def tiempo(self):
        global seg
        global mi
        global cerrarthread
        if cerrarthread:
            seg+=1
            if seg==60:
                player1.stop()
                seg=0
                mi+=1
                self.minuto.configure(text=mi)
            self.segundo.configure(text=seg)
            self.puntaje()
            self.ventana_win()
            self.prueba()
            time.sleep(1)
            return self.tiempo()

#Fuvion que mueve al enemigo
    def Animacion(self,estrella,circulo,triangulo,canvas):
        global cerrarthread
        if  cerrarthread:
            x=5
            y=5
        
            w=10
            z=10
        
            o=5
            p=5
        
            while True:
                if not cerrarthread:
                    break
                else:
                    velocidad=randint(0,10)
                    figura=self.canvas.coords(triangulo)
                    circu=self.canvas.coords(circulo)
                    estre=self.canvas.coords(estrella)
                    if figura[0]<=0:
                        x=velocidad
                    elif figura[0]>=580:
                        x=-velocidad
                    elif figura[1]<=0:
                        y=velocidad
                    elif figura[1]>=580:
                        y=-velocidad

                    elif circu[0]<=0:
                        w=velocidad
                    elif circu[0]>=580:
                        w=-velocidad
                    elif circu[1]<=0:
                        z=velocidad
                    elif circu[1]>=580:
                        z=-velocidad

                    elif estre[0]<=0:
                        o=velocidad
                    elif estre[0]>=580:
                        o=-velocidad
                    elif estre[1]<=0:
                        p=velocidad
                    elif estre[1]>=580:
                        p=-velocidad
                        
                    time.sleep(0.01)

                    self.canvas.move(triangulo,x,y)
                    self.canvas.move(circulo,w,z)
                    self.canvas.move(estrella,o,p)
                    self.colision()
            
#Funcion para pasar de nivel.
    def puntaje(self):
        global seg
        global puntaje
        if seg%1==0:
            puntaje=puntaje+1
            self.puntuacion.configure(text="Puntaje: "+str(puntaje))
        
#Se define el movimiento de la figura
    def mover_cuadrado(self,event):
        x,y=self.canvas.coords(self.cuadradoimg)
        if event.char=="s":
            if y+10<640-80:
                self.canvas.coords(self.cuadradoimg,x,y+10)
        elif event.char=="w":
            if y-10>0:
                self.canvas.coords(self.cuadradoimg,x,y-10)
        elif event.char=="d":
            if x+10<630-70:
                self.canvas.coords(self.cuadradoimg,x+10,y)
        elif event.char=="a":
            if x-10>0:
                self.canvas.coords(self.cuadradoimg,x-10,y)
                
#Funcion que hace que el jugador pierda vidas.
    def colision(self):
        global sihaycolision
        global vidanave
        triangulocoords=self.canvas.bbox(self.trianguloimg)
        cuadradocoords=self.canvas.bbox(self.cuadradoimg)
        estrellacoords=self.canvas.bbox(self.estrellaimg)
        circulocoords=self.canvas.bbox(self.circuloimg)
        if cuadradocoords[0]<=triangulocoords[2] and cuadradocoords[2]>=triangulocoords[0] and cuadradocoords[1]<=triangulocoords[3] and cuadradocoords[3]>=triangulocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=estrellacoords[2] and cuadradocoords[2]>=estrellacoords[0] and cuadradocoords[1]<=estrellacoords[3] and cuadradocoords[3]>=estrellacoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=circulocoords[2] and cuadradocoords[2]>=circulocoords[0] and cuadradocoords[1]<=circulocoords[3] and cuadradocoords[3]>=circulocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        else:
            sihaycolision=False
            return False
        self.ventana_lose()
        self.prueba()

#Clase pantalla del nivel 1  
class Pantalla_n2:
    def __init__(self):

        pass

    def correr(self,nombre,pantalla3):
        player2.play()
        self.nombre=nombre
        self.pantalla3=pantalla3
        global vidanave
        vidanave=3
        global puntaje
        puntaje=0
        global seg
        seg=0
        global mi
        mi=0
        global cerrarthread
        cerrarthread=True
        self.reset_puntajes()
        
        self.canvas=Canvas(width=600, height=600, bg="snow", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.place(x=0,y=0)

        #Permite detectar cualquier boton que se asigne
        window.bind_all("<KeyRelease>",self.mover_cuadrado)

        #Imagen de fondo
        self.fondo=cargar_imagen('fondo2.png')
        self.fondoimg = self.canvas.create_image(0,0,image=self.fondo,ancho=NW)
        
        #Se carga la imagen de la figura que usara el jugador y el emnemigo
        self.cuadrado=cargar_imagen('cuadrado.png')
        self.cuadradoimg = self.canvas.create_image(300,540,image=self.cuadrado,ancho=NW)

        self.cuadrado=cargar_imagen('cuadrado.png')
        self.cuadradoimg = self.canvas.create_image(300,540,image=self.cuadrado,ancho=NW)

        self.triangulo=cargar_imagen('triangulo.png')
        self.trianguloimg = self.canvas.create_image(randint(0,300),randint(0,300),image=self.triangulo,ancho=NW)

        self.circulo=cargar_imagen('circulo.png')
        self.circuloimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.circulo,ancho=NW)

        self.estrella=cargar_imagen('estrella.png')
        self.estrellaimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.estrella,ancho=NW)

        self.rombo=cargar_imagen('rombo.png')
        self.romboimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.rombo,ancho=NW)

        self.cilindro=cargar_imagen('cilindro.png')
        self.cilindroimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.cilindro,ancho=NW)

        #Boton para retornar a la pantalla inicial
        self.button_return=Button(self.canvas,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.regresar_ventana)
        self.button_return.place(x=15,y=565,width=100,height=30)

        #Label que muestra la puntuacion, la vida y el nombre del jugador 
        self.puntuacion= Label(self.canvas,text= "Puntaje: " + str(puntaje), font=("Times New Roman",9), fg="snow", bg="grey")
        self.puntuacion.place(x=425,y=575,width=65, height=20)
        self.vida=Label(self.canvas,text= "Vidas: " + str(vidanave), font=("Times New Roman",9), fg="snow", bg="grey")
        self.vida.place(x=525,y=575,width=65, height=20)
        
        #Label con el Nombre
        self.mostrar= Label(self.canvas,text=""+self.nombre, font=("Times New Roman",9), fg="snow", bg="grey")
        self.mostrar.place(x=320,y=575,width=65, height=20)

        #Canvas de ganar
        self.win=Canvas(width=600, height=600, bg="white", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.boton_nivel=Button(self.win,text="Siguiente", command=self.siguiente)
        self.boton_nivel.place(x=75,y=540)

        #Labels de ganador
        label1 = Label(self.win, text="Felicidades", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label1.place(x=150, y=45)
        label2 = Label(self.win, text="por", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label2.place(x=170, y=85)
        label3 = Label(self.win, text="la victoria", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label3.place(x=200, y=125)
        label4 = Label(self.win, text="presiona", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label4.place(x=230, y=165)
        label5 = Label(self.win, text="el boton para continuar", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label5.place(x=260, y=205)

        #Canvas de perder
        self.lose=Canvas(width=600, height=600, bg="black", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.button_return=Button(self.lose,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.regresar_ventana)
        self.button_return.place(x=15,y=565,width=100,height=30)

        #Labels de perdedor
        label6 = Label(self.lose, text="Game", font=("Haettenschweiler", 40), bg="black", fg="red")
        label6.place(x=253,y=50)
        label7 = Label(self.lose, text="Over", font=("Haettenschweiler", 40), bg="black", fg="red")
        label7.place(x=259,y=120)


        #Cronometro
        self.minuto=Label(self.canvas,text="",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.minuto.place(x=5,y=3)
        self.segundo=Label(self.canvas,text="",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.segundo.place(x=65,y=3)
        self.dos_puntos=Label(self.canvas,text=":",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.dos_puntos.place(x=35,y=3)

        #Thread del cronometro (lo inicia)
        self.reloj=Thread(target=self.tiempo,args=[])
        self.reloj.start()

        #Thread de la animacion
        animacion = Thread(target = self.Animacion, args = (self.trianguloimg,self.circuloimg,self.estrellaimg,self.romboimg,self.cilindroimg,self.canvas))
        animacion.start()

#Funcion que resetea los puntajes cuando se ingresa a un nivel especifico
    def reset_puntajes(self):
        global puntaje
        global reset
        if reset==False:
            puntaje=0
            return True
        else:
            reset=True
            return False
        
#Funcion que guarda los puntajes y el nombre
    def prueba(self):
        global vidanave
        global seg
        if vidanave<=0:
            textop=str(self.nombre) + "-" + str(puntaje)+"\n"
            archivo(textop)

#Funcion del cronometro
    def tiempo(self):
        global seg
        global mi
        global cerrarthread
        if cerrarthread:
            seg+=1
            if seg==60:
                seg=0
                mi+=1
                self.minuto.configure(text=mi)
            self.segundo.configure(text=seg)
            self.puntaje()
            self.ventana_win()
            self.prueba()
            time.sleep(1)
            return self.tiempo()

#Funcion para ir a la pantalla de victoria
    def ventana_win(self):
        global seg
        global cerrarthread
        if seg==20:
            player2.stop()
            cerrarthread=False
            self.canvas.place_forget()
            return self.win.place(x=0,y=0)

#Funcion que lo envia a la pantalla
    def siguiente(self):
        global reset
        reset=True
        self.pantalla3.correr(self.nombre)

#Funcion para ir a la pantalla de derrota
    def ventana_lose(self):
        global vidanave
        global cerrarthread
        if vidanave==0:
            player2.stop()
            cerrarthread=False
            self.canvas.place_forget()
            return self.lose.place(x=0,y=0)

        #Imagen estrella
        self.trofeo=cargar_imagen('trofeo.png')
        self.trofeoimg = self.win.create_image(250,300,image=self.trofeo,ancho=NW)

        #Imagen calabera
        self.calabera=cargar_imagen('calabera.png')
        self.calaberaimg = self.lose.create_image(185,300,image=self.calabera,ancho=NW)
        
#Fucion que mueve a los enemigos
    def Animacion(self,estrella,circulo,triangulo,rombo,cilindro,canvas):
        global cerrarthread
        if  cerrarthread:
            x=5
            y=5
        
            w=10
            z=10
        
            o=5
            p=5

            q=10
            r=10

            s=5
            t=5
        while True:
                if not cerrarthread:
                    break
                else:
                    velocidad=randint(0,10)
                    figura=self.canvas.coords(triangulo)
                    circu=self.canvas.coords(circulo)
                    estre=self.canvas.coords(estrella)
                    diamante=self.canvas.coords(rombo)
                    cilin=self.canvas.coords(cilindro)
                    if figura[0]<=0:
                        x=velocidad
                    elif figura[0]>=580:
                        x=-velocidad
                    elif figura[1]<=0:
                        y=velocidad
                    elif figura[1]>=580:
                        y=-velocidad

                    elif circu[0]<=0:
                        w=velocidad
                    elif circu[0]>=580:
                        w=-velocidad
                    elif circu[1]<=0:
                        z=velocidad
                    elif circu[1]>=580:
                        z=-velocidad

                    elif estre[0]<=0:
                        o=velocidad
                    elif estre[0]>=580:
                        o=-velocidad
                    elif estre[1]<=0:
                        p=velocidad
                    elif estre[1]>=580:
                        p=-velocidad

                    elif diamante[0]<=0:
                        q=velocidad
                    elif diamante[0]>=580:
                        q=-velocidad
                    elif diamante[1]<=0:
                        r=velocidad
                    elif diamante[1]>=580:
                        r=-velocidad

                    elif cilin[0]<=0:
                        s=velocidad
                    elif cilin[0]>=580:
                        s=-velocidad
                    elif cilin[1]<=0:
                        t=velocidad
                    elif cilin[1]>=580:
                        t=-velocidad
                        
                    time.sleep(0.01)

                    self.canvas.move(triangulo,x,y)
                    self.canvas.move(circulo,w,z)
                    self.canvas.move(estrella,o,p)
                    self.canvas.move(rombo,q,r)
                    self.canvas.move(cilindro,s,t)
                    self.colision()

#Funcion para pasar de nivel.
    def puntaje(self):
        global seg
        global puntaje
        if seg%1==0:
            puntaje=puntaje+3
            self.puntuacion.configure(text="Puntaje: "+str(puntaje))

#Se define el movimiento de la figura
    def mover_cuadrado(self,event):
        x,y=self.canvas.coords(self.cuadradoimg)
        if event.char=="s":
            if y+10<640-80:
                self.canvas.coords(self.cuadradoimg,x,y+10)
        elif event.char=="w":
            if y-10>0:
                self.canvas.coords(self.cuadradoimg,x,y-10)
        elif event.char=="d":
            if x+10<630-70:
                self.canvas.coords(self.cuadradoimg,x+10,y)
        elif event.char=="a":
            if x-10>0:
                self.canvas.coords(self.cuadradoimg,x-10,y)

#Funcion que hace que el jugador pierda vidas.
    def colision(self):
        global sihaycolision
        global vidanave
        triangulocoords=self.canvas.bbox(self.trianguloimg)
        cuadradocoords=self.canvas.bbox(self.cuadradoimg)
        estrellacoords=self.canvas.bbox(self.estrellaimg)
        circulocoords=self.canvas.bbox(self.circuloimg)
        rombocoords=self.canvas.bbox(self.romboimg)
        cilindocoords=self.canvas.bbox(self.cilindroimg)
        if cuadradocoords[0]<=triangulocoords[2] and cuadradocoords[2]>=triangulocoords[0] and cuadradocoords[1]<=triangulocoords[3] and cuadradocoords[3]>=triangulocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=estrellacoords[2] and cuadradocoords[2]>=estrellacoords[0] and cuadradocoords[1]<=estrellacoords[3] and cuadradocoords[3]>=estrellacoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=circulocoords[2] and cuadradocoords[2]>=circulocoords[0] and cuadradocoords[1]<=circulocoords[3] and cuadradocoords[3]>=circulocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=rombocoords[2] and cuadradocoords[2]>=rombocoords[0] and cuadradocoords[1]<=rombocoords[3] and cuadradocoords[3]>=rombocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=cilindocoords[2] and cuadradocoords[2]>=cilindocoords[0] and cuadradocoords[1]<=cilindocoords[3] and cuadradocoords[3]>=cilindocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        else:
            sihaycolision=False
            return False
        self.ventana_lose()
        self.prueba()
        
#Clase pantalla del nivel 1  
class Pantalla_n3:
    def __init__(self):

        pass

    def correr(self,nombre):
        player3.play()
        self.nombre=nombre
        global vidanave
        vidanave=3
        global puntaje
        puntaje=0
        global seg
        seg=0
        global mi
        mi=0
        global cerrarthread
        cerrarthread=True
        self.reset_puntajes()
        
        self.canvas=Canvas(width=600, height=600, bg="snow", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.place(x=0,y=0)

        #Permite detectar cualquier boton que se asigne
        window.bind_all("<KeyRelease>",self.mover_cuadrado)

        #Imagen de fondo
        self.fondo=cargar_imagen('fondo3.png')
        self.fondoimg = self.canvas.create_image(0,0,image=self.fondo,ancho=NW)
        
        #Se carga la imagen de la figura que usara el jugador y el enemigo
        self.cuadrado=cargar_imagen('cuadrado.png')
        self.cuadradoimg = self.canvas.create_image(300,540,image=self.cuadrado,ancho=NW)

        self.cuadrado=cargar_imagen('cuadrado.png')
        self.cuadradoimg = self.canvas.create_image(300,540,image=self.cuadrado,ancho=NW)

        self.triangulo=cargar_imagen('triangulo.png')
        self.trianguloimg = self.canvas.create_image(randint(0,300),randint(0,300),image=self.triangulo,ancho=NW)

        self.circulo=cargar_imagen('circulo.png')
        self.circuloimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.circulo,ancho=NW)

        self.estrella=cargar_imagen('estrella.png')
        self.estrellaimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.estrella,ancho=NW)

        self.rombo=cargar_imagen('rombo.png')
        self.romboimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.rombo,ancho=NW)

        self.cilindro=cargar_imagen('cilindro.png')
        self.cilindroimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.cilindro,ancho=NW)

        self.trapecio=cargar_imagen('trapecio.png')
        self.trapecioimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.trapecio,ancho=NW)

        self.rectangulo=cargar_imagen('rectangulo.png')
        self.rectanguloimg = self.canvas.create_image(randint(0,400),randint(0,400),image=self.rectangulo,ancho=NW)
        
        #Boton para retornar a la pantalla inicial
        self.button_return=Button(self.canvas,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.regresar_ventana)
        self.button_return.place(x=15,y=565,width=100,height=30)

        #Label que muestra la puntuacion, la vida y el nombre del jugador 
        self.puntuacion= Label(self.canvas,text= "Puntaje: " + str(puntaje), font=("Times New Roman",9), fg="snow", bg="grey")
        self.puntuacion.place(x=425,y=575,width=65, height=20)
        self.vida=Label(self.canvas,text= "Vidas: " + str(vidanave), font=("Times New Roman",9), fg="snow", bg="grey")
        self.vida.place(x=525,y=575,width=65, height=20)
        
        #Label con el Nombre
        self.mostrar= Label(self.canvas,text=""+self.nombre, font=("Times New Roman",9), fg="snow", bg="grey")
        self.mostrar.place(x=320,y=575,width=65, height=20)

        #Canvas de ganar
        self.win=Canvas(width=600, height=600, bg="white", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.boton_nivel=Button(self.win,text="Siguiente",command=ventana_principal.regresar_ventana)
        self.boton_nivel.place(x=75,y=540)

        #Labels de ganador
        label1 = Label(self.win, text="Felicidades", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label1.place(x=150, y=45)
        label2 = Label(self.win, text="por", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label2.place(x=170, y=85)
        label3 = Label(self.win, text="la victoria", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label3.place(x=200, y=125)
        label4 = Label(self.win, text="presiona", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label4.place(x=230, y=165)
        label5 = Label(self.win, text="el boton para continuar", font=("Haettenschweiler", 30), bg="snow", fg="green")
        label5.place(x=260, y=205)

        #Canvas de perder
        self.lose=Canvas(width=600, height=600, bg="black", highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.button_return=Button(self.lose,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.regresar_ventana)
        self.button_return.place(x=15,y=565,width=100,height=30)

        #Labels de perdedor
        label6 = Label(self.lose, text="Game", font=("Haettenschweiler", 40), bg="black", fg="red")
        label6.place(x=253,y=50)
        label7 = Label(self.lose, text="Over", font=("Haettenschweiler", 40), bg="black", fg="red")
        label7.place(x=259,y=120)
        
        #Cronometro
        self.minuto=Label(self.canvas,text="",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.minuto.place(x=5,y=3)
        self.segundo=Label(self.canvas,text="",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.segundo.place(x=65,y=3)
        self.dos_puntos=Label(self.canvas,text=":",font=("Times New Roman",12),fg="black",bg="snow",width=1,height=1)
        self.dos_puntos.place(x=35,y=3)

        #Thread del cronometro (lo inicia)
        self.reloj=Thread(target=self.tiempo,args=[])
        self.reloj.start()

        #Thread de la animacion
        animacion = Thread(target = self.Animacion, args = (self.trianguloimg,self.circuloimg,self.estrellaimg,self.romboimg,self.cilindroimg,self.trapecioimg,self.rectanguloimg,self.canvas))
        animacion.start()
        
#Funcion que resetea los puntajes cuando se ingresa a un nivel especifico
    def reset_puntajes(self):
        global puntaje
        global reset
        if reset==False:
            puntaje=0
            return True
        else:
            reset=True
            return False
        
#Funcion que guarda el puntaje
    def prueba(self):
        global vidanave
        global seg
        if seg==10 or vidanave<=0:
            textop=str(self.nombre) + "-" + str(puntaje)+"\n"
            archivo(textop)

#Funcion del cronometro
    def tiempo(self):
        global seg
        global mi
        global cerrarthread
        if cerrarthread:
            seg+=1
            if seg==60:
                seg=0
                mi+=1
                self.minuto.configure(text=mi)
            self.segundo.configure(text=seg)
            self.puntaje()
            self.ventana_win()
            self.prueba()
            time.sleep(1)
            return self.tiempo()

#Funcion para ir a la pantalla de victoria
    def ventana_win(self):
        global seg
        global cerrarthread
        if seg==7:
            player3.stop()
            cerrarthread=False
            self.canvas.place_forget()
            return self.win.place(x=0,y=0)
        
#Funcion para ir a la pantalla de derrota
    def ventana_lose(self):
        global vidanave
        global cerrarthread
        if vidanave==0:
            player3.stop()
            cerrarthread=False
            self.canvas.place_forget()
            return self.lose.place(x=0,y=0)

        #Imagen estrella
        self.ganador=cargar_imagen('ganador.png')
        self.ganadorimg = self.win.create_image(250,300,image=self.ganador,ancho=NW)

        #Imagen calabera
        self.calabera=cargar_imagen('calabera.png')
        self.calaberaimg = self.lose.create_image(185,300,image=self.calabera,ancho=NW)

#Fucion que mueve a los enemigos
    def Animacion(self,estrella,circulo,triangulo,rombo,cilindro,trapecio,rectangulo,canvas):
        global cerrarthread
        if  cerrarthread:
            x=5
            y=5
        
            w=10
            z=10
        
            o=5
            p=5

            q=10
            r=10

            s=5
            t=5

            a=5
            b=5

            c=10
            d=10
        
        while True:
                if not cerrarthread:
                    break
                else:
                    velocidad=randint(0,10)
                    figura=self.canvas.coords(triangulo)
                    circu=self.canvas.coords(circulo)
                    estre=self.canvas.coords(estrella)
                    diamante=self.canvas.coords(rombo)
                    cilin=self.canvas.coords(cilindro)
                    tra=self.canvas.coords(trapecio)
                    rec=self.canvas.coords(rectangulo)
                    if figura[0]<=0:
                        x=velocidad
                    elif figura[0]>=580:
                        x=-velocidad
                    elif figura[1]<=0:
                        y=velocidad
                    elif figura[1]>=580:
                        y=-velocidad

                    elif circu[0]<=0:
                        w=velocidad
                    elif circu[0]>=580:
                        w=-velocidad
                    elif circu[1]<=0:
                        z=velocidad
                    elif circu[1]>=580:
                        z=-velocidad

                    elif estre[0]<=0:
                        o=velocidad
                    elif estre[0]>=580:
                        o=-velocidad
                    elif estre[1]<=0:
                        p=velocidad
                    elif estre[1]>=580:
                        p=-velocidad

                    elif diamante[0]<=0:
                        q=velocidad
                    elif diamante[0]>=580:
                        q=-velocidad
                    elif diamante[1]<=0:
                        r=velocidad
                    elif diamante[1]>=580:
                        r=-velocidad

                    elif cilin[0]<=0:
                        s=velocidad
                    elif cilin[0]>=580:
                        s=-velocidad
                    elif cilin[1]<=0:
                        t=velocidad
                    elif cilin[1]>=580:
                        t=-velocidad

                    elif tra[0]<=0:
                        a=velocidad
                    elif tra[0]>=580:
                        a=-velocidad
                    elif tra[1]<=0:
                        b=velocidad
                    elif tra[1]>=580:
                        b=-velocidad

                    elif rec[0]<=0:
                        c=velocidad
                    elif rec[0]>=580:
                        c=-velocidad
                    elif rec[1]<=0:
                        d=velocidad
                    elif rec[1]>=580:
                        d=-velocidad
                        
                    time.sleep(0.01)

                    self.canvas.move(triangulo,x,y)
                    self.canvas.move(circulo,w,z)
                    self.canvas.move(estrella,o,p)
                    self.canvas.move(rombo,q,r)
                    self.canvas.move(cilindro,s,t)
                    self.canvas.move(trapecio,a,b)
                    self.canvas.move(rectangulo,c,d)
                    self.colision()

#Funcion para pasar de nivel.
    def puntaje(self):
        global seg
        global puntaje
        if seg%1==0:
            puntaje=puntaje+5
            self.puntuacion.configure(text="Puntaje: "+str(puntaje))

#Se define el movimiento de la figura
    def mover_cuadrado(self,event):
        x,y=self.canvas.coords(self.cuadradoimg)
        if event.char=="s":
            if y+10<640-80:
                self.canvas.coords(self.cuadradoimg,x,y+10)
        elif event.char=="w":
            if y-10>0:
                self.canvas.coords(self.cuadradoimg,x,y-10)
        elif event.char=="d":
            if x+10<630-70:
                self.canvas.coords(self.cuadradoimg,x+10,y)
        elif event.char=="a":
            if x-10>0:
                self.canvas.coords(self.cuadradoimg,x-10,y)

#Funcion que hace que el jugador pierda vidas.                
    def colision(self):
        global sihaycolision
        global vidanave
        triangulocoords=self.canvas.bbox(self.trianguloimg)
        cuadradocoords=self.canvas.bbox(self.cuadradoimg)
        estrellacoords=self.canvas.bbox(self.estrellaimg)
        circulocoords=self.canvas.bbox(self.circuloimg)
        rombocoords=self.canvas.bbox(self.romboimg)
        cilindocoords=self.canvas.bbox(self.cilindroimg)
        trapeciocoords=self.canvas.bbox(self.trapecioimg)
        rectangulocoords=self.canvas.bbox(self.rectanguloimg)
        if cuadradocoords[0]<=triangulocoords[2] and cuadradocoords[2]>=triangulocoords[0] and cuadradocoords[1]<=triangulocoords[3] and cuadradocoords[3]>=triangulocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=estrellacoords[2] and cuadradocoords[2]>=estrellacoords[0] and cuadradocoords[1]<=estrellacoords[3] and cuadradocoords[3]>=estrellacoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=circulocoords[2] and cuadradocoords[2]>=circulocoords[0] and cuadradocoords[1]<=circulocoords[3] and cuadradocoords[3]>=circulocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=rombocoords[2] and cuadradocoords[2]>=rombocoords[0] and cuadradocoords[1]<=rombocoords[3] and cuadradocoords[3]>=rombocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=cilindocoords[2] and cuadradocoords[2]>=cilindocoords[0] and cuadradocoords[1]<=cilindocoords[3] and cuadradocoords[3]>=cilindocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=trapeciocoords[2] and cuadradocoords[2]>=trapeciocoords[0] and cuadradocoords[1]<=trapeciocoords[3] and cuadradocoords[3]>=trapeciocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        elif cuadradocoords[0]<=rectangulocoords[2] and cuadradocoords[2]>=rectangulocoords[0] and cuadradocoords[1]<=rectangulocoords[3] and cuadradocoords[3]>=rectangulocoords[1]:
            if not sihaycolision:
                player4.play()
                sihaycolision=True
                vidanave=vidanave-1
                self.vida.config(text="Vidas: " + str(vidanave))
                return True
        else:
            sihaycolision=False
            return False
        self.ventana_lose()
        self.prueba()

#class Ganadores:

class Pantalla_ganadores:
    def __init__(self):
        
        pass #permite pasar a la función run para ver todo el contenido de la ventana
        
    def correr(self):
        self.canvas = Canvas(width=600,height=600,highlightthickness=0,relief='ridge',bg="gray25")
        self.canvas.place(x=0,y=0)
        
        #Imagen de fondo
        self.fondo=cargar_imagen('ganadores.png')
        self.fondoimg = self.canvas.create_image(-15,0,image=self.fondo,ancho=NW)
        
        #Titulo
        self.titulo=Label(self.canvas,text="GANADORES",font=("Times New Roman",20),fg="white",bg="black")
        self.titulo.place(x=215,y=20)
        
        #Label con el nombre
        self.nombres=Label(self.canvas,text="Mejores 7 puntajes",font=("Times New Roman",15),fg="white",bg="black")
        self.nombres.place(x=220,y=90)
        
        #Boton para volver a la pantalla de inicio 
        self.button_return=Button(self.canvas,text="Regresar",font=("Times New Roman",10),bg="snow",fg="black",command=ventana_principal.correr)
        self.button_return.place(x=255,y=550,width=100,height=30)

        x=quicksort(read())

        #Primer lugar
        self.primero=Label(self.canvas,text=""+str(x[0]),font=("Times New Roman",12),fg="white",bg="black")
        self.primero.place(x=250,y=130)

        #Segundo lugar
        self.segundo=Label(self.canvas,text=""+str(x[1]),font=("Times New Roman",12),fg="white",bg="black")
        self.segundo.place(x=250,y=180)

        #Tercer lugar
        self.tercero=Label(self.canvas,text=""+str(x[2]),font=("Times New Roman",12),fg="white",bg="black")
        self.tercero.place(x=250,y=230)

        #Cuarto lugar
        self.cuarto=Label(self.canvas,text=""+str(x[3]),font=("Times New Roman",12),fg="white",bg="black")
        self.cuarto.place(x=250,y=280)

        #Quinto lugar
        self.quinto=Label(self.canvas,text=""+str(x[4]),font=("Times New Roman",12),fg="white",bg="black")
        self.quinto.place(x=250,y=330)

        #Sexto lugar
        self.sexto=Label(self.canvas,text=""+str(x[5]),font=("Times New Roman",12),fg="white",bg="black")
        self.sexto.place(x=250,y=380)

        #Septimo lugar
        self.septimo=Label(self.canvas,text=""+str(x[6]),font=("Times New Roman",12),fg="white",bg="black")
        self.septimo.place(x=250,y=430)
        
window=Tk()                       
var=IntVar()
ventana_principal = Ventana_inicio(window)
window.title("Juego_2")
window.minsize(600,600)
ventana_principal.correr()
window.resizable(False,False)
window.mainloop()
player.stop()
player1.stop()
player2.stop()
player3.stop()
player4.stop()
