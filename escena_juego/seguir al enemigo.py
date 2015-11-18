#Hacer que el enemigo siga al jugador  
class SeguirAOtro(pilasengine.habilidades.Habilidad):

    def iniciar(self, receptor, actor_perseguido, velocidad):
        self.receptor = receptor
        self.otro = actor_perseguido
        self.velocidad = velocidad
        x_pos=random.randint(0,1)
        y_pos=random.randint(0,1)
        y_delta = random.randrange(200, 300)
        x_delta = random.randrange(200, 300)
        
        if x_pos == 0:
            self.receptor.x = self.otro.x + x_delta
        if x_pos == 1:
            self.receptor.x = self.otro.x - x_delta

        if y_pos == 0:
            self.receptor.y = self.otro.y + y_delta
        if y_pos == 1:
            self.receptor.y = self.otro.y - y_delta
        
        
        
    def actualizar(self):
        if self.receptor:
            if self.receptor.x > self.otro.x:                
                self.receptor.x -= self.velocidad
            else:
                self.receptor.x += self.velocidad

            if self.receptor.y > self.otro.y:
                self.receptor.y -= self.velocidad
            else:
                self.receptor.y += self.velocidad

                        
            
pilas.habilidades.vincular(SeguirAOtro)

#nueva tarea de crear mono

tcm = pilas.tareas.agregar(1, crear_mono)
