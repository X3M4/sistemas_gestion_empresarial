''' Escriba un programa que pida dos números y que escriba su media aritmética.'''

def ejercicio1Media(a:float, b:float):
    c = (a+b)/2
    print(f"La media de {a:.1f} y {b:.1f} es {c}")


try:
    ejercicio1Media(a=float(input("Escribe el primer número\n")), b=float(input("Escribe el segundo número\n")))
except:
    print("Algún valor escrito no es un número entero válido")
    ejercicio1Media(a=float(input("Escribe el primer número\n")), b=float(input("Escribe el segundo número\n")))
