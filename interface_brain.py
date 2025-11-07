import pygame as pg

import Gallows
import abc_gui

def promt_calculate(word_length, screen_size):
    space_length = word_length - 1
    space_needed = 20 * word_length + space_length * 5
    print(space_needed)
    place_in_space = screen_size - space_needed
    start_point = place_in_space / 2
    return start_point

def draw_prompts(screen, start_point, word_length):
    for i in range(word_length):
        end_point = start_point + 19
        pg.draw.line(screen, (125, 200, 31), (start_point, 300), (end_point, 300), 5)
        start_point = start_point + 25


def place_letter(screen, symbol, place, start_point, height):
    symbol = symbol.capitalize()
    print(symbol)
    for j in range(place):
        start_point = start_point + 25
    if symbol == 'I':
        start_point = start_point + 6
    abc_gui.draw_symbol(screen, symbol, start_point, height, 28)

def hangman(stage, screen):
    if stage == 0:
        y = 8
    elif stage == 1:
        Gallows.gallows_1(screen)
    elif stage == 2:
        Gallows.gallows_2(screen)
    elif stage == 3:
        Gallows.gallows_3(screen)
    elif stage == 4:
        Gallows.gallows_4(screen)
    elif stage == 5:
        Gallows.gallows_5(screen)
    elif stage == 6:
        Gallows.gallows_6(screen)
    elif stage == 7:
        Gallows.gallows_7(screen)
    elif stage == 8:
        Gallows.gallows_8(screen)
    elif stage == 9:
        Gallows.gallows_9(screen)
    elif stage == 10:
        Gallows.gallows_10(screen)
    else:
        exit(10)




def alphabet_init(screen, choosen):
    x = 30
    y = 100
    new_line = 0
    for letter in abc_gui.abc:
        color = [50,50,50]
        if letter in choosen:
            color = [150,20,200]
        abc_gui.draw_symbol_col(screen, letter, x, y, 15, color)
        x = x + 13
        new_line = new_line + 1
        if new_line == 5:
            new_line = 0
            y = y + 17
            x = 30
