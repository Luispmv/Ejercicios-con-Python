# Ejercicios con upper()
# Convertir una cadena a mayúsculas.
cadena = "Hola tilines"
print(cadena.upper())
# Validación de entrada en mayúsculas.
cadena_entrada = input("Ingresa una cadena ")
for cadena in cadena_entrada:
    if cadena.upper() in cadena_entrada:
        print("Hay una mayuscula")
    else: 
        print("Puras minusculas")


# Contar letras mayúsculas en una cadena.
cadena_entrada = input("Ingresa una cadena ")
contador = 0
for cadena in cadena_entrada:
    if cadena.upper() in cadena_entrada:
        print("Hay una mayuscula")
        contador += 1
    else: 
        print("Puras minusculas")

# Reemplazar todas las letras minúsculas por mayúsculas en una cadena.
caracteres = "Hola"
print(caracteres.upper())















# Ejercicios con lower()

# Convertir una cadena a minúsculas.
palabra = "Messi el mejor jugador del mundo"
print(palabra.lower())
# Validación de entrada en minúsculas.
palabra_entrada = input("Elige una palabra")
contador = 0
for p in palabra_entrada:
    if p.lower() in palabra_entrada:
        contador += 1

resultado = "Hay minusculas en la cadena " if contador > 0 else "No hay minusculas"
print(resultado)

# Contar letras minúsculas en una cadena.
palabra_entrada = input("Elige una palabra")
contador = 0
for p in palabra_entrada:
    if p.lower() in palabra_entrada:
        contador += 1

if contador > 0:
    print("Hay ", contador, " minusculas en la cadena")
# Reemplazar todas las letras mayúsculas por minúsculas en una cadena.
minusculas = "Hola a todos ¿COMO SE ENCUENTRAN?"
print(minusculas.lower())

# Convertir la primera letra de cada palabra a minúsculas en una cadena.
palabras = "Hola amigos"
palabras = palabras[0].lower() + palabras[1:]
print(palabras) 

# Eliminar espacios en blanco y convertir toda la cadena a minúsculas.
espacios = "Esta es una cadena"
espacios = espacios.replace(" ", "")
print(espacios.lower())

# Verificar si una cadena contiene solo letras minúsculas.
contenido = "ola amiHos"
sumador = 0
for c in contenido:
    if c.lower() in contenido:
        print("minuscula")
    else: 
        sumador += 1
    
if sumador > 0:
    print("La cadena contiene mayusculas")
else:
    print("La cadena solo tiene minusculas")

# Convertir una lista de cadenas a minúsculas.
lista_cadenas = ["LISTa cadeNa", "LAtinOAmericA", "TILin"]

for i in range(len(lista_cadenas)):
    lista_cadenas[i] = lista_cadenas[i].lower()

print(lista_cadenas)


# Eliminar signos de puntuación y convertir una cadena a minúsculas.
cadena = "(Hola Amigos)"
signos_puntuacion = [".", ",", ":", ";", "!", "?", "'", "\"", "(", ")", "[", "]", "{", "}", "-", "_", "/", "\\", "<", ">", "|", "&", "@", "#", "$", "%", "^", "*", "+", "="]

print(cadena)
for signo in signos_puntuacion:
    if signo in cadena:
        cadena =  cadena.replace(signo, "")

cadena = cadena.lower()
print(cadena)

# Filtrar una lista de cadenas para incluir solo aquellas que contienen letras minúsculas.
lista_cadenas = ["A", "b", "c", "D", "e"]
nueva_lista = []

for cadena in lista_cadenas:
    contiene_minusculas = False
    for letra in cadena:
        if letra.islower():
            contiene_minusculas = True
            break
    if contiene_minusculas:
        nueva_lista.append(cadena)

print(nueva_lista)















# Ejercios con count()

# Contar letras:Escribe una función que tome una cadena de texto y un carácter como entrada, y devuelva cuántas veces aparece ese carácter en la cadena.

def contarletra(cadena, letra):
    contador = cadena.count(letra)
    return contador

print(contarletra("amarillo", "l"))

# Contar elementos en una lista:Escribe una función que tome una lista y un elemento como entrada, y devuelva cuántas veces aparece ese elemento en la lista.
def contar_elementos(lista, elemento):
  contador = lista.count(elemento)
  return contador

lista_elementos = [1,2,3,4,5,6,7,7,7,7,7,9]
print(contar_elementos(lista_elementos, 7))

# Contar palabras en una oración:Escribe una función que tome una oración y una palabra como entrada, y devuelva cuántas veces aparece esa palabra en la oración.
def contar_oracion(oracion, palabra):
    contador = oracion.count(palabra)
    return contador

print(contar_oracion("Holaaaa", "a"))

# Contar caracteres únicos en una cadena:Escribe una función que tome una cadena de texto como entrada y devuelva cuántos caracteres únicos hay en la cadena.

def contar_unicos(texto):
    signos_puntuacion = [".", ",", ":", ";", "!", "?", "'", "\"", "(", ")", "[", "]", "{", "}", "-", "_", "/", "\\", "<", ">", "|", "&", "@", "#", "$", "%", "^", "*", "+", "="]
    for caracter in texto:
        if caracter in signos_puntuacion:
            contador = texto.count(caracter)

    return print("El caracter ", caracter, " aparece ", contador, " veces en ", texto)

print(contar_unicos("Hola$$$$$"))

#Escribe una función que tome una lista de listas como entrada y devuelva la cuenta total de elementos repetidos en todas las listas.
lista_de_listas = [[1,1,1,1,3,4,5,6,7],["a","a","b","c"],[7,7,7,7,7,7,9]]
def total_repetidos(lista):
    repetidos = []
    elementos_repetidos = []
    contador = 0
    for sublista in lista:
        for item in sublista:
           if sublista.count(item) >1:
                repetidos.append(item)
                contador = len(repetidos)

    for item in repetidos:
        if repetidos.count(item) > 1 and item not in elementos_repetidos:
            elementos_repetidos.append(item)
    return f"En la lista {lista} los elementos repetidos son: {elementos_repetidos} ya que aparecen {contador} veces"


