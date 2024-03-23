# declarar variables para juego de piedra, papel y tijera
# importar la libreria random
# crear un ciclo while para que el juego se repita
# crear una variable para que el usuario pueda ingresar su eleccion
# crear una variable para que la computadora elija una opcion
# crear una condicion para que el juego se continue si el usuario quiere
# guardar el historial de resultados de la partida
# crear una condicion para que el juego termine si el usuario no quiere seguir jugando
# crear una condicion para que el juego se reinicie si el usuario quiere
# eliminar el historial de las partidas si se reinicia el juego
# imprimir la cantidad de victorias, derrotas y empates
# imprimir el historial de partidas
# imprimir un mensaje de despedida
# volver a preguntar si el usuario ingresa una opción incorrecta

import random

historial = []

while True:
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Reiniciar")
    print("5. Salir")
    opcion = input("¿Qué eliges?: ")

    if opcion == "1":
        usuario = "Piedra"
    elif opcion == "2":
        usuario = "Papel"
    elif opcion == "3":
        usuario = "Tijera"
    elif opcion == "4":
        print("Juego Reiniciado")
        historial.clear()
        victorias = 0
        derrotas = 0
        empates = 0
    elif opcion == "5":
        print("Gracias por jugar")
        print(f"Victorias: {historial.count('Ganaste')}")
        print(f"Derrotas: {historial.count('Perdiste')}")
        print(f"Empates: {historial.count('Empate')}")
        print("Historial: ", historial)
        break
    else:
        print("Opción incorrecta")
        continue

    computadora = random.choice(["Piedra", "Papel", "Tijera"])
    if usuario == "Piedra" and computadora == "Piedra":
        resultado = "Empate"
    elif usuario == "Piedra" and computadora == "Papel":
        resultado = "Perdiste"
    elif usuario == "Piedra" and computadora == "Tijera":
        resultado = "Ganaste"
    elif usuario == "Papel" and computadora == "Piedra":
        resultado = "Ganaste"
    elif usuario == "Papel" and computadora == "Papel":
        resultado = "Empate"
    elif usuario == "Papel" and computadora == "Tijera":
        resultado = "Perdiste"
    elif usuario == "Tijera" and computadora == "Piedra":
        resultado = "Perdiste"
    elif usuario == "Tijera" and computadora == "Papel":
        resultado = "Ganaste"
    elif usuario == "Tijera" and computadora == "Tijera":
        resultado = "Empate"

    historial.append(resultado)

    print(f"Usuario: {usuario}")
    print(f"Computadora: {computadora}")
    print(f"Resultado: {resultado}")

    if resultado == "Ganaste":
        print("¡Felicidades!")
    elif resultado == "Perdiste":
        print("¡Inténtalo de nuevo!")
    else:
        print("¡Empate!")

