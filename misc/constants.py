"""Define all constants to be used throughout the program.

This module holds all of the program's constants, in order to minimize the
presence of magic numbers/variables throughout code. The constants in this
file are organized into groups, with the first being general constants used
throughout the program, and all other groups being organized by which classes
they show up in.
"""

import os

# Used throughout program.
GAME_WINDOW_WIDTH = 800
GAME_WINDOW_HEIGHT = 500
BACKGROUND_BLIT_POS = (0, 0)

GAME_TEXT_BLUE = (10, 115, 205)
GAME_TEXT_LIGHT_BLUE = (28, 173, 255)  # Alternate light blue: (20, 150, 224)
GAME_TEXT_GREEN = (16, 200, 16)
GAME_TEXT_WHITE = (255, 255, 255)
GAME_COLOR_LIGHT_GREY = (211, 211, 211)
GAME_COLOR_STONE_GREY = (128, 128, 128)
GAME_COLOR_BLACK = (0, 0, 0)
BUBBLE_FONT_FILE = os.path.join('project_assets', 'fonts', 'bubble_pixelated.TTF')
ARCADE_FONT_FILE = os.path.join('project_assets', 'fonts', 'PressStart2P-Regular.ttf')

BUTTON_CLICK_TIME_DELAY = 200
QUIT_BUTTON_CLICK_TIME_DELAY = 600

# Splash screen class.
SPLASH_TITLE_Y_POS = 200
SPLASH_TITLE_FONT_SIZE = 115
SPLASH_CAPTION1_Y_POS = 320
SPLASH_CAPTION1_FONT_SIZE = 15

# Main menu screen class.
MENU_TITLE_FONT_SIZE = 90
MENU_TITLE_Y_POS = 80

MENU_BUTTON_WIDTH = 315
MENU_BUTTON_HEIGHT = 60

MENU_BUTTONS_FONT_SIZE = 26

START_BUTTON_POS = (400, 220)
START_BUTTON_TEXT = 'START GAME'
HIGH_SCORES_BUTTON_POS = (400, 295)
HIGH_SCORES_BUTTON_TEXT = 'LEADERBOARD'
GAME_OPTIONS_BUTTON_POS = (400, 370)
GAME_OPTIONS_BUTTON_TEXT = 'SETTINGS'
QUIT_BUTTON_POS = (400, 445)
QUIT_BUTTON_TEXT = 'QUIT'

# High scores screen class.
SCORE_DATA_LABEL_FONT_SIZE = 22
SCORE_DATA_FONT_SIZE = 15
SCORE_BOARD_SIZE = (750, 400)
SCORE_BOARD_BLIT_POS = (25, 25)
SCORES_PER_PAGE = 10

ARROW_BUTTON_WIDTH = 35
ARROW_BUTTON_HEIGHT = 35
PREV_ARROW_BUTTON_POS = (50, 399)
NEXT_ARROW_BUTTON_POS = (750, 399)

# Game options screen classes.
TEXT_BUTTON_FONT_SIZE = 22
TEXT_BUTTON_WIDTH = 115
TEXT_BUTTON_HEIGHT = 35
BACK_BUTTON_POS = (75, 465)
BACK_BUTTON_TEXT = 'BACK'
APPLY_BUTTON_POS = (725, 465)
APPLY_BUTTON_TEXT = 'APPLY'

CUTOUT_ARROW_BUTTON_WIDTH = 32
CUTOUT_ARROW_BUTTON_HEIGHT = 28.9

GAME_OPTIONS_TITLE_FONT_SIZE = 42
GAME_OPTIONS_TITLE_POS = (250, 38)
GAME_OPTIONS_LABEL_FONT_SIZE = 25
GAME_OPTIONS_OPTION_FONT_SIZE = 14
GAME_OPTIONS_OPTION_SPACER = 20

# Pause menu class.
PAUSE_MENU_DIMENSIONS = (400, 300)
PAUSE_MENU_POS = (200, 100)
PAUSE_MENU_FONT_SIZE = 20
PAUSE_MENU_VOLUME = 0.5
PAUSE_MENU_MUSIC_START_TIME_DELAY = 600

# Snake game screen classes.
SNAKE_PLAYER_START_POS = (400, 430)
SNAKE_PLAYER_START_DIRECTION = 'up'
NUMBER_OF_APPLE_SNACKS = 3
GAME_LOOP_DELAY = 100
GAME_LOOP_TICK = 20
GAME_VOLUME = 1.0

# Game over screen class.
GAME_OVER_TITLE_FONT_SIZE = 60
GAME_OVER_TITLE_POS = (400, 120)
GAME_OVER_TEXT_FONT_SIZE = 18

GAME_OVER_SCREEN_TIME_DELAY = 1500

GAME_OVER_BUTTON_FONT_SIZE = 18
GAME_OVER_BUTTON_HEIGHT = 40
NO_THANKS_BUTTON_WIDTH = 170
NO_THANKS_BUTTON_POS = (130, 445)
NO_THANKS_BUTTON_TEXT = 'NO THANKS'
CONTINUE_BUTTON_WIDTH = 150
CONTINUE_BUTTON_POS = (680, 445)
CONTINUE_BUTTON_TEXT = 'CONTINUE'

INPUT_BOX_FONT_SIZE = 18
INPUT_BOX_WIDTH = 222
INPUT_BOX_HEIGHT = 35
INPUT_BOX_POS = (400, 300)

# Post game screen class.
POST_GAME_TITLE_FONT_SIZE = 140
POST_GAME_TITLE_POS = (400, 240)

POST_GAME_SCORES_TITLE_FONT_SIZE = 40
POST_GAME_SCORES_TITLE_POS = (400, 32)

POST_GAME_BUTTON_FONT_SIZE = 20
POST_GAME_BUTTON_HEIGHT = 40
MAIN_MENU_BUTTON_WIDTH = 190
MAIN_MENU_BUTTON_POS = (140, 445)
MAIN_MENU_BUTTON_TEXT = 'MAIN MENU'
PLAY_AGAIN_BUTTON_WIDTH = 200
PLAY_AGAIN_BUTTON_POS = (655, 445)
PLAY_AGAIN_BUTTON_TEXT = 'PLAY AGAIN'

# Game border ui class.
GAME_BORDER_LEFT = 30
GAME_BORDER_RIGHT = 30
GAME_BORDER_UPPER = 60
GAME_BORDER_LOWER = 20

GAME_UI_FONT_SIZE = 14
GAME_UI_SCORE_MULTIPLIER = 100
GAME_UI_TEXT_BG_HEIGHT = 20

# Rules board class.
RULES_BOARD_POS = (125, 100)
RULES_BOARD_DIMENSIONS = (550, 300)
RULES_BOARD_TEXT_FONT_SIZE = 12

# Snake player class.
SNAKE_CUBE_WIDTH = 20
SNAKE_CUBE_HEIGHT = SNAKE_CUBE_WIDTH
SNAKE_CUBE_DISPLACEMENT = SNAKE_CUBE_WIDTH

# Apple item class.
ITEM_APPLE_SNACK_WIDTH = 20
ITEM_APPLE_SNACK_HEIGHT = ITEM_APPLE_SNACK_WIDTH

# Text box class.
TEXT_BOX_CHAR_LIMIT = 12
