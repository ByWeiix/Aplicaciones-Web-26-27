import random

num_adivinar = random.randint(1, 10)

val = int(input("Introduce un valor entre 1 y 10: "))

if val == num_adivinar:
    print("Has adivinadoooo")
elif num_adivinar > val:
    print("El numero es mas alto. Te queda 2 intento")
    val = int(input("Introduce un valor entre 1 y 10: "))

    if val == num_adivinar:
        print("Has adivinadoooo")
    elif num_adivinar > val:
        print("El numero es mas alto. Te queda 1 intento")
        val = int(input("Introduce un valor entre 1 y 10: "))

        if val == num_adivinar:
            print("Has adivinadoooo")
        elif num_adivinar > val:
            print(f"El numero era mas alto. Te queda 0 intento. El numero era {num_adivinar}")
        else:
            print(f"El numero era mas bajo. Te queda 0 intento. El numero era {num_adivinar}")
    else:
        print("El numero es mas bajo. Te queda 1 intento")
        val = int(input("Introduce un valor entre 1 y 10: "))

        if val == num_adivinar:
            print("Has adivinadoooo")
        elif num_adivinar > val:
            print(f"El numero era mas alto. Te queda 0 intento. El numero era {num_adivinar}")
        else:
            print(f"El numero era mas bajo. Te queda 0 intento. El numero era {num_adivinar}")
else:
    print("El numero es mas bajo. Te queda 2 intento")
    val = int(input("Introduce un valor entre 1 y 10: "))

    if val == num_adivinar:
        print("Has adivinadoooo")
    elif num_adivinar > val:
        print("El numero es mas alto. Te queda 1 intento")
        val = int(input("Introduce un valor entre 1 y 10: "))

        if val == num_adivinar:
            print("Has adivinadoooo")
        elif num_adivinar > val:
            print(f"El numero era mas alto. Te queda 0 intento. El numero era {num_adivinar}")
        else:
            print(f"El numero era mas bajo. Te queda 0 intento. El numero era {num_adivinar}")
    else:
        print("El numero es mas bajo. Te queda 1 intento")
        val = int(input("Introduce un valor entre 1 y 10: "))

        if val == num_adivinar:
            print("Has adivinadoooo")
        elif num_adivinar > val:
            print(f"El numero era mas alto. Te queda 0 intento. El numero era {num_adivinar}")
        else:
            print(f"El numero era mas bajo. Te queda 0 intento. El numero era {num_adivinar}")