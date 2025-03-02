import random
import time

# Definir el entorno (mapa)
class Entorno:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def hay_obstaculo(self, x, y):
        return (x, y) in self.obstacles

    def mostrar(self, agente):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == (agente.x, agente.y):
                    print("A", end=" ")
                elif (x, y) in self.obstacles:
                    print("#", end=" ")
                elif (x, y) in agente.visitados:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

# Definir el agente explorador
class AgenteExplorador:
    def __init__(self, entorno, x, y):
        self.entorno = entorno
        self.x = x
        self.y = y
        self.visitados = set()
        self.direccion = random.choice(["N", "S", "E", "O"])

    def mover(self):
        movimientos = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "O": (-1, 0)}
        dx, dy = movimientos[self.direccion]
        nuevo_x = self.x + dx
        nuevo_y = self.y + dy
        
        if 0 <= nuevo_x < self.entorno.width and 0 <= nuevo_y < self.entorno.height:
            if not self.entorno.hay_obstaculo(nuevo_x, nuevo_y) and (nuevo_x, nuevo_y) not in self.visitados:
                self.x, self.y = nuevo_x, nuevo_y
                self.visitados.add((self.x, self.y))
            else:
                self.cambiar_direccion()
        else:
            self.cambiar_direccion()

    def cambiar_direccion(self):
        self.direccion = random.choice(["N", "S", "E", "O"])

# Configurar entorno y agente explorador
def main():
    width, height = 10, 10
    obstacles = {(3, 3), (4, 4), (5, 5), (6, 6), (7, 7)}
    entorno = Entorno(width, height, obstacles)
    agente = AgenteExplorador(entorno, 0, 0)
    
    for _ in range(50):  # Número de pasos
        entorno.mostrar(agente)
        agente.mover()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
