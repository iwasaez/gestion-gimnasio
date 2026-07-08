# Gestión de Gimnasio - Trabajo Final Integrador

## Integrantes del grupo
- Sáez, Iván Walter Agustín (Legajo: 25672)
- Escobar, Nélida María Luz (Legajo: 26670)
- Passarello, Julián (Legajo: 30309)

## Comisión
- Comisión B - Grupo B24

## Descripción general del sistema
Sistema por consola, desarrollado en Python, que permite administrar
un gimnasio: registro de socios, control de cuotas mensuales según el
tipo de membresía (Básica, Full, Estudiante), inscripción a
actividades (Musculación, Spinning, Funcional, Yoga, Crossfit),
registro de asistencia y estadísticas básicas de concurrencia
(cuotas al día/pendientes, total recaudado, actividad más elegida,
asistencias por actividad).

El sistema incluye validaciones de datos (DNI, opciones de menú,
IDs de socio) y manejo de errores mediante try/except para evitar
que el programa se corte ante una entrada inválida.

## Instrucciones de ejecución
1. Tener Python 3 instalado.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:
   ```
   python3 gestion_gimnasio.py
   ```
4. Usar el menú numérico que aparece en pantalla para navegar entre
   las opciones (registrar socio, ver socios, registrar pago, etc.).

## Uso de Inteligencia Artificial
Se utilizó Claude (Anthropic) como herramienta de apoyo puntual para:
- Resolver dudas de sintaxis de Python (por ejemplo, cómo usar try/except o diccionarios).
- Sugerir mensajes de error más claros para el usuario.
- Detectar errores concretos durante las pruebas (bugs) y explicar por qué pasaban.

El diseño de la solución, la lógica del sistema, las decisiones sobre
qué validaciones y estructuras usar, y las pruebas de funcionamiento
fueron trabajadas y comprendidas por el equipo. La IA funcionó como
consulta de apoyo, similar a buscar en documentación o foros, pero el
razonamiento y las decisiones finales fueron del grupo.
