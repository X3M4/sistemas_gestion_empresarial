'''Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una
persona y que calcule su índice de masa corporal (imc).'''

def calculoIMC(peso:float, altura:float):
    imc = peso/altura**2

    if imc > 25:
        print(f"Su IMC es de {imc}.\nUn IMC muy alto indica obesidad. Los valores normales de IMC están entre 20 y 25," 
              "pero esos límites dependen del sexo, edad y constitución física")
    elif imc < 20:
        print(f"Su IMC es de {imc}.\nUn IMC muy bajo indica infrapeso. Los valores normales de IMC están entre 20 y 25," 
              "pero esos límites dependen del sexo, edad y constitución física")

try:
    calculoIMC(peso = float(input("CÁLCULO DEL IMC\nEscribe el peso\n")), altura = float(input("Escribe el altura\n")))
except:
    print("Uno de los valores no es un número decimal")
    calculoIMC(peso = float(input("CÁLCULO DEL IMC\nEscribe el peso\n")), altura = float(input("Escribe el altura\n")))