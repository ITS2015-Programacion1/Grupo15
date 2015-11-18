import pilasengine
pilas = pilasengine.iniciar()

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