def cuantosParesImpares():
    secuencia = int(input("¿Cuantos valores va a introducir: "))
    pares = 0
    impares = 0
    
    for i in range(1, secuencia+1):
        numero = int(input(f"Escriba el valor {i}: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f"Ha escrito {pares} pares y {impares} impares\nGracias por su colaboración")

cuantosParesImpares()