print ("Ingresa un número")
a = int(input())
numero = 0
while numero < 1000:
    numero = numero + a
    print ("Ingresa otro número")
    print (numero)
    a = int (input())
    print ("La suma es: ", numero)
