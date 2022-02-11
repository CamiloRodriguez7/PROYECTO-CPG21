import pygame, sys
import numpy as np
import pygame.freetype

pygame.init()

ANCHO = 600
ALTO = 600
ANCHO_LINEAS = 15
FILAS_TABLERO = 3
COLUMNAS_TABLERO = 3
RADIO_CIRCULO = 60
ANCHO_CIRCULO = 15
ANCHO_CRUZ = 25
ESPACIO = 55

#colorcittos ROJO, VERDE, AZUL
ROJO = (255, 0, 0) #MÁXIMO DE ESTE COLOR
COLOR_PANTALLA = (233, 232, 227) #(200, 250, 156)
COLOR_LINEAS = (57, 149, 160) #(23, 135, 115)
COLOR_CIRCULO = (171, 118, 176) #(255, 0, 0) #(239, 231, 200)
COLOR_CRUZ = (120,40,140)
BLANCO = (255, 255, 255)
NEGRO = (150,150,150)
TICTAC = (114,112,247)
wining= (0,0,0)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("El triqui más áspero uwu")
pantalla.fill(COLOR_PANTALLA)

#tablero
tablero = np.zeros((FILAS_TABLERO, COLUMNAS_TABLERO))

#fuentes
menufont = pygame.font.SysFont("SHOWCARD GOTHIC", 45)
menufont2 = pygame.font.SysFont("SHOWCARD GOTHIC", 35)
menufont3 = pygame.font.SysFont("SHOWCARD GOTHIC", 50)

