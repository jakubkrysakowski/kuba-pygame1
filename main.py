#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pygame
import game
import menu
from levels import *
pygame.init()

CAPTION = "Kuba PyGame 1"
SCREEN_SIZE = (1024, 768)
FULLSCREEN = False

def getLevel(level_name):
    return globals()[level_name].Level(pygame)

if __name__ == "__main__":
    # todo: add level changing
    #level = level_test.Level(pygame)
    #level = level1.Level(pygame)

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption(CAPTION)
    pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN if FULLSCREEN else 0)

    while True:
        level_name = menu.Menu().run()
        level = getLevel(level_name)
        game.Game(level).run()

    pygame.quit()
