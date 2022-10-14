
"""
_______________________________________________________________

     Training NICE                  ────────▓▓╬▓──────────
     Desafío: Batalla Naval         ───────▓▓▓║▓▓─────────
     Nombre: Cecilia Antezana       ──────▓▓▓▓╬▓▓▓▓───────
     Fecha: 14/10/2022              ───▄─▓▓▓▓▓║▓▓▓▓▓──────
                                    ░░▀████████████████▀░░
_______________________________________________________________

"""

import random 

from colorama import Fore, init, Style
init()

JUGADOR_1  = "Jugador_1"
JUGADOR_2  = "Jugador_2"

PORTAAVION = "P"                 # 5 Espacios horizontales
ACORAZADO  = "A"                 # 4 Espacios horizontales
CRUCERO    = "C"                 # 3 Espacios horizontales
SUBMARINO  = "S"                 # 3 Espacios verticales
DESTRUCTOR = "D"                 # 2 Espacios verticales

EJE_X = 10                       # Eje de abscisas 
EJE_Y = 10                       # Eje de ordenadas 

MAR = " "
IMPACTO_FALLADO    = Fore.RED+"X"+Style.RESET_ALL 
IMPACTO_ACERTADO   = Fore.GREEN+"*"+Style.RESET_ALL 
IMPACTOS_INICIALES = 10



def crear_matriz_inicial():         # Crear matriz MAR con espacios vacios.
    matriz = []   
    for y in range(EJE_X):  
        matriz.append([])           # Agregamos un arreglo a la matriz, que sería una fila.
        for x in range(EJE_Y): 
            matriz[y].append(MAR)   # Agregamos una celda a esa fila. Por defecto lleva "Mar".
    return matriz


def aumentar_letra(letra):          # Ord Devuelve el la representacion de la letra en codigo unicode
    return chr(ord(letra)+1)        # chr Devuelve el la representacion de un numero en letra


def desplegar_separador_horizontal():    # Imprimir un renglón dependiendo de las columnas  
    for _ in range(EJE_Y+1):
        print("----", end="")
    print("-")                           

def desplegar_fila_de_numeros():
    print("|   ", end="")
    for x in range(EJE_Y):
        print(f"| {x+1} ", end="")
    print("|")                           


def coordenada_es_mar(x, y, matriz):     # Indica si una coordenada de la matriz está vacía le pone el valor de MAR osea un espacio
    return matriz[y][x] == MAR

def coordenada_en_rango(x, y):           # Indica si las coordenadas x y y estan dentro de las posiciones permitidos de 0 a 9.
    return x >= 0 and x <= EJE_Y-1 and y >= 0 and y <= EJE_X-1

def asignar_y_desplegar_barcos(matriz, cantidad_barcos, jugador):
    
    cantidad_barcos = 1                  # Asignamos la cantidad : cada tipo 1

    if jugador == JUGADOR_1:
        print("\nDescripción, horientación y cantidad de barcos del Jugador_1:\n")
    else:
        print("\nDescripción, horientación y  de barcos del Jugador_2:\n")
    
    print("- Porta Avión Horizontal (5 Espacios): 1\n- Acorazado Horizontal   (4 Espacios): 1\n- Crucero Vertical       (3 Espacios): 1\n- Submarino Horizontal   (3 Espacios): 1\n- Destructor Vertical    (2 Espacios): 1\n\nTotal de barcos: 5\n")
    
    matriz = asignar_porta_avion(1, PORTAAVION, matriz)
    matriz = asignar_acorazado  (1, ACORAZADO, matriz)
    matriz = asignar_crucero    (1, CRUCERO, matriz)
    matriz = asignar_submarino  (1, SUBMARINO, matriz)
    matriz = asignar_destructor (1, DESTRUCTOR, matriz)

    return matriz


def generar_x_aleatoria():              # Posicion aleatoria x (0 - 9) 
    return random.randint(0, EJE_Y-1)


def generar_y_aleatoria():              # Posicion aleatoria y (0 - 9)
    return random.randint(0, EJE_X-1)

