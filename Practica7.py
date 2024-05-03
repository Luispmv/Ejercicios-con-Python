#Practica con listas

# Suma de elementos: Dada una lista de números, escribe un programa para calcular la suma de todos los elementos de la lista.
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
contador = 0
for numero in lista_numeros:
    contador += numero

print(contador)

# Buscar el máximo y el mínimo: Dada una lista de números, encuentra el valor máximo y el valor mínimo en la lista.
n_list = [10,20,90,70,54,1450,45]
def maxmin(list):
    biggest = n_list[0]
    lowest = n_list[0]
    for n in n_list:
        if n > biggest:
            biggest = n
        if n < lowest:
            lowest = n
    return f"el mas grande es {biggest} y el menor es {lowest}"

call = maxmin(n_list)
print(call)

# Eliminar duplicados: Dada una lista que puede contener elementos duplicados, escribe un programa para eliminar los elementos duplicados y obtener una lista sin duplicados.

def eliminar_duplicados(list):
    duplicates = []
    for element in list:
        if list.count(element) > 1 and element not in duplicates:
            duplicates.append(element)
    return f"Los elementos duplicados son {duplicates}"

listilla = [1,1,1,1,2,3,4,5,5,6,7,9,9,8,9,9,9]

call = eliminar_duplicados(listilla)
print(call)


# Invertir una lista: Dada una lista, escribe un programa para invertir el orden de los elementos de la lista.
numeros_impares = [1,3,5,7,9,11,13,15,17,19,21]
lista_invertida = numeros_impares[::-1]
print(lista_invertida)

# Contar elementos: Dada una lista y un elemento específico, cuenta cuántas veces aparece ese elemento en la lista.

def contarElemento(lista, especifico):
    contador = 0
    for elemento in lista:
        if elemento == especifico:
            contador += 1
    return contador

call = contarElemento([1,1,1,2,3,4,5,6],6)
print(call)

# Ordenar una lista: Dada una lista de números, escribe un programa para ordenar los elementos de la lista en orden ascendente.
numerillos = [10,4,3,2,8,9,5,1]
numerillos.sort()
print(numerillos)

# Unir dos listas: Dadas dos listas, escribe un programa para unirlas en una sola lista.
def unirListas(lista1, lista2):
    nueva_lista = lista1 + lista2
    return nueva_lista

call = unirListas([1,2,3],[4,5,6])
print(call)

# Eliminar elementos específicos: Dada una lista y un elemento específico, escribe un programa para eliminar todas las ocurrencias de ese elemento de la lista.
def eliminarEspecifico(lista, especifico):
    new_list = []
    for elemento in lista:
        if elemento != especifico:
            new_list.append(elemento)
    return new_list

call = eliminarEspecifico([1,2,3,4,5,5,5],5)
print(call)


# Sumar elementos de dos listas: Dadas dos listas del mismo tamaño que contienen números, escribe un programa para sumar los elementos correspondientes de las dos listas y obtener una nueva lista con las sumas.
def sumarListas(lista1, lista2):
    sumaLista1 = 0
    sumaLista2 = 0
    sumaListas = []

    for item in lista1:
        sumaLista1 += item
    sumaListas.append(sumaLista1)

    for item in lista2:
        sumaLista2 += item
    sumaListas.append(sumaLista2)
    
    return sumaListas

call = sumarListas([1,2],[3,4])
print(call)

# Contar elementos únicos: Dada una lista que puede contener elementos duplicados, escribe un programa para contar cuántos elementos únicos hay en la lista.
def contadorUnicos(lista):
    contador_unicos = 0
    numeros_unicos = []
    for item in lista:
        if lista.count(item) == 1:
            contador_unicos += 1
            numeros_unicos.append(item)
    return f"Hay {contador_unicos} elementos unicos y son {numeros_unicos}"

numeros_lista = [1,1,2,3,4,4,4,5,6,7,7,8]
call = contadorUnicos(numeros_lista)
print(call)















#insert()

# Insertar elementos al principio: Dada una lista, inserta un elemento en la primera posición de la lista utilizando insert().

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.insert(0, 0)
print(numeros)

# Insertar elementos en posiciones específicas: Dada una lista, inserta un elemento en una posición específica de la lista utilizando insert().

def inserccionEspecifica(lista, posicion, elemento):
    lista.insert(posicion, elemento)
    return lista

call = inserccionEspecifica([1,2,3], 0, 98)
print(call)

# Insertar múltiples elementos: Dada una lista, inserta múltiples elementos en diferentes posiciones de la lista utilizando insert().

import random
lista_num = [1,2,3,4,5]
new_position = random.choice(range(0,10))
new_num = random.choice(range(0,100))
lista_num.insert(new_position, new_num)
print(lista_num)

# Insertar en una lista de listas: Dada una lista de listas, inserta un elemento en una posición específica de una de las sublistas utilizando insert().

def insertarEnSublista(list_lists, posicion, elemento):
    list_lists[posicion].insert(posicion, elemento)
    return list_lists

list_list = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15,16],[17,18,19,20]]
call = insertarEnSublista(list_list, 3, "Mariana")
print(call)















