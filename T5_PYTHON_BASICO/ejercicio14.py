'''1. Crea una tupla llamada estudiante con los siguientes elementos: ('Juan', 20,
'Ciencias de la Computación').'''
estudiante = ('Juan', 20, 'Ciencias de computación')

'''2. Desempaqueta la tupla en tres variables: nombre, edad y carrera.'''
nombre, edad, carrera = estudiante

'''3. Imprime cada variable por separado.'''
print(nombre)
print(edad)
print(carrera)

'''4. Crea otra tupla llamada info_curso con los elementos: ('Programación en
Python', 3).'''
info_curso = ('Programación en python', 3)

'''5. Desempaqueta la tupla info_curso en dos variables: nombre_curso y
horas_crédito.'''
nombre_curso, horas_credito = info_curso

'''6. Imprime el nombre del curso y las horas de crédito por separado.'''
print(nombre_curso)
print(horas_credito)

'''7. Crea una nueva tupla llamada info_combinada concatenando las tuplas
estudiante e info_curso.'''
info_combinada = estudiante + info_curso

'''8. Imprime la tupla info_combinada.'''
print(f"La información combinada: {info_combinada}")
