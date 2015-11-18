# coding: utf-8
import pilasengine

import random

pilas = pilasengine.iniciar()

fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar('spronkou.jpg')

class Policia(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen = "policia.png"


	def actualizar(self):
		if pilas.control.izquierda:
			self.x -=5
			self.espejado = True
		if pilas.control.derecha:
  			self.x +=5
			self.espejado = False
policia = Policia(pilas)
policia.aprender(pilas.habilidades.LimitadoABordesDePantalla)
policia.y = -200

class Caja(pilasengine.actores.Actor):

    def iniciar(self):
       	self.imagen = "caja.png"
        self.escala=1
        self.x=255
        self.y=-180
caja = Caja(pilas)

	
class ActorQueCae(pilasengine.actores.Actor):
    
    def iniciar(self):
        self.imagen = "maleta{}.png".format(random.randint(1,3))
        self.y = 300
        self.escala=0.45
        self.x = self.pilas.azar(-300, 143)
        
    def actualizar(self):
        if self.y>-205:
            self.y = self.y - 3

def crear_actor_al_azar():
    pilas.actores.ActorQueCae()
    
pilas.actores.vincular(ActorQueCae)
pilas.tareas.siempre(2, crear_actor_al_azar)

def agarrar_maleta(ActorQueCae, policia):
    maleta.transparencia = 100
    maleta.aprender(MoverseConElTeclado)

def dejar_maleta(ActorQueCae, caja):
    maleta.eliminar()

pilas.ejecutar() 
