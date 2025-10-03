def pedir_vector(dimension):
    vector = []
    for i in range(dimension):
        valor = float(input(f"Ingrese el valor del eje {['X','Y','Z'][i]}: "))
        vector.append(valor)
    return vector

def sumar_vectores(*vectores):
    dimension = len(vectores[0])
    suma = [0]*dimension
    for v in vectores:
        for i in range(dimension):
            suma[i] += v[i]
    return suma

def restar_vectores(*vectores):
    dimension = len(vectores[0])
    resultado = vectores[0].copy()
    for v in vectores[1:]:
        for i in range(dimension):
            resultado[i] -= v[i]
    return resultado

def producto_escalar(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))

def multiplicar_escalar_vector(escalar, v):
    return [escalar*x for x in v]

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Operaciones con vectores 2D")
        print("2. Operaciones con vectores 3D")
        print("3. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1" or opcion == "2":
            dimension = 2 if opcion == "1" else 3
            n = int(input(f"¿Cuántos vectores desea operar? (Máximo 3): "))
            if n < 1 or n > 3:
                print("Debe ingresar entre 1 y 3 vectores.")
                continue

            vectores = []
            for i in range(n):
                print(f"Ingrese vector {i+1}:")
                vectores.append(pedir_vector(dimension))

            print("\n--- Operaciones disponibles ---")
            print("1. Suma de todos los vectores")
            print("2. Resta de todos los vectores")
            print("3. Producto escalar (solo 2 vectores)")
            print("4. Multiplicar vector por un escalar")
            op = input("Elija operación: ")

            if op == "1":
                resultado = sumar_vectores(*vectores)
                print("Resultado de la suma:", resultado)
            elif op == "2":
                resultado = restar_vectores(*vectores)
                print("Resultado de la resta:", resultado)
            elif op == "3":
                if n != 2:
                    print("El producto escalar solo se puede calcular entre 2 vectores.")
                else:
                    resultado = producto_escalar(vectores[0], vectores[1])
                    print("Producto escalar:", resultado)
            elif op == "4":
                escalar = float(input("Ingrese el valor del escalar: "))
                for i, v in enumerate(vectores):
                    print(f"Escalar * vector {i+1}:", multiplicar_escalar_vector(escalar, v))
            else:
                print("Opción inválida.")

        elif opcion == "3":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()
