'''1. Crea un diccionario llamado estudiantes con al menos cinco estudiantes y sus
respectivas edades.'''
estudiantes = {'estudiante 1': 18,
               'estudiante 2': 23,
               'estudiante 3':20,
               'estudiante 4':18,
               'estudiante 5':29}

'''2. Utiliza un bucle for para imprimir cada nombre de estudiante y su edad en una
línea separada.'''
for i in estudiantes:
    print(f"{i}: {estudiantes[i]} \n")
    
'''3. Solicita al usuario que introduzca un nuevo estudiante y su edad, y agrega esta
información al diccionario.'''
estudiante = input("Escribe el nombre del nuevo estudiante: ")
edad = int(input("Escribe la edad del nuevo estudiante: "))
estudiantes[estudiante] = edad

'''4. Imprime la información actualizada del diccionario.'''
print(estudiantes)

'''5. Utiliza un bucle for para imprimir solo los nombres de los estudiantes en una línea
separada.'''
for i in estudiantes:
    print(i)

'''6. Utiliza un bucle while para eliminar estudiantes del diccionario hasta que tenga
una longitud de 3.'''
while len(estudiantes) > 3:
    clave = list(estudiantes.keys())[0]
    del estudiantes[clave]
    
'''7. Imprime la versión final del diccionario.'''
print(estudiantes)