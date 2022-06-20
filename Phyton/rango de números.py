from random import randrange
n = randrange (10)
print(n)

"""
pedir un numero al usuario:              usuario introduce: 10
la pc genera un random de 0-30           PC: Aleatorio 10
Se muestra en la pantalla lo siguientes condiciones:
* Si es igual MANDAR EN LA PANTALLA GANADOR, y terminar el proceso
* Si es menor al aleatorio MANDAR EN LA PANTALLA POR DEBAJO, volver a intentar
* Si es mayor al aleatorio MANDAR EN PANTALLA POR ARRIBA, volver a intentar
"""

n = True
while n:
    print ("Introduce un número: ")
    op = int(input())
    if op == 5:
        print ("GANADOR")
        n = False
        while op <= 4:
            print("Por debajo", op)
        if op >= 6:
            print ("Por arriba", op)
            
