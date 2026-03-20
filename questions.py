import random
import string

words = {
    "programa": [
        "python",
        "programa",
    ],
    "estructuras_de_control": [ 
        "funcion",
        "bucle",
    ],
    "tipos_de_datos": [
        "variable",
        "cadena",
        "entero",
        "lista",
    ]
}

next_round = True
while next_round:
    category = words[input(f"Elija una categoria: {"\n".join(list(words.keys()))} \n")]
    chosen_category = random.sample(category, len(category))
    for word in chosen_category:
        guessed = []
        attempts = 6

        print("¡Bienvenido al Ahorcado!")
        print()

        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)

            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                print("¡Ganaste!")
                break

            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")

            letter = input("Ingresá una letra: ").lower()

            if len(letter) != 1 or letter not in string.ascii_lowercase:
                print("Entrada no válida.")
                continue
            if letter in guessed:
             print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")

            print()
        else:
            print(f"¡Perdiste! La palabra era: {word}")
        print(f"El puntaje es {attempts}")
    next_round = "s" == input("¿Quiere jugar otra ronda? s/n:" )
else:
    print("Fin del juego")