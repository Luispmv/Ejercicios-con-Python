#Ciclos for y ciclos while

#Ciclos for 
# Escribe un programa que imprima los números del 1 al 10 en orden ascendente.
for i in range(1,11):
    print(i)

# Escribe un programa que imprima los números del 10 al 1 en orden descendente.
for i in range(10, 0, -1):
    print(i)

# Escribe un programa que imprima los primeros 10 números pares.
for i in range(0,21,2):
    print(i)

# Escribe un programa que imprima los primeros 10 números impares.
for i in range(1,21,2):
    print(i)

# Escribe un programa que pida al usuario un número entero positivo y luego imprima todos los números del 1 hasta ese número.
numero_usuario = int(input("Escribe un numero: "))
for i in range(0+1, numero_usuario+1):
    print(i)

# Escribe un programa que pida al usuario un número entero positivo y luego imprima la suma de todos los números del 1 hasta ese número.
numero_usuario = int(input("Coloca un numero: "))
suma = 0
for i in range(0+1, numero_usuario+1):
    suma += i
print(suma)

# Escribe un programa que pida al usuario un número entero positivo y luego imprima la tabla de multiplicar de ese número del 1 al 10.
numero = int(input("Ingresa un numero: "))
for i in range(1,13):
    print(f"{numero} x {i} = {numero*i}")

# Escribe un programa que genere un número aleatorio entre 1 y 100, y luego pida al usuario que lo adivine. Si el usuario no adivina el número, el programa debe imprimir si el número aleatorio es mayor o menor que el número ingresado por el usuario, y permitirle seguir intentando hasta que lo adivine.
import random
numero_intentos = 5
for i in range(numero_intentos):
    numero_usuario = int(input("Coloca el numero: "))
    aleatorio = random.choice(range(1,5))
    if numero_usuario == aleatorio:
        print(numero_usuario, " es el numero aleatorio")
        break
    else:
        print("no es el numero aleatorio")

# Escribe un programa que pida al usuario un número entero positivo y luego imprima todos los divisores de ese número.
numero_positivo = int(input("Ingresa un numero: "))
for i in range(1,numero_positivo):
    if numero_positivo % i == 0:
        print(i)
















#Ejercicios con ciclos while
# Contador regresivo: Imprimir los números del 10 al 1 en orden descendente.
n = 11
while n >= 1:
    n -= 1
    print(n)

#Suma hasta cierto límite: Solicitar al usuario un número y luego sumar todos los números desde 1 hasta ese número.
limite = int(input("Ingrese un número: "))
suma = 0 
numero = 1 
while numero <= limite: 
    suma += numero 
    numero += 1  
print("La suma de los números desde 1 hasta", limite, "es:", suma) 


#Adivinar número: Generar un número aleatorio entre 1 y 100. Pedir al usuario que adivine el número y proporcionar pistas si el número es mayor o menor.

#import random
input_usuario = int(input("Escribe un numero aleatorio: "))
while True:
    numero_random = random.choice(range(1,5))
    if input_usuario == numero_random:
        print("Encontraste el numero")
        break
    else:
       input_usuario = int(input("Escribe un numero aleatorio: "))

#Validación de entrada: Solicitar al usuario que ingrese una contraseña hasta que sea correcta
usuario_contraseña = input("Escribe tu contraseña: ")
while usuario_contraseña != repetir_contraseña:
    repetir_contraseña = input("Escribe de nuevo la contraseña: ")
    if usuario_contraseña == repetir_contraseña:
        print("La contraseña coincide")
    else:
        repetir_contraseña = input("Escribe de nuevo la contraseña: ")


#Suma de números pares: Calcular la suma de todos los números pares del 1 al 100.
n = 101
suma = 0
while n >= 1:
    n -= 1
    # print(n)
    if n % 2 == 0:
        suma += n

print(f"La suma de todos los numeros pares es de {suma}")


#Tabla de multiplicar: Imprimir la tabla de multiplicar de un número dado por el usuario.
numero_usuario = int(input("Ingresa un numero: "))
numero_multiplicar = 1

while numero_multiplicar <= 12:
    multiplicacion = numero_usuario * numero_multiplicar
    print(f"{numero_usuario} x {numero_multiplicar} = {multiplicacion}")
    numero_multiplicar += 1


#Cuenta regresiva personalizada: Pedir al usuario un número y luego contar regresivamente desde ese número hasta 1.
numeroUsuario = int(input("Coloca un numero: "))
while numeroUsuario >= 1:
    print(numeroUsuario)
    numeroUsuario -= 1


#Calculadora básica: Implementar una calculadora que realice operaciones básicas (+, -, *, /) hasta que el usuario decida salir.
def suma(numero1, numero2):
    resultado = numero1 + numero2
    return f"El resultado es {resultado}"

def resta(numero1, numero2):
    resultado = numero1 - numero2
    return f"El resultado es {resultado}"
    
def multiplicacion(numero1, numero2):
    resultado = numero1 * numero2
    return f"El resultado es {resultado}"

def division(numero1, numero2):
    resultado = numero1 / numero2
    return f"El resultado es {resultado}"
    
while True:
    userChoice = int(input("Ingresa la operacion que quieras realizar:\n 1.Suma: \n 2.Resta: \n 3.Multiplicacion: \n 4.Division:\n 5.Salir\n"))
    if userChoice == 1:
        print("Suma")
        userNumero1 = int(input("Ingresa el primer numero: "))
        userNumero2 = int(input("Ingresa el segundo numero: "))
        call = suma(userNumero1, userNumero2)
        print(call)
        print("\n")
    elif userChoice == 2:
        print("Resta")
        userNumero1 = int(input("Ingresa el primer numero: "))
        userNumero2 = int(input("Ingresa el segundo numero: "))
        call = resta(userNumero1, userNumero2)
        print(call)
        print("\n")
    elif userChoice == 3:
        print("Multiplicacion")
        userNumero1 = int(input("Ingresa el primer numero: "))
        userNumero2 = int(input("Ingresa el segundo numero: "))
        call = multiplicacion(userNumero1, userNumero2)
        print(call)
        print("\n")
    elif userChoice == 4:
        print("Division")
        userNumero1 = int(input("Ingresa el primer numero: "))
        userNumero2 = int(input("Ingresa el segundo numero: "))
        call = division(userNumero1, userNumero2)
        print(call)
        print("\n")
    else:
        break

