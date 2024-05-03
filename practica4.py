#Numeros Flotantes 

# Escribe un programa que solicite al usuario su peso en kilogramos y 
# su altura en metros, y luego calcule y muestre su IMC. 
peso_k = int(input("Ingresa tu peso en Kilogramos "))
altura = float(input("Ingresa tu altura "))
resultado = (peso_k/altura**2)
print(round(resultado, 2))

# Escribe un programa que calcule el monto total acumulado después de ciertos años con un interés compuesto. El usuario debe ingresar el capital inicial, la tasa de interés anual y el número de años.
capital_inicial = 1500
tasa_interes_anual = 15
numero_años = 10
monto_total = capital_inicial * (1 + tasa_interes_anual/100)**numero_años
print(monto_total)

# Desarrolla un programa que simule una inversión en la bolsa de valores. El usuario debe ingresar el monto inicial de inversión, el rendimiento esperado como un porcentaje anual, y el número de años de inversión. El programa debe calcular y mostrar el monto final después del período de inversión.

monto_inicial = float(input("Ingresa el monto inicial de inversion: "))
rendimiento = float(input("Ingresa el rendimiento anual esperado: "))
plazo = float(input("Ingresa el tiempo en el que haras la inversion: "))
retorno =(monto_inicial * (1 + (rendimiento/100))**plazo)
print(round(retorno, 6))

#Operador AND con booleanos 

# Escribe un programa que solicite al usuario ingresar un número y luego imprima si el número está entre 10 y 20.
numero = int(input("Escribe un numero "))
if numero >= 10 and numero <= 10:
    print(numero, " se encuentra en el rango")
else:
    print(numero, " no se encuentra en el rango ")

# Escribe un programa que pida al usuario ingresar su edad y su nombre. Luego, verifica si el nombre tiene más de 5 caracteres y si la edad está entre 18 y 30 años. Si ambas condiciones se cumplen, imprime "¡Bienvenido!".

nombre = "Luis Pablo Mujica Vargas "
edad = 21
if len(nombre) > 5 and edad >=18 and edad <30:
    print("Bienvenido")


# Crea un programa que solicite al usuario ingresar su nombre de usuario y contraseña. Verifica si el nombre de usuario es "admin" y la contraseña es "admin123". Si ambas condiciones son verdaderas, imprime "Inicio de sesión exitoso".

username = "admin"
contraseña = "admin123"

if username == "admin" and contraseña == "admin123":
    print("Inicio de Sesion Exitoso")


# Escribe un programa que solicite al usuario ingresar dos números enteros. Verifica si ambos números son mayores que 0 utilizando el operador and. Si ambas condiciones se cumplen, imprime la suma de los dos números.

nu_uno = 2
nu_dos = 6
if nu_uno and nu_dos > 0:
    print(nu_uno + nu_dos)

#Operador OR con booleanos

#Escribe un programa que solicite al usuario ingresar su nombre. Verifica si el nombre ingresado es "Juan" o "María". Si alguna de estas condiciones se cumple, imprime "Bienvenido Juan o María!".

nombre = input("Ingresa tu nombre ")
if nombre == "Maria" or nombre == "Juan":
    print("Bienvenido ", nombre)


# Crea un programa que solicite al usuario ingresar un número. Verifica si el número ingresado es menor que 0 o mayor que 100. Si alguna de estas condiciones se cumple, imprime "El número está fuera del rango permitido".

numero_ingresado = 78
if numero_ingresado < 0 or numero_ingresado > 100:
    print("El numero esta fuera del rango permitido")
else:
    print(None)

# Escribe un programa que pregunte al usuario si quiere continuar (responder "sí" o "no"). Verifica si el usuario ha respondido "sí" o "Si" o "sI" o "SI" utilizando el operador or. Si alguna de estas opciones se cumple, imprime "Continuando...".

respuesta = "Si"
listaSi = ["Si", "sI", "SI" ]
if respuesta in listaSi:
    print("Continuando ...")

#Operador NOT con booleanos


#  Escribe un programa que solicite al usuario que ingrese una contraseña. Si la contraseña ingresada no coincide con la contraseña almacenada en el programa, imprime un mensaje indicando que la contraseña es incorrecta.

verdad = True
if verdad:
    print( not verdad)

#Ejercicios NOT AND

hola = True and True

if hola:
    print(not hola)