print(total_repetidos(lista_de_listas))


# Contar elementos que cumplen una condición en una lista:Escribe una función que tome una lista de números y un número objetivo como entrada, y devuelva cuántos elementos en la lista son mayores que el número objetivo.

def cumple_condicion(lista, numero):
    numeros_mayores = []
    for n in lista:
        if n > numero:
            numeros_mayores.append(n)
    return f"De la lista: {lista}, los numeros: {numeros_mayores} son mayores a {numero}"

print(cumple_condicion([1,2,3,4,5,6,7,8,9],7))















# Ejercicios con swapcase()
mensaje = "Soy un UsUario"
mensaje = mensaje.swapcase()
print(mensaje)















# Ejercicios startswith()

# Verificación de Prefijo de Números de Teléfono: Crea un programa que valide si un número de teléfono dado comienza con un código de país específico. Por ejemplo, verifica si un número de teléfono comienza con "+1" para Estados Unidos.

lista_numeros = ["+1 57789907", "+52 477 221049", "+1 890022421"]

for numero in lista_numeros:
    if numero.startswith("+1"):
        print(numero, " es de Estados Unidos")
    else: 
        print(numero, " es de otro pais")


# Clasificación de Palabras por Prefijo: Desarrolla un programa que tome una lista de palabras y clasifique las palabras en dos grupos: aquellas que comienzan con un prefijo específico y aquellas que no. Por ejemplo, clasifica las palabras que comienzan con "pre-" y las que no.

list_words = ["prefijo", "predestinado", "presuncion", "Asuncion", "Aritmetica", "Amigable"]

pre_list = []
no_pre_list = []

for word in list_words:
    if word.startswith("pre"):
        pre_list.append(word)
    else:
        no_pre_list.append(word)

print("Array orginal ==>", list_words)
print("pre_list ==> ", pre_list)
print("no_pre_list ==> ", no_pre_list)

# Validación de Prefijos de URL: Crea una función que verifique si una URL dada comienza con "http://" o "https://", asegurando que esté formateada correctamente.

paginas_web = [
    "https://www.youtube.com",
    "https://www.forbes.com",
    "https://www.stripe.com",
    "https://www.dribble.com",
    "http://www.viperplay.com",
    "http://www.bbva.com"
]
paginas_seguras = []
paginas_inseguras = []
for url in paginas_web:
    if url.startswith("https://"):
        paginas_seguras.append(url)
    else:
        paginas_inseguras.append(url)

print("Las paginas seguras son: ", paginas_seguras)
print("\n")
print("Las paginas inseguras son: ", paginas_inseguras)















# Ejercicios con endswith()

# Escribe un programa que recorra una lista de nombres de archivos y devuelva aquellos archivos que terminen con una extensión específica, por ejemplo, todos los archivos que terminen con ".txt".

archivos = ["documento1.txt", "imagen.png", "codigo.py", "hoja_de_calculo.xlsx"]

for archivo in archivos:
    if archivo.endswith(".txt"):
        print(archivo)


# Clasificación de Palabras por Sufijo: Escribe una función que tome una lista de palabras y clasifique las palabras en dos grupos: aquellas que terminan con un sufijo específico y aquellas que no.
sufijo = ["dor", "oso", "simo", "dora", "ente", "osa", "simo", "crata"]
palabra = ["Contador", "Estudioso", "Buenisimo", "Entrenadora", "Dirigente", "Revoltosa", "pesimo", "Burocrata", "baboso"]
sufijo_oso = []

for p in palabra:
    if p.endswith("oso"):
        print(p)



# Validación de Correos Electrónicos: Desarrolla una función que verifique si una dirección de correo electrónico dada termina con un dominio específico, como ".com" o ".org".

correos = ["luis@gmail.com","manuel@.com", "telas@.org", "pisos@.org"]
correo_personal = []
correo_corporativo = []

for dominio in correos:
    if dominio.endswith("org"):
        correo_corporativo.append(dominio)
    else:
        correo_personal.append(dominio)

print("Correo personal >",correo_personal)
print("Correo corporativo",correo_corporativo)

# Filtrado de Elementos en una Lista: Escribe un script que tome una lista de nombres y devuelva solo aquellos que terminen con una letra o conjunto de letras específicos.

lista_nombres = ["Mariano", "Venustiano", "Soriano", "Julian"]
for nombre in lista_nombres:
    if nombre.endswith("ano"):
        print(nombre)


# Análisis de Cadenas de Texto: Crea un programa que analice una cadena de texto en busca de patrones específicos que terminen con ciertas palabras clave.
cadena = "Hola soy Pablo"
cadena = cadena.split(" ")
print(cadena)

contador = 0
for c in cadena:
    if c.endswith("blo"):
        print(c)


# Validación de Prefijos de URL: Desarrolla una función que verifique si una URL dada termina con una extensión específica, como ".html" o ".php".
terminaciones_web = ["index.html", "index.php", "close.html", "data.php"]
for terminacion in terminaciones_web:
    if terminacion.endswith(".html"):
        print(terminacion)

# Clasificación de Imágenes por Formato: Desarrolla un programa que tome una lista de nombres de archivos de imágenes y clasifique las imágenes en dos grupos: aquellas que terminan con una extensión de archivo de imagen conocida, como ".jpg" o ".png", y aquellas que no.

lista_extensiones = ["imagen.png","img.jpg","img2.png","img3.jpg"]
lista_png = []
lista_jpg = []

