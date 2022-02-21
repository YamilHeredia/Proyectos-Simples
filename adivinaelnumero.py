# Adivina el número
import random 

def adivinaelNumero(x):

    print("-------ADIVINA EL NÚMERO--------")

    numeroAleatorio = random.randint(1, x) # Número aleatorio entre 1 y x inclusive

    prediccion = 0

    while prediccion != numeroAleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y x: "))

        if prediccion < numeroAleatorio:
            print("Intenta otra vez. Este número es muy pequeño")

        elif prediccion > numeroAleatorio:
            print("Intenta otra vez. Este número es muy grande")

        
    print(f"Adivinaste el número correctamente {numeroAleatorio}. Felicidades!!!")

adivinaelNumero(30)
