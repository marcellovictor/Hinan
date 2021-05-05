from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameimage import *

def play_lev1p3(character_matrix):
    # ///-----window and keyboard-----///
    window_1_3 = Window(800, 600)
    window_1_3.set_title("Level 1 - part 2")

    keyboard_1_3 = Keyboard()

    # ///-----map settings-----///
    gravity = 0.5 * 0.01

    # pinks
    pink_ground_lev1p3 = Sprite("images\\pink_ground_lev1p1.png")
    pink_ground_lev1p3.y = 540


    # game images
    #////////////////////

    # ///-----character settings-----///
    for i in character_matrix:
        for j in i:
            j.x = 28
            j.y = 410

    character_matrix[0][1].set_total_duration(1000)
    character_matrix[0][0].set_total_duration(1000)
    character_matrix[1][1].set_total_duration(1000)
    character_matrix[1][0].set_total_duration(1000)
    character_matrix[2][1].set_total_duration(500)
    character_matrix[2][0].set_total_duration(500)


    charachter_life = 5

    crono_attacking = 0

    # states
    walking = False
    jumping = False
    attacking = False
    looking_right = True
    invincible = False

    # character physics
    player_speed_x = 70 * 0.01
    player_speed_y = 0
    initial_jump_y = character_matrix[0][0].y
    delta_jump = 200

    crono_jump = 0

    # ///-----projectiles settings-----///
    mage_fire = Sprite("images\\fire1.png")
    shoots = []
    shoot_v = 250
    shoot_crono = 0

    while True:
        window_1_3.update()
        window_1_3.set_background_color((100, 100, 100))


        # pinks
        pink_ground_lev1p3.draw()

        # game images
        #//////////////// 

        # next level
        if character_matrix[0][0].x > window_1_3.width:
            return True

        # ///-----character walking moves-----///
        if keyboard_1_3.key_pressed("RIGHT") and keyboard_1_3.key_pressed("LEFT"):
            looking_right = True
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x += player_speed_x
        if keyboard_1_3.key_pressed("RIGHT"):
            looking_right = True
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x += player_speed_x
        if keyboard_1_3.key_pressed("LEFT"):
            looking_right = False
            walking = True
            if character_matrix[0][0].x > 0:
                for i in character_matrix:
                    for j in i:
                        j.x -= player_speed_x
        if not keyboard_1_3.key_pressed("RIGHT") and not keyboard_1_3.key_pressed("LEFT"):
            walking = False

        
        # ///-----gravity-----///

        if character_matrix[0][0].y + character_matrix[0][0].height < pink_ground_lev1p3.y and not jumping:
            for i in character_matrix:
                for j in i:
                    j.y += player_speed_y
                    player_speed_y += gravity

        if character_matrix[0][0].y + character_matrix[0][0].height >= pink_ground_lev1p3.y and not jumping:
            player_speed_y = 0


        # ///-----jump-----///
        crono_jump += window_1_3.delta_time()
        if keyboard_1_3.key_pressed("SPACE") and crono_jump > 0.7:
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
        window_1_3.draw_text(f"Vidas: {charachter_life}", 10, 10, size=15, color=(100, 100, 100))

        if looking_right:
            if attacking:
                character_matrix[2][1].draw()
            else:
                if walking:
                    character_matrix[1][1].draw()
                else:
                    character_matrix[0][1].draw()
        if not looking_right:
            if attacking:
                character_matrix[2][0].draw()
            else:
                if walking:
                    character_matrix[1][0].draw()
                else:
                    character_matrix[0][0].draw()

        # ///-----character update-----///
        for i in character_matrix:
            for j in i:
                j.update()

        # character positioning
        for i in character_matrix:
                for j in i:
                    j.x = character_matrix[0][0].x
                    j.y = character_matrix[0][0].y


        # ///-----attacking settings-----///
        crono_attacking += window_1_3.delta_time()
        if keyboard_1_3.key_pressed("w") and crono_attacking >= 0.5:
            crono_attacking = 0
            attacking = True
        if crono_attacking >= 0.5:
            attacking = False


        # ///-----projectiles settings-----///
        # shooting
        if keyboard_1_3.key_pressed("q") and shoot_crono >= 0.5:
            shoot_crono = 0
            if looking_right:
                shoot = [Sprite("images\\fire1.png"), character_matrix[0][0].x+30, character_matrix[0][0].y+60, "right"]
            else:
                shoot = [Sprite("images\\fire1.png"), character_matrix[0][0].x-20, character_matrix[0][0].y+60, "left"]
            shoots.append(shoot)

        # shoots movements
        for s in shoots:
            if s[3] == "right":
                s[1] += shoot_v * window_1_3.delta_time()
            else:
                s[1] -= shoot_v * window_1_3.delta_time()
        shoot_crono += window_1_3.delta_time()

        # deactivate shoots
        for s in shoots:
            if s[1] > window_1_3.width or s[1] < 0 - s[0].width:
                shoots.remove(s)

        # projectile drawings
        for s in shoots:
            sho = s[0]
            sho.x = s[1]
            sho.y = s[2]
            sho.draw()