for extension in lista_extensiones:
    if extension.endswith("png"):
        lista_png.append(extension)
    else:
        lista_jpg.append(extension)

print(lista_png)
print(lista_jpg)















# Ejercicios con replace()

# Escribe un programa que tome una cadena de texto y reemplace todas las instancias de un carácter específico por otro carácter dado.
cadena = "Hola"
cadena = cadena.replace("Hola", "Hellow")
print(cadena)

# Normalización de Texto: Desarrolla un script que tome una cadena de texto y reemplace todas las letras mayúsculas con sus equivalentes en minúsculas, y viceversa.
cadena_textual = "CADENA DE TEXTO"
for word in cadena_textual:
    cadena_textual = cadena_textual.replace(word, word.upper())
    if word.upper():
        cadena_textual = cadena_textual.replace(word, word.lower())

print(cadena_textual)

#Crea un programa que censure ciertas palabras en un texto dado. El usuario debe ingresar una lista de palabras a censurar, y el programa debe reemplazar cada una de esas palabras con una serie de asteriscos del mismo tamaño.
numeros_palabras_censurar = int(input("Ingresa cuantas palabras colocaras: "))


def censura(usuario):
    censurar = []
    for i in range(usuario):
        palabras = input("Ingresa una palabra: ")
        palabras_censuradas = palabras.replace(palabras, len(palabras) * "*")
        censurar.append(palabras_censuradas)
    return print(censurar)

resultado = censura(numeros_palabras_censurar)

# Eliminación de Caracteres Especiales: Crea un script que tome una cadena de texto y elimine todos los caracteres especiales, como signos de puntuación o caracteres no alfanuméricos.
cadena = "No!!!!!!"
signos_puntuacion = [".", ",", ":", ";", "!", "?", "'", "\"", "(", ")", "[", "]", "{", "}", "-", "_", "/", "\\", "<", ">", "|", "&", "@", "#", "$", "%", "^", "*", "+", "="]

for item in cadena:
    if item in signos_puntuacion:
        cadena = cadena.replace(item, " ")

print(cadena)















# Ejercicios con capitalize()

#Escribe un programa que solicite al usuario que ingrese una frase y luego imprima la misma frase con la primera letra de cada palabra en mayúscula utilizando capitalize().
frase_usuario = input("Ingresa una frase: ")

frase_usuario = frase_usuario.split(" ")

for palabra in frase_usuario:
  print(palabra.capitalize())


# Crea una función que tome una lista de nombres como argumento y devuelva una nueva lista con cada nombre capitalizado utilizando capitalize().
def capitalize(lista):
  nueva_lista = []
  for nombre in lista:
    nombre = nombre.capitalize()
    nueva_lista.append(nombre)
  return nueva_lista


usuario = int(input("Ingresa un numero de elementos a ingresar: "))
lista_usuario = []
for i in range(usuario):
  elemento = input("Ingresa un elemento: ")
  lista_usuario.append(elemento)

print(capitalize(lista_usuario))

# Diseña un programa que le pida al usuario que ingrese su nombre completo y luego imprima un mensaje de bienvenida utilizando capitalize() para capitalizar el primer nombre.


def capitalize_name(name):
  name = name.capitalize()
  return f"Bienvendio {name}"


nombres_usuario = input("Escribe tu nombre: ")
call = capitalize_name(nombres_usuario)
print(call)


# Escribe una función que tome una cadena de palabras separadas por espacios y devuelva la misma cadena con cada palabra capitalizada utilizando capitalize().
def capitalize_chain(cadena):
  cadena = cadena.split(" ")
  new = []
  for chain in cadena:
    chain = chain.capitalize()
    new.append(chain)
  return " ".join(new)


print(
    capitalize_chain(
        "Hola amigos y amigas es un placer tenerlos aqui reunidos"))


# Desarrolla un programa que tome una oración como entrada y reemplace cada palabra por su versión capitalizada utilizando capitalize(), excepto las palabras "a", "an" y "the".
def capitalizeExcept(cadena):
  palabras_prohibidas = ["a", "an", "the"]
  cadena = cadena.split(" ")
  new_chain = []
  for palabra in cadena:
    if palabra in palabras_prohibidas:
      new_chain.append(palabra)
    else:
      palabra = palabra.capitalize()
      new_chain.append(palabra)
  return " ".join(new_chain)


print(
    capitalizeExcept(
        "the cat chased an elusive mouse through a maze of tunnels"))















# Ejercicios con title()
# Capitalizar nombres completos: Escribe un programa que solicite al usuario que ingrese su nombre completo y luego imprima el nombre capitalizado utilizando el método title().
nombre_usuario = input("Ingresa tu nombre completo: ")
nombre_usuario = nombre_usuario.split(" ")
nombre_capitalizado = []
for item in nombre_usuario:
  item = item.title()
  nombre_capitalizado.append(item)

resultado = " ".join(nombre_capitalizado)
print(resultado)

# Formatear títulos de libros: Dada una lista de títulos de libros en minúsculas, capitaliza cada palabra en cada título utilizando title() y luego imprime los títulos formateados.
libros = [[
    "el principito", "harry potter y la piedra filosofal", "el código da vinci"
], ["1984", "rebelión en la granja", "un mundo feliz"],
          ["el señor de los anillos", "juego de tronos", "crónicas marcianas"]]

for item in libros:
  for i in item:
    print(i.title())

# Generar saludos personalizados: Crea un programa que solicite al usuario que ingrese su nombre y su país de origen, luego genere un saludo personalizado que incluya el nombre capitalizado y el país de origen capitalizado utilizando title().


def saludo_personalizado(nombre, pais):
  nombre = nombre.title()
  pais = pais.title()
  return f"Bienvenido desde {pais}, {nombre}"


