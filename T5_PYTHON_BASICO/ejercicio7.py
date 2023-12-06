def comparador():
    primero = float(input("COMPARADOR DE NÚMEROS\nEscriba un número: "))
    segundo = float(input("Escriba otro número: "))
    
    try:
        numeros = ([primero, segundo])
        numeros.sort()
        print(f"Menor: {numeros[0]:.2f}; Mayor: {numeros[1]:.2f}")
    except:
        print("Uno o más de los valores escritos no son números")
        
comparador()