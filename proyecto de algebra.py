def sumar_vectores(v1, v2):
    return [a + b for a, b in zip(v1, v2)]

def restar_vectores(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def producto_escalar(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def multiplicar_escalar_vector(escalar, v):
    return [escalar * x for x in v]

def pedir_vector(n):
    """Pide al usuario ingresar un vector de dimensión n"""
    vector = []
    for i in range(n):
        valor = float(input(f"Ingrese el valor {i+1} del vector: "))
        vector.append(valor)
    return vector

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Operaciones con 2 vectores")
        print("2. Operaciones con 3 vectores")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            dimension = int(input("Ingrese la dimensión de los vectores (ejemplo: 2, 3, 4...): "))
            v1 = pedir_vector(dimension)
            v2 = pedir_vector(dimension)

            print("\n--- Operaciones con 2 vectores ---")
            print("1. Suma")
            print("2. Resta")
            print("3. Producto escalar")
            print("4. Multiplicar un escalar por un vector")
            op = input("Elija operación: ")

            if op == "1":
                print("Resultado:", sumar_vectores(v1, v2))
            elif op == "2":
                print("Resultado:", restar_vectores(v1, v2))
            elif op == "3":
                print("Resultado:", producto_escalar(v1, v2))
            elif op == "4":
                escalar = float(input("Ingrese el escalar: "))
                print("Escalar * v1:", multiplicar_escalar_vector(escalar, v1))
                print("Escalar * v2:", multiplicar_escalar_vector(escalar, v2))
            else:
                print("Opción inválida.")

        elif opcion == "2":
            dimension = int(input("Ingrese la dimensión de los vectores (ejemplo: 2, 3, 4...): "))
            v1 = pedir_vector(dimension)
            v2 = pedir_vector(dimension)
            v3 = pedir_vector(dimension)

            print("\n--- Operaciones con 3 vectores ---")
            print("1. Suma (v1 + v2 + v3)")
            print("2. Resta (v1 - v2 - v3)")
            print("3. Producto escalar combinado (v1·v2 + v2·v3 + v1·v3)")
            print("4. Multiplicar escalar por cada vector")
            op = input("Elija operación: ")

            if op == "1":
                print("Resultado:", sumar_vectores(sumar_vectores(v1, v2), v3))
            elif op == "2":
                print("Resultado:", restar_vectores(restar_vectores(v1, v2), v3))
            elif op == "3":
                total = producto_escalar(v1, v2) + producto_escalar(v2, v3) + producto_escalar(v1, v3)
                print("Resultado:", total)
            elif op == "4":
                escalar = float(input("Ingrese el escalar: "))
                print("Escalar * v1:", multiplicar_escalar_vector(escalar, v1))
                print("Escalar * v2:", multiplicar_escalar_vector(escalar, v2))
                print("Escalar * v3:", multiplicar_escalar_vector(escalar, v3))
            else:
                print("Opción inválida.")

        elif opcion == "3":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida, intente de nuevo.")



menu()
