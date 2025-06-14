import random

# Lista de personajes con pistas
personajes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "pistas": ["Lanza telarañas y vive en Nueva York", "Escala edificios", "Lo mordió una araña"]},
    {"nombre": "Harry Potter", "universo": "Harry Potter", "pistas": ["Tiene una cicatriz en forma de rayo", "Usa magia", "Enemigo del innombrable"]},
    {"nombre": "Darth Vader", "universo": "Star Wars", "pistas": ["Respira fuerte y dice 'yo soy tu padre'", "Lado oscuro", "Era un Jedi"]},
    {"nombre": "Mario", "universo": "Nintendo", "pistas": ["Es un plomero con bigote que salta sobre tortugas", "Luigi rojo", "Wario flaco"]},
    {"nombre": "Batman", "universo": "DC", "pistas": ["Mataron a sus papás", "Murciélago", "Es millonario"]},
    {"nombre": "Naruto", "universo": "Naruto", "pistas": ["Tiene un Jinchuriki", "Le gusta Sasuke", "Pelo amarillo"]},
    {"nombre": "Bart", "universo": "Simpson", "pistas": ["El Barto", "Su papá lo ahorca", "Travieso =)"]}
]

puntaje_total = 0
print("¡Bienvenido al juego de adivinanzas!")
print("Intenta adivinar el personaje. Tendrás pistas progresivas.")
print("Escribe 'salir' si deseas rendirte.\n")

while True:
    personaje = random.choice(personajes)
    pistas = personaje['pistas']
    intentos = 0
    adivinado = False

    for i in range(len(pistas)):
        print(f"Pista {i + 1}: {pistas[i]}")
        respuesta = input("¿Quién crees que es? ").strip().lower()
        intentos += 1

        if respuesta == "salir":
            print(f"Te rendiste. El personaje era: {personaje['nombre']}")
            adivinado = True 
            break
        elif respuesta == personaje['nombre'].lower():
            puntos += 10
            puntaje_total += puntos
            print(f"¡Correcto! Era {personaje['nombre']}. Lo lograste en {intentos} intento(s).")
            print(f"Ganaste {puntos} puntos. Puntaje total: {puntaje_total}")
            adivinado = True
            break
        else:
            print("No es correcto.")
            if i < len(pistas) - 1:
                print("Te daré otra pista...\n")
            else:
                print("No quedan más pistas.\n")

    if not adivinado:
        print(f"No lograste adivinar. El personaje era: {personaje['nombre']}")

    jugar_otra = input("\n¿Deseas jugar otra vez? (si/no): ").strip().lower()
    if jugar_otra != "si":
        print(f"\nGracias por jugar. Tu puntaje final fue: {puntaje_total} puntos.")
        break
