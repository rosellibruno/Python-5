import json
import random
import os

ARCHIVO = "datos.json"

# ---------------- BASE DE DATOS ----------------
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    else:
        return {
            "stats": {"victorias": 0, "derrotas": 0, "empates": 0},
            "historial_jugadas": {"piedra": 0, "papel": 0, "tijera": 0}
        }

def guardar_datos(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)

datos = cargar_datos()

# ---------------- IA MEJORADA ----------------
def elegir_ia():
    historial = datos["historial_jugadas"]

    total = sum(historial.values())

    # Si no hay datos, elegir random
    if total == 0:
        return random.choice(["piedra", "papel", "tijera"])

    # Probabilidad basada en lo que más usás
    probabilidades = {
        "piedra": historial["piedra"] / total,
        "papel": historial["papel"] / total,
        "tijera": historial["tijera"] / total
    }

    # IA contrarresta lo más probable
    jugada_probable = max(probabilidades, key=probabilidades.get)

    if jugada_probable == "piedra":
        return "papel"
    elif jugada_probable == "papel":
        return "tijera"
    else:
        return "piedra"

# ---------------- RESULTADO ----------------
def calcular_resultado(jugador, ia):
    if jugador == ia:
        return "empate"
    elif (jugador == "piedra" and ia == "tijera") or \
         (jugador == "papel" and ia == "piedra") or \
         (jugador == "tijera" and ia == "papel"):
        return "victoria"
    else:
        return "derrota"

# ---------------- JUEGO IA ----------------
def juego_ia():
    print("\n🎮 Piedra, Papel o Tijera (IA inteligente)")
    
    jugador = input("Elegí (piedra/papel/tijera): ").lower()

    if jugador not in ["piedra", "papel", "tijera"]:
        print("Opción inválida")
        return

    datos["historial_jugadas"][jugador] += 1

    ia = elegir_ia()
    print("IA eligió:", ia)

    resultado = calcular_resultado(jugador, ia)

    if resultado == "victoria":
        print("¡Ganaste!")
        datos["stats"]["victorias"] += 1
    elif resultado == "derrota":
        print("Perdiste")
        datos["stats"]["derrotas"] += 1
    else:
        print("Empate")
        datos["stats"]["empates"] += 1

# ---------------- JUEGO ADIVINANZA ----------------
def adivinanza():
    numero = random.randint(1, 20)
    intentos = 3

    print("\n🎯 Adivinanza (tenés 3 intentos)")

    while intentos > 0:
        intento = int(input("Número: "))

        if intento == numero:
            print("¡Correcto!")
            datos["stats"]["victorias"] += 1
            return
        elif intento < numero:
            print("Más alto")
        else:
            print("Más bajo")

        intentos -= 1

    print("Perdiste, era:", numero)
    datos["stats"]["derrotas"] += 1

# ---------------- CALCULADORA PRO ----------------
def calculadora():
    print("\n🧮 Calculadora")

    try:
        n1 = float(input("Número 1: "))
        op = input("Operación (+, -, *, /): ")
        n2 = float(input("Número 2: "))

        if op == "+":
            print("Resultado:", n1 + n2)
        elif op == "-":
            print("Resultado:", n1 - n2)
        elif op == "*":
            print("Resultado:", n1 * n2)
        elif op == "/":
            print("Resultado:", n1 / n2 if n2 != 0 else "Error")
        else:
            print("Operación inválida")

    except:
        print("Error: entrada inválida")

# ---------------- ESTADÍSTICAS ----------------
def ver_stats():
    print("\n📊 Estadísticas")
    for clave, valor in datos["stats"].items():
        print(clave.capitalize() + ":", valor)

# ---------------- MENÚ ----------------
def menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Juego IA")
        print("2. Adivinanza")
        print("3. Calculadora")
        print("4. Estadísticas")
        print("5. Salir")

        opcion = input("Elegí: ")

        if opcion == "1":
            juego_ia()
        elif opcion == "2":
            adivinanza()
        elif opcion == "3":
            calculadora()
        elif opcion == "4":
            ver_stats()
        elif opcion == "5":
            guardar_datos(datos)
            print("Datos guardados. Chau!")
            break
        else:
            print("Opción inválida")

menu()