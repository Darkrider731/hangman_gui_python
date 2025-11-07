import time

import pygame


def key_pressed_abc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quitting...")
            return False, "QUIT"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                return True, "A"
            elif event.key == pygame.K_b:
                return True, "B"
            elif event.key == pygame.K_c:
                return True, "C"
            elif event.key == pygame.K_d:
                return True, "D"
            elif event.key == pygame.K_e:
                return True, "E"
            elif event.key == pygame.K_f:
                return True, "F"
            elif event.key == pygame.K_g:
                return True, "G"
            elif event.key == pygame.K_h:
                return True, "H"
            elif event.key == pygame.K_i:
                return True, "I"
            elif event.key == pygame.K_j:
                return True, "J"
            elif event.key == pygame.K_k:
                return True, "K"
            elif event.key == pygame.K_l:
                return True, "L"
            elif event.key == pygame.K_m:
                return True, "M"
            elif event.key == pygame.K_n:
                return True, "N"
            elif event.key == pygame.K_o:
                return True, "O"
            elif event.key == pygame.K_p:
                return True, "P"
            elif event.key == pygame.K_q:
                return True, "Q"
            elif event.key == pygame.K_r:
                return True, "R"
            elif event.key == pygame.K_s:
                return True, "S"
            elif event.key == pygame.K_t:
                return True, "T"
            elif event.key == pygame.K_u:
                return True, "U"
            elif event.key == pygame.K_v:
                return True, "V"
            elif event.key == pygame.K_w:
                return True, "W"
            elif event.key == pygame.K_x:
                return True, "X"
            elif event.key == pygame.K_y:
                return True, "Y"
            elif event.key == pygame.K_z:
                return True, "Z"
            else:
                Exception("invalid key")
    return True, "NULL"


def wait_for_input():
    while True:
        not_quit, input_choice = key_pressed_abc()
        if not not_quit:
            exit(1)

        if input_choice != "NULL":
            break

        elif input_choice == "NULL":
            time.sleep(0.1)


    input_choice = input_choice.lower()
    return not_quit, input_choice


