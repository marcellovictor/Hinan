from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameimage import *

def play_lev1p3(character_matrix, gray_matrix):
    # ///-----window and keyboard-----///
    window_1_3 = Window(800, 600)
    window_1_3.set_title("Level 1 - part 3")

    keyboard_1_3 = Keyboard()

    # ///-----map settings-----///
    gravity = 0.5 * 0.01

    # tutorial baloons
    fala7 = GameImage("images\\fala7.png")
    fala8 = GameImage("images\\fala8.png")

    fala7.x = 100
    fala7.y = 100
    fala8.x = fala7.x + fala7.width + 20
    fala8.y = fala7.y
    

    crono_tutorial3 = 0

    # pinks
    pink_ground_lev1p3 = Sprite("images\\pink_ground_lev1p1.png")
    pink_ground_lev1p3.y = 540

    pink_1_3_1 = Sprite("images\\smallpink.png")
    pink_1_3_1.x = 105
    pink_1_3_1.y = 380

    # game images
    map_lev1p3 = Sprite("images\\map_lev1p3.jpg")

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


    character_life = 5

    crono_attacking = 0

    vida1 = GameImage("images\\1vida.jpg")
    vida2 = GameImage("images\\2vidas.jpg")
    vida3 = GameImage("images\\3vidas.jpg")
    vida4 = GameImage("images\\4vidas.jpg")
    vida5 = GameImage("images\\5vidas.jpg")

    # states
    walking = False
    jumping = False
    attacking = False
    looking_right = True
    invincible = False

    # character physics
    player_speed_x = 50 * 0.01
    player_speed_y = 0
    initial_jump_y = character_matrix[0][0].y
    delta_jump = 200

    crono_jump = 0

    # ///-----gray settings-----///
    gray_matrix[0][1].set_total_duration(1000)
    gray_matrix[0][0].set_total_duration(1000)
    gray_matrix[1][1].set_total_duration(1000)
    gray_matrix[1][0].set_total_duration(1000)

    for i in gray_matrix:
        for j in i:
            j.x = 500
            j.y = 425


    gray_life = 2

    # gray states
    gray_walking = True
    gray_jumping = False
    gray_attacking = False
    gray_looking_right = True

    # gray physics
    gray_speed_x = 15 * 0.01

    # ///-----projectiles settings-----///
    mage_fire = Sprite("images\\fire1.png")
    shoots = []
    shoot_v = 250
    shoot_crono = 0

    # ///-----gray projectiles settings-----///
    purplefire_right = Sprite("images\\purplefire_right.png")
    purplefire_left = Sprite("images\\purplefire_left.png")
    purplefire_shoots = []
    purplefire_shoot_v = 200
    purplefire_shoot_crono = 0

    while True:
        window_1_3.update()
        window_1_3.set_background_color((100, 100, 100))


        # pinks
        pink_ground_lev1p3.draw()
        pink_1_3_1.draw()

        # game images
        map_lev1p3.draw()
        

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

        
        if gray_life > 0:
            # ///-----gray walking moves-----///
            for i in gray_matrix:
                    for j in i:
                        j.x += gray_speed_x
            if gray_matrix[0][0].x <= window_1_3.width/2:
                gray_speed_x *= -1
                gray_looking_right = True
            if gray_matrix[0][0].x + gray_matrix[0][0].width > window_1_3.width:
                gray_speed_x *= -1
                gray_looking_right = False

        # ///-----gravity-----///

        if character_matrix[0][0].y + character_matrix[0][0].height < pink_ground_lev1p3.y and not jumping:
            for i in character_matrix:
                for j in i:
                    j.y += player_speed_y
                    player_speed_y += gravity

        if character_matrix[0][0].y + character_matrix[0][0].height >= pink_ground_lev1p3.y and not jumping:
            player_speed_y = 0

        # pink_1_3_1
        if (character_matrix[0][0].y + character_matrix[0][0].height >= pink_1_3_1.y and character_matrix[0][0].y + character_matrix[0][0].height <= pink_1_3_1.y + pink_1_3_1.height) and (character_matrix[0][0].x > pink_1_3_1.x - 10 and character_matrix[0][0].x < pink_1_3_1.x + pink_1_3_1.width) and not jumping:
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
        if character_life == 5:
            vida5.draw()
        if character_life == 4:
            vida4.draw()
        if character_life == 3:
            vida3.draw()
        if character_life == 2:
            vida2.draw()
        if character_life == 1:
            vida1.draw()

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


        # NPC drawing
        crono_tutorial3 += window_1_3.delta_time()
        if crono_tutorial3 > 7:
            fala8.draw()
        fala7.draw()
        

        if gray_life > 0:
            # ///-----gray drawings-----///
            if gray_looking_right:
                if gray_walking:
                    gray_matrix[1][1].draw()
                else:
                    gray_matrix[0][1].draw()
            if not gray_looking_right:
                if gray_walking:
                    gray_matrix[1][0].draw()
                else:
                    gray_matrix[0][0].draw()

            # ///-----gray update-----///
            for i in gray_matrix:
                for j in i:
                    j.update()

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
            if (s[1] - 1) < gray_matrix[0][0].x < (s[1] + 1) or (s[1] - 1) < (gray_matrix[0][0].x + gray_matrix[0][0].width) < (s[1] + 1):
                if gray_matrix[0][0].y < s[2] < gray_matrix[0][0].y + gray_matrix[0][0].height:
                    shoots.remove(s)
                    #gray taking damage
                    gray_life -= 1

        # projectile drawings
        for s in shoots:
            sho = s[0]
            sho.x = s[1]
            sho.y = s[2]
            sho.draw()


        if gray_life > 0:
            # ///-----gray projectiles settings-----///
            # gray shooting
            if purplefire_shoot_crono >= 2.1:
                purplefire_shoot_crono = 0
                if gray_looking_right:
                    purplefire_shoot = [Sprite("images\\purplefire_right.png"), gray_matrix[0][0].x+30, gray_matrix[0][0].y+60, "right"]
                else:
                    purplefire_shoot = [Sprite("images\\purplefire_left.png"), gray_matrix[0][0].x-20, gray_matrix[0][0].y+60, "left"]
                purplefire_shoots.append(purplefire_shoot)

            # gray shoots movements
            for s in purplefire_shoots:
                if s[3] == "right":
                    s[1] += purplefire_shoot_v * window_1_3.delta_time()
                else:
                    s[1] -= purplefire_shoot_v * window_1_3.delta_time()
            purplefire_shoot_crono += window_1_3.delta_time()

            # gray deactivate shoots
            for s in purplefire_shoots:
                if s[1] > window_1_3.width or s[1] < 0 - s[0].width:
                    purplefire_shoots.remove(s)
                if (s[1] - 1) < character_matrix[0][0].x < (s[1] + 1) or (s[1] - 1) < (character_matrix[0][0].x + character_matrix[0][0].width) < (s[1] + 1):
                    if character_matrix[0][0].y < s[2] < character_matrix[0][0].y + character_matrix[0][0].height:
                        purplefire_shoots.remove(s)
                        # character taking damage
                        character_life -= 1


            # gray projectile drawings
            for s in purplefire_shoots:
                sho = s[0]
                sho.x = s[1]
                sho.y = s[2]
                sho.draw()