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
    pink_ground_lev1p2.y = 540

    # game images (a implementar---//---)
    #//////////////////

    # ///-----character settings-----///
    for i in character_matrix:
        for j in i:
            j.x = 40
            j.y = 100

    character_matrix[0][1].set_total_duration(1000)
    character_matrix[0][0].set_total_duration(1000)
    character_matrix[1][1].set_total_duration(1000)
    character_matrix[1][0].set_total_duration(1000)


    charachter_life = 5
    # states
    walking = False
    jumping = False
    attacking = False
    looking_right = True

    # character physics
    player_speed_x = 70 * 0.01
    player_speed_y = 0
    initial_jump_y = character_matrix[0][0].y
    delta_jump = 200

    crono_jump = 0

    while True:
        window_1_2.update()
        window_1_2.set_background_color((100, 100, 100))

        # pinks
        pink_ground_lev1p2.draw()


        # ///-----character walking moves-----///
        if keyboard_1_2.key_pressed("RIGHT") and keyboard_1_2.key_pressed("LEFT"):
            looking_right = True
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x += player_speed_x
        if keyboard_1_2.key_pressed("RIGHT"):
            looking_right = True
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x += player_speed_x
        if keyboard_1_2.key_pressed("LEFT"):
            looking_right = False
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x -= player_speed_x
        if not keyboard_1_2.key_pressed("RIGHT") and not keyboard_1_2.key_pressed("LEFT"):
            walking = False

        # ///-----gravity-----///

        if character_matrix[0][0].y + character_matrix[0][0].height < pink_ground_lev1p2.y and not jumping:
            for i in character_matrix:
                for j in i:
                    j.y += player_speed_y
                    player_speed_y += gravity

        if character_matrix[0][0].y + character_matrix[0][0].height >= pink_ground_lev1p2.y and not jumping:
            player_speed_y = 0

        # ///-----jump-----///
        crono_jump += window_1_2.delta_time()
        if keyboard_1_2.key_pressed("SPACE") and crono_jump > 0.7:
            crono_jump = 0
            jumping = True
        
        if jumping and player_speed_y == 0 and crono_jump < 0.2:
            player_speed_y = 50 * 0.01
            initial_jump_y = character_matrix[0][0].y

        if jumping:
            for i in character_matrix:
                for j in i:
                    j.y -= player_speed_y
                    player_speed_y += gravity

        if character_matrix[0][0].y < initial_jump_y - delta_jump:
            jumping = False
            player_speed_y = 30 * 0.01

        
        # ///-----character drawings-----///
        window_1_2.draw_text(f"Vidas: {charachter_life}", 10, 10, size=15, color=(100, 100, 100))

        if looking_right:
            if walking:
                character_matrix[1][1].draw()
            else:
                character_matrix[0][1].draw()
        if not looking_right:
            if walking:
                character_matrix[1][0].draw()
            else:
                character_matrix[0][0].draw()

        # ///-----character update-----///
        for i in character_matrix:
            for j in i:
                j.update()
