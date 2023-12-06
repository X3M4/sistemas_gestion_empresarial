def mayorMenorMedia():
    secuencia = int(input("¿Cuántos números va a introducir? "))
    numeros = []
    media = 0
    
    for i in range(secuencia):
        num = int(input(f"Escriba el número {i+1}: "))
        numeros.append(num)
    
    for n in numeros:
        media += n
    
    media = media / len(numeros)
    numeros.sort()
    
    print(f"El número más pequeño es {numeros[0]}")
    print(f"El número más grande es {numeros[len(numeros)-1]}")
    print(f"La media los números introducidos es: {media:.2f}")

mayorMenorMedia()