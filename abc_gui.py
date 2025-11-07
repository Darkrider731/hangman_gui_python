import pygame as pg


def draw_symbol(screen, symbol, x, y, size):  # screen, x, y, scale):
    pg.font.init()
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(symbol, True, (150, 150, 150), )
    screen.blit(text, (x, y))


abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

def draw_symbol_col(screen, symbol, x, y, size, color):  # screen, x, y, scale):
    pg.font.init()
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(symbol, True, color)
    screen.blit(text, (x, y))
