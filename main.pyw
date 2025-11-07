import time
import brains_logic
import pygame as pg
import Gallows
import input
import interface_brain

pg.init()
pg.display.set_caption('hangman')

# Initialize font for popup
font = pg.font.Font(None, 36)

def show_popup(screen, message):
    # Create a semi-transparent overlay
    overlay = pg.Surface((330, 330))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(128)
    screen.blit(overlay, (0, 0))
    
    # Split message into lines and draw each line
    lines = message.split('\n')
    for i, line in enumerate(lines):
        text = font.render(line, True, (255, 255, 255))
        text_rect = text.get_rect(center=(165, 100 + i * 30))
        screen.blit(text, text_rect)
    
    # Draw colored options on separate lines
    restart_text = font.render("Press 'P' to Restart", True, (0, 255, 0))  # Green
    restart_rect = restart_text.get_rect(center=(165, 180))
    screen.blit(restart_text, restart_rect)
    
    quit_text = font.render("Press 'Q' to Quit", True, (255, 0, 0))  # Red
    quit_rect = quit_text.get_rect(center=(165, 220))
    screen.blit(quit_text, quit_rect)
    
    pg.display.flip()
    
    # Wait for user input
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return "quit"
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    # Clear the screen before returning
                    screen.fill((0, 0, 0))
                    pg.display.flip()
                    return "play"
                if event.key == pg.K_q:
                    return "quit"
        time.sleep(0.1)

def main():
    global screen, comp_choice, word_length, word_converted, start_point, empty_spaces, not_out, game_play, hung, choosen, input_list
    screen = pg.display.set_mode((330, 330))
    score = 0
    games_played = 0
    
    while True:
        comp_choice = brains_logic.comp_choice()
        word_length = len(comp_choice)
        word_converted = list(comp_choice)
        start_point = interface_brain.promt_calculate(word_length, 330)
        empty_spaces = brains_logic.analytics(comp_choice)
        not_out = True
        game_play = True
        hung = 0
        choosen = []
        input_list = []
        
        interface_brain.draw_prompts(screen, start_point, word_length)
        interface_brain.alphabet_init(screen, choosen)
        pg.display.flip()
        
        while game_play:
            not_out, input_key = input.wait_for_input()
            screen.fill((0, 0, 0))
            empty_spaces = brains_logic.update_empty_spaces(empty_spaces, input_key, comp_choice)
            
            if empty_spaces == comp_choice:
                input_list.append(input_key)
                arrange_input(screen, input_list, start_point)
                pg.display.flip()
                score += 1
                games_played += 1
                message = f"You won!\nThe word was: {comp_choice}\nYour score: {score}/{games_played}"
                choice = show_popup(screen, message)
                if choice == "quit":
                    return
                game_play = False
                break
                
            if_exists = input_key in comp_choice
            if if_exists:
                input_list.append(input_key)
            else:
                # Only increment hung if the letter hasn't been chosen before
                if input_key not in choosen:
                    hung = hung + 1
            
            choosen.append(input_key)
            arrange_input(screen, input_list, start_point)
            interface_brain.hangman(hung, screen)
            interface_brain.alphabet_init(screen, choosen)
            interface_brain.draw_prompts(screen, start_point, word_length)
            pg.display.flip()
            
            # Check for game over after drawing the hangman
            if hung >= 10:  # Game over condition
                games_played += 1
                message = f"You lost!\nThe word was: {comp_choice}\nYour score: {score}/{games_played}"
                choice = show_popup(screen, message)
                if choice == "quit":
                    return
                game_play = False
                break

def arrange_input(screen, input_list, start_point):
    place = 0
    for letter in word_converted:
        if letter in input_list:
            interface_brain.place_letter(screen, letter, place, start_point, 270)
        place = place + 1

if __name__ == "__main__":
    main()