#remove()
#El operador del nos sirve para eliminar un elemento dado su indice
lista = [1,2,3,4,5]
del lista[2]
print(lista)

# Eliminar un elemento específico: Dada una lista y un elemento específico, escribe un programa para eliminar la primera ocurrencia de ese elemento de la lista utilizando el método remove().
lista_enteros = [1,2,3,4,5,5,6,7,8]
elemento = 5

lista_enteros.remove(elemento)
print(lista_enteros)


# Eliminar elementos en una lista de listas: Dada una lista de listas, escribe un programa para eliminar una sublista específica de la lista utilizando el método remove().
lista_de_listas = [["a","b","c"],[1,2,3]]
lista_de_listas.remove(lista_de_listas[1])

print(lista_de_listas)

# Eliminar elementos por tipo: Dada una lista mixta que contiene elementos de diferentes tipos, escribe un programa para eliminar todos los elementos de un tipo específico utilizando el método remove().
lista = [1,2.5,"2.5"]

for item in lista:
    if isinstance(item, float):
        lista.remove(item)
print(lista)















#reverse()
# Invierte una lista de números.
cadena_numerica = [1,3,6,9,18,36,72]
cadena_numerica.reverse()
print(cadena_numerica)

# Invierte una cadena de caracteres.
caracteres = "Esto son muchos caracteres"
caracteres = list(caracteres)
caracteres.reverse()
print("".join(caracteres))

# Invierte una lista de palabras en una oración.
oracion = ["Wait for you love", "i'll wait for your love", "now that you made me"]
oracion_reversa = []
for item in oracion:
    item = list(item)
    item.reverse()
    item_invertido = "".join(item)
    oracion_reversa.append(item_invertido)

print(oracion_reversa)

# Invierte los dígitos de un número entero.
numero = 45 
numero = str(numero)
numero = list(numero)
numero.reverse()
new_number = "".join(numero)
print(new_number)

# Invierte el orden de las palabras en una oración sin invertir el orden de las letras en cada palabra.
oracion_palabras = "Esta es una cadena llena de palabras"
oracion_palabras =  oracion_palabras.split()
oracion_palabras.reverse()
print(oracion_palabras)

# Invierte el orden de los caracteres en cada palabra de una oración sin invertir el orden de las palabras.
oracion_cracteres = "Got my head in the stars"
oracion_cracteres = oracion_cracteres.split()
nueva_oracion = []
for item in oracion_cracteres:
    item = list(item)
    item.reverse()
    invertido = "".join(item)
    print(invertido)
    nueva_oracion.insert(0, invertido)
nueva_oracion.reverse()
print(nueva_oracion)
# Invierte una lista de tuplas.
lista_tuplas = [(1,2,3,4,5,6,7),(10,20,30,40,50),(100,200,300,400,500)]
lista_tuplas.reverse()
print(lista_tuplas)
















#sort()
# Ordenar una lista de números en orden ascendente.
lista_desordenada = [6,7,8,4,3,1,2,5,9,10]
lista_desordenada.sort()
print(lista_desordenada)
# Ordenar una lista de cadenas de texto en orden alfabético.
vocales = ["e","i","a","u","o"]
vocales.sort()
print(vocales)

# Ordenar una lista de números en orden descendente.
numerales = [1,4,5,7,8,9,4,3]
numerales.sort()
numerales = numerales[::-1]
print(numerales)

# Ordenar una lista de cadenas de texto en orden inverso (de Z a A).
alfabeto =  ['m', 'h', 'e', 'x', 'z', 'q', 'i', 'c', 'r', 'a', 'j', 'd', 'y', 'w', 'f', 'p', 'b', 'k', 'l', 'g', 'v', 'o', 's', 'n', 'u', 't']
alfabeto.sort()
alfabeto.reverse()
print(alfabeto)















#Tuplas
# Acceder a elementos: Crea una tupla con algunos elementos y luego accede a ellos utilizando índices positivos y negativos.
def accederTupla(lista,posicion):
    return lista[posicion]

call = accederTupla((1,2,3,4,5,6,7),-1)
print(call)

# Modificar una tupla: Intenta modificar una tupla directamente y observa el error que se produce. Luego, intenta modificarla mediante conversiones a listas, modificación y luego la conversión nuevamente a tupla.
def modificarTupla(tupla, item):
    tupla = list(tupla)
    tupla.append(item)
    tupla = tuple(tupla)
    return f"La tupla modificada es {tupla}, agregando el elemento {item}"

call = modificarTupla((1,2,3,4), "Maynez")
print(call)

# Iterar sobre una tupla: Crea una tupla e itera sobre ella usando un bucle for.
nombres = ("Luis","Miguel","Roberto","Liam","Ernesto")
for nombre in nombres:
    print(nombre)

# Desempaquetar tuplas: Define una tupla con varios elementos y luego desempaquétala en variables individuales.
nomeros = (1,2,3,4,5,6,7,8)
nomeros = list(nomeros)
var1 = []
var2 = []
for numero in nomeros:
    if numero <= 4:
        var1.append(numero)
    else:
        var2.append(numero)
print(var1)
print(var2)


