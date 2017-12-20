#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Level(object):
    NAME = 'House'
    FLOOR_Y = [
        344,
        466,
        588,
        744
    ]

    LIFT_X = 660
    LIFT_MARGIN = 12

    initial_player_position_x = 310
    initial_floor = 0
    initial_player_facing = 1

    background_color = None
    background_image = None
    foreground_image = None
    textures = {}
    tilemap = []

    TILESIZE=64
    MAPWIDTH=0
    MAPHEIGHT=0

    def __init__(self, pygame):
        self.background_image = pygame.image.load('./images/home_background.png')
        self.foreground_image = pygame.image.load('./images/home_foreground.png')

    def getFloorY(self, floor_index):
        return self.FLOOR_Y[floor_index]

    def getFloorIndex(self, y):
        key = 0
        for floor_y in self.FLOOR_Y:
            if y < floor_y:
                return key
            key = key + 1
        return 0
