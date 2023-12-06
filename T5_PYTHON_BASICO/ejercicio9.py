def cuantosNumeros():
    secuencia = int(input("¿Cuántos valores va a introducir? "))
    numero = int(input("Escriba un número "))
    
    if secuencia < 0:
        print("¡Imposible!")
    
    for i in range(secuencia-1):
        numant = numero
        numero = int(input(f"Escriba un número mayor que {numero}: "))
        
        if numero < numant:
            print(f"¡{numero} no es mayor que {numant}!")

cuantosNumeros()        