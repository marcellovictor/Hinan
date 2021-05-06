from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameimage import *

def play_lev2p1(character_matrix, knight_matrix, gray_matrix):
    # ///-----window and keyboard-----///
    window_2_1 = Window(800, 600)
    window_2_1.set_title("Level 1 - part 2")

    keyboard_2_1 = Keyboard()

    # ///-----map settings-----///
    gravity = 0.5 * 0.01

    # pinks
    pink_ground_lev2p1 = Sprite("images\\pink_ground_lev1p1.png")
    pink_ground_lev2p1.y = 540


    # game images
    map_lev2p1 = GameImage("images\\forest.jpg")

    # plats
    plat_2_1_1 = Sprite("images\\plat_a.png", 1)
    plat_2_1_1.x = 105
    plat_2_1_1.y = 380

    plat_2_1_2 = Sprite("images\\plat_a.png", 1)
    plat_2_1_2.x = 400
    plat_2_1_2.y = 220

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

    # ///-----knight settings-----///
    knight_matrix[0][1].set_total_duration(1000)
    knight_matrix[0][0].set_total_duration(1000)
    knight_matrix[1][1].set_total_duration(1000)
    knight_matrix[1][0].set_total_duration(1000)
    knight_matrix[2][1].set_total_duration(1000)
    knight_matrix[2][0].set_total_duration(1000)

    for i in knight_matrix:
        for j in i:
            j.x = plat_2_1_1.x
            j.y = plat_2_1_1.y - knight_matrix[0][0].height


    knight_life = 2

    crono_knight_attack = 0

    # knight states
    knight_walking = True
    knight_jumping = False
    knight_attacking = False
    knight_looking_right = True

    # knight physics
    knight_speed_x = 15 * 0.01


    # ///-----gray settings-----///
    gray_matrix[0][1].set_total_duration(1000)
    gray_matrix[0][0].set_total_duration(1000)
    gray_matrix[1][1].set_total_duration(1000)
    gray_matrix[1][0].set_total_duration(1000)

    for i in gray_matrix:
        for j in i:
            j.x = plat_2_1_2.x
            j.y = plat_2_1_2.y - plat_2_1_2.height


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
        window_2_1.update()
        window_2_1.set_background_color((100, 100, 100))


        # pinks
        pink_ground_lev2p1.draw()

        # game images
        map_lev2p1.draw()

        # plats
        plat_2_1_1.draw()
        plat_2_1_2.draw()


        # next level
        if character_matrix[0][0].x > window_2_1.width:
            return True

        # ///-----character walking moves-----///
        if keyboard_2_1.key_pressed("RIGHT") and keyboard_2_1.key_pressed("LEFT"):
            looking_right = True
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x += player_speed_x
        if keyboard_2_1.key_pressed("RIGHT"):
            looking_right = True
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x += player_speed_x
        if keyboard_2_1.key_pressed("LEFT"):
            looking_right = False
            walking = True
            if character_matrix[0][0].x > 0:
                for i in character_matrix:
                    for j in i:
                        j.x -= player_speed_x
        if not keyboard_2_1.key_pressed("RIGHT") and not keyboard_2_1.key_pressed("LEFT"):
            walking = False


        if gray_life > 0:
            # ///-----gray walking moves-----///
            for i in gray_matrix:
                    for j in i:
                        j.x += gray_speed_x
            if gray_matrix[0][0].x <= plat_2_1_2.x:
                gray_speed_x *= -1
                gray_looking_right = True
            if gray_matrix[0][0].x + gray_matrix[0][0].width > plat_2_1_2.x + plat_2_1_2.width:
                gray_speed_x *= -1
                gray_looking_right = False


        if knight_life > 0:
            # ///-----knight walking moves-----///
            for i in knight_matrix:
                    for j in i:
                        j.x += knight_speed_x
            if knight_matrix[0][0].x <= plat_2_1_1.x:
                knight_speed_x *= -1
                knight_looking_right = True
            if knight_matrix[0][0].x + knight_matrix[0][0].width > plat_2_1_1.x + plat_2_1_1.width:
                knight_speed_x *= -1
                knight_looking_right = False

        # ///-----gravity-----///

        if character_matrix[0][0].y + character_matrix[0][0].height < pink_ground_lev2p1.y and not jumping:
            for i in character_matrix:
                for j in i:
                    j.y += player_speed_y
                    player_speed_y += gravity

        if character_matrix[0][0].y + character_matrix[0][0].height >= pink_ground_lev2p1.y and not jumping:
            player_speed_y = 0

        # plat_2_1_1
        if (character_matrix[0][0].y-20 + character_matrix[0][0].height >= plat_2_1_1.y and character_matrix[0][0].y-20 + character_matrix[0][0].height <= plat_2_1_1.y + plat_2_1_1.height) and (character_matrix[0][0].x > plat_2_1_1.x - 10 and character_matrix[0][0].x < plat_2_1_1.x + plat_2_1_1.width) and not jumping:
            player_speed_y = 0

        # plat_2_1_2
        if (character_matrix[0][0].y-20 + character_matrix[0][0].height >= plat_2_1_2.y and character_matrix[0][0].y-20 + character_matrix[0][0].height <= plat_2_1_2.y + plat_2_1_2.height) and (character_matrix[0][0].x > plat_2_1_2.x - 10 and character_matrix[0][0].x < plat_2_1_2.x + plat_2_1_2.width) and not jumping:
            player_speed_y = 0


        # ///-----jump-----///
        crono_jump += window_2_1.delta_time()
        if keyboard_2_1.key_pressed("SPACE") and crono_jump > 0.7:
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


        if knight_life > 0:
            # ///-----knight drawings-----///
            if knight_looking_right:
                if knight_walking and not knight_attacking:
                    knight_matrix[1][1].draw()
                else:
                    knight_matrix[2][1].draw()
            if not knight_looking_right:
                if knight_walking and not knight_attacking:
                    knight_matrix[1][0].draw()
                else:
                    knight_matrix[2][0].draw()

            # ///-----knight update-----///
            for i in knight_matrix:
                for j in i:
                    j.update()

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
        crono_attacking += window_2_1.delta_time()
        if keyboard_2_1.key_pressed("w") and crono_attacking >= 0.5:
            crono_attacking = 0
            attacking = True
        if crono_attacking >= 0.5:
            attacking = False

        # causing knight damage
        if attacking and ((knight_matrix[0][0].x < character_matrix[0][0].x < knight_matrix[0][0].x + knight_matrix[0][0].width) and (knight_matrix[0][0].y + knight_matrix[0][0].height > character_matrix[0][0].y > knight_matrix[0][0].y)):
            crono_knight_damaging += window_2_1.delta_time()
            if crono_knight_damaging >= 0.45:
                knight_life -= 1
                crono_knight_damaging = 0
        else:
            crono_knight_damaging = 0

        # ///-----projectiles settings-----///
        # shooting
        if keyboard_2_1.key_pressed("q") and shoot_crono >= 0.5:
            shoot_crono = 0
            if looking_right:
                shoot = [Sprite("images\\fire1.png"), character_matrix[0][0].x+30, character_matrix[0][0].y+60, "right"]
            else:
                shoot = [Sprite("images\\fire1.png"), character_matrix[0][0].x-20, character_matrix[0][0].y+60, "left"]
            shoots.append(shoot)

        # shoots movements
        for s in shoots:
            if s[3] == "right":
                s[1] += shoot_v * window_2_1.delta_time()
            else:
                s[1] -= shoot_v * window_2_1.delta_time()
        shoot_crono += window_2_1.delta_time()

        # deactivate shoots
        for s in shoots:
            if s[1] > window_2_1.width or s[1] < 0 - s[0].width:
                shoots.remove(s)
            #knight taking damage
            if knight_life > 0:
                if (s[1] - 1) < knight_matrix[0][0].x < (s[1] + 1) or (s[1] - 1) < (knight_matrix[0][0].x + knight_matrix[0][0].width) < (s[1] + 1):
                    if knight_matrix[0][0].y < s[2] < knight_matrix[0][0].y + knight_matrix[0][0].height:
                        shoots.remove(s)
                        knight_life -= 1
            #gray taking damage
            if (s[1] - 1) < gray_matrix[0][0].x < (s[1] + 1) or (s[1] - 1) < (gray_matrix[0][0].x + gray_matrix[0][0].width) < (s[1] + 1):
                if gray_matrix[0][0].y < s[2] < gray_matrix[0][0].y + gray_matrix[0][0].height:
                    shoots.remove(s)
                    gray_life -= 1

        # projectile drawings
        for s in shoots:
            sho = s[0]
            sho.x = s[1]
            sho.y = s[2]
            sho.draw()

        if knight_life > 0:
            # ///-----knight attacking settings-----///
            if (knight_matrix[0][0].x < character_matrix[0][0].x < knight_matrix[0][0].x + knight_matrix[0][0].width) and (knight_matrix[0][0].y + knight_matrix[0][0].height > character_matrix[0][0].y > knight_matrix[0][0].y) :
                knight_attacking = True
                crono_knight_attack += window_2_1.delta_time()
                if crono_knight_attack >= 1 and not invincible:
                    crono_knight_attack = 0
                    character_life -= 1
            else:
                knight_attacking = False
                crono_knight_attack = 0

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
                    s[1] += purplefire_shoot_v * window_2_1.delta_time()
                else:
                    s[1] -= purplefire_shoot_v * window_2_1.delta_time()
            purplefire_shoot_crono += window_2_1.delta_time()

            # gray deactivate shoots
            for s in purplefire_shoots:
                if s[1] > window_2_1.width or s[1] < 0 - s[0].width:
                    purplefire_shoots.remove(s)
                if (s[1] - 1) < character_matrix[0][0].x < (s[1] + 1) or (s[1] - 1) < (character_matrix[0][0].x + character_matrix[0][0].width) < (s[1] + 1):
                    if character_matrix[0][0].y < s[2] < character_matrix[0][0].y + character_matrix[0][0].height:
                        purplefire_shoots.remove(s)
                        # character taking damage
                        charachter_life -= 1


            # gray projectile drawings
            for s in purplefire_shoots:
                sho = s[0]
                sho.x = s[1]
                sho.y = s[2]
                sho.draw()