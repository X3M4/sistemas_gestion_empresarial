def calculoParImpar():
    
    primero = int(input("PAR E IMPAR\nEscriba un número par: "))
    segundo = int(input("Escriba nu número impar: "))
    
    try:
        if primero % 2 == 0 and segundo % 2 != 0:
            print("Gracias por su colaboración")
        else:
            print("Uno o más de los valores que ha escrito no son correctos\nEjecute de nuevo el programa para volver a intentarlo")
            
    except:
        print("No ha escrito un número")
        calculoParImpar

calculoParImpar()