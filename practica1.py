#Conceptos a practicar 
# funcion input

#Solicitar al usuario que ingrese su nombre y edad, luego imprimir un mensaje de bienvenida.
nombre_usuario = input("Ingresa tu nombre ")
print("Hola", nombre_usuario)
print("\n")

#Pedir al usuario que ingrese dos números y luego imprimir su suma.
numero_uno = input("Ingresa un numero ")
numero_dos = input("Ingresa otro numero ")
suma =int(numero_uno) + int(numero_dos)
print("La suma es", suma)
print("\n")

#Solicitar al usuario su edad y calcular el año en que cumplirá 100 años.
año_actual = 2024
años_limite = 100
edad_usuario = input("Cual es tu edad? ")
años_restantes = años_limite - int(edad_usuario)
año_centenario = año_actual + años_restantes
print("Cumpliras 100 años en ", años_restantes, " años en el año ", año_centenario)
print("\n")

#Pedir al usuario que ingrese una frase y luego imprimir su longitud.
frase = input("Ingresa una frase ")
longitud_frase = len(frase)
print("La longitud de la frase es ", longitud_frase)
print("\n")

#Solicitar al usuario un número y verificar si es par o impar.
numero_usuario = input("Ingresa cualquier numero ")
if int(numero_usuario)%2==0:
    print("El numero es par")
else:
    print("El numero es impar")
print("\n")

#Pedir al usuario un número e imprimir su tabla de multiplicar del 1 al 10.
numerito = input("Ingresa un numero para imprimir su tabla ")
numerito = int(numerito)
for i in range(1,12):
    multipliacion = numerito * i
    print(numerito, "x", i ,"=", multipliacion)
print("\n")

#Solicitar al usuario su altura en metros y convertirla a pies y pulgadas.

print("\n")

#Pedir al usuario tres números separados por comas y luego imprimir su suma.
numeros_comas = input("Coloca los numeros separados por comas ")
numeros_comas = numeros_comas.split(",")
suma = 0
for i in numeros_comas:
    suma += int(i)
print("La suma de los numeros es ", suma)
