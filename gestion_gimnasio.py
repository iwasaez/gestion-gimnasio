"""
Sistema de Gestión de Gimnasio
Trabajo Final Integrador - Laboratorio de Python
Grupo B24

Descripción:
Sistema por consola que permite administrar socios de un gimnasio:
registro de socios, control de cuotas, inscripción a actividades,
control de asistencia y estadísticas básicas de concurrencia.

Estructuras utilizadas: condicionales, repetitivas (while/for), funciones,
validaciones, acumuladores y contadores, y manejo básico de errores.
"""

import datetime

# =========================================================
# DATOS "FIJOS" DEL SISTEMA (no cambian durante la ejecución)
# =========================================================

ACTIVIDADES_DISPONIBLES = ["Musculación", "Spinning", "Funcional", "Yoga", "Crossfit"]

# Tipos de membresía y su costo mensual (esto cubre "promociones/tipos de membresía")
MEMBRESIAS = {
    "Básica": 8000,
    "Full": 12000,
    "Estudiante": 6000
}


# =========================================================
# FUNCIONES DE VALIDACIÓN (reutilizables en todo el sistema)
# =========================================================

def pedir_entero(mensaje, minimo=None, maximo=None):
    """
    Pide un número entero por consola y no continúa hasta que sea válido.
    Usa try/except para manejar errores de tipo (manejo de errores).
    """
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"  ⚠ El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ⚠ El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ⚠ Debés ingresar un número entero válido.")


