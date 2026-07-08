MEMBRESIAS = {
    "Básica": 8000,
    "Full": 12000,
    "Estudiante": 6000
}


def pedir_entero(mensaje):
    """Pide un numero entero y no continua hasta que sea valido."""
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Tenes que ingresar un numero entero valido.")


def elegir_membresia():
    """Muestra las membresias disponibles y devuelve la elegida."""
    print("Membresias disponibles:")
    opciones = list(MEMBRESIAS.items())
    for i, (nombre, precio) in enumerate(opciones, start=1):
        print(f"  {i}. {nombre} - ${precio}")
    opcion = pedir_entero("Elegi una membresia: ")
    nombre_membresia, precio = opciones[opcion - 1]
    return nombre_membresia, precio


def registrar_socio(socios, siguiente_id):
    """Pide los datos de un socio nuevo y lo agrega a la lista."""
    nombre = input("Nombre: ")
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return siguiente_id  # Correccion: ya no avanza el id si falla

    dni = input("DNI: ").strip()
    if dni == "":
        print("El DNI no puede estar vacio.")
        return siguiente_id  # Correccion: ya no avanza el id si falla

    for socio in socios:
        if socio["dni"] == dni:
            print("Ya existe un socio con ese DNI. No se registro.")
            return siguiente_id  # Correccion: ya no avanza el id si falla

    membresia, precio = elegir_membresia()

    socio = {
        "id": siguiente_id,
        "nombre": nombre,
        "dni": dni,
        "membresia": membresia,
        "precio_membresia": precio,
        "cuota_pagada": False,
    }
    socios.append(socio)
    print(f"Socio registrado con ID {siguiente_id}.")
    return siguiente_id + 1  # ahora si avanza solo cuando funciono


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
        estado = "Al dia" if socio["cuota_pagada"] else "Pendiente"
        print("ID", socio["id"], "-", socio["nombre"], "- Cuota:", estado)


def registrar_pago(socios, total_recaudado, total_pagos):
    """Registra el pago de la cuota de un socio."""
    
    id_socio = pedir_entero("ID del socio: ")
    socio = buscar_socio_por_id(socios, id_socio)

    if socio is None:
        print("No existe un socio con ese ID.")
        return total_recaudado, total_pagos

    socio["cuota_pagada"] = True
    total_recaudado += socio["precio_membresia"]
    total_pagos += 1
    print(f"Pago registrado: ${socio['precio_membresia']}.")
    return total_recaudado, total_pagos


def main():
    socios = []
    siguiente_id = 1
    total_recaudado = 0
    total_pagos = 0

    while True:
        print("\n===== GESTION DE GIMNASIO =====")
        print("1. Registrar socio")
        print("2. Ver socios")
        print("3. Registrar pago de cuota")
        print("4. Salir")
        opcion = pedir_entero("Elegi una opcion: ")

        if opcion == 1:
            siguiente_id = registrar_socio(socios, siguiente_id)
        elif opcion == 2:
            listar_socios(socios)
        elif opcion == 3:
            total_recaudado, total_pagos = registrar_pago(socios, total_recaudado, total_pagos)
        elif opcion == 4:
            print(f"Total recaudado: ${total_recaudado} en {total_pagos} pagos. Chau!")
            break
        else:
            print("Opcion invalida.")


main()