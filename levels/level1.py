#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Level1(object):
    NAME = 'House'

    initial_player_position = (310, 280)
    initial_player_facing = 1

    TILE_STONE = 0
    TILE_WOOD = 1

    background_image = None
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
        self.background_image = pygame.image.load('./images/home_background.png')

        self.textures = {
            self.TILE_STONE: pygame.image.load('./images/tile_stone.png'),
            self.TILE_WOOD:  pygame.image.load('./images/tile_wood.png')
        }
