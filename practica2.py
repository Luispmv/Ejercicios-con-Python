#Strings
#Numbers
#Booleanos
#Transformaciones a tipos de datos 

#Strings

# Reemplaza todas las ocurrencias de una letra específica en una cadena con otra letra. Por ejemplo, reemplaza todas las "a" con "x".
nombre = "Juanjo"
if "J" in nombre and "j" in nombre:
    nombre = nombre.replace("J", "X")
    nombre = nombre.replace("j", "x")
    print(nombre)

# Cuenta cuántas veces aparece una palabra específica en una cadena de texto.
palabra = "Hola"
cadena = "Hola, ¿cómo estás? Hola, ¿qué tal?"
if palabra in cadena:
    conteo = cadena.count(palabra)
    print(conteo)

# Convierte todas las letras de una cadena en mayúsculas o minúsculas.
cadena_letras = "HOLA MUCHO GUSTO"
print(cadena_letras.lower())

# Cuenta cuántas vocales hay en una cadena de texto.
vocales = ["a", "e", "i", "o", "u"]
texto = "Hola amigos estan bien?"
suma = 0
for vocal in vocales:
    if vocal in texto:
        suma += texto.count(vocal)
    
print(suma)
# Encuentra la longitud de la palabra más larga en una cadena de texto.
palabra_grande = "Hola a todos amigazos"
palabra_grande = palabra_grande.split(" ")
print(palabra_grande)

longitud_maxima = 0

for palabra in palabra_grande:
    longitud_palabra = len(palabra)
    if longitud_palabra > longitud_maxima:
        longitud_maxima = longitud_palabra
        palabra_mas_larga = palabra

print("La palabra más larga es:", palabra_mas_larga)

# Invierte una cadena de texto.
cadena_texto = "Hola"
cadena_invertida = cadena_texto[::-1]
print(cadena_invertida)

# Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
cadena_original = "ala"
cadena_invertida = cadena_original[::-1]
print(cadena_invertida)
if cadena_original == cadena_invertida:
    print("Es un palindromo")
else:
    print("No es un palindromo")

# Separa una cadena en palabras individuales y guárdalas en una lista.
palabras_cadena = "Hola esta es una cadena"
palabras_cadena = palabras_cadena.split(" ")
lista_cadena = list(palabras_cadena)
print(type(lista_cadena))


#Numbers
# Suma de dígitos: Escribe un programa que tome un número entero positivo y calcule la suma de sus dígitos.
numero_entero_positivo = int(input("Escribe un numero "))
if numero_entero_positivo > 0:
    numero_entero_positivo = str(numero_entero_positivo)
    lista_entero_positivo = list(numero_entero_positivo)
else:
    print("El numero no es positvo")

sumita = 0

for entero in lista_entero_positivo:
    entero = int(entero)
    sumita += entero

print(sumita)

# Factorial: Escribe un programa que calcule el factorial de un número entero dado.
# Número de Fibonacci: Escribe un programa que calcule el término n-ésimo de la secuencia de Fibonacci.
# Tabla de multiplicar: Escribe un programa que genere la tabla de multiplicar de un número entero dado.
numero_multiplicar = int(input("Coloca un numero "))
for i in range(1,13):
    resultado = numero_multiplicar * i
    print(numero_multiplicar, " X ", i, " = ", resultado)
    
# Conteo de dígitos pares e impares: Escribe un programa que cuente el número de dígitos pares e impares en un número entero dado.
npi = input("Digita numeros pares o impares ")
npi = list(npi)
conteo_pares = 0
array_pares = []
conteo_impares = 0
array_impares = []
for numero in npi:
    numero = int(numero)
    if numero % 2 == 0:
        conteo_pares += 1
        array_pares.append(numero)
    else:
        conteo_impares +=1
        array_impares.append(numero)

print("el numero de pares son ",conteo_pares,"y son => ", array_pares)
print("el numero de impares es ", conteo_impares,"y son => ", array_impares)

