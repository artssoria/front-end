import random

while True:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    resultado_dados = (dado1+dado2)

    print("El primer dado obtuvo: ", dado1)
    print("El segundo dado obtuvo: ", dado2)
    print("La suma de los dados es: ", resultado_dados)

    input("presiona cualquier tecla: ")