nombre_usuario = input("Ingresa tu nombre: ")
pais_usuario = input("Ingresa tu pais: ")
call = saludo_personalizado(nombre_usuario, pais_usuario)
print(call)

# Formatear nombres de ciudades: Dada una lista de nombres de ciudades en minúsculas, capitaliza cada palabra en cada nombre de ciudad utilizando title() y luego imprime los nombres de las ciudades formateados.
ciudades = [
    "ciudad de méxico", "guadalajara", "monterrey", "puebla", "tijuana",
    "león", "querétaro", "cancún", "mérida", "morelia"
]
for ciudad in ciudades:
  ciudad = ciudad.title()
  print(ciudad)















# Ejercicios con isdigit()
# Validación de números enteros: Escribe un programa que solicite al usuario que ingrese un número. El programa debe verificar si el número ingresado consiste solo en dígitos utilizando el método isdigit() y luego imprimir un mensaje indicando si es un número válido o no.

entero = "12345600"
if entero.isdigit():
  print(True)
else:
  print(False)

# Conteo de dígitos en una cadena: Dada una cadena ingresada por el usuario, escribe un programa que cuente cuántos dígitos contiene la cadena. Utiliza el método isdigit() para verificar cada carácter de la cadena y llevar un contador de dígitos.
cadena = "12345678abc"
contador = 0
for c in cadena:
  if c.isdigit():
    contador += 1
print(contador)

# Validación de código PIN: Escribe un programa que solicite al usuario que ingrese un código PIN de cuatro dígitos. El programa debe verificar si el código PIN ingresado consiste solo en dígitos y tiene una longitud de cuatro caracteres utilizando isdigit() y len(). Luego, imprime un mensaje indicando si el código PIN es válido o no.
usuario_pin = input("Ingresa un codigo PIN")
if len(usuario_pin) <= 4 and usuario_pin.isdigit():
  print("El codigo es valido")
else:
  print("El codigo no es valido")

#Conversión de cadena a número: Escribe un programa que solicite al usuario que ingrese un número como una cadena. El programa debe verificar si la cadena consiste solo en dígitos utilizando isdigit() y, si es así, convertir la cadena en un número entero utilizando int().
numero = input("Ingresa un numero")
if numero.isdigit():
  numero = int(numero)
  print(type(numero))















# Ejercicios con count()
# Conteo de caracteres en una cadena: Escribe un programa que solicite al usuario que ingrese una cadena y un carácter específico. Luego, el programa debe contar cuántas veces aparece ese carácter en la cadena utilizando el método count().
cadena = "Hola pueblo majuica, pero como estas?"
cadena = cadena.count("p")
print(cadena)

#Conteo de ocurrencias de palabras en una lista: Dada una lista de palabras y una palabra específica ingresada por el usuario, escribe un programa que cuente cuántas veces aparece esa palabra en la lista utilizando count().
def palabra_conteo(lista,palabra):
  lista = lista.count(palabra)
  return lista

lista_usuario = []
input_usuario = int(input("Ingresa cuantos elementos tendra la lista: "))
for i in range(input_usuario):
  palabra = input("Ingresar elemento: ")
  lista_usuario.append(palabra)


palabra_usuario = input("Que palabra quieres elegir: ")

call = palabra_conteo(lista_usuario, palabra_usuario)
print(call)


# Conteo de elementos en una lista: Dada una lista de elementos, escribe un programa que cuente cuántas veces aparece un elemento específico en la lista utilizando count().
lista = [1,1,1,1,3,4,7,8,9,10]
lista = lista.count(1)
print(lista)


# Conteo de subcadenas en una cadena: Dada una cadena y una subcadena ingresada por el usuario, escribe un programa que cuente cuántas veces aparece esa subcadena en la cadena principal utilizando count().
def aparicion_caracter(cadena, subcadena):
  return cadena.count(subcadena)

cadena_usuario = input("Escribe una frase: ")
subcadena_usuario = input("Escribe una subcadena: ")

call = aparicion_caracter(cadena_usuario, subcadena_usuario)
print(call)

# Conteo de vocales en una cadena: Escribe un programa que solicite al usuario que ingrese una cadena y luego cuente cuántas vocales (a, e, i, o, u) hay en esa cadena utilizando el método count().
def conteoVocales(cadena):
  vocales = ["a","e","i","o","u"]
  contador = 0
  contadorA = 0
  contadorE = 0
  contadorI = 0
  contadorO = 0
  contadorU = 0
  for v in vocales:
      if v in cadena:
          contador += cadena.count(v)
          if v == "a":
              contadorA += cadena.count(v)
          elif v == "e":
              contadorE += cadena.count(v)
          elif v == "i":
              contadorI += cadena.count(v)
          elif v == "o":
              contadorO += cadena.count(v)
          elif v == "u":
              contadorU += cadena.count(v)
  return f"las vocales aparecen {contador} veces \n, la a aparece: {contadorA} veces \n, la e aparece {contadorE} veces \n, la i aparece {contadorI} veces \n, la o aparece {contadorO} veces \n,la u aparece {contadorU}  "

chain = input("Coloca una palabra: ")
call = conteoVocales(chain)
print(call)


# Conteo de elementos únicos en una lista: Dada una lista de elementos, escribe un programa que cuente cuántos elementos únicos hay en la lista (es decir, cuántos elementos tienen una ocurrencia de uno) utilizando count().
lista = [1,1,1,1,1,1,2,3,4,5,6,7,8,9,9]

def noRepetidos(array):
    lista_no_repetidos = []
    for item in lista:
        if lista.count(item) > 1:
            c = lista.remove(item)
        else:
            lista_no_repetidos.append(item)

    return f"los elementos que no se repetian fueron los siguientes: {lista_no_repetidos} ya que aparecieron un total de {len(lista_no_repetidos)} veces"

