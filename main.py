from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sound import *

from levels.lev1p1 import *
from levels.lev1p2 import *
from levels.lev1p3 import *

from levels.lev2p1 import *

menu = Window(800, 600)
menu.set_title("Main Menu")

keyboard_menu = Keyboard()

mouse = Mouse()

background_menu = GameImage("images\\MenuPlay.jpg")
charac_choice_pic = GameImage("images\\CharacterChoice.jpg")
game_complete = GameImage("images\\GameComplete.jpg")

button_play = Sprite("images\\ButtonPlay.png", 1)
button_play.x = 325
button_play.y = 205
button_exit = Sprite("images\\ButtonExit.png", 1)
button_exit.x = 330
button_exit.y = 380

playorexit = True
ganhou = False

mage_choice = Sprite("images\\mage_jumping_right.png", 7)
mage_choice.set_total_duration(1500)
mage_choice.x = 210
mage_choice.y = 380


viking_choice = Sprite("images\\viking_jumping_left.png", 7)
viking_choice.set_total_duration(1500)
viking_choice.x = 490
viking_choice.y = 380

crono_menu = 0

 # sound
sound_menu = Sound("sounds\\medieval.ogg")
sound_menu.play()
sound_menu.set_repeat(True)

sound_choice = Sound("sounds\\start.ogg")


"""
[j0: left][j1: right]
i = 0: just standing
i = 1: walking
i = 2: attacking
"""
# Characters Matrix

mage_matrix = [[Sprite("images\\mage_left.png", 1), Sprite("images\\mage_right.png", 1)],
    [Sprite("images\\full_walk_mage_left.png", 6), Sprite("images\\full_walk_mage_right.png", 6)],
    [Sprite("images\\mage_attacking_left.png", 7), Sprite("images\\mage_attacking_right.png", 7)]]

viking_matrix = [[Sprite("images\\viking_left.png", 1), Sprite("images\\viking_right.png", 1)],
    [Sprite("images\\viking_walking_left.png", 6), Sprite("images\\viking_walking_right.png", 6)],
    [Sprite("images\\viking_attacking_left.png", 5), Sprite("images\\viking_attacking_right.png", 5)]]

knight_matrix = [[Sprite("images\\horn_left.png", 1), Sprite("images\\horn_right.png", 1)],
    [Sprite("images\\horn_walking_left.png", 10), Sprite("images\\horn_walking_right.png", 10)],
    [Sprite("images\\horn_attacking_left.png", 10), Sprite("images\\horn_attacking_right.png", 10)]]

gray_matrix = [[Sprite("images\\gray_left.png", 1), Sprite("images\\gray_right.png", 1)],
    [Sprite("images\\full_walk_gray_left.png", 9), Sprite("images\\full_walk_gray_right.png", 9)]]

next_level = False
character_died = False

while True:
    menu.update()
    if character_died:
        menu.set_background_color((100, 100, 100))
        menu.draw_text("Você perdeu, pressione C para continuar!", 200, menu.height/2, size=20)
        if keyboard_menu.key_pressed("C"):
            character_died = False
            sound_menu.play()
            sound_menu.set_repeat(True)
    else:
        if playorexit:
            background_menu.draw()
            button_play.draw()
            button_exit.draw()
            if mouse.is_over_object(button_play) and mouse.is_button_pressed(BUTTON_LEFT):
                playorexit = False
            if mouse.is_over_object(button_exit) and mouse.is_button_pressed(BUTTON_LEFT):
                break
        else:
            charac_choice_pic.draw()

            mage_choice.draw()
            mage_choice.update()
            
            viking_choice.draw()
            viking_choice.update()

            crono_menu += menu.delta_time()
            if crono_menu < 1.5/2:
                mage_choice.y -= 20 * 0.01
                viking_choice.y -= 20 * 0.01
            elif crono_menu < 1.5:
                mage_choice.y += 20 * 0.01
                viking_choice.y += 20 * 0.01
            else:
                crono_menu = 0

    if ganhou:
        game_complete.draw()
        if keyboard_menu.key_pressed("P"):
            ganhou = False
            sound_menu.play()


    #Mage

    if keyboard_menu.key_pressed("M"):
        sound_choice.play()
        sound_menu.stop()

        # sound level
        sound_1_1 = Sound("sounds\\level.ogg")
        sound_1_1.play()
        sound_1_1.set_repeat(True)

        playorexit = True
        character_died = False
        next_level = play_lev1p1(mage_matrix[:][:], sound_1_1)

        if next_level:
            next_level = play_lev1p2(mage_matrix[:][:], knight_matrix[:][:], sound_1_1)
        else:
            character_died = True
            sound_1_1.stop()

        if next_level:
            next_level = play_lev1p3(mage_matrix[:][:], gray_matrix[:][:], sound_1_1)
        else:
            character_died = True
            sound_1_1.stop()

        if next_level:
            next_level = play_lev2p1(mage_matrix[:][:], knight_matrix[:][:], gray_matrix[:][:], sound_1_1)
        else:
            character_died = True
            sound_1_1.stop()

        if next_level:
            sound_1_1.stop()
            ganhou = True
                
# end

    
    #Viking

    if keyboard_menu.key_pressed("V"):
        sound_choice.play()
        sound_menu.stop()

        # sound level
        sound_1_1 = Sound("sounds\\level.ogg")
        sound_1_1.play()
        sound_1_1.set_repeat(True)

        playorexit = True
        character_died = False
        next_level = play_lev1p1(viking_matrix[:][:], sound_1_1)

        if next_level:
            next_level = play_lev1p2(viking_matrix[:][:], knight_matrix[:][:], sound_1_1)
        else:
            character_died = True
            sound_1_1.stop()

        if next_level:
            next_level = play_lev1p3(viking_matrix[:][:], gray_matrix[:][:], sound_1_1)
        else:
            character_died = True
            sound_1_1.stop()

        if next_level:
            next_level = play_lev2p1(viking_matrix[:][:], knight_matrix[:][:], gray_matrix[:][:], sound_1_1)
        else:
            character_died = True
            sound_1_1.stop()

        if next_level:
            sound_1_1.stop()
            ganhou = True

# end




"""
pinks are the collisions bars in the levels that stay
behind the background just acting for easier collision
mechanics.
"""