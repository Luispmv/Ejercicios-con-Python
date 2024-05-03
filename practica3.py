#Operadores aritmeticos 

# Suma: Escribe un programa que sume dos números ingresados por el usuario y muestre el resultado.
print("SUMA")
n1 = int(input("Ingresa un numero "))
n2 = int(input("Ingresa otro numero "))
print(n1+n2)
print("\n")
# Resta: Escribe un programa que reste dos números ingresados por el usuario y muestre el resultado.
print("RESTA")
n1 = int(input("Ingresa un numero "))
n2 = int(input("Ingresa otro numero "))
print(n1-n2)
print("\n")
# Multiplicación: Escribe un programa que multiplique dos números ingresados por el usuario y muestre el resultado.
print("MULTIPLICACION")
n1 = int(input("Ingresa un numero "))
n2 = int(input("Ingresa otro numero "))
print(n1*n2)
print("\n")

# División: Escribe un programa que divida un número entre otro ingresados por el usuario y muestre el resultado.
print("DIVISION")
n1 = int(input("Ingresa un numero "))
n2 = int(input("Ingresa otro numero "))
print(n1/n2)
print("\n")

# Potenciación: Escribe un programa que eleve un número a una potencia ingresada por el usuario y muestre el resultado.
print("POTENCIACION")
numero = 2
potencia = int(input("Ingresa un numero para potenciar 2 :"))
resultado = numero **potencia
print(resultado)
print("\n")

# Raíz cuadrada: Escribe un programa que calcule la raíz cuadrada de un número ingresado por el usuario y muestre el resultado.


# Área de un rectángulo: Escribe un programa que calcule el área de un rectángulo dados su largo y su ancho.
# Area = Base * Altura
base = 20
altura = 50
print(base * altura)

# Área de un círculo: Escribe un programa que calcule el área de un círculo dado su radio.
pi = 3.1416
radio = 23
resultado = (pi * radio**2)
print(resultado)

# Escribe un programa que convierta una temperatura en grados Celsius a grados Fahrenheit
# (la fórmula es Fahrenheit = Celsius * 9/5 + 32).
grados = int(input("Elige Grados Celsius o Fahreneheit "))
if grados == 1:
    temperatura = int(input("Escribe la temperatura "))
    resultado = temperatura * (9/5) + 32
    print(temperatura, " en Celsius es igual a ", resultado, " en Fahreneheit")
elif grados == 2: 
    temperatura = int(input("Escribe la temperatura "))
    resultado = temperatura - 32 * (5/9)
    print(temperatura, " en Fahrenheit es igual a ", resultado, " en Celsius")
else:
    print("Tu eleccion no esta disponible")

print("\n")

# Promedio de tres números: Escribe un programa que calcule el promedio de tres números ingresados por el usuario.
numeros_usuario = list(input("Ingresa numeros: "))
print(numeros_usuario)
suma = 0
for numero in numeros_usuario:
    numero = int(numero)
    suma += numero
print(suma)
resultado = suma / len(numeros_usuario)

print("\n")

#Operador modulo

# Determinar si un número es par o impar.
numero = 2
if numero % 2 == 0:
    print("El numero es par")
else:
    print("no es par")
# Calcular el residuo de una división entre dos números.
division = 10%5
print(division)


#Operador de divison

# División entera y resto: Escribir un programa que tome dos números como entrada y muestre su división entera y su resto.
n1 = 10
n2 = 5 
print(n1/n2)
print(n1%n2)

# Verificar si un número es divisible por otro: Escribir una función que tome dos números como entrada y verifique si el primero es divisible por el segundo.
# Calculadora de propinas: Escribir un programa que calcule el monto de la propina a partir de un total de la cuenta y un porcentaje de propina.
totalCuenta = 1500
porcentaje = 10
resultado = (totalCuenta * porcentaje) / 100
print(int(resultado))

# Cálculo del precio por unidad: Escribir un programa que tome el precio total de un producto y la cantidad comprada, y calcule el precio por unidad.
precio_total = 100
compra = 20
resultado = (precio_total * compra) / compra
print(resultado)
# Divisibilidad por múltiplos: Escribir una función que tome un número y verifique si es divisible por todos los números del 1 al 10.
# Cálculo del porcentaje: Escribir una función que tome dos números como entrada (un valor y un porcentaje) y calcule el valor correspondiente al porcentaje dado.
# División larga: Implementar la división larga manualmente en una función que tome dos números enteros y devuelva el cociente y el resto.