call = noRepetidos(lista)
print(call)




# Conteo de palabras en un texto: Dado un texto ingresado por el usuario, escribe un programa que cuente cuántas veces aparece una palabra específica en el texto utilizando count().
cadena_usuario = input("Escribe una frase: ")
palabras_usuario = input("Escribe una palabra dentro de esa frase: ")

def contadorPalabras(cadena, palabra):
    return cadena.count(palabra)


call = contadorPalabras(cadena_usuario, palabras_usuario)    
print(call)


# Conteo de ocurrencias de pares de caracteres en una cadena: Escribe un programa que solicite al usuario que ingrese una cadena y cuente cuántas veces aparecen pares de caracteres específicos (por ejemplo, "ab", "cd", "xy") en la cadena utilizando count().

canena = "abcdario sobre cdemonia en un cd de xy"
def contarPares(cadena):
    pares = ["ab", "cd", "xy"]

    count_ab = 0
    count_cd = 0
    count_xy = 0

    for elemento in pares:
        if elemento in cadena:
            if elemento == "ab":
                count_ab += cadena.count(elemento)
            elif elemento == "cd":
                count_cd += cadena.count(elemento) 
            elif elemento == "xy":
                count_xy += cadena.count(elemento) 

    return f"ab aparece: {count_ab} veces \n cd aparece: {count_cd} veces \n xy aparece: {count_xy}"   

call = contarPares(canena)
print(call)















# Ejercicios con find()
# Escribe un programa que tome una cadena de texto y encuentre la primera posición de una palabra específica dentro de esa cadena.
Cadenilla = "El regente thrag esta rotisimo"
print(Cadenilla.find("regente"))


# Desarrolla un programa que solicite al usuario una cadena y una subcadena, luego verifica si la subcadena está presente en la cadena principal utilizando el método find().
usuario_pregunta = input("Escribe una cadena de texto : ")
subcadena_pregunta = input("Escribe una subcadena : ")

def encontrar(cadena, subcadena):
    return cadena.find(subcadena)

call = encontrar(usuario_pregunta, subcadena_pregunta)
print(call)

# Crea un programa que tome una lista de nombres y encuentre aquellos que contienen una letra específica, utilizando el método find() para cada nombre.

def encontarLetra(lista, palabraBuscada):
    item_buscado = []
    for item in lista:
        if item.find(palabraBuscada) != -1:
            item_buscado.append(item)
    return f"los unicos elementos con ' {palabraBuscada} ' son: {item_buscado}"

usuario_cantidad = int(input("Ingresa un numero de items: "))
usuario_lista = []
for i in range(usuario_cantidad):
    usuario_item = input("Ingresa el elemento: ")
    usuario_lista.append(usuario_item)

usuario_caracter = input("Ingresa un caracter: ")
call =  encontarLetra(usuario_lista, usuario_caracter)
print(call)


# Desarrolla un script que reciba una cadena de texto y encuentre todas las apariciones de una subcadena dada. Imprime las posiciones de inicio de cada aparición.


cadena_recibir = "Hola estoy bien amora"
cadena_recibir = cadena_recibir.split(" ")
palabra = "a"
print(cadena_recibir)

for item in cadena_recibir:
    if item.find(palabra) != -1:
        print(item.find(palabra))















# Ejercicios con index()
# lista.index(elemento[, inicio[, fin]])
#inicio nos indica desde donde iniciar la busqueda
#fin nos indica donde terminarla
numeros = [10, 20, 30, 40, 50, 40, 60]
indice = numeros.index(30, 2)
print(f"El índice de '40' a partir del tercer elemento es: {indice}")

# Escribir un programa que tome una lista como entrada y un elemento específico, y luego imprima el índice de la primera ocurrencia de ese elemento en la lista utilizando el método index().

def primeraOucurrencia(lista, elemento):
    return lista.index(elemento)

numeros = [2,3,4,5,6,7,1]
numero = 1
call = primeraOucurrencia(numeros, numero)
print(call)

# Desarrollar un script que tome una cadena de texto como entrada y encuentre el índice de la primera ocurrencia de una subcadena específica utilizando el método index().

texto_entrada = "Hola Mundo"
subcadena_entrada = "M"

def primeraOcurrencia(cadena, subcadena):
    return cadena.index(subcadena)

call = primeraOcurrencia(texto_entrada, subcadena_entrada)
print(call)


# Crear una función que tome una lista de números como entrada y encuentre el índice del primer número primo utilizando el método index().

def es_primo(num):
	if num < 2:
		return False
	for i in range(2, num):
		if num % i == 0:
			return False	
	return True

def primeraOcurrencia(lista):
    array_primos = []
    primera_ocurrencia = 0
    for numero in lista:
        if es_primo(numero):
            array_primos.append(numero)
            primera_ocurrencia = lista.index(numero)
            
    return f"Los numeros primos son: {array_primos} y dentro del array original: {lista} el primer numero primo aparece en la posicion: {primera_ocurrencia}"

call = primeraOcurrencia([8,7,7])
print(call)


# Escribir un programa que tome una lista de palabras como entrada y encuentre el índice de la palabra más larga utilizando el método index().
cadena = ["JavaScript", "Python", "Csahrp", "Typescript", "mysql", "Programacion", "perro", "electroencefalogramastografiable"]

longest = ""
for c in cadena:
    if len(c) > len(longest):
        longest = c
print(cadena.index(longest))


# Desarrollar un script que tome una lista de números como entrada y encuentre el índice del mayor número utilizando el método index().
numeros = [1,2,3,4,5,6,7,8,9,10,1200,890]
numerote = 0
for n in numeros:
    if n> numerote:
        numerote = n

