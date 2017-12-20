#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Level(object):
    NAME = 'Test'

    initial_player_position = (92, 128)
    initial_player_facing = 1

    TILE_STONE = 0
    TILE_WOOD = 1

    background_color = (158, 180, 216)
    background_image = None
    foreground_image = None
    textures = {}

    tilemap = [
        [TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE],
        [TILE_STONE, None,       None,       None,       None,       None,       None,       TILE_STONE],
        [TILE_STONE, None,       TILE_WOOD,  None,       None,       None,       None,       TILE_STONE],
        [TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE, TILE_STONE]
    ]

    TILESIZE=64
    MAPWIDTH=8
    MAPHEIGHT=4

    def __init__(self, pygame):
        self.textures = {
            self.TILE_STONE: pygame.image.load('./images/tile_stone.png'),
            self.TILE_WOOD:  pygame.image.load('./images/tile_wood.png')
        }
