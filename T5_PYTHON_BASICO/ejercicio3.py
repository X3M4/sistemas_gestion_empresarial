'''Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa
distancia en centímetros'''

def calculoCm(pies:int, pulgadas:int):
    cm = (pies*12+pulgadas)*2.54
    print("CONVERTIDOR DE MEDIDAS AL SISTEMA INTENACIONAL DESDE EL SISTEMA IMPERIAL\n")
    print(f"{pies} pies y {pulgadas} pulgadas son {cm} cm")

try:
    calculoCm(pies = int(input("Escriba una cantidad de pies\n")), pulgadas=int(input("Escribas una cantidad de pulgadas\n")))
except:
    print("Uno de los valores escritos no es un número entero")
    calculoCm(pies = int(input("Escriba una cantidad de pies\n")), pulgadas=int(input("Escribas una cantidad de pulgadas\n")))