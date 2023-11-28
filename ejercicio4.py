'''Escriba un programa que pida una temperatura en grados Celsius y que escriba esa
temperatura en grados Fahrenheit.'''

def temperaturaFahrenheit(celsius:float):
    print(f"{celsius:.1f}ºC son {celsius*1.8+32:.1f}ºF")

temperaturaFahrenheit(float(input("CONVERTIDOR DE GRADOS CELSIUS A FAHRENHEIT\nEscriba una temperatura en grados Celsius: ")))