#Operador exponencial

# Calcular el cuadrado de un número ingresado por el usuario.
#Solucion 1
numero_user = 2
print(numero_user ** 2)
#Solucion 2
numero_user = 2
print(pow(numero_user, 2))
# Calcular el cubo de un número ingresado por el usuario.
usern = 3
print(usern ** 3)
print(pow(usern, 3))

# Calcular el volumen de un cubo con longitud del lado ingresada por el usuario.
lado = 3
volumen = (lado**3)
print(volumen)
# Calcular el interés compuesto con una tasa de interés ingresada por el usuario.
user_numb = int(input("Ingresa una tasa de interes "))/100
interes = user_numb
ci = 1500
n = 70
cf = ci * (1 + interes)**n
print(int(cf))

# Calcular la hipotenusa de un triángulo rectángulo con las longitudes de los catetos ingresadas por el usuario.

# Calcular el monto final de una inversión con el capital inicial, la tasa de interés y el número de períodos ingresados por el usuario.

#Operador mayor que 

# Comparación de edades: Escribir un programa que compare las edades de dos personas e imprima un mensaje indicando quién es mayor.
personaUno = int(input("Ingresa tu edad"))
personaDos = int(input("Ingresa otra edad"))

if personaUno > personaDos:
    print("La mayor edad es ", personaUno)
elif personaDos > personaUno:
    print("La myor edad es ", personaDos)
else:
    print("Tienen la misma edad")
# Comparación de promedios: Desarrollar un programa que compare los promedios de dos estudiantes y muestre el nombre del que tiene un promedio mayor.
listaUno = [10,10,9,8,7,6]
listaDos = [10,10,10,10,9]

suma = 0
for numero in listaUno:
    suma+=numero

promedioUno = suma/len(listaUno)

suma2 = 0
for numero in listaDos:
    suma2+=numero

promedioDos = suma2/len(listaDos)

if promedioUno > promedioDos:
    print("El primer estudiante tiene mejor promedio")
elif promedioUno < promedioDos:
    print("El segundo estudiante tiene mejor promedio")
else:
    print("Promedios iguales")

# Ordenar números: Escribir una función que tome una lista de números como entrada y devuelva una lista ordenada de forma ascendente utilizando el operador mayor que.

# Filtrar números: Crear un programa que tome una lista de números como entrada y devuelva una lista de números mayores que un valor específico dado por el usuario.
valorEspecifico = 3
ln = [1,2,3,4,5,6,7,8,9,10]
nl = []

for n in ln:
    if n > valorEspecifico:
        nl.append(n)

print(nl)

# Filtrar palabras: Desarrollar un script que tome una lista de palabras y devuelva una lista de aquellas que tengan más caracteres que una longitud dada.
longitud_dada = int(input("Ingresa una cantidad de caracteres"))
palabras = ["Hola", "oa", "numero", "Hackhaton"]
nuevas_palabras = []

for p in palabras:
    if len(p) > longitud_dada:
        nuevas_palabras.append(p)

print(nuevas_palabras)

# Análisis de poblaciones: Crear un programa que compare la población de dos ciudades y determine cuál tiene una población mayor.
poblacionUno = int(input("Ingresa la poblacion de tu primera ciudad: "))
poblacionDos = int(input("Ingresa la poblacion de tu segunda ciudad: "))

resultado = (poblacionUno, " es mayor") if poblacionUno > poblacionDos else (poblacionDos, " es mayor")

# Ordenar palabras: Escribir una función que tome una lista de palabras como entrada y devuelva una lista ordenada alfabéticamente utilizando el operador mayor que para comparar cadenas.
letras = ["a","e", "c", "d", "b"]
print(sorted(letras))

#Operador de igualdad

# Búsqueda de elementos repetidos: Escribe una función que tome una lista como entrada y devuelva True si hay elementos repetidos en la lista, y False si todos los elementos son únicos. Utiliza el operador de igualdad para comparar los elementos de la lista.
array = [1,1,1,1,1,3,5,5,6,7,8]
def elementos_repetidos(lista):
    conjunto = set()
    for elemento in lista:
        if elemento in conjunto:
            return True
        else:
            conjunto.add(elemento)
            return False

print(elementos_repetidos(array))