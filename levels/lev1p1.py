from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameimage import *


"""def ground_colliding(character_matrix, ground):
    colliding = False
    for line in character_matrix:
        for spr in line:
            if spr.collided_perfect(ground):
                colliding = True
    return colliding"""




def play_lev1p1(character_matrix):
    # ///-----window and keyboard-----///
    window_1_1 = Window(800, 600)
    window_1_1.set_title("Level 1 - part 1")

    keyboard_1_1 = Keyboard()


    # ///-----map settings-----///
    gravity = 0.5 * 0.01

    # tutorial
    jeweler = Sprite("images\\jeweler.png")
    jeweler.x = 50
    jeweler.y = 450
    sage = Sprite("images\\sage.png")
    sage.x = 50
    sage.y = 450

    # tutorial baloons
    fala1 = GameImage("images\\fala1.png")
    fala2 = GameImage("images\\fala2.png")
    fala3 = GameImage("images\\fala3.png")

    fala1.x = sage.x + sage.width - 40
    fala1.y = sage.y - 100
    fala2.x = fala1.x
    fala2.y = fala1.y
    fala3.x = fala1.x
    fala3.y = fala1.y

    crono_tutorial = 0

    # pinks
    pink_ground_lev1p1 = Sprite("images\\pink_ground_lev1p1.png")
    pink_ground_lev1p1.y = 540

    pink_1_1_1 = Sprite("images\\smallpink.png")
    pink_1_1_1.x = 465
    pink_1_1_1.y = 440

    pink_1_1_2 = Sprite("images\\micropink.png")
    pink_1_1_2.x = 590
    pink_1_1_2.y = 395
    

    # game images
    ground_lev1p1 = GameImage("images\\ground_lev1p1.png")
    background_lev1p1 = GameImage("images\\background_lev1p1.jpg")
    map_lev1p1 = GameImage("images\\map_lev1p1.jpg")


    # ///-----character settings-----///
    for i in character_matrix:
        for j in i:
            j.x = 144
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

    # character physics
    player_speed_x = 50 * 0.01
    player_speed_y = 0
    initial_jump_y = character_matrix[0][0].y
    delta_jump = 200

    crono_jump = 0


    """# ///-----enemy1 settings-----///
    enemy1_matrix[0][1].set_total_duration(1000)
    enemy1_matrix[0][0].set_total_duration(1000)
    enemy1_matrix[1][1].set_total_duration(1000)
    enemy1_matrix[1][0].set_total_duration(1000)

    for i in enemy1_matrix:
        for j in i:
            j.x = 500
            j.y = 425


    enemy1_life = 2

    # enemy1 states
    enemy1_walking = True
    enemy1_jumping = False
    enemy1_attacking = False
    enemy1_looking_right = True

    # enemy1 physics
    enemy1_speed_x = 30 * 0.01"""

    # ///-----projectiles settings-----///
    mage_fire = Sprite("images\\fire1.png")
    shoots = []
    shoot_v = 250
    shoot_crono = 0

    """# ///-----enemy1 projectiles settings-----///
    purplefire_right = Sprite("images\\purplefire_right.png")
    purplefire_left = Sprite("images\\purplefire_left.png")
    purplefire_shoots = []
    purplefire_shoot_v = 200
    purplefire_shoot_crono = 0"""

    while True:
        window_1_1.update()
        window_1_1.set_background_color((100, 100, 100))

        # pinks
        pink_ground_lev1p1.draw()
        pink_1_1_1.draw()
        pink_1_1_2.draw()

        # game images
        #background_lev1p1.draw()
        #ground_lev1p1.draw()
        map_lev1p1.draw()
        

        # next level
        if character_matrix[0][0].x > window_1_1.width:
            return True

        # ///-----character walking moves-----///
        if keyboard_1_1.key_pressed("RIGHT") and keyboard_1_1.key_pressed("LEFT"):
            looking_right = True
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x += player_speed_x
        if keyboard_1_1.key_pressed("RIGHT"):
            looking_right = True
            walking = True
            for i in character_matrix:
                for j in i:
                    j.x += player_speed_x
        if keyboard_1_1.key_pressed("LEFT"):
            looking_right = False
            walking = True
            if character_matrix[0][0].x > 0:
                for i in character_matrix:
                    for j in i:
                        j.x -= player_speed_x
        if not keyboard_1_1.key_pressed("RIGHT") and not keyboard_1_1.key_pressed("LEFT"):
            walking = False

        """if enemy1_life > 0:
            # ///-----enemy1 walking moves-----///
            for i in enemy1_matrix:
                    for j in i:
                        j.x += enemy1_speed_x
            if enemy1_matrix[0][0].x <= window_1_1.width/2:
                enemy1_speed_x *= -1
                enemy1_looking_right = True
            if enemy1_matrix[0][0].x + enemy1_matrix[0][0].width > window_1_1.width:
                enemy1_speed_x *= -1
                enemy1_looking_right = False"""

        # ///-----gravity-----///
        """if not ground_colliding(character_matrix, pink_ground_lev1p1) and not jumping:
            for i in character_matrix:
                for j in i:
                    j.y += player_speed_y
                    player_speed_y += gravity

        if ground_colliding(character_matrix, pink_ground_lev1p1):
            player_speed_y = 0"""

        if character_matrix[0][0].y + character_matrix[0][0].height < pink_ground_lev1p1.y and not jumping:
            for i in character_matrix:
                for j in i:
                    j.y += player_speed_y
                    player_speed_y += gravity

        if character_matrix[0][0].y + character_matrix[0][0].height >= pink_ground_lev1p1.y and not jumping:
            player_speed_y = 0

        # pink_1_1_1
        if (character_matrix[0][0].y + character_matrix[0][0].height >= pink_1_1_1.y and character_matrix[0][0].y + character_matrix[0][0].height <= pink_1_1_1.y + pink_1_1_1.height) and (character_matrix[0][0].x > pink_1_1_1.x - 10 and character_matrix[0][0].x < pink_1_1_1.x + pink_1_1_1.width) and not jumping:
            player_speed_y = 0

        # pink_1_1_2
        if (character_matrix[0][0].y + character_matrix[0][0].height >= pink_1_1_2.y and character_matrix[0][0].y + character_matrix[0][0].height <= pink_1_1_2.y + pink_1_1_2.height) and (character_matrix[0][0].x > pink_1_1_2.x - 10 and character_matrix[0][0].x < pink_1_1_2.x + pink_1_1_2.width) and not jumping:
            player_speed_y = 0

        # ///-----jump-----///
        crono_jump += window_1_1.delta_time()
        if keyboard_1_1.key_pressed("SPACE") and crono_jump > 0.7:
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
        crono_tutorial += window_1_1.delta_time()
        sage.draw()
        if crono_tutorial <= 50:
            fala3.draw()
        if crono_tutorial <= 20:
            fala2.draw()
        if crono_tutorial <= 10:
            fala1.draw()

        """if enemy1_life > 0:
            # ///-----enemy1 drawings-----///
            if enemy1_looking_right:
                if enemy1_walking:
                    enemy1_matrix[1][1].draw()
                else:
                    enemy1_matrix[0][1].draw()
            if not enemy1_looking_right:
                if enemy1_walking:
                    enemy1_matrix[1][0].draw()
                else:
                    enemy1_matrix[0][0].draw()

            # ///-----enemy1 update-----///
            for i in enemy1_matrix:
                for j in i:
                    j.update()"""


        # ///-----attacking settings-----///
        crono_attacking += window_1_1.delta_time()
        if keyboard_1_1.key_pressed("w") and crono_attacking >= 0.5:
            crono_attacking = 0
            attacking = True
        if crono_attacking >= 0.5:
            attacking = False


        # ///-----projectiles settings-----///
        # shooting
        if keyboard_1_1.key_pressed("q") and shoot_crono >= 0.5:
            shoot_crono = 0
            if looking_right:
                shoot = [Sprite("images\\fire1.png"), character_matrix[0][0].x+30, character_matrix[0][0].y+60, "right"]
            else:
                shoot = [Sprite("images\\fire1.png"), character_matrix[0][0].x-20, character_matrix[0][0].y+60, "left"]
            shoots.append(shoot)

        # shoots movements
        for s in shoots:
            if s[3] == "right":
                s[1] += shoot_v * window_1_1.delta_time()
            else:
                s[1] -= shoot_v * window_1_1.delta_time()
        shoot_crono += window_1_1.delta_time()

        # deactivate shoots
        for s in shoots:
            if s[1] > window_1_1.width or s[1] < 0 - s[0].width:
                shoots.remove(s)
            """if (s[1] - 1) < enemy1_matrix[0][0].x < (s[1] + 1) or (s[1] - 1) < (enemy1_matrix[0][0].x + enemy1_matrix[0][0].width) < (s[1] + 1):
                if enemy1_matrix[0][0].y < s[2] < enemy1_matrix[0][0].y + enemy1_matrix[0][0].height:
                    shoots.remove(s)
                    #enemy1 taking damage
                    enemy1_life -= 1"""

        # projectile drawings
        for s in shoots:
            sho = s[0]
            sho.x = s[1]
            sho.y = s[2]
            sho.draw()

        """if enemy1_life > 0:
            # ///-----enemy1 projectiles settings-----///
            # enemy1 shooting
            if purplefire_shoot_crono >= 2.1:
                purplefire_shoot_crono = 0
                if enemy1_looking_right:
                    purplefire_shoot = [Sprite("images\\purplefire_right.png"), enemy1_matrix[0][0].x+30, enemy1_matrix[0][0].y+60, "right"]
                else:
                    purplefire_shoot = [Sprite("images\\purplefire_left.png"), enemy1_matrix[0][0].x-20, enemy1_matrix[0][0].y+60, "left"]
                purplefire_shoots.append(purplefire_shoot)

            # enemy1 shoots movements
            for s in purplefire_shoots:
                if s[3] == "right":
                    s[1] += purplefire_shoot_v * window_1_1.delta_time()
                else:
                    s[1] -= purplefire_shoot_v * window_1_1.delta_time()
            purplefire_shoot_crono += window_1_1.delta_time()

            # enemy1 deactivate shoots
            for s in purplefire_shoots:
                if s[1] > window_1_1.width or s[1] < 0 - s[0].width:
                    purplefire_shoots.remove(s)
                if (s[1] - 1) < character_matrix[0][0].x < (s[1] + 1) or (s[1] - 1) < (character_matrix[0][0].x + character_matrix[0][0].width) < (s[1] + 1):
                    if character_matrix[0][0].y < s[2] < character_matrix[0][0].y + character_matrix[0][0].height:
                        purplefire_shoots.remove(s)
                        # character taking damage
                        charachter_life -= 1


            # enemy1 projectile drawings
            for s in purplefire_shoots:
                sho = s[0]
                sho.x = s[1]
                sho.y = s[2]
                sho.draw()"""