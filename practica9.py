#Aqui colocare la solucion para el proyecto de piedra papel y tijeras

import random

Opciones = ("piedra", "papel", "tijera")

#Contadores
empate_count = 0
user_count = 0
computer_count = 0


while True:
    user_choice = input("Elige Piedra, Papel, Tijera: ")
    user_choice = user_choice.lower()
    computer_choice = random.choice(Opciones)

    if user_choice == computer_choice:
        print("Esto es un empate 🤝")
        empate_count += 1
    elif user_choice == Opciones[0]:
        if computer_choice == "papel":
            print("El compútador gana el combate 📄")
            computer_count += 1
        else:
            print(f"El usuario gano el combate 🪨")
            user_count += 1
    elif user_choice == Opciones[1]:
        if computer_choice == "tijera":
            print(f"El computador gano el combate ✂️")
            computer_count += 1
        else:
            print(f"El usuario gano el combate 📄")
            user_count += 1
    elif user_choice == Opciones[2]:
        if computer_choice == "piedra":
            print("El computador gano el combate 🪨")
            computer_count += 1
        else:
            print("El usuario gano el combate ✂️")
            user_count += 1
    else:
        print("La opcion no se encuentra dentro 🤷\n")


    if empate_count == 3:
        print("Muchos empates 🤝")
        False
        break

    if computer_count == 2:
        print("Computador es el ganador definitivo 💻")
        False
        break

    if user_count == 2:
        print("Usuario es el ganador definitivo 🧑")
        False
        break