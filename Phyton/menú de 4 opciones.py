"""
Menu 4 opciones
a.-
b.-
c.-

d.-
"""

n = True #Variable verdadera
while n: #Ciclo
    print ("Escoge una opción: ")
    print("Opción A . Pares")
    print("Opción B . Impares")
    print("Opción C . Suma a 100")
    print("Opción D . Salir")
    op = input() #Variable por teclado
    if op == "A" or op== "a":
        print ("La cantidad de números a sumar:")
        m = int(input()) #Parámetro necesario
        p = 1
        suma = 0
        while p <= m: #Utilizarlos, 1 hasta n
            print ("Dame el número:",p)
            num = int(input()) #Se le pide un valor al usuario
            if num % 2 == 0: #Validar números pares
                suma = suma + num #Sumar los números
            p = p + 1
            print ("La suma de los números es",suma)
            
    if op == "B" or op== "b":
        print ("Bienvenido B")
        print ("La cantidad de números a sumar:")
        m = int(input()) #Parámetro necesario
        p = 1
        suma = 0
        while p <= m: #Utilizarlos, 1 hasta n
            print ("Dame el número:",p)
            num = int(input()) #Se le pide un valor al usuario
            if num % 2 == 1: #Validar números impares
                suma = suma + num #Sumar los números
            p = p + 1
            print ("La suma de los números es",suma)
            
    if op == "C" or op== "c":
        w = True
        suma=0
        while w:
            print ("Dame un número: ")
            num = int(input)
            suma = suma + num
            
    if op == "D" or op== "d":
        print ("Hasta luego, vuelve pronto")
        n = False