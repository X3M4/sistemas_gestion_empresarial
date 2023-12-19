'''1. Crea una lista llamada numeros con los elementos: 5, 10, 15, 20, 25.'''
numeros = [5,10,15,20,25]

'''2. Imprime la longitud de la lista.'''
print(f"La longitud de la lista números es: {len(numeros)}")

'''3. Modifica el segundo elemento de la lista para que sea el doble de su valor actual.'''
numeros[1] = numeros[1]*2

'''4. Agrega el número 30 al final de la lista.'''
numeros.append(30)

'''5. Imprime la lista resultante.'''
print(f"Lista resultante: {numeros}")

'''6. Extrae e imprime los elementos en las posiciones 2 a 4 (inclusive) de la lista.'''
numeros_extraidos = numeros[2:5]
print(f"Lista resultante: {numeros_extraidos}")

'''7. Verifica si el número 10 está presente en la lista e imprime el resultado.'''
print(f"El números 10 está presente: {10 in numeros}")