print(numeros.index(numerote))

# Crear una función que tome una lista de nombres como entrada y encuentre el índice del nombre que comienza con una letra específica utilizando el método index().

def inicioEspecifico(lista, especifico):
    item_posicion = 0
    for item in lista:
        if item.startswith(especifico):
            item_posicion =  lista.index(item)
    return item_posicion
alumnos = ["Marian","Javier","Miguel", "Ariel", "Muriel", "Samuel", "uriel"]

call = inicioEspecifico(alumnos, "ur")
print(call)



# Desarrollar un script que tome una lista de cadenas como entrada y encuentre el índice de la cadena más corta utilizando el método index().
cadenaza = ["Ho", "c", "estan"]
shortest = cadenaza[0]
for c in cadenaza:
    if len(c) < len(shortest):
        shortest = c

indice_cadena_mas_corta = cadenaza.index(shortest)
print(f"El indice de la cadena mas corta '{shortest}' es: {indice_cadena_mas_corta}")


# Crear una función que tome una lista de números como entrada y encuentre el índice del primer número negativo utilizando el método index().

def primerNegativo(lista):
    for n in lista:
        if n < 0:
           negativoIndex = lista.index(n)
    return f"El numero negativo de: {lista}, se encuentra en la posicion {negativoIndex}"

call = primerNegativo([1,2,3,4,-5,3,2,1])
print(call)

# Escribir un programa que tome una lista como entrada y encuentre el índice del último elemento utilizando el método index().

elementos_lista = [1,2,3,4,5,6,7,8,9]
ultimo_elemento = elementos_lista[-1]
print(f"El ultimo elemento se encuentra en la posicion: {elementos_lista.index(ultimo_elemento)}, el elemento es {ultimo_elemento}")















# Ejercicios con isalnum()
# Validación de contraseña alfanumérica: Crea un programa que pida al usuario ingresar una contraseña y luego verifique si la contraseña contiene solo caracteres alfanuméricos.
contraseña = "1234!"
print(contraseña.isalnum())

# Conteo de palabras alfanuméricas: Escribe un programa que cuente cuántas palabras en una lista son completamente alfanuméricas.
palabras_alfanumericas = ["Hola", "Miguel,", "como", "estas?"]
contador = 0
no_alfanumericas = []
si_alfanumericas = []
for p in palabras_alfanumericas:
    if p.isalnum() == False:
        no_alfanumericas.append(p)
    else:
          contador += 1
          si_alfanumericas.append(p)

print(f"Las cadenas que contienen caracteres no alfanumericos son: {no_alfanumericas}, las cadenas que contienenen solo caracteres alfanumericos son {si_alfanumericas} estas son {contador}")

# Eliminación de caracteres no alfanuméricos de una cadena: Escribe un programa que tome una cadena como entrada y elimine todos los caracteres que no" son alfanuméricos.
cadena_entrada = "!Hola Mundo!?¡"
def isNotAlpha(cadena):
    notalpha = []
    for elemento in cadena:
        if elemento.isalnum() != True:
            notalpha.append(elemento)
            cadena = cadena.replace(elemento, "")
    return f"Los elementos {notalpha} en la cadena ingresada no son alfanumericos"

call = isNotAlpha(cadena_entrada)
print(call)















# Ejercicios con isalpha()
# Validación de nombres: Pide al usuario que ingrese su nombre y verifica si contiene solo letras alfabéticas.
nombre_usuario = input("Ingresa tu nombre: ")
if nombre_usuario.isalpha() == True:
    print("Tu nombre no contiene numeros")
else:
    print("Tu nombre contiene numeros")

# Conteo de palabras alfabéticas: Cuenta cuántas palabras en una lista son completamente alfabéticas.
lista_alfabetica = ["a","e","3","o","u", "5", "$"]
cuenta = 0
for item in lista_alfabetica:
    if item.isalpha() != True:
        cuenta += lista_alfabetica.count(item)
print(cuenta)

# Verificación de contraseña alfanumérica: Solicita al usuario que ingrese una contraseña y verifica si contiene solo letras del alfabeto.
user_password = input("Ingresa un contraseña")
new = None
if user_password.isalpha() == True:
    print("contraseña correcta")
else:
    print("contraseña incorrecta")

for item in user_password:
    user_password = user_password.replace(item, "*")

print(user_password)















# Ejercicios con isdecimal()
#Escribe un programa que solicite al usuario que ingrese un número decimal y luego verifique si el número ingresado es válido (es decir, si contiene solo dígitos decimales).
n_decimal = input("Ingres un numero: ")
if n_decimal.isdecimal() == True:
    print("Es decimal")
else:
    print("No lo es")

#Escribe un programa que recorra una lista de cadenas y cuente cuántas de esas cadenas representan números decimales válidos (es decir, si contienen solo dígitos decimales).
cadenas_decimales = ["10","30","40","30.2","90", "6.2","9.3"]
decimal_count = 0
nodecimal_count = 0
for c in cadenas_decimales:
    if c.isdecimal() == True:
        decimal_count += 1
    else:
        nodecimal_count += 1
print(decimal_count)
print(nodecimal_count)

# Conversión segura a decimal: Implementa una función que tome una cadena como entrada y, si representa un número decimal válido, lo convierta a tipo decimal. Si la cadena no representa un número decimal válido, la función debe devolver un mensaje de error.
def conversion_decimal(cadena):
    if cadena.isdecimal() == True:
        cadena = int(cadena)
    else:
        cadena = float(cadena)
    return type(cadena)

call = conversion_decimal("17")
print(call)















# Ejercicios con islower()
# Validación de minúsculas: Pide al usuario que ingrese una cadena y verifica si todas las "letras de la cadena están en minúsculas.
chain_usuario = input("Ingresa una frase: ")

