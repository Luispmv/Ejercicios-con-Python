numeros = {
    "cero": 0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9
}
def hacerOperacion(signo, numero1, numero2):
    if signo == "+":
        return f"La suma de {numero1} + {numero2} es {numero1 + numero2}"
    elif signo == "-":
        return f"La resta de {numero1} - {numero2} es {numero1 - numero2}"
    elif signo == "*":
        return f"La multiplicacion de {numero1} X {numero2} es {numero1 * numero2}"
    elif signo == "/":
        return f"La division de {numero1} / {numero2} es {numero1 / numero2}"
    else:
        return "Operacion no valida"

usuario = input("Coloca un numero del 0 al 9 ya sea en numero o la palabra: ")
usuario2 = input("Coloca otro numero del 0 al 9 ya sea en numero o la palabra: ")
operacionUser = input("Coloca el signo de la operacion que quieres hacer (+, -, *, /): ")

if usuario in numeros.keys() and usuario2 in numeros.keys():
    operacion = hacerOperacion(operacionUser, numeros[usuario], numeros[usuario2])
    print(operacion)
elif usuario in numeros.values() or usuario2 in numeros.keys():
    number1 = int(usuario)
    operacion = hacerOperacion(operacionUser, number1, numeros[usuario2])
    print(operacion)
elif usuario2 in numeros.values() or usuario in numeros.keys():
    number2 = int(usuario2)
    operacion = hacerOperacion(operacionUser, numeros[usuario], number2)
    print(operacion)
else:
    operacion = hacerOperacion(operacionUser, int(usuario), int(usuario2))
    print(operacion)