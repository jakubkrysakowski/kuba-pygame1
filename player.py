#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math

class Player(object):
    HEIGHT = 64
    TILE_GROUP_IDLE_LEFT = 0
    TILE_GROUP_IDLE_RIGHT = 1
    TILE_GROUP_WALK_LEFT = 2
    TILE_GROUP_WALK_RIGHT = 3

    SEQUENCE_LENGTH_IDLE = 2
    SEQUENCE_LENGTH_WALK = 2

    TILES_CHANGE_SPEED = 0.005
    WALK_SPEED = 130

    TARGET_MARGIN = 4

    position_x = 0
    current_floor = 0
    facing = 1
    is_walking = False

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

    def goTo(self, click_pointer, dt):
        if click_pointer.position != None:
            if math.fabs(click_pointer.position[0] - self.position_x) > self.TARGET_MARGIN:
                self.goToX(click_pointer.position[0], dt)
            else:
                click_pointer.position = None
                self.is_walking = False

    def goToLift(self, lift_x, dt):
        self.goToX(lift_x, dt)

    def goToX(self, target_x, dt):
        self.facing = 1 if target_x > self.position_x else -1
        self.position_x = self.position_x + (self.facing * self.WALK_SPEED * dt)
        self.is_walking = True