#sonido
pygame.mixer.music.load("Sonido/sound1.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

sonidocirculo = pygame.mixer.Sound("Sonido/circulo.wav")
sonidocruz = pygame.mixer.Sound("Sonido/cruz.wav")

fin_del_juego = True

### TEXTO JUGADOR GANADOR###
gano1 = menufont3.render("Ganó el jugador 1", True, wining)
gano2 = menufont3.render("Ganó el jugador 2", True, wining)

def gano_1():
    pantalla.blit(gano1, (0, 540))
    pygame.mixer.music.load("Sonido/gg.wav")
    pygame.mixer.music.play()

def gano_2():
    pantalla.blit(gano2, (0, 540))
    pygame.mixer.music.load("Sonido/gg.wav")
    pygame.mixer.music.play()


def dibujar_lineas():
    #horizontales
    pygame.draw.line(pantalla, COLOR_LINEAS, (0, 200), (ANCHO, 200), ANCHO_LINEAS)
    pygame.draw.line(pantalla, COLOR_LINEAS, (0, 400), (ANCHO, 400), ANCHO_LINEAS)
    #verticales
    pygame.draw.line(pantalla, COLOR_LINEAS, (200, 0), (200, ALTO), ANCHO_LINEAS)
    pygame.draw.line(pantalla, COLOR_LINEAS, (400, 0), (400, ALTO), ANCHO_LINEAS)

def dibujar_figuras():
    for fila in range(FILAS_TABLERO):
        for columna in range(COLUMNAS_TABLERO):
            if tablero[fila][columna] == 1:
                pygame.draw.circle(pantalla, COLOR_CIRCULO, (int(columna * 200 + 100), int(fila * 200 + 100)), RADIO_CIRCULO, ANCHO_CIRCULO)
            elif tablero[fila][columna] == 2:
                pygame.draw.line(pantalla, COLOR_CRUZ, (columna * 200 + ESPACIO, fila * 200 + 200 - ESPACIO), (columna * 200 + 200 - ESPACIO, fila * 200 + ESPACIO), ANCHO_CRUZ)
                pygame.draw.line(pantalla, COLOR_CRUZ, (columna * 200 + ESPACIO, fila * 200 + ESPACIO), (columna * 200 + 200 - ESPACIO, fila * 200 + 200 - ESPACIO), ANCHO_CRUZ)

def marcar_celda(fila, columna, jugador):
    tablero[fila][columna] = jugador
    if jugador == 1:
        sonidocirculo.play()
    elif jugador == 2:
        sonidocruz.play()

def celda_disponible(fila, columna):
    return tablero[fila][columna] == 0

def tablero_lleno():
    for fila in range(FILAS_TABLERO):
        for columna in range(COLUMNAS_TABLERO):
            if tablero[fila][columna] == 0:
                return False

        return True

def ganador(jugador):
    for columna in range(COLUMNAS_TABLERO):
        if tablero[0][columna] == jugador and tablero[1][columna] == jugador and tablero[2][columna] == jugador:
            linea_vertical(columna, jugador)
            return True

    for fila in range(FILAS_TABLERO):
        if tablero[fila][0] == jugador and tablero[fila][1] == jugador and tablero[fila][2] == jugador:
            linea_horizontal(fila, jugador)
            return True

    if tablero[2][0] == jugador and tablero[1][1] == jugador and tablero[0][2] == jugador:
        diagonal_ascendente(jugador)
        return True

    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        diagonal_descendente(jugador)
        return True

    return False

#________________#lineas al ganar#_____________________#

def linea_vertical(columna, jugador):
    posX = columna * 200 + 100

    if jugador == 1:
        columna = COLOR_CIRCULO
        pygame.draw.line(pantalla, columna, (posX, 15), (posX, ALTO - 15), 15)
        gano_1()
    elif jugador == 2:
        columna = COLOR_CRUZ
        pygame.draw.line(pantalla, columna, (posX, 15), (posX, ALTO - 15), 15)
        gano_2()


def linea_horizontal(fila, jugador):
    posY = fila * 200 + 100

    if jugador == 1:
        columna = COLOR_CIRCULO
        pygame.draw.line(pantalla, columna, (15, posY), (ANCHO - 15, posY), 15)
        gano_1()
    elif jugador == 2:
        columna = COLOR_CRUZ
        pygame.draw.line(pantalla, columna, (15, posY), (ANCHO - 15, posY), 15)
        gano_2()


def diagonal_ascendente(jugador):
    if jugador == 1:
        columna = COLOR_CIRCULO
        pygame.draw.line(pantalla, columna, (15, ALTO - 15), (ANCHO - 15, 15), 15)
        gano_1()
    elif jugador == 2:
        columna = COLOR_CRUZ
        pygame.draw.line(pantalla, columna, (15, ALTO - 15), (ANCHO - 15, 15), 15)
        gano_2()


def diagonal_descendente(jugador):
    if jugador == 1:
        columna = COLOR_CIRCULO
        pygame.draw.line(pantalla, columna, (15, 15), (ANCHO - 15, ALTO - 15), 15)
        gano_1()
    elif jugador == 2:
        columna = COLOR_CRUZ
        pygame.draw.line(pantalla, columna, (15, 15), (ANCHO - 15, ALTO - 15), 15)
        gano_2()


#________________#lineas al ganar#_____________________#

def c_reditos():
    creditos_img = pygame.image.load("images/creditos.jpg")
    pantalla.blit(creditos_img, (0, 0))




def intromenu():
    punto = 0
    while 1:
        image_menu = pygame.image.load("images/fondomenu.jpg")
        pantalla.blit(image_menu, (0,0))
        tic_tac_toe = menufont.render("TIC TAC TOE", True, TICTAC)
        pantalla.blit(tic_tac_toe, (170,80))
        if punto == 0:
            jugar = menufont2.render("JUGAR", True, NEGRO)
            creditos = menufont2.render("CREDITOS", True, BLANCO)
            salir = menufont2.render("SALIR", True, BLANCO)
        elif punto == 1:
            jugar = menufont2.render("JUGAR", True, BLANCO)
            creditos = menufont2.render("CREDITOS", True, NEGRO)
            salir = menufont2.render("SALIR", True, BLANCO)
        elif punto == 2:
            jugar = menufont2.render("JUGAR", True, BLANCO)
            creditos = menufont2.render("CREDITOS", True, BLANCO)
            salir = menufont2.render("SALIR", True, NEGRO)
        pantalla.blit(jugar, (240,200))
        pantalla.blit(creditos, (215, 300))
        pantalla.blit(salir, (250, 400))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    punto += 1
                elif evento.key == pygame.K_UP:
                    punto -= 1
                elif evento.key == pygame.K_RETURN:
                    if punto == 0:
                        return True
                    elif punto == 1:
                        return c_reditos()
                    elif punto == 2:
                        pygame.quit()
                        sys.exit()
        punto %= 3
        pygame.display.update()






def reiniciar():
    pantalla.fill(COLOR_PANTALLA)
    dibujar_lineas()
    for fila in range(FILAS_TABLERO):
        for columna in range(COLUMNAS_TABLERO):
            tablero[fila][columna] = 0



if intromenu() == True:
    image_controles = pygame.image.load("images/instrucciones.jpg")#se tiene que cambiar#
    pantalla.blit(image_controles, (0,0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                dibujar_lineas()
                jugador = 1
                fin_del_juego = False








while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not fin_del_juego:

            x = event.pos[0]
            y = event.pos[1]

            FILA_SELECCIONADA = int(y // 200)
            COLUMNA_SELECCIONADA = int(x // 200)

            if celda_disponible(FILA_SELECCIONADA, COLUMNA_SELECCIONADA):

                marcar_celda(FILA_SELECCIONADA, COLUMNA_SELECCIONADA, jugador)
                if ganador(jugador):
                    fin_del_juego = True
                jugador = jugador % 2 + 1

                dibujar_figuras()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: #El K_r es la tecla para reiniciar, se puede cambiar la letra
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Sonido/music1.wav")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.09)
                reiniciar()
                jugador = 1
                fin_del_juego = False

    pygame.display.update()
