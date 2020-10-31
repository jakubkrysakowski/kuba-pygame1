#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pygame
import game
import menu
from levels import *
pygame.init()

window_caption = "Poznajmy PyGame"
max_display_height = int(pygame.display.Info().current_h * 0.9)
display_size = (1024, min(768, max_display_height))
fullscreen = False

def getLevel(level_name):
    return globals()[level_name].Level(pygame)

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption(window_caption)

    pygame.display.set_mode(display_size, pygame.FULLSCREEN if fullscreen else 0)

    while True:
        level_name = menu.Menu().run()
        level = getLevel(level_name)
        game.Game(level).run()

    pygame.quit()
