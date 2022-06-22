## maquina de bebidas

n = True
while n:
    print("Opción A Costo 270")
    print("Opción B Costo 340")
    print("Opción C Costo 390")
    print("Opción D . Salir")
    sel = input()
    if sel == "A" or sel== "a":
        print ("EL COSTO DE LA BEBIDA ES DE 270, SOLO ACEPTA MONEDAS DE 10, 50 Y 100:")
        moneda = int(input()) 
        p = 1
        suma = 0
        while p <= moneda: 
            print ("Ingresa una moneda:",p)
            num = int(input()) 
            if num % 2 == 0:
                suma = suma + num 
            p = p + 1
            print ("El total de su compra es:",suma)
            
    if op == "D" or op== "d":
        print ("Hasta luego, vuelve pronto")
        n = False
