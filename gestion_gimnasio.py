nombres = []
dnis = []

while True:
    print("\n===== GESTION DE GIMNASIO =====")
    print("1. Registrar socio")
    print("2. Ver socios")
    print("3. Salir")
    opcion = input("Elegi una opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        nombres.append(nombre)
        dnis.append(dni)
        print("Socio registrado.")

    elif opcion == 2:
        print("--- Socios ---")
        i = 0
        while i < len(nombres):
            print(nombres[i], "-", dnis[i])
            i = i + 1

    elif opcion == 3:
        print("Chau!")
        break

    else:
        print("Opcion invalida")
