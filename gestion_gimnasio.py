def registrar_socio(socios, siguiente_id):
    """Pide los datos de un socio nuevo y lo agrega a la lista."""
    nombre = input("Nombre: ")
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return siguiente_id

    # Correccion: usamos .strip() para sacar espacios de mas
    dni = input("DNI: ").strip()
    if dni == "":
        print("El DNI no puede estar vacio.")
        return siguiente_id

    for socio in socios:
        if socio["dni"] == dni:
            print("Ya existe un socio con ese DNI. No se registro.")
            return siguiente_id

    socio = {"id": siguiente_id, "nombre": nombre, "dni": dni}
    socios.append(socio)
    print(f"Socio registrado con ID {siguiente_id}.")
    return siguiente_id + 1


def buscar_socio_por_id(socios, id_socio):
    """Busca un socio por su ID."""
    for socio in socios:
        if socio["id"] == id_socio:
            return socio
    return None


def listar_socios(socios):
    """Muestra todos los socios registrados."""
    print("--- Socios ---")
    if len(socios) == 0:
        print("Todavia no hay socios registrados.")
        return

    for socio in socios:
        print("ID", socio["id"], "-", socio["nombre"], "-", socio["dni"])


def buscar_socio(socios):
    """Pide un ID y muestra el socio encontrado."""
    # NOTA: aca esta el bug de esta etapa (input() sin convertir a int)
    id_socio = input("ID del socio a buscar: ")
    socio = buscar_socio_por_id(socios, id_socio)
    if socio is None:
        print("No se encontro ningun socio con ese ID.")
    else:
        print("Encontrado:", socio["nombre"], "-", socio["dni"])


def main():
    socios = []
    siguiente_id = 1

    while True:
        print("\n===== GESTION DE GIMNASIO =====")
        print("1. Registrar socio")
        print("2. Ver socios")
        print("3. Buscar socio por ID")
        print("4. Salir")
        opcion = input("Elegi una opcion: ")

        if opcion not in ("1", "2", "3", "4"):
            print("Opcion invalida.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            siguiente_id = registrar_socio(socios, siguiente_id)
        elif opcion == 2:
            listar_socios(socios)
        elif opcion == 3:
            buscar_socio(socios)
        elif opcion == 4:
            print("Chau!")
            break


main()