def asignar_porta_avion(cantidad, tipo_barco, matriz): # Porta Avión Horizontal (5 Espacios)
    barcos_colocados = 0
    while True:
        x = generar_x_aleatoria()
        y = generar_y_aleatoria()
        x2 = x+1
        x3 = x+2
        x4 = x+3
        x5 = x+4
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and coordenada_en_rango(x3, y) and coordenada_en_rango(x4, y) and coordenada_en_rango(x5, y) and coordenada_es_mar(x, y, matriz) and coordenada_es_mar(x2, y, matriz) and coordenada_es_mar(x3, y, matriz) and coordenada_es_mar(x4, y, matriz) and coordenada_es_mar(x5, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            matriz[y][x3] = tipo_barco
            matriz[y][x4] = tipo_barco  
            matriz[y][x5] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados == cantidad: 
            break
    return matriz

def asignar_acorazado(cantidad, tipo_barco, matriz): # Acorazado Horizontal (4 Espacios)
    barcos_colocados = 0
    while True:
        x = generar_x_aleatoria()
        y = generar_y_aleatoria()
        x2 = x+1
        x3 = x+2
        x4 = x+3
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and coordenada_en_rango(x3, y) and coordenada_en_rango(x4, y) and coordenada_es_mar(x, y, matriz) and coordenada_es_mar(x2, y, matriz) and coordenada_es_mar(x3, y, matriz) and coordenada_es_mar(x4, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            matriz[y][x3] = tipo_barco
            matriz[y][x4] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados == cantidad:
            break
    return matriz

def asignar_crucero(cantidad, tipo_barco, matriz): # Crucero Vertical (3 Espacios)
    barcos_colocados = 0
    while True:
        x = generar_x_aleatoria()
        y = generar_y_aleatoria()
        x2 = x+1
        x3 = x+2
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and coordenada_en_rango(x3, y) and coordenada_es_mar(x, y, matriz) and coordenada_es_mar(x2, y, matriz) and coordenada_es_mar(x3, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            matriz[y][x3] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados == cantidad:
            break
    return matriz

def asignar_submarino(cantidad, tipo_barco, matriz): # Submarino Horizontal (3 Espacios)
    barcos_colocados = 0
    while True:
        x = generar_x_aleatoria()
        y = generar_y_aleatoria()
        y2 = y+1
        y3 = y+2
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and coordenada_en_rango(x, y3) and coordenada_es_mar(x, y, matriz) and coordenada_es_mar(x, y2, matriz) and coordenada_es_mar(x, y3, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            matriz[y3][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados == cantidad:
            break
    return matriz

def asignar_destructor(cantidad, tipo_barco, matriz): # Destructor Vertical (2 Espacios)
    barcos_colocados = 0
    while True:
        x = generar_x_aleatoria()
        y = generar_y_aleatoria()
        y2 = y+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and coordenada_es_mar(x, y, matriz) and coordenada_es_mar(x, y2, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados == cantidad:
            break
    return matriz


def desplegar_disparos_restantes(disparos_restantes, jugador):
    print(f"\nDisparos restantes del {jugador}: {disparos_restantes}")


def desplegar_matriz(matriz, deberia_mostrar_barcos, jugador):
    print(f"\nEste es el tablero del {jugador}: ")
    letra = "A"
    for y in range(EJE_X):
        desplegar_separador_horizontal()
        print(f"| {letra} ", end="")
        for x in range(EJE_Y):
            celda = matriz[y][x]
            valor_real = celda
            if not deberia_mostrar_barcos and valor_real != MAR and valor_real != IMPACTO_FALLADO and valor_real != IMPACTO_ACERTADO:
                valor_real = " "
            print(f"| {valor_real} ", end="")
        letra = aumentar_letra(letra)
        print("|",) 
    desplegar_separador_horizontal()
    desplegar_fila_de_numeros()
    desplegar_separador_horizontal()


def solicitar_coordenadas(jugador):
    print(f"\nSolicitando coordenadas de impacto al {jugador}")
    # Ciclo infinito. Se rompe cuando ingresan una fila correcta
    y = None
    x = None
    while True:
        letra_fila = input("\nIngrese la letra de la fila: ")

        if len(letra_fila) != 1: # Si se ingresa una letra que no es de 1 carácter usamos continue para repetir este ciclo
            print("\nDebe ingresar únicamente una letra")
            continue

        y = ord(letra_fila) - 65 # Convertir la letra a su codigo unicode y le restamos 65 (el 65 es el ASCII de la A, por lo que A es 0)
        if coordenada_en_rango(0, y): # Verificar si es válida. En caso de que sí, rompemos el ciclo
            break
        else:
            print("\nFila inválida, ingrese una fila de la A a la J.")
    # Hacemos lo mismo pero para la columna
    while True:
        try:
            x = int(input("\nIngresa el número de columna: "))
            if coordenada_en_rango(x-1, 0):
                x = x-1  # Queremos el índice, así que restamos un 1 siempre
                break
            else:
                print("\nColumna inválida")
        except:
            print("\nIngresa una columna válida del 1 al 10")

    return x, y


def disparar(x, y, matriz) -> bool:
    if coordenada_es_mar(x, y, matriz):
        matriz[y][x] = IMPACTO_FALLADO
        return False
    # Si ya había disparado antes, tambien se cuenta como falla.
    elif matriz[y][x] == IMPACTO_FALLADO or matriz[y][x] == IMPACTO_ACERTADO:
        return False
    else:
        matriz[y][x] = IMPACTO_ACERTADO
        return True


def oponente_de_jugador(jugador):
    if jugador == JUGADOR_1:
        return JUGADOR_2
    else:
        return JUGADOR_1


def validar_flota_hundida(matriz):
    for y in range(EJE_X):
        for x in range(EJE_Y):
            celda = matriz[y][x]
            # Si no es mar o un disparo, significa que todavía hay un barco por ahí
            if celda != MAR and celda != IMPACTO_ACERTADO and celda != IMPACTO_FALLADO:
                return False
    # Acabamos de recorrer toda la matriz y no regresamos en la línea anterior. Entonces todos los barcos han sido hundidos
    return True


def desplegar_victoria(jugador):
    print(f"\nFin del juego\nEl {jugador} es el ganador")


def desplegar_fracaso(jugador):
    print(f"\nFin del juego\nEl {jugador} pierde. Se han acabado sus disparos")


def desplegar_matrices_con_barcos(matriz_j1, matriz_j2):
    print("\nMostrando ubicación de los barcos de ambos jugadores:")
    desplegar_matriz(matriz_j1, True, JUGADOR_1)
    desplegar_matriz(matriz_j2, True, JUGADOR_2)


def jugar():
    disparos_restantes_j1 = IMPACTOS_INICIALES
    disparos_restantes_j2 = IMPACTOS_INICIALES
    cantidad_barcos = 5
    matriz_j1, matriz_j2 = crear_matriz_inicial(), crear_matriz_inicial() 
    matriz_j1 = asignar_y_desplegar_barcos(matriz_j1, cantidad_barcos, JUGADOR_1) 
    matriz_j2 = asignar_y_desplegar_barcos(matriz_j2, cantidad_barcos, JUGADOR_2) 
    
    turno_actual = JUGADOR_1 
    print(Fore.GREEN + "\n_____INICIANDO PARTIDA_____"+Style.RESET_ALL)
    
    while True:
        print(f"\nTurno del {turno_actual}")
        disparos_restantes = disparos_restantes_j2

        if turno_actual == JUGADOR_1:
            disparos_restantes = disparos_restantes_j1
        desplegar_disparos_restantes(disparos_restantes, turno_actual)
        matriz_oponente = matriz_j1 
        
        if turno_actual == JUGADOR_1:
            matriz_oponente = matriz_j2
        desplegar_matriz(matriz_oponente, True, oponente_de_jugador(turno_actual)) # False matriz
        x, y = solicitar_coordenadas(turno_actual)
        acertado = disparar(x, y, matriz_oponente)
        
        if turno_actual == JUGADOR_1:
            disparos_restantes_j1 -= 1
        else:
            disparos_restantes_j2 -= 1

        desplegar_matriz(matriz_oponente, True, oponente_de_jugador(turno_actual)) # False matriz
        
        if acertado:
            print(Fore.GREEN + "\nImpacto Acertado" +Style.RESET_ALL)
            if  validar_flota_hundida(matriz_oponente):
                desplegar_victoria(turno_actual)
                desplegar_matrices_con_barcos(matriz_j1, matriz_j2)
                break
        else:
            print(Fore.RED + "\nImpacto Fallido" +Style.RESET_ALL)
            if disparos_restantes-1 <= 0:
                desplegar_fracaso(turno_actual)
                desplegar_matrices_con_barcos(matriz_j1, matriz_j2)
                break
        turno_actual = oponente_de_jugador(turno_actual)


def instrucciones_del_juego():
    print(Fore.BLUE + "\n_______INSTRUCCIONES_______\n\n" + Style.RESET_ALL + Fore.LIGHTWHITE_EX + "───║─▄──▄──▄──▄──║────\n───║─▓──▓──▓──▓──║────\n───░░░░░░░░░░░░░─║────\n▀███████████████████──\n░██████████████████▀░░\n"+ Style.RESET_ALL )
    print(Fore.BLUE + "\n_______OBJETIVO DEL JUEGO_______" + Style.RESET_ALL + "\n\nHundir la flota naval del oponente.\n")
    print(Fore.BLUE + "\n_______REGLAS GENERALES_______\n" + Style.RESET_ALL + "\n\n* Número de jugadores: 2 (mínimo y máximo).\n* Se podra impactar en cualquier casilla valida del tablero.\n* Las filas validas se denotan por letras (A - J).\n* Las columnas validas se denotan por numeros (1 a 10).\n* Cada jugador tiene un turno.\n* La partida acaba cuando un jugador ha hundido la flota completa del enemigo.\n")
    print(Fore.BLUE + "\n_______DESCRIPCIÓN DE LA FLOTA_______\n" + Style.RESET_ALL + "\n\nCada flota naval esta compuesta por 5 barcos, descritos en tamaño y horientación:\n\n- Porta Avión Horizontal (5 Espacios): 1\n- Acorazado Horizontal   (4 Espacios): 1\n- Crucero Vertical       (3 Espacios): 1\n- Submarino Horizontal   (3 Espacios): 1\n- Destructor Vertical    (2 Espacios): 1" + Fore.BLUE +"\n_______________________________________\n" + Style.RESET_ALL )
   

def menu():

    print(Fore.BLUE + "\n\n\n_____BIENVENIDOS A BATALLA NAVAL_____" + Style.RESET_ALL)
    
    opcion_elegida = ""
    while opcion_elegida != "3":
        menu = """

Por favor elija una de las siguientes opciones:

1. Iniciar partida
2. Instrucciones
3. Salir 

Opción: """

        opcion_elegida = input(menu)
        if opcion_elegida == "1":
            jugar()
        elif opcion_elegida == "2":
            instrucciones_del_juego()
        else:
            break    

menu()