if chain_usuario.islower():
    print("Todos los caracteres son minusculas")
else:
    print(chain_usuario.islower !=True) 

# Conteo de cadenas en minúsculas: Recorre una lista de cadenas y cuenta cuántas de esas cadenas están completamente en minúsculas.
chain_minuscula = "Hola a todos amigos"
contador = 0
for c in chain_minuscula:
    if c.islower():
        contador += 1
print(contador)


# Filtrado de cadenas: Dado un conjunto de cadenas, filtra solo las que están en minúsculas utilizando el método islower().
cadena_listas = ["Cadena 1", "cadena 2", "cadenA 3", "cadena 4"]
for c in cadena_listas:
    if c.islower():
        print(c)


# Transformación a minúsculas segura: Implementa una función que tome una cadena como entrada y, si todas las letras de la cadena están en minúsculas, la función devolverá la cadena en minúsculas. Si hay al menos una letra en mayúsculas, la función debe devolver un mensaje de error.
def devolverMinusculas(cadena):
    cadena_true = []
    for c in cadena:
        if not c.islower():
            return "Error: La cadena contiene al menos una letra en mayúsculas."
        cadena_true.append(c)
    return "La cadena es " + "".join(cadena_true)

call = devolverMinusculas("Mariano")
print(call)















# Ejercicios con isnumeric()
# Validación de números enteros: Escribe un programa que solicite al usuario que ingrese un número entero y luego verifique si el número ingresado es válido (es decir, si contiene solo dígitos numéricos).
enterillo = "23"
if enterillo.isnumeric():
    print(enterillo)

# Conteo de cadenas numéricas: Recorre una lista de cadenas y cuenta cuántas de esas cadenas representan números enteros válidos (es decir, si contienen solo dígitos numéricos).

cadena_enterilla = ["23", "24", "24.5", "25.5"]
counter = 0
for c in cadena_enterilla:
    if c.isnumeric():
        counter += 1
        print(c)
print(counter)

# Filtrado de datos numéricos: Dado un conjunto de datos que contiene diferentes tipos de valores (cadenas, enteros, decimales), escribe un programa que filtre solo los valores que son números enteros válidos utilizando el método isnumeric().

lista_combinada = ["1","2","3","4","2.5","2.5"]

for item in lista_combinada:
    if item.isnumeric():
        print(item)

# Conversión segura a entero: Implementa una función que tome una cadena como entrada y, si representa un número entero válido, lo convierta a tipo entero. Si la cadena no representa un número entero válido, la función debe devolver un mensaje de error.

def conversionEntero(cadena):
    if cadena.isnumeric():
        cadena = int(cadena)
    return type(cadena)

call = conversionEntero("23")
print(call)















# Ejercicios con istitle()

# Validación de títulos: Escribe un programa que solicite al usuario que ingrese un título y luego verifique si el título ingresado sigue las convenciones de capitalización de un título (es decir, si cada palabra comienza con mayúscula y el resto de las letras está en minúscula).

titulo_usuario = "Capital"
if titulo_usuario.istitle():
    print(True)

# Conteo de títulos válidos: Recorre una lista de cadenas y cuenta cuántas de esas cadenas representan títulos válidos (es decir, si siguen las convenciones de capitalización de un título).
lista_titulos = ["Capital", "miguel", "Manuel", "Mireya"]
for item in lista_titulos:
    if item.istitle():
        print(item)















# Ejercicios con join()
# Concatenación de cadenas: Escribe un programa que tome una lista de palabras como entrada y use el método join() para concatenarlas en una sola cadena separada por espacios.
lista_palabras = ["Hola", "amigos", ", como estan?"]
print(" ".join(lista_palabras))

# Creación de una cadena CSV: Escribe un programa que tome una lista de elementos y use el método join() para crear una cadena CSV (valores separados por comas).
fruta = ["Manzana","Platano","Fresa","Durazno"]
print(",".join(fruta))


# Generación de una cadena de números: Escribe un programa que tome una lista de números enteros y use el método join() para crear una cadena de números separados por un guion medio.
numers = ["1","2","3","4","5","6","7","8","9"]
numers = "-".join(numers)
print(numers)















# Ejercicios con replace()
# Eliminar caracteres específicos de una cadena: Escribe un programa que solicite al usuario una cadena y un carácter específico, luego elimina todas las ocurrencias de ese carácter en la cadena utilizando el método replace().
def eliminarCaracter(cadena, caracter, sustitucion):
    cadena =  cadena.replace(caracter, sustitucion)
    return f"La cadena es => {cadena}"

cadena_usuario = input("Escribe una frase: ")
caracter_usuario = input("Escribe un caracter a eliminar: ")
sustitucion_usuario = input("Escribe un sustituto: ")

call = eliminarCaracter(cadena_usuario, caracter_usuario, sustitucion_usuario)


# Reemplazar múltiples caracteres en una cadena: Crea un programa que tome una cadena de texto y reemplace todas las ocurrencias de una lista de caracteres especificada por el usuario con un nuevo carácter utilizando replace().
def reemplazarCaracteres(cadena, ocurrencias, reemplazo):
    for item in ocurrencias:
        if item in cadena and reemplazo in cadena:
            cadena = cadena.replace(item,reemplazo)
    return cadena  

cadena_usuario = input("Escribe una frase: ")
numero_usuario = int(input("Escribe un numero para el tamaño de una lista: "))
ocurrencias_usuario = []
for i in range(numero_usuario):
    elemento_usuario = input("Ingresa un elemento de la lista: ")
    ocurrencias_usuario.append(elemento_usuario)

reemplazo_usuario = input("Escribe una letra a reemplazar: ")

call = reemplazarCaracteres(cadena_usuario, ocurrencias_usuario, reemplazo_usuario)
print(call)

