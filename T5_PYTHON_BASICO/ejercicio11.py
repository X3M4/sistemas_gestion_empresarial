def paresImpares():
    numero_1 = int(input("Escriba un número entero: "))
    numero_2 = int(input(f"Escriba un número entero mayor o igual a {numero_1}: "))
    
    if numero_2 < numero_1:
        print(f"Le he pedido un número entero igual o mayor a {numero_1}")
    else:
        for i in range(numero_1, numero_2+1):
            if i%2 == 0:
                print(f"El número {i} es par")
            else:
                print(f"El número {i} es impar")

paresImpares()