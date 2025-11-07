import word_list
import random


def comp_choice():
    choice = random.randint(0, 800)
    com_choice = (word_list.words[choice])
    return com_choice

def analytics(com_choice):
    line = '_'
    word_length = len(com_choice)
    empty_spaces = str(line * word_length)
    return str(empty_spaces)


def update_empty_spaces(empty_spaces, letter_choice, com_choice):
            correct_spaces = [x for x, v in enumerate(com_choice) if v == letter_choice]
            for i in correct_spaces:
                empty_spaces = empty_spaces[:i] + letter_choice + empty_spaces[i + 1:]
            return empty_spaces