def pedir_texto_no_vacio(mensaje):
    """Pide un texto y valida que no esté vacío ni sean solo espacios."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("  ⚠ El campo no puede estar vacío.")
        else:
            return texto


def pedir_dni(mensaje):
    """Pide un DNI y valida que sean solo dígitos."""
    while True:
        dni = input(mensaje).strip()
        if dni.isdigit() and len(dni) >= 6:
            return dni
        print("  ⚠ Ingresá un DNI válido (solo números, al menos 6 dígitos).")


# =========================================================
# FUNCIONES SOBRE SOCIOS
# =========================================================

def buscar_socio_por_id(socios, id_socio):
    """
    Recorre la lista de socios y devuelve el socio con ese id, o None
    si no lo encuentra. Función reutilizada por varias operaciones
    (modularización: evita repetir el mismo bucle en cada función).
    """
    for socio in socios:
        if socio["id"] == id_socio:
            return socio
    return None


def elegir_membresia():
    """Muestra las membresías disponibles y valida la elección del usuario."""
    print("\nMembresías disponibles:")
    opciones = list(MEMBRESIAS.items())
    for i, (nombre, precio) in enumerate(opciones, start=1):
        print(f"  {i}. {nombre} - ${precio}")

    opcion = pedir_entero("Elegí una membresía (número): ", 1, len(opciones))
    nombre_membresia, precio = opciones[opcion - 1]
    return nombre_membresia, precio


def registrar_socio(socios, siguiente_id):
    """Da de alta un nuevo socio y lo agrega a la lista de socios."""
    print("\n--- Registrar nuevo socio ---")
    nombre = pedir_texto_no_vacio("Nombre y apellido: ")
    dni = pedir_dni("DNI: ")

    # Validación: que no exista ya un socio con ese DNI
    for socio in socios:
        if socio["dni"] == dni:
            print("  ⚠ Ya existe un socio registrado con ese DNI. No se registró.")
            return siguiente_id

    membresia, precio = elegir_membresia()

    nuevo_socio = {
        "id": siguiente_id,
        "nombre": nombre,
        "dni": dni,
        "membresia": membresia,
        "precio_membresia": precio,
        "cuota_pagada": False,
        "actividades": [],
        "asistencias": 0
    }
    socios.append(nuevo_socio)
    print(f"  ✔ Socio registrado con éxito. ID asignado: {siguiente_id}")
    return siguiente_id + 1  # el próximo socio tendrá un id distinto


def listar_socios(socios):
    """Muestra todos los socios registrados. Usa un contador para enumerarlos."""
    print("\n--- Listado de socios ---")
    if len(socios) == 0:
        print("  No hay socios registrados todavía.")
        return

    contador = 0  # contador simple de socios mostrados
    for socio in socios:
        contador += 1
        estado_cuota = "Al día" if socio["cuota_pagada"] else "Pendiente"
        actividades = ", ".join(socio["actividades"]) if socio["actividades"] else "Ninguna"
        print(f"  {contador}. ID {socio['id']} - {socio['nombre']} (DNI {socio['dni']})")
        print(f"     Membresía: {socio['membresia']} | Cuota: {estado_cuota}")
        print(f"     Actividades: {actividades} | Asistencias: {socio['asistencias']}")
    print(f"  Total de socios: {contador}")


# =========================================================
# FUNCIONES DE CUOTAS
# =========================================================

def registrar_pago(socios, total_recaudado, total_pagos):
    """
    Registra el pago de la cuota de un socio.
    total_recaudado y total_pagos son acumulador y contador que se
    van sumando a lo largo de toda la ejecución del programa.
    """
    print("\n--- Registrar pago de cuota ---")
    id_socio = pedir_entero("ID del socio: ", 1)
    socio = buscar_socio_por_id(socios, id_socio)

    if socio is None:
        print("  ⚠ No existe un socio con ese ID.")
        return total_recaudado, total_pagos

    if socio["cuota_pagada"]:
        print(f"  ⚠ {socio['nombre']} ya tiene la cuota de este mes al día.")
        return total_recaudado, total_pagos

    socio["cuota_pagada"] = True
    total_recaudado += socio["precio_membresia"]  # acumulador de dinero
    total_pagos += 1  # contador de pagos realizados
    print(f"  ✔ Pago registrado: ${socio['precio_membresia']} ({socio['membresia']}).")
    return total_recaudado, total_pagos


# =========================================================
# FUNCIONES DE ACTIVIDADES Y ASISTENCIA
# =========================================================

def inscribir_actividad(socios):
    """Inscribe a un socio existente en una actividad del gimnasio."""
    print("\n--- Inscribir a una actividad ---")
    id_socio = pedir_entero("ID del socio: ", 1)
    socio = buscar_socio_por_id(socios, id_socio)

    if socio is None:
        print("  ⚠ No existe un socio con ese ID.")
        return

    print("Actividades disponibles:")
    for i, actividad in enumerate(ACTIVIDADES_DISPONIBLES, start=1):
        print(f"  {i}. {actividad}")

    opcion = pedir_entero("Elegí una actividad (número): ", 1, len(ACTIVIDADES_DISPONIBLES))
    actividad_elegida = ACTIVIDADES_DISPONIBLES[opcion - 1]

    if actividad_elegida in socio["actividades"]:
        print(f"  ⚠ {socio['nombre']} ya está inscripto en {actividad_elegida}.")
    else:
        socio["actividades"].append(actividad_elegida)
        print(f"  ✔ {socio['nombre']} fue inscripto en {actividad_elegida}.")


def registrar_asistencia(socios, asistencia_por_actividad):
    """
    Registra la asistencia de un socio a una actividad puntual.
    asistencia_por_actividad es un diccionario contador: cuenta cuántas
    veces se asistió a cada actividad (para las estadísticas).
    """
    print("\n--- Registrar asistencia ---")
    id_socio = pedir_entero("ID del socio: ", 1)
    socio = buscar_socio_por_id(socios, id_socio)

    if socio is None:
        print("  ⚠ No existe un socio con ese ID.")
        return

    if not socio["actividades"]:
        print(f"  ⚠ {socio['nombre']} no está inscripto en ninguna actividad.")
        return

    print("¿A qué actividad asistió?")
    for i, actividad in enumerate(socio["actividades"], start=1):
        print(f"  {i}. {actividad}")

    opcion = pedir_entero("Elegí una opción: ", 1, len(socio["actividades"]))
    actividad_elegida = socio["actividades"][opcion - 1]

    socio["asistencias"] += 1  # contador individual del socio
    asistencia_por_actividad[actividad_elegida] = asistencia_por_actividad.get(actividad_elegida, 0) + 1

    fecha_hoy = datetime.date.today().strftime("%d/%m/%Y")
    print(f"  ✔ Asistencia registrada: {socio['nombre']} - {actividad_elegida} ({fecha_hoy}).")


# =========================================================
# ESTADÍSTICAS
# =========================================================

def mostrar_estadisticas(socios, total_recaudado, total_pagos, asistencia_por_actividad):
    """Muestra un resumen general del gimnasio usando los acumuladores del sistema."""
    print("\n--- Estadísticas del gimnasio ---")
    total_socios = len(socios)
    print(f"  Total de socios registrados: {total_socios}")

    if total_socios == 0:
        print("  No hay más estadísticas disponibles aún.")
        return

    # Contadores de cuotas al día / pendientes
    al_dia = 0
    pendientes = 0
    for socio in socios:
        if socio["cuota_pagada"]:
            al_dia += 1
        else:
            pendientes += 1

    print(f"  Cuotas al día: {al_dia} | Cuotas pendientes: {pendientes}")
    print(f"  Total recaudado este período: ${total_recaudado}")
    print(f"  Cantidad de pagos registrados: {total_pagos}")

    # Actividad más elegida según inscripciones (contador con diccionario)
    conteo_inscripciones = {}
    for socio in socios:
        for actividad in socio["actividades"]:
            conteo_inscripciones[actividad] = conteo_inscripciones.get(actividad, 0) + 1

    if conteo_inscripciones:
        actividad_top = max(conteo_inscripciones, key=conteo_inscripciones.get)
        print(f"  Actividad con más inscriptos: {actividad_top} ({conteo_inscripciones[actividad_top]} socios)")
    else:
        print("  Todavía no hay inscripciones a actividades.")

    # Concurrencia real (asistencias registradas) por actividad
    if asistencia_por_actividad:
        print("  Asistencias registradas por actividad:")
        for actividad, cantidad in asistencia_por_actividad.items():
            print(f"     - {actividad}: {cantidad}")
    else:
        print("  Todavía no se registraron asistencias.")


# =========================================================
# MENÚ PRINCIPAL
# =========================================================

def mostrar_menu():
    print("\n===== GESTIÓN DE GIMNASIO =====")
    print("1. Registrar socio")
    print("2. Ver listado de socios")
    print("3. Registrar pago de cuota")
    print("4. Inscribir socio a una actividad")
    print("5. Registrar asistencia")
    print("6. Ver estadísticas")
    print("7. Salir")


def main():
    socios = []
    siguiente_id = 1

    # Acumulador y contador globales de la sesión
    total_recaudado = 0
    total_pagos = 0
    asistencia_por_actividad = {}  # contador por actividad

    while True:
        mostrar_menu()
        opcion = pedir_entero("Elegí una opción: ", 1, 7)

        if opcion == 1:
            siguiente_id = registrar_socio(socios, siguiente_id)
        elif opcion == 2:
            listar_socios(socios)
        elif opcion == 3:
            total_recaudado, total_pagos = registrar_pago(socios, total_recaudado, total_pagos)
        elif opcion == 4:
            inscribir_actividad(socios)
        elif opcion == 5:
            registrar_asistencia(socios, asistencia_por_actividad)
        elif opcion == 6:
            mostrar_estadisticas(socios, total_recaudado, total_pagos, asistencia_por_actividad)
        elif opcion == 7:
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
