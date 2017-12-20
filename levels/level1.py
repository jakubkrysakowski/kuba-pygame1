#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Level(object):
    NAME = 'House'

    initial_player_position = (310, 280)
    initial_player_facing = 1

    background_color = None
    background_image = None
    textures = {}
    tilemap = []

    TILESIZE=64
    MAPWIDTH=0
    MAPHEIGHT=0

    def __init__(self, pygame):
        self.background_image = pygame.image.load('./images/home_background.png')
