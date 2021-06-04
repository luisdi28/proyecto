#Importes

from tkinter import*
from tkinter import Canvas 
import time 
from random import*
import os
from threading import Thread

#Globales

global vidanave
vidanave=3
global puntaje
puntaje=0
global progreso
progreso=0

#Pantalla Inicio

class Pantalla_inicio:

    def __init__(self):

        self.pantalla_inicio = Tk()
        self.pantalla_inicio.config(background="grey")
        self.pantalla_inicio.minsize(700,500)
        self.canvas = Canvas(self.pantalla_inicio, width=700, height=500, bg="grey", bd=0, highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.pack()
        
        self.label_nombre= Label(self.canvas,text="Inserte nombre :")
        self.label_nombre.place(x=225, y=125, width=100, height=30)
        self.enter_nombre= Entry(self.canvas)
        self.enter_nombre.place(x=375, y=125, width=100, height=30)
        
        self.mensaje= Label(self.canvas, text=  "Bienvenido a nuestro juego, esperamos te guste", font=("Arial",10), fg="green")
        self.mensaje.place(x=35, y=200, width=625, height=30)
        
        self.nivel= Label(self.canvas, text= "Escoge el nivel", font=("Arial",12), fg="green")
        self.nivel.place(x=297,y=275)
        self.nivel_1 = Button(self.canvas, text="Nivel 1",command=self.nivel1)
        self.nivel_1.place(x=230, y=335)
        self.nivel_2 = Button(self.canvas, text="Nivel 2",command=self.nivel2)
        self.nivel_2.place(x=330, y=335)
        self.nivel_3 = Button(self.canvas, text="Nivel 3",command=self.nivel2)
        self.nivel_3.place(x=430, y=335)
        
        self.boton_about= Button(self.canvas, text = "Pantalla 'About'",command=self.empezar)
        self.boton_about.place(x=305, y=400, width=100, height=30)

    def empezar(self):
        if self.enter_nombre.get() != "":
            self.pantalla_inicio.destroy()
            Pantalla_about()
            
    def nivel1(self):
        if self.enter_nombre.get() != "":
            self.enter_nombre.destroy()
            Pantalla_1(self.pantalla_inicio)
            

    def nivel2(self):
         if self.enter_nombre.get() != "":
            self.enter_nombre.destroy()
            Pantalla_2(self.pantalla_inicio)

    def nivel3(self):
        if self.enter_nombre.get() != "":
            self.pantalla_inicio.destroy()
            Pantalla_3(self.pantalla_inicio)

#Pantalla About
            
class Pantalla_about:

    def __init__(self):
        
        self.pantalla_about = Tk()
        self.pantalla_about.config(background="grey")
        self.pantalla_about.minsize(700,500)
        self.canvas = Canvas(self.pantalla_about, width=700, height=500, bg="grey", bd=0, highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.pack()

        self.pais= Label(self.canvas, text="Costa Rica", font=("Arial",14), fg="black")
        self.pais.place(x=300, y=0, width=100, height=30)

        self.universidad= Label(self.canvas, text="TEC", font=("Arial",14), fg="black")
        self.universidad.place(x=315, y=37, width=70, height=30)

        self.carrera= Label(self.canvas, text="Ingenieria en Computadores", font=("Arial",14), fg="black")
        self.carrera.place(x=175, y=74, width=350, height=30)

        self.curso= Label(self.canvas, text="Taller de Programacion", font=("Arial",14), fg="black")
        self.curso.place(x=175, y=111, width=350, height=30)

        self.year= Label(self.canvas, text="2021", font=("Arial",14), fg="black")
        self.year.place(x=325, y=148, width=50, height=30)

        self.grupo= Label(self.canvas, text="Grupo: 4", font=("Arial",14), fg="black")
        self.grupo.place(x=305, y=185, width=85, height=30)

        self.profesor= Label(self.canvas, text="Luis Artavia Barbosa", font=("Arial",14), fg="black")
        self.profesor.place(x=225, y=222, width=250, height=30)

        self.programa= Label(self.canvas, text="Python 3.9", font=("Arial",14), fg="black")
        self.programa.place(x=300, y=259, width=100, height=30)

        self.estudiantes= Label(self.canvas, text="Luis Diego Araya y Carlos Contreras", font=("Arial",14), fg="black")
        self.estudiantes.place(x=150, y=296, width=400, height=30)

        self.autores= Label(self.canvas, text="Luis Diego Araya y Carlos Contreras", font=("Arial",14), fg="black")
        self.autores.place(x=150, y=333, width=400, height=30)

        self.instrucciones= Label(self.canvas, text= "Presione el boton Volver para ir de vuelta al menu principal", font=("Arial",14), fg="black")
        self.instrucciones.place(x=100, y=370, width=500, height=30)
        
        self.button_volver= Button(self.canvas, text = "Volver",command=self.volver)
        self.button_volver.place(x=315, y=407, width=75, height=30)

    def volver(self):
        self.pantalla_about.destroy()
        Pantalla_inicio()

class Pantalla_1:
    
    def __init__(self,master):

        self.pantalla_1 = Toplevel()
        self.pantalla_1.title("Nivel 1")
        self.pantalla_1.config(background="black")
        self.pantalla_1.minsize(700,500)
        self.canvas=Canvas(self.pantalla_1, width=700, height=500, bg="grey", bd=0, highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.pack()
        self.master=master
        self.gif1=PhotoImage(file='')
        self.gif2=PhotoImage(file='')
        self.nave = self.canvas.create_image(317,350,image=self.gif1,ancho=NW)
        self.meteoro = self.canvas.create_image(307,100,image=self.gif2,ancho=NW)
        self.pantalla_1.bind('<Up>', self.move_nave_arriba)
        self.pantalla_1.bind('<Down>', self.move_nave_abajo)
        self.pantalla_1.bind('<Left>', self.move_nave_izquierda)
        self.pantalla_1.bind('<Right>', self.move_nave_derecha)
        movimiento_meteorito = Thread(target=self.movimiento_meteorito,args=(self.meteorito,25,2))
        movimiento_meteorito.start()
        
        self.s=0
        self.m=0

        self.tiempo= Label(self.canvas, text= "", width=5, font=("Arial",9), fg="green", bg="black")
        self.tiempo.place(x=30,y=0,width=20, height=20)
        self.puntajelabel= Label(self.canvas,text= "Puntaje: " + str(score), font=("Arial",9), fg="green", bg="black")
        self.puntajelabel.place(x=310,y=475,width=75, height=20)
        self.vidanavelabel=Label(self.canvas,text= "Vida: " + str(lifespaceship), font=("Arial",9), fg="green", bg="black")
        self.vidanavelabel.place(x=460,y=475,width=150, height=20)

        self.Pantalla_1.mainloop()
          
    def mover_nave_arriba(self,event):
        xspeed = 0
        yspeed = -25
        self.canvas.move(self.spaceship,xspeed,yspeed)

    def move_nave_abajo(self,event):
        xspeed = 0
        yspeed = 25
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def move_nave_izquierda(self,event):
        xspeed = -25
        yspeed = 0
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def move_nave_derecha(self,event):
        xspeed = 25
        yspeed = 0
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def iniciar(self):
        if self.s >= 60:
            self.s=0
            self.m>= 60.
            self.m=0
            self.time.configure(text=str(self.m)+":"+str(self.s))
            self.s+=1
            process=self.canvas.after(1000,self.start)

    def detenerse():
        global process
        time.after_cancel(process)
            
    def mover_meteorito_izquierda(self):
        xspeed = -10
        yspeed = 0
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def mover_meteorito_derecha(self):
        xspeed = 10
        yspeed = 0
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def mover_meteorito_abajo(self):
        xspeed = 0
        yspeed = 10
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def movimiento (self):
        time.sleep(0.05)
        self.canvas.move(self.meteorito,0,10)
        if self.canvas.coords(self.boss)[1]>350:
            return self.anti_lunge()
        else:
            return self.lunge()

    def anti(self):
        time.sleep(0.05)
        self.canvas.move(self.meteorito,0,-10)
        if self.canvas.coords(self.boss)[1]<89:
            return self.mover_boss_derecha()
        else:
            return self.anti()

    def colision(self,shiping,nave,meteorito):
        global livel
        meteoritocoords=self.canvas.bobox(self.boss)
        navecoords=self.canvas.bobox
        if navecoords[0]<meteoritocoords[2] and nave[2]>meteoritocoords[0] and navecoords[1]<meteorito[3] and meteoritocoords[3]>navecoords[1]:
            global vidanave
            lifespaceship-=1
            self.vidanave.config(text="Vidas: " + str(vida))
            return True
        else:
            return False

    def movimiento_meteorito(self,enemy,movement,time_lunge):
        coords=self.canvas.coords(enemy)
        x=coords[0]
        y=coords[1]
        if movement<0:
            if x+movement>0:
                self.mover_meteorito_izquierda()
            else:
                movement*=-1
        else:
            if x+movement<650:
                self.mover_meteorito_derecha()
            else:
                movement*=-1
                
        if time_lunge<=0:
            self.lunge()
            self.anti()
            time_lunge=2

        time.sleep(0.05)

        self.meteorito_movement(enemy,movement,time_lunge-0.05)

class Pantalla_2:

#Screen
    
    def __init__(self,master):

        self.pantalla_2 = Toplevel()
        self.pantalla_2.title("Nivel 2")
        self.pantalla_2.config(background="black")
        self.pantalla_2.minsize(700,500)
        self.canvas=Canvas(self.window_2, width=700, height=500, bg="grey", bd=0, highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.pack()
        self.master=master
        self.gif1=PhotoImage(file='')
        self.gif2=PhotoImage(file='')
        self.nave = self.canvas.create_image(317,350,image=self.gif1,ancho=NW)
        self.meteoro = self.canvas.create_image(307,100,image=self.gif3,ancho=NW)
        self.pantalla_2.bind('<Up>', self.move_nave_arriba)
        self.pantalla_2.bind('<Down>', self.move_nave_abajo)
        self.pantalla_2.bind('<Left>', self.move_nave_izquierda)
        self.pantalla_2.bind('<Right>', self.move_nave_derecha)
        movimiento_meteorito = Thread(target=self.movimiento_meteorito,args=(self.meteorito,25,2))
        movimiento_meteorito.start()
        
        self.s=0
        self.m=0

        self.tiempo= Label(self.canvas, text= "", width=5, font=("Arial",9), fg="green", bg="black")
        self.tiempo.place(x=30,y=0,width=20, height=20)
        self.puntajelabel= Label(self.canvas,text= "Score: " + str(score), font=("Arial",9), fg="green", bg="black")
        self.puntajelabel.place(x=310,y=475,width=75, height=20)
        self.vidanavelabel=Label(self.canvas,text= "Spaceship's life: " + str(lifespaceship), font=("Arial",9), fg="green", bg="black")
        self.vidanavelabel.place(x=460,y=475,width=150, height=20)

        self.Pantalla_2.mainloop()
    

        self.tiempo= Label(self.canvas, text= "", width=5, font=("Arial",9), fg="green", bg="black")
        self.tiempo.place(x=30,y=0,width=20, height=20)
        self.puntajelabel= Label(self.canvas,text= "Score: " + str(score), font=("Arial",9), fg="green", bg="black")
        self.puntajelabel.place(x=310,y=475,width=75, height=20)
        self.vidanavelabel=Label(self.canvas,text= "Vidas nave : " + str(lifespaceship), font=("Arial",9), fg="green", bg="black")
        self.vidanavelabel.place(x=460,y=475,width=150, height=20)

        self.Pantalla_1.mainloop()
          
    def mover_nave_arriba(self,event):
        xspeed = 0
        yspeed = -25
        self.canvas.move(self.spaceship,xspeed,yspeed)

    def move_nave_abajo(self,event):
        xspeed = 0
        yspeed = 25
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def move_nave_izquierda(self,event):
        xspeed = -25
        yspeed = 0
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def move_nave_derecha(self,event):
        xspeed = 25
        yspeed = 0
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def iniciar(self):
        if self.s >= 60:
            self.s=0
            self.m>= 60.
            self.m=0
            self.time.configure(text=str(self.m)+":"+str(self.s))
            self.s+=1
            process=self.canvas.after(1000,self.start)

    def detenerse():
        global process
        time.after_cancel(process)
            
    def mover_meteorito_izquierda(self):
        xspeed = -10
        yspeed = 0
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def mover_meteorito_derecha(self):
        xspeed = 10
        yspeed = 0
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def mover_meteorito_abajo(self):
        xspeed = 0
        yspeed = 10
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def movimiento (self):
        time.sleep(0.05)
        self.canvas.move(self.meteorito,0,10)
        if self.canvas.coords(self.boss)[1]>350:
            return self.anti_lunge()
        else:
            return self.lunge()

    def anti(self):
        time.sleep(0.05)
        self.canvas.move(self.meteorito,0,-10)
        if self.canvas.coords(self.boss)[1]<89:
            return self.mover_boss_derecha()
        else:
            return self.anti()

    def colision(self,shiping,nave,meteorito):
        global livel
        meteoritocoords=self.canvas.bobox(self.boss)
        navecoords=self.canvas.bobox
        if navecoords[0]<meteoritocoords[2] and nave[2]>meteoritocoords[0] and navecoords[1]<meteorito[3] and meteoritocoords[3]>navecoords[1]:
            global vidanave
            lifespaceship-=1
            self.vidanave.config(text="Vidas: " + str(vida))
            return True
        else:
            return False

    def movimiento_meteorito(self,enemy,movement,time_lunge):
        coords=self.canvas.coords(enemy)
        x=coords[0]
        y=coords[1]
        if movement<0:
            if x+movement>0:
                self.mover_meteorito_izquierda()
            else:
                movement*=-1
        else:
            if x+movement<650:
                self.mover_meteorito_derecha()
            else:
                movement*=-1
                
        if time_lunge<=0:
            self.lunge()
            self.anti()
            time_lunge=2

        time.sleep(0.05)

        self.movimiento_meteorito(enemy,movement,time_movimiento-0.05)

class Pantalla_3:
    
    def __init__(self,master):
        self.pantalla_3 = Toplevel()
        self.pantalla_3.title("Nivel 3")
        self.pantalla_3.config(background="green")
        self.pantalla_3.minsize(700,500)
        self.canvas=Canvas(self.window_3, width=700, height=500, bg="grey", bd=0, highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.pack()
        self.gif1=PhotoImage(file='')
        self.gif2=PhotoImage(file='')
        self.nave = self.canvas.create_image(317,350,image=self.gif1,ancho=NW)
        self.meteoro = self.canvas.create_image(307,100,image=self.gif3,ancho=NW)
        self.pantalla_3.bind('<Up>', self.move_nave_arriba)
        self.pantalla_3.bind('<Down>', self.move_nave_abajo)
        self.pantalla_3.bind('<Left>', self.move_nave_izquierda)
        self.pantalla_3.bind('<Right>', self.move_nave_derecha)
        movimiento_meteorito = Thread(target=self.movimiento_meteorito,args=(self.meteorito,25,2))
        movimiento_meteorito.start()
        
        self.s=0
        self.m=0

        self.tiempo= Label(self.canvas, text="", width=5, font=("Arial",9), fg="green", bg="black")
        self.tiempo.place(x=30,y=0,width=25, height=20)
        self.puntajelabel= Label(self.canvas,text= "Puntaje: " + str(score), font=("Arial",9), fg="green", bg="black")
        self.puntajelabel.place(x=310,y=475,width=75, height=20)
        self.vidanave=Label(self.canvas,text= "Vidas: " + str(lifespaceship), font=("Arial",9), fg="green", bg="black")
        self.vidanavelabel.place(x=465,y=475,width=150, height=20)

        self.window_3.mainloop()
        
        self.tiempo= Label(self.canvas, text= "", width=5, font=("Arial",9), fg="green", bg="black")
        self.tiempo.place(x=30,y=0,width=20, height=20)
        self.puntajelabel= Label(self.canvas,text= "Puntaje: " + str(score), font=("Arial",9), fg="green", bg="black")
        self.puntajelabel.place(x=310,y=475,width=75, height=20)
        self.vidanavelabel=Label(self.canvas,text= "Vidas: " + str(lifespaceship), font=("Arial",9), fg="green", bg="black")
        self.vidanavelabel.place(x=460,y=475,width=150, height=20)

        self.Pantalla_1.mainloop()
          
    def mover_nave_arriba(self,event):
        xspeed = 0
        yspeed = -25
        self.canvas.move(self.spaceship,xspeed,yspeed)

    def move_nave_abajo(self,event):
        xspeed = 0
        yspeed = 25
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def move_nave_izquierda(self,event):
        xspeed = -25
        yspeed = 0
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def move_nave_derecha(self,event):
        xspeed = 25
        yspeed = 0
        self.canvas.move(self.spaceship,xspeed, yspeed)

    def iniciar(self):
        if self.s >= 60:
            self.s=0
            self.m>= 60.
            self.m=0
            self.time.configure(text=str(self.m)+":"+str(self.s))
            self.s+=1
            process=self.canvas.after(1000,self.start)

    def detenerse():
        global process
        time.after_cancel(process)
            
    def mover_meteorito_izquierda(self):
        xspeed = -10
        yspeed = 0
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def mover_meteorito_derecha(self):
        xspeed = 10
        yspeed = 0
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def mover_meteorito_abajo(self):
        xspeed = 0
        yspeed = 10
        self.canvas.move(self.meteorito,xspeed, yspeed)

    def movimiento (self):
        time.sleep(0.05)
        self.canvas.move(self.meteorito,0,10)
        if self.canvas.coords(self.boss)[1]>350:
            return self.anti_lunge()
        else:
            return self.lunge()

    def anti(self):
        time.sleep(0.05)
        self.canvas.move(self.meteorito,0,-10)
        if self.canvas.coords(self.boss)[1]<89:
            return self.mover_boss_derecha()
        else:
            return self.anti()

    def colision(self,shiping,nave,meteorito):
        global livel
        meteoritocoords=self.canvas.bobox(self.boss)
        navecoords=self.canvas.bobox
        if navecoords[0]<meteoritocoords[2] and nave[2]>meteoritocoords[0] and navecoords[1]<meteorito[3] and meteoritocoords[3]>navecoords[1]:
            global vidanave
            lifespaceship-=1
            self.vidanave.config(text="Vidas: " + str(vida))
            return True
        else:
            return False

    def movimiento_meteorito(self,enemy,movement,time_lunge):
        coords=self.canvas.coords(enemy)
        x=coords[0]
        y=coords[1]
        if movement<0:
            if x+movement>0:
                self.mover_meteorito_izquierda()
            else:
                movement*=-1
        else:
            if x+movement<650:
                self.mover_meteorito_derecha()
            else:
                movement*=-1
                
        if time_movimiento<=0:
            self.lunge()
            self.anti()
            time_lunge=2

        time.sleep(0.05)

        self.mover_meteorito(enemy,movement,time_movimiento-0.05)
    
class Pantalla_puntajes:

    def __init__(self):

        self.pantalla_puntajes = Tk()
        self.pantalla_puntajes.title("Mejores puntahes")
        self.pantalla_puntajes.config(background="grey")
        self.pantalla_puntajes.minsize(700,500)
        self.canvas = Canvas(self.pantalla_puntajes, width=700, height=500, bg="grey", bd=0, highlightthickness=1, relief="ridge", highlightbackground="grey")
        self.canvas.pack()

Pantalla_inicio()


        