# Concatenar tuplas: Crea dos tuplas y únelas para formar una tupla más grande.
nombres = ("Miguel", "Armando")
mas_nombres = ("Oscar", "Omar", "Alexis")
tuplota = nombres + mas_nombres
print(tuplota)

# Comparación de tuplas: Crea dos tuplas y compáralas utilizando los operadores de comparación (<, <=, ==, !=, >=, >).
tupla1 = (1,2,3,4,5)
tupla2 = (6,7,8,9,10,11)

if len(tupla1) > len(tupla2):
    print("tupla1 es mayor que tupla 2")
elif len(tupla1) < len(tupla2):
    print("tupla 2 es mayor")
elif len(tupla1) == len(tupla2):
    print("son iguales")


# Encontrar el mínimo y el máximo: Define una tupla de números y encuentra el valor mínimo y máximo.
tupla_numerica = (11,2,3,4,5,6,7,8,9,10)
mayor = tupla_numerica[0]
menor = tupla_numerica[0]

for numero in tupla_numerica:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
print(mayor)
print(menor)

# Contar elementos: Crea una tupla con elementos repetidos y cuenta cuántas veces aparece un elemento específico en la tupla.
repetidos = (1,1,1,2,3,4,5,6,7,8)
elemento = 1
contador = 0
for item in repetidos:
    if item == elemento:
        contador += 1
print(contador)

# Conversión de tupla: Convierte una tupla en una lista y viceversa.

def conversion(grupo):
    if isinstance(grupo, tuple):
        grupo = list(grupo)
    else:
        grupo = tuple(grupo)
    
    return type(grupo)

call = conversion([1,2,3])
print(call)

# Operaciones matemáticas: Realiza operaciones matemáticas con elementos de una tupla, como suma, resta, multiplicación o cualquier otra operación que puedas imaginar.
elementos = (1,2,3,4,5)
suma = 0
resta = 0
multiplicacion = 1
division = 0
eleccionUsaurio = int(input(f"Elige una operacion matematica para aplicar a esta tupla {elementos}\n 1. Suma\n 2. Resta \n 3. Multiplicacion \n 4. Division"))

if eleccionUsaurio == 1:
    for item in elementos:
        suma += item
    print(suma)
elif eleccionUsaurio == 2:
    for item in elementos:
        resta -= item
    print(resta)
elif eleccionUsaurio == 3:
    for item in elementos:
        multiplicacion *= item
    print(multiplicacion)
else:
    for item in elementos:
        division /= item
    print(division)















#Diccionarios
# Acceso a elementos: Crea un diccionario con algunos pares clave-valor y accede a los valores utilizando las claves.
persona = {
    "nombre": "Luis Pablo",
    "edad": 21
}
nombre = persona["nombre"]
edad = persona["edad"]

print(f"El nombre es {nombre} y la edad es {edad}")

# Agregar y modificar elementos: Agrega nuevos elementos al diccionario y modifica los valores existentes.
estudiante = {
    "nombre": "Luis Pablo",
    "edad": 21
}
estudiante["calificacion"] = 10
print(estudiante)

# Eliminar elementos: Elimina elementos del diccionario utilizando la palabra clave del o el método pop().
del estudiante["calificacion"]
estudiante.pop("edad")
print(estudiante)

# Iteración sobre un diccionario: Utiliza bucles for para iterar sobre las claves, los valores o ambos del diccionario.
jugador = {
    "name": "Messi",
    "equipo": "Barcelona",
    "ranking": 97
}
for key in jugador:
    print(key) 
    print(jugador[key])


# Longitud del diccionario: Utiliza la función len() para determinar la cantidad de elementos en el diccionario.
print(len(jugador))

# Combinar diccionarios: Combina dos diccionarios en uno solo utilizando el método update().
diccionario1 = {"a": 1, "b": 2}
diccionario2 = {"b": 3, "c": 4, "d": 5}
diccionario1.update(diccionario2)
print(diccionario1)

# Copiar diccionarios: Copia un diccionario utilizando el método copy() y observa cómo se comportan las modificaciones en la copia y el original.
empresa = {
    "nombre": "Coca cola",
    "sector": "Alimentos"
}
empresa_copia = empresa.copy()
print(empresa_copia)

# Verificar si una clave existe: Utiliza la palabra clave in para verificar si una clave existe en el diccionario.
if "nombre" in empresa:
    print(empresa["nombre"])

# Obtener valores por defecto: Utiliza el método get() para obtener un valor por defecto si la clave no existe en el diccionario.
print(empresa.get("pais", "Segundo argumento por si no existe el valor"))

# Ordenación de diccionarios: Observa que los diccionarios en Python no tienen un orden específico, pero puedes ordenar las claves o los valores utilizando las funciones sorted() o sorted() con un argumento key.

mi_diccionario = {"z": 3, "a": 1, "b": 2}
valores_ordenados = sorted(mi_diccionario.values())
print("Valores ordenados:", valores_ordenados)

# Imprime las llaves y valores de un diccionario

empresas_tech = {
    "nombre": "Google",
    "ceo": "Sundar Pichai"
}
print(empresas_tech.keys())
print(empresas_tech.values())