# Número de Armstrong: Escribe un programa que determine si un número entero dado es un número de Armstrong o no.
# Divisores de un número: Escribe un programa que encuentre todos los divisores de un número entero dado.


#Booleanos 

# Comparación de números: Escribe un programa que compare dos números enteros y determine si son iguales o no.
n1 = 3
n2 = 3
if n1 == n2:
    print(True)
else:
    print(False)
# Verificación de paridad: Escribe un programa que verifique si un número entero dado es par o impar.
n = 11
if n%2==0:
    print(True)
else:
    print(False)

# Comprobación de múltiplos: Escribe un programa que determine si un número entero dado es múltiplo de otro número dado.

# Comparación de cadenas: Escribe un programa que compare dos cadenas y determine si son iguales o no.
chain1 = "Hola"
chain2 = "Hola"

if chain1 == chain2:
    print(True)
else:
    print(False)

# Verificación de subcadena: Escribe un programa que verifique si una cadena dada es una subcadena de otra cadena dada.
cadenilla = "Hola a todos"
for letra in cadenilla:
    print(letra)

# Comprobación de pertenencia a una lista: Escribe un programa que determine si un elemento dado está presente en una lista dada.
lista_elementos = [1,2,3,4,5,6,7,8,9,10]
numero_usuario = int(input("Escribe un numero "))
if numero_usuario in lista_elementos:
    print(True)
else:
    print(False)
# Comparación de valores lógicos: Escribe un programa que compare dos valores booleanos y determine si son iguales o no.
# Comprobación de vacío: Escribe un programa que verifique si una lista dada está vacía o no.
lista = []
if len(lista) == 0:
    print(True, " la lista esta vacia")
else:
    print(False, " la lista contiene ", lista)

# Verificación de condición compuesta: Escribe un programa que evalúe una condición compuesta y devuelva un valor booleano.
# Comprobación de validez de entrada: Escribe un programa que verifique si una entrada dada por el usuario es válida o no según ciertos criterios predefinidos.


#Transformacion a tipos de datos

# Entero a cadena: Escribe un programa que tome un número entero como entrada y lo convierta en una cadena.
entero = int(input("Ingresa un numero "))
entero = str(entero)
print(type(entero))
if entero == str:
    print("Es un string")
else:
    print("No es un string")
# Cadena a entero: Escribe un programa que tome una cadena que represente un número entero como entrada y lo convierta en un entero.
numero_entero = int(input("Escribe un numerillo: "))

if isinstance(numero_entero, int):
    print("Es un numero entero")

# Flotante a cadena: Escribe un programa que tome un número flotante como entrada y lo convierta en una cadena.
numero_flotante = 12.5
print(type(numero_flotante))
numero_flotante = str(numero_flotante)
print(type(numero_flotante))

# Cadena a flotante: Escribe un programa que tome una cadena que represente un número flotante como entrada y lo convierta en un flotante.
cadena_flotante = "12.5"
print(type(cadena_flotante))
cadena_flotante = float(cadena_flotante)
print(type(cadena_flotante))

# Lista a cadena: Escribe un programa que tome una lista de elementos como entrada y la convierta en una cadena.
lista_elementos = ["A","E","I","O","U"]
cadena = ""
for elemento in lista_elementos:
    elemento = str(elemento)
    cadena+= elemento
print(cadena)

# Cadena a lista: Escribe un programa que tome una cadena que contenga elementos separados por comas como entrada y la convierta en una lista.
cadenita = "1,2,3,4,5,6"
print(cadenita.split(","))

# Tupla a lista: Escribe un programa que tome una tupla como entrada y la convierta en una lista.
tupla_ejemplo = (1,2,3,4,5,6,7,8,9,10)
print(type(tupla_ejemplo))
tupla_ejemplo = list(tupla_ejemplo)
print(type(tupla_ejemplo))

# Lista a tupla: Escribe un programa que tome una lista como entrada y la convierta en una tupla.
lista_ejemplo = [1,2,3,4,5,6,7,8,9,10]
print(type(lista_ejemplo))
lista_ejemplo = tuple(lista_ejemplo)
print(type(lista_ejemplo))