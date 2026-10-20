# FOOTLAB Scout & Detective

## Descripción

FOOTLAB Scout & Detective es una aplicación de consola desarrollada en Python que permite explorar y analizar resultados de partidos de LaLiga española 2024/25 mediante un archivo CSV.

El proyecto combina dos enfoques: **Scout**, orientado a consultar información y estadísticas de los equipos, y **Detective**, enfocado en encontrar partidos con determinadas características y comparar el rendimiento de los clubes.

## Objetivo

Aplicar los fundamentos de programación en Python para cargar, organizar, consultar y analizar datos reales de fútbol.

## Funcionalidades

### Scout

- **Búsqueda de partidos:** permite buscar encuentros por el nombre de un equipo.
- **Estadísticas numéricas:** calcula el valor máximo, mínimo y promedio de un campo numérico.
- **Informe de equipo:** presenta partidos jugados, victorias, empates, derrotas, puntos, goles a favor, goles en contra, diferencia de goles, promedio de goles y porcentaje de victorias.

#### Glosario de la opción 2: Consultar estadísticas

- **Máximo:** valor más alto encontrado.
- **Mínimo:** valor más bajo encontrado.
- **Promedio:** suma de los valores dividida entre la cantidad de datos válidos.
- **FTHG:** goles del equipo local.
- **FTAG:** goles del equipo visitante.
- **HS:** remates del equipo local, si este campo está presente en el CSV.

#### Glosario de equipos: nombres exactos de los equipos incluidos para buscarlos, en negrita el nombre exacto de cada equipo dentro del programa
-**Alaves:** Deportivo Alavés
-**Ath Bilbao:** Athletic Club de Bilbao
-**Ath Madrid:** Club Atlético de Madrid
-**Barcelona:** F.C. Barcelona
-**Celta:** R.C. Celta de Vigo
-**Espanol:** R.C.D. Espanyol de Barcelona
-**Getafe:** Getafe C.F.
-**Girona:** Girona F.C.
-**Las Palmas:** U.D. Las Palmas
-**Leganes:** C.D. Leganés
-**Mallorca:** R.C.D. Mallorca
-**Osasuna:** C.A. Osasuna
-**Vallecano:** Rayo Vallecano
-**Betis:** Real Betis Balompié
-**Real Madrid:** Real Madrid C.F.
-**Sociedad:** Real Sociedad
-**Valladolid:** Real Valladolid C.F.
-**Sevilla:** Sevilla F.C.
-**Valencia:** Valencia C.F.
-**Villarreal:** Villarreal C.F.

### Detective

- **Filtro por goles:** encuentra partidos con una cantidad de goles totales igual o superior al mínimo introducido por el usuario.
- **Comparación de equipos:** compara los puntos, goles a favor, victorias y porcentajes de victorias de dos equipos.

La aplicación también incluye un menú interactivo para seleccionar las operaciones y salir del programa.

## Tecnologías y conceptos utilizados

- Python 3.
- Lectura y procesamiento de archivos CSV mediante herramientas estándar de Python.
- Variables, cadenas de texto y conversión de tipos.
- Listas y diccionarios.
- Funciones con parámetros y valores de retorno.
- Condicionales y ciclos.
- Búsqueda y filtrado de registros.
- Manejo de errores mediante excepciones.

El proyecto no requiere bibliotecas externas.

## Requisitos

- Python 3 instalado.
- El archivo `main.py`.
- El archivo de datos `laliga.csv`, ubicado en la misma carpeta que `main.py`.

## Instalación y ejecución

1. Descarga o clona el repositorio.
2. Comprueba que `main.py` y `laliga.csv` estén ubicados en la misma carpeta.
3. Abre una terminal en la carpeta del proyecto.
4. Ejecuta el siguiente comando:

```bash
python3 main.py
```

Si tu sistema utiliza el comando `python`, también puedes ejecutar:

```bash
python main.py
```

Sigue las instrucciones del menú que aparece en la terminal para utilizar las funcionalidades.

## Datos utilizados

El proyecto utiliza un archivo CSV con resultados de partidos de LaLiga española de la temporada 2024/25, obtenido de [Football-Data](https://football-data.co.uk/data.php).

Cada registro contiene información del encuentro, incluidos los equipos participantes y los goles marcados por cada uno.

Entre los campos utilizados se encuentran `HomeTeam`, `AwayTeam`, `FTHG` y `FTAG`, según los nombres presentes en el archivo de datos.

Los registros se cargan y procesan con Python para realizar las consultas y los cálculos de la aplicación.

## Estado del proyecto

**Primera entrega:** aplicación de consola funcional con búsqueda de partidos, estadísticas numéricas, informes de equipos, filtrado por goles y comparación de equipos.
