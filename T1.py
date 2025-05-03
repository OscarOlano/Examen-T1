import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

    def puntos(self):
        # Genera un número aleatorio de puntos entre 10 y 28
        return random.randint(10, 28)

    def puntos_extras(self):
        # Genera un número aleatorio de puntos extra entre 0 y 6
        return random.randint(0, 6)

    def registrar_set(self, equipo_ganador):
        # Incrementa el set ganado de un equipo
        if equipo_ganador == 1:
            self.setGanados += 1
        elif equipo_ganador == 2:
            self.setGanados += 1

        if self.setGanados == 3:
            return True  # El equipo ha ganado el partido
        return False

    def jugar_partido(self, equipo2):
        set_equipo1 = 0
        set_equipo2 = 0

        # Simulamos los sets para que un equipo gane el partido
        while True:
            puntos_equipo1 = self.puntos()
            puntos_equipo2 = equipo2.puntos()

            print(f"{self.nombre} vs {equipo2.nombre} - Puntos: {puntos_equipo1} vs {puntos_equipo2}")

            if puntos_equipo1 < 25 and puntos_equipo2 < 25:

                while puntos_equipo1 < 25 and puntos_equipo2 < 25:
                    puntos_equipo1 += self.puntos_extras()
                    puntos_equipo2 += equipo2.puntos_extras()
                    print(f"Puntos Extras: {self.nombre} {puntos_equipo1} - {equipo2.nombre} {puntos_equipo2}")
                

            if puntos_equipo1 > puntos_equipo2:
                set_equipo1 += 1
                print(f"{self.nombre} gana el set")
            else:
                set_equipo2 += 1
                print(f"{equipo2.nombre} gana el set")

            if set_equipo1 == 3:
                self.registrar_set(1)
                equipo2.registrar_set(2)
                print(f"{self.nombre} gana el partido")
                return 1 
            elif set_equipo2 == 3:
                self.registrar_set(2)
                equipo2.registrar_set(1)
                print(f"{equipo2.nombre} gana el partido")
                return 2  

    def mostrar_resultado(self, equipo2):
        print(f"\nResultado del torneo:")
        print(f"{self.nombre} - Partidos Ganados: {self.partidosGanados}, Partidos Perdidos: {self.partidosPerdidos}")
        print(f"{equipo2.nombre} - Partidos Ganados: {equipo2.partidosGanados}, Partidos Perdidos: {equipo2.partidosPerdidos}")


# Crear los equipos
nombre_equipo1 = input("Ingrese el nombre del primer equipo: ")
nombre_equipo2 = input("Ingrese el nombre del segundo equipo: ")

equipo1 = Equipo(nombre_equipo1)
equipo2 = Equipo(nombre_equipo2)

# Jugar el número de partidos indicado
partidos_a_jugar = int(input("Ingrese el número de partidos por jugar: "))

for _ in range(partidos_a_jugar):
    print(f"\nIniciando un nuevo partido entre {equipo1.nombre} y {equipo2.nombre}")
    ganador = equipo1.jugar_partido(equipo2)
    
    # Se registra al ganador del partido
    if ganador == 1:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
    elif ganador == 2:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1

# Mostrar el resultado final
equipo1.mostrar_resultado(equipo2)