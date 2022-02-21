from random import randint 

eleccion = ["piedra", "papel","tijeras"]


#Condiciones del juego

def main():
    # La computadora elige aleatoriamente entre las opciones de arriba
    computadora = eleccion[randint(0,2)]    

    print("Bienvenido al juego de Piedra, papel o tijeras \n")
    jugador = input("Su elección: ").lower()
    print(f"La computadora eligió: {computadora}" )

    if jugador == computadora:
        print("Empate")
    elif jugador == "piedra" and computadora == "papel": 
        print("La computadora gana")
    elif jugador == "piedra" and computadora == "tijeras":
        print("Ganaste!!!!")
    elif jugador == "papel" and computadora == "tijeras": 
        print("La computadora gana")
    elif jugador == "papel" and computadora == "piedra":
        print("Ganaste!!!!")        
    elif jugador == "tijeras" and computadora == "piedra": 
        print("La computadora gana")
    elif jugador == "tijeras" and computadora == "papel":
        print("Ganaste!!!!")
           
    