# Eliminar palabras específicas de una cadena: Solicita al usuario una cadena de texto y una palabra específica. Luego, elimina todas las ocurrencias de esa palabra en la cadena utilizando replace().
cadena_usuario = "Esta es una cadena escrita por el usuario"
u_word = "es"
r_word = "se"
for subcadena in cadena_usuario:
    cadena_usuario = cadena_usuario.replace(u_word, r_word)

print(cadena_usuario)















# Ejercicios con rindex()


# Encontrar la última ocurrencia de una palabra en una lista de frases:
# Dada una lista de frases, encuentra la última ocurrencia de una palabra específica en cada frase utilizando rindex().
lista_frases = ["This is sparta" "Here it is", "There she is"]
found: False
for frase in lista_frases:
    print(frase.rindex("is"))

# Eliminar la última ocurrencia de un carácter en una cadena:
# Escribe una función que tome una cadena y un carácter, y elimine la última ocurrencia de ese carácter en la cadena utilizando rindex().

def eliminarUltimaOcurrencia(cadena, caracter, reemplazo):
    ultimaOcurrencia = 0
    ultimaOcurrencia = cadena.rindex(caracter)

    cadena = cadena.replace(cadena[ultimaOcurrencia], reemplazo)

    return cadena

call = (eliminarUltimaOcurrencia("cadenilla", "e", "x"))
print(call)















# Ejercicios con rsplit()

# División de una cadena en palabras inversamente:
# Dada una cadena que representa una frase, divide la cadena en palabras pero comenzando desde el final de la cadena hacia el principio utilizando rsplit(). Luego, imprime las palabras en orden inverso.
cadena = "Hola, esta es una frase"
invertidas = cadena.rsplit()
palabras_invertidas = invertidas[::-1]
print(palabras_invertidas)















# Ejercicios con split()
# Conteo de palabras:
# Dada una cadena que representa una oración, utiliza split() para dividir la cadena en palabras y contar cuántas palabras hay en total.

oracion = "Esta es una oriacion"
division = oracion.split()
count = 0
for i in division:
    count += 1
print(count)

# Suma de números:
# Dada una cadena que contiene una serie de números separados por comas, utiliza split() para dividir la cadena en números y luego suma todos los números.
cadena_numerica = "1,2,3,4,5,6,7,8,9,10"
nueva_cadena = cadena_numerica.split(",")
suma = 0
for item in nueva_cadena:
    elemento = int(item)
    suma += elemento
print(suma)

# Conteo de vocales:
# Dada una cadena de texto, utiliza split() para dividir la cadena en letras y luego cuenta cuántas vocales (a, e, i, o, u) hay en total.
cadena_vocales = "Esta es una cadena de texto y contaremos las vocales en ella"
cadena_vocales = cadena_vocales.lower()
vocales = ["a","e","i","o","u"]
vocal_count = 0
cadena_division = cadena_vocales.split()

for palabra in cadena_division:
    for item in palabra:
        if item in vocales:
            vocal_count += 1
print(vocal_count)
















# Ejercicios con isinstance()
# Verificar tipos de datos:
# Dados varios objetos, utiliza isinstance() para verificar si cada objeto es de un tipo de datos específico, como int, str, float, list, tuple, dict, etc.
entero = 20
if isinstance(entero, int):
    print("es entero")


flotante = 23.5
if isinstance(flotante, float):
    print("es flotante")

string = "Cadena"
if isinstance(string, str):
    print("es un string")

lista = [1,2,3,4,5,6,7]
if isinstance(lista, list):
    print("es una lista")

tupla = (1,2,3,4,5,6,7,9)
if isinstance(tupla, tuple):
    print("es una tupla")

diccionario = {
    "nombre": "Javier",
    "apellido": "Mandela"
}
if isinstance(diccionario, dict):
    print("es un diccionario")

# Filtrar una lista por tipo de datos:
# Dada una lista mixta que contiene varios tipos de datos, utiliza isinstance() para filtrar la lista y obtener solo los elementos de un tipo de datos específico.
lista_datos = [1,"1",1.1,[1,2,3,4,5],(1,2,3,4,5),{"nombre":"luis"}]
for dato in lista_datos:
    if isinstance(dato, dict):
        print(dato)

# Manejar diferentes tipos de entrada en una función:
# Escribe una función que acepte un argumento y utilice isinstance() para verificar el tipo de datos del argumento. Luego, realiza una acción específica dependiendo del tipo de datos del argumento.

def instancia(argumento):
    datos_disponibles = (int, float, str)
    if isinstance(argumento, datos_disponibles):
        return True
    else:
        return False
call = instancia(1)
print(call)

# Crear una función polimórfica:
# Escribe una función que acepte varios tipos de datos como entrada y realice operaciones diferentes dependiendo del tipo de datos de entrada. Utiliza isinstance() para determinar el tipo de datos de cada entrada.

def datosVariados(tipoDato):
    if isinstance(tipoDato, int):
        numero_usuario = int(input("Ingresa un numero"))
        return tipoDato + numero_usuario
    elif isinstance(tipoDato, str):
        for c in tipoDato:
            print(c)
        return c
    elif isinstance(tipoDato,float):
        numero_flotante = float(input("Ingresa un numero decimal"))
        return tipoDato + numero_flotante
    elif isinstance(tipoDato, bool):
        return f"ingresaste un booleano ya que {type(tipoDato)}"
    elif isinstance(tipoDato, list):
        return f"ingresaste una lista ya que {type(tipoDato)}"
    elif isinstance(tipoDato, tuple):
        return f"ingresaste una tupla ya que {type(tipoDato)}"
    else:
        return f"No ingresaste nada"

call = datosVariados((1,2,3,4,5))
print(call)