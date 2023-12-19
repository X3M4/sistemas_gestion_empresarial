'''1. Crea un diccionario llamado pelicula con las siguientes claves y valores:
• 'titulo': 'El Padrino'
• 'director': 'Francis Ford Coppola'
• 'lanzamiento': 1972
• 'duracion': 175'''

pelicula = {'título': 'El Padrino', 
            'director' : 'Francis Ford Coppola', 
            'lanzamiento': 1972, 
            'duranción': 175}

'''2. Imprime el diccionario.'''
print(pelicula)

'''3. Agrega una nueva clave 'genero' con el valor 'Drama'.'''
pelicula['género'] = 'Drama'

'''4. Actualiza el valor de 'duracion' a 180.'''
pelicula['duranción'] = 180

'''5. Imprime todas las claves del diccionario.'''
print(pelicula.keys())

'''6. Elimina la clave 'lanzamiento' y su valor asociado.'''
if 'lanzamiento' in pelicula:
    del pelicula['lanzamiento']

'''7. Verifica si 'actor_principal' está en el diccionario e imprime el resultado.'''
print(f"¿Existe actor_principal en el en diccionario?: {'actor_principal' in pelicula}")