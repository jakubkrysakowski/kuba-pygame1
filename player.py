#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math

class Player(object):
    TILE_GROUP_IDLE_LEFT = 0
    TILE_GROUP_IDLE_RIGHT = 1
    TILE_GROUP_WALK_LEFT = 2
    TILE_GROUP_WALK_RIGHT = 3

    SEQUENCE_LENGTH_IDLE = 2
    SEQUENCE_LENGTH_WALK = 2

    TILES_CHANGE_SPEED = 0.005

    position = (0,0)
    facing = 1
    is_walking = False
    speed = 10

    textures = {
        TILE_GROUP_IDLE_LEFT: [
            pygame.image.load('./images/character/idleA1.png'),
            pygame.image.load('./images/character/idleA2.png')
        ],

        TILE_GROUP_IDLE_RIGHT: [
            pygame.transform.flip(pygame.image.load('./images/character/idleA1.png'), True, False),
            pygame.transform.flip(pygame.image.load('./images/character/idleA2.png'), True, False)
        ],

        TILE_GROUP_WALK_LEFT: [
            pygame.image.load('./images/character/walkA1.png'),
            pygame.image.load('./images/character/walkA2.png')
        ],

        TILE_GROUP_WALK_RIGHT: [
            pygame.transform.flip(pygame.image.load('./images/character/walkA1.png'), True, False),
            pygame.transform.flip(pygame.image.load('./images/character/walkA2.png'), True, False)
        ]
    }

    def getTile(self):
        # defaults
        sequence_frame = 0
        tile_group = tile_group = self.TILE_GROUP_IDLE_RIGHT

        if self.is_walking:
            sequence_frame = int((math.floor(pygame.time.get_ticks() * self.TILES_CHANGE_SPEED) % self.SEQUENCE_LENGTH_WALK))
            if self.facing >= 0:
                tile_group = self.TILE_GROUP_WALK_RIGHT
            else:
                tile_group = self.TILE_GROUP_WALK_LEFT
        else: # Idle
            sequence_frame = int((math.floor(pygame.time.get_ticks() * self.TILES_CHANGE_SPEED) % self.SEQUENCE_LENGTH_IDLE))

            if self.facing >= 0:
                tile_group = self.TILE_GROUP_IDLE_RIGHT
            else:
                tile_group = self.TILE_GROUP_IDLE_LEFT

        return self.textures[tile_group][sequence_frame]
