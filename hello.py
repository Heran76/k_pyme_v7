import pygame as pg

pg.init()
pantalla =pg.display.set_mode((600, 400))
pg.display.set_caption("Hola")

game_over = False

while not game_over:
    #gestion de eventos
    #lista_eventos = pg.event.get()
    for evento in pg.event.get():
        pass

    print("Hola mundo")



    pantalla.fill((0,255,0))
    pg.display.flip()




