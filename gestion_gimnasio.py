def registrar_socio(socios):
    """Pide los datos de un socio nuevo y lo agrega a la lista."""
    nombre = input("Nombre: ")
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    dni = input("DNI: ")
    if dni == "":
        print("El DNI no puede estar vacio.")
        return

    # Correccion: ahora si validamos que no exista ya ese DNI
    for socio in socios:
        if socio["dni"] == dni:
            print("Ya existe un socio con ese DNI. No se registro.")
            return

    socio = {"nombre": nombre, "dni": dni}
    socios.append(socio)
    print("Socio registrado.")


def listar_socios(socios):
    """Muestra todos los socios registrados."""
    print("--- Socios ---")
    if len(socios) == 0:
        print("Todavia no hay socios registrados.")
        return

    for socio in socios:
        print(socio["nombre"], "-", socio["dni"])


def main():
    socios = []

    while True:
        print("\n===== GESTION DE GIMNASIO =====")
        print("1. Registrar socio")
        print("2. Ver socios")
        print("3. Salir")
        opcion = input("Elegi una opcion: ")

        if opcion != "1" and opcion != "2" and opcion != "3":
            print("Opcion invalida, elegi 1, 2 o 3.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            registrar_socio(socios)
        elif opcion == 2:
            listar_socios(socios)
        elif opcion == 3:
            print("Chau!")
            break


main()