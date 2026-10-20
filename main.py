#función donde se abre y se lee el csv
def cargar_datos(nombre_archivo):
    partidos = []

    with open(nombre_archivo, "r", encoding="utf-8-sig") as archivo:
        encabezados = archivo.readline().strip().split(";")

        for linea in archivo:
            datos = linea.strip().split(";")

            if len(datos) == len(encabezados):
                partido = {}

                for i in range(len(encabezados)):
                    partido[encabezados[i].strip()] = datos[i].strip()

                partidos.append(partido)

    return partidos


#función para buscar los registros acorde a lo que ingresa el usuario, ignorando mayusculas o minusculas
def buscar_registros(partidos, termino):
    encontrados = []
    termino = termino.lower().strip()

    for partido in partidos:
        local = partido.get(
            "Home Team", partido.get("HomeTeam", "")
        )
        visitante = partido.get(
            "AwayTeam", partido.get("Away Team", "")
        )

        if termino in local.lower() or termino in visitante.lower():
            encontrados.append(partido)

    return encontrados


#funcion donde se calculan las estadisticas, máximo, minimo, promedio y datos adicionales necesarios para el análisis futbolístico
def calcular_estadisticas(partidos, campo):
    valores = []

    for partido in partidos:
        valor = partido.get(campo, "")
    #se trasforman los datos a float para poder operar con ellos
        try:
            numero = float(valor)
            valores.append(numero)
        except ValueError:
            continue

    if len(valores) == 0:
        return None

    mayor = valores[0]
    menor = valores[0]
    suma = 0

    for numero in valores:
        if numero > mayor:
            mayor = numero

        if numero < menor:
            menor = numero

        suma = suma + numero

    promedio = suma / len(valores)

    return mayor, menor, promedio


#funcion adicional propia, donde se filtran partidos con mayor cantidad de goles a las que introduce el usuario
def filtrar_por_goles(partidos, minimo):
    encontrados = []

    for partido in partidos:
        try:
            goles_local = int(partido["FTHG"])
            goles_visitante = int(partido["FTAG"])
        except (ValueError, KeyError):
            continue

        total_goles = goles_local + goles_visitante

        if total_goles >= minimo:
            encontrados.append(partido)

    return encontrados


#funcion que genera el informe con las estadisticas de un equipo introducido por el usuario durante toda la temporada
def informe_equipo(partidos, equipo_buscado):
    partidos_jugados = 0
    victorias = 0
    empates = 0
    derrotas = 0
    goles_favor = 0
    goles_contra = 0

    for partido in partidos:
        local = partido.get(
            "Home Team", partido.get("HomeTeam", "")
        )
        visitante = partido.get(
            "AwayTeam", partido.get("Away Team", "")
        )

        es_local = local.lower() == equipo_buscado.lower()
        es_visitante = visitante.lower() == equipo_buscado.lower()

        if not es_local and not es_visitante:
            continue

        try:
            goles_local = int(partido["FTHG"])
            goles_visitante = int(partido["FTAG"])
        except (ValueError, KeyError):
            continue

        if es_local:
            goles_favor_partido = goles_local
            goles_contra_partido = goles_visitante
        else:
            goles_favor_partido = goles_visitante
            goles_contra_partido = goles_local

        partidos_jugados += 1
        goles_favor += goles_favor_partido
        goles_contra += goles_contra_partido

        if goles_favor_partido > goles_contra_partido:
            victorias += 1
        elif goles_favor_partido == goles_contra_partido:
            empates += 1
        else:
            derrotas += 1

    if partidos_jugados == 0:
        return None

    diferencia = goles_favor - goles_contra
    promedio = goles_favor / partidos_jugados
    porcentaje_victorias = victorias / partidos_jugados * 100
    puntos = victorias * 3 + empates
    #retorna todos los datos para ser usados mas adelante
    return {
        "partidos": partidos_jugados,
        "victorias": victorias,
        "empates": empates,
        "derrotas": derrotas,
        "goles_favor": goles_favor,
        "goles_contra": goles_contra,
        "diferencia": diferencia,
        "promedio": promedio,
        "porcentaje_victorias": porcentaje_victorias,
        "puntos": puntos
    }


#función que compara el rendimiento de dos equipos teniendo en cuenta sus estadísticas
def comparar_equipos(partidos, equipo1, equipo2):
    informe1 = informe_equipo(partidos, equipo1)
    informe2 = informe_equipo(partidos, equipo2)

    if informe1 is None or informe2 is None:
        return None

    comparacion = {
        "equipo1": equipo1,
        "equipo2": equipo2,
        "puntos1": informe1["puntos"],
        "puntos2": informe2["puntos"],
        "goles1": informe1["goles_favor"],
        "goles2": informe2["goles_favor"],
        "victorias1": informe1["victorias"],
        "victorias2": informe2["victorias"],
        "porcentaje1": informe1["porcentaje_victorias"],
        "porcentaje2": informe2["porcentaje_victorias"]
    }

    return comparacion


#función principal del menú
def mostrar_menu(partidos):
    while True:
        print("\n" + "-" * 40)
        print("       FOOTLAB SCOUT & DETECTIVE")
        print("-" * 40)
        print("[ SCOUT ]")
        print("1. Buscar partidos por equipo")
        print("2. Consultar estadisticas")
        print("3. Informe completo de equipo")
        print()
        print("[ DETECTIVE ]")
        print("4. Filtrar partidos por goles")
        print("5. Comparar dos equipos")
        print("6. Salir")
        print("-" * 40)

        opcion = input("Elige una opción: ")
        #opcion 1 del menu, registro de partidos de un equipo, la funcion puede buscar equipos por semejanza de caracteres, por ejemplo, si se introduce "Bar", buscará los resultados del barcelona, o en caso de escribir "Ath" buscará los resultados tanto de Ath Bilbao como Ath Madrid
        if opcion == "1":
            termino = input("Equipo que quieres buscar: ")
            resultados = buscar_registros(partidos, termino)

            print("Registros encontrados:", len(resultados))

            for partido in resultados:
                print(
                    partido.get("Home Team", partido.get("HomeTeam", "?")),
                    partido.get("FTHG", "?"),
                    "-",
                    partido.get("FTAG", "?"),
                    partido.get("AwayTeam", partido.get("Away Team", "?"))
                )
        #opcion 2 del menu, estadísticas
        elif opcion == "2":
            campo = input(
                "Campo numérico (por ejemplo, FTHG, FTAG o HS) (Más opciones en el glosario): "
            )

            estadisticas = calcular_estadisticas(partidos, campo)

            if estadisticas is None:
                print("No se encontraron valores numéricos para ese campo.")
            else:
                mayor, menor, promedio = estadisticas
                print("Máximo:", mayor)
                print("Mínimo:", menor)
                print("Promedio:", round(promedio, 2))
        #opcion 3, aqui si se debe poner el nombre exacto del equipo, listado de equipos en el glosario
        elif opcion == "3":
            equipo = input("Nombre exacto del equipo: ")
            informe = informe_equipo(partidos, equipo)

            if informe is None:
                print("No se encontraron partidos para ese equipo.")
            else:
                print("\n--- INFORME DEL EQUIPO ---")
                print("Equipo:", equipo)
                print("Partidos jugados:", informe["partidos"])
                print("Victorias:", informe["victorias"])
                print("Empates:", informe["empates"])
                print("Derrotas:", informe["derrotas"])
                print("Puntos:", informe["puntos"])
                print("Goles a favor:", informe["goles_favor"])
                print("Goles en contra:", informe["goles_contra"])
                print("Diferencia de goles:", informe["diferencia"])
                print("Promedio de goles:", round(informe["promedio"], 2))
                print(
                    "Porcentaje de victorias:",
                    round(informe["porcentaje_victorias"], 2),
                    "%"
                )
        #opcion 4 del menú, filtro de partidos con mayor cantidad de goles a la introducida
        elif opcion == "4":
            try:
                minimo = int(input("Mínimo de goles totales: "))
                resultados = filtrar_por_goles(partidos, minimo)

                print("Partidos encontrados:", len(resultados))

                for partido in resultados:
                    print(
                        partido.get("Home Team", partido.get("HomeTeam", "?")),
                        partido.get("FTHG", "?"),
                        "-",
                        partido.get("FTAG", "?"),
                        partido.get("AwayTeam", partido.get("Away Team", "?"))
                    )

            except ValueError:
                print("Debes escribir un número entero.")

        #opcion 5, comparador de equipos
        elif opcion == "5":
            equipo1 = input("Primer equipo: ")
            equipo2 = input("Segundo equipo: ")

            comparacion = comparar_equipos(
                partidos, equipo1, equipo2
            )

            if comparacion is None:
                print("No se encontraron datos de uno o ambos equipos.")
            else:
                print("\n--- COMPARACION DE EQUIPOS ---")
                print(
                    comparacion["equipo1"],
                    "vs",
                    comparacion["equipo2"]
                )

                print("\nPuntos:")
                print(comparacion["equipo1"] + ":",
                      comparacion["puntos1"])
                print(comparacion["equipo2"] + ":",
                      comparacion["puntos2"])

                print("\nGoles a favor:")
                print(comparacion["equipo1"] + ":",
                      comparacion["goles1"])
                print(comparacion["equipo2"] + ":",
                      comparacion["goles2"])

                print("\nVictorias:")
                print(comparacion["equipo1"] + ":",
                      comparacion["victorias1"])
                print(comparacion["equipo2"] + ":",
                      comparacion["victorias2"])

                print("\nPorcentaje de victorias:")
                print(comparacion["equipo1"] + ":",
                      round(comparacion["porcentaje1"], 2), "%")
                print(comparacion["equipo2"] + ":",
                      round(comparacion["porcentaje2"], 2), "%")
        #opcion 6, cerrar el programa con un break
        elif opcion == "6":
            print("Gracias por usar FOOTLAB.")
            break


        else:
            print("Opción no válida. Intenta nuevamente.")


#pantalla inicial de presentación del programa FOOTLAB, usando .center para centrar el texto
partidos = cargar_datos("laliga.csv")
print()
print("*" * 48)
print("*" + " " * 46 + "*")
print("*" + "   FOOTLAB SCOUT & DETECTIVE".center(46) + "*")
print("*" + " " * 46 + "*")
print("*" + "  TU FUTBOL. TUS DATOS. TUS DESCUBRIMIENTOS.".center(46) + "*")
print("*" + " " * 46 + "*")
print("*" * 48)

print()
print("  COMPETICION:", "LaLiga espanola 2024/25")
print("  PARTIDOS CARGADOS:", len(partidos))
print()
print("  Sistema de exploracion y analisis futbolistico")
print()

mostrar_menu(partidos)
