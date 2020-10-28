import random

def main():
    print ("Â¡Bienvenidos al Programa de Dados! A continuaciÃ³n se tiran sus dados en dos ocasiones:")

    Numero_1 = random.choice([1,2,3,4,5,6])
    print ("El primer nÃºmero del dado es: ", Numero_1)

    Numero_2 = random.choice([1,2,3,4,5,6])
    print ("El segundo nÃºmero  del dado es: ", Numero_2)

    Suma_Total = Numero_1 + Numero_2
    print ("La suma de ambos da como resultado: ", Suma_Total)

    print ("Â¿Desea volver a tirar los dados otra vez? Si o No?")
    Respuesta = input()
    if Respuesta in (["si", "sÃ­","SÃ­","Si","SI","SÃ","s","Yes","yes"]):
        return main()
    else:
        print ("Fin del programa. Â¡Saludos!")
main()