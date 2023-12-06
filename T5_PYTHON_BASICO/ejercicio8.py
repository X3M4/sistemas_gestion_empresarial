def comparadorTiempo():
    primero = int(input("COMPARADOR DE AÑOS\n¿En qué año estamos?: "))
    segundo = int(input("Escriba un año cualquiera: "))

    try:
        if primero > segundo:
            print(f"Desde el año {segundo} han pasado: {primero-segundo} años")
        elif segundo > primero:
            print(f"Para llegar al año {segundo} faltan {segundo-primero} años")
    except:
        print("Uno o más de los años escritos no son números")

comparadorTiempo()
