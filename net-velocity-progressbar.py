import time

def convertir_unidades_datos(cantidad, unidad):
    unidades_datos = {
        "kibibyte": 1,
        "mebibyte": 1024,
        "gibibyte": 1024 ** 2
    }
    return cantidad * unidades_datos[unidad]

def simulador_barra_progreso(velocidad_total, unidad_datos, tiempo_total):
    unidades_datos_ejemplos = ["kibibyte", "mebibyte", "gibibyte"]
    unidades_tiempo_ejemplos = ["segundo", "minuto", "hora", "día"]

    print("Ejemplos de unidades de datos:")
    for unidad in unidades_datos_ejemplos:
        print("1 {} = {} kibibytes".format(unidad, convertir_unidades_datos(1, unidad)))
    print()

    print("Ejemplos de unidades de tiempo:")
    for unidad in unidades_tiempo_ejemplos:
        print("1 {} = {} segundos".format(unidad, convertir_unidades_datos(1, unidad_datos) * tiempo_total))
    print()

    progreso = 0
    datos_transferidos = 0

    while progreso <= tiempo_total:
        porcentaje = (progreso / tiempo_total) * 100
        print("Progreso: [{:10s}] {:.2f}%".format('#' * int(porcentaje / 10), porcentaje))

        datos_transferidos = velocidad_total * progreso
        print("Datos transferidos: {} {}".format(convertir_unidades_datos(datos_transferidos, unidad_datos), unidad_datos))

        progreso += 1

        time.sleep(1)  # Esperar un segundo antes de actualizar el progreso

# Solicitar preferencias al usuario
cantidad = float(input("Ingresa la cantidad de datos: "))
unidad_datos = input("Ingresa la unidad de datos (kibibyte, mebibyte, gibibyte): ")
while unidad_datos not in ["kibibyte", "mebibyte", "gibibyte"]:
    print("Unidad de datos no válida. Intenta de nuevo.")
    unidad_datos = input("Ingresa la unidad de datos (kibibyte, mebibyte, gibibyte): ")
    
tiempo_total = int(input("Ingresa el número total de segundos: "))

# Ejecutar el simulador
simulador_barra_progreso(cantidad, unidad_datos, tiempo_total)