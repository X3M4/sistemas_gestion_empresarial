'''Crea una lista llamada nombres con al menos cinco nombres de personas.'''
nombres = ['Manuel', 'Ana', 'Emilio', 'Andrea', 'Silvia']

'''1. Utiliza un bucle for para imprimir cada nombre en una línea separada.'''
for i in nombres:
    print(i)

'''2. Solicita al usuario que ingrese un nuevo nombre y agrega ese nombre a la lista.'''  
nuevo_nombre = input("Escribe un nuevo nombre para añadir a la lista: ")
nombres.append(nuevo_nombre)


'''3. Imprime la lista actualizada.'''
print(nombres)

'''4. Utiliza un bucle while para eliminar nombres de la lista hasta que tenga una
longitud de 3.'''
while len(nombres) > 3:
    nombres.pop(0)    

'''5. Imprime la lista final.'''
print(nombres)