#Indexing en python
#Slicing en python

#Ejercicios con indexing en Python
# Acceso a elementos de una lista: Dada una lista de números, accede al primer, último y algún otro elemento de la lista utilizando indexing.
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

def accesoElementos(lista, numero):
    primer_elemento = lista[0]
    ultimo_elemento = lista[-1]
    otro_elemento = lista[numero]
    return f"El primer elemento es {primer_elemento}, el ultimo elemento es {ultimo_elemento} y un elemento aleatorio es {otro_elemento}"

call = accesoElementos(lista_numeros, 5)
print(call)


# Acceso a caracteres de una cadena: Dada una cadena de texto, accede al primer, último y algún otro carácter de la cadena utilizando indexing.
def accesoCaracter(cadena, numero):
    primer_elemento = cadena[0]
    ultimo_elemento = cadena[-1]
    otro_elemento = cadena[numero]
    return f"El primer elemento es {primer_elemento}, el ultimo elemento es {ultimo_elemento} y un elemento aleatorio es {otro_elemento}"

call = accesoCaracter("Hoy fumar salvara vidas", 4)
print(call)

# Acceso a elementos de una tupla: Dada una tupla de valores, accede a algún elemento de la tupla utilizando indexing.
tuplilla = (1,2,3,4,5,6,7,8,9,10)
numerillo = 4

def accesoTupla(tupla, numero):
    primer_elemento = tupla[0]
    ultimo_elemento = tupla[-1]
    otro_elemento = tupla[numero]
    return f"El primer elemento es {primer_elemento}, el ultimo elemento es {ultimo_elemento} y un elemento aleatorio es {otro_elemento}"

call = accesoTupla(tuplilla, numerillo)
print(call)

# Acceso a valores de un diccionario: Dado un diccionario, accede a algún valor del diccionario utilizando indexing.
jugador = {
    "nombre":"Messi",
    "equipo": "Barcelona",
    "promedio": 100
}

print(jugador["nombre"])



#Ejercicios con slicing en python

# Obtener una sublista de una lista: Dada una lista, utiliza slicing para obtener una sublista que contenga solo algunos elementos de la lista original.

lista = [1,2,3,4,5,6,7,8,9,10]
lista = lista[1::2]
print(lista)
# Extraer una parte de una cadena: Dada una cadena de texto, utiliza slicing para extraer una parte de la cadena original.
cadena = "Esta es una cadena original"
#Extraeremos la palabra cadena
cadena = cadena[12:18]
print(cadena)

# Invertir una lista: Dada una lista, utiliza slicing para invertir el orden de los elementos de la lista original.

numbers = [1,2,3,4,5,6,7,8,9,10]
lista_invertida = numbers[::-1]
print(lista_invertida)

# Extraer columnas de una matriz: Dada una matriz (lista de listas), utiliza slicing para extraer una columna específica de la matriz original.

matriz = [[1,3,5,67,9],[2,4,6,8,10],[1,2,3,4,5,6,7,8,9,10]]
matriz = matriz[1:2]
print(matriz)

