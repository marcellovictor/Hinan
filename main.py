from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameimage import *

from levels.lev1p1 import *
from levels.lev1p2 import *

menu = Window(800, 600)
menu.set_title("Main Menu")

keyboard_menu = Keyboard()

"""
[j0: left][j1: right]
i = 0: just standing
i = 1: walking
"""
# Characters Matrix

mage_matrix = [[Sprite("images\\mage_left.png", 1), Sprite("images\\mage_right.png", 1)],
    [Sprite("images\\full_walk_mage_left.png", 6), Sprite("images\\full_walk_mage_right.png", 6)]]

gray_matrix = [[Sprite("images\\gray_left.png", 1), Sprite("images\\gray_right.png", 1)],
    [Sprite("images\\full_walk_gray_left.png", 9), Sprite("images\\full_walk_gray_right.png", 9)]]

next_level = False

while True:
    menu.update()
    menu.draw_text('Press "G" to start!', 100, 200, 42, (255, 255, 255))

    if keyboard_menu.key_pressed("G"):
        next_level = play_lev1p1(mage_matrix, gray_matrix)

        if next_level:
            play_lev1p2(mage_matrix, gray_matrix)



"""
pinks are the collisions bars in the levels that stay
behind the background just acting for easier collision
mechanics.
"""