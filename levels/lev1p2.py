from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameimage import *

def play_lev1p2(character_matrix, enemy1_matrix):
    # ///-----window and keyboard-----///
    window_1_2 = Window(800, 600)
    window_1_2.set_title("Level 1 - part 2")

    keyboard_1_2 = Keyboard()

    # ///-----map settings-----///
    gravity = 0.5 * 0.01

    # pinks
    pink_ground_lev1p2 = Sprite("images\\pink_ground_lev1p1.png")
    pink_ground_lev1p2.y = 500

    # game images (a implementar---//---)
    #//////////////////

    # ///-----character settings-----///
    character_matrix[0][1].set_total_duration(1000)
    character_matrix[0][0].set_total_duration(1000)
    character_matrix[1][1].set_total_duration(1000)
    character_matrix[1][0].set_total_duration(1000)

    # states
    walking = False
    jumping = False
    attacking = False
    looking_right = True

    # character physics
    player_speed_x = 40 * 0.01
    player_speed_y = 0
    initial_jump_y = character_matrix[0][0].y
    delta_jump = 200

    crono_jump = 0

    while True:
        window_1_2.update()
        window_1_2.set_background_color((100, 100, 100))

        # pinks
        pink_ground_lev1p2.draw()
