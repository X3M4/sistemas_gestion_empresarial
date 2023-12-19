'''1. Crea una tupla llamada frutas con los siguientes elementos: 'manzana', 'plátano',
'cereza', 'naranja'.'''
frutas = ("manzana", "plátanos", "cereza", "naranja")

'''2. Imprime la longitud de la tupla.'''
print(f"La longitud de la tupla frutas es: {len(frutas)}")

'''3. Accede e imprime el segundo elemento de la tupla.'''
print(f"El sgundo elemento de la tupla es: {frutas[1]}")

'''4. Crea una nueva tupla llamada más_frutas con los elementos: 'uva', 'kiwi', 'melón'.'''
mas_frutas = ("uva", "kiwi", "melón")

'''5. Concatena las dos tuplas y almacena el resultado en una nueva tupla llamada
todas_las_frutas.'''
todas_las_frutas = frutas + mas_frutas

'''6. Imprime la tupla todas_las_frutas.'''
print(f"Todas las frutas son: {todas_las_frutas}")

'''7. Verifica si 'kiwi' está presente en la tupla todas_las_frutas e imprime el
resultado.'''
print(f"¿Kiwi está presente? {'kiwi' in todas_las_frutas}")
