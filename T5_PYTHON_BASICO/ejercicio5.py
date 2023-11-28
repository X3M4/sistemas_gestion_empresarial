'''Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y
segundos son.'''

def convertidorTiempo(seg:int):
    minutos = int(seg/60)
    segundos = seg - minutos*60
    print(f"{seg} segundos son {minutos} minutos y {segundos} segundos")

try:
    convertidorTiempo(int(input("Escriba una cantidad de segundos: ")))
except:
    print("El valor escrito no es un número entero")
    convertidorTiempo(int(input("Escriba una cantidad de segundos: ")))