#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math

class Game(object):
    level = None

    PLAYER_IDLE_LEFT = 0
    PLAYER_IDLE_RIGHT = 1
    PLAYER_WALK_LEFT = 2
    PLAYER_WALK_RIGHT = 3

    PLAYER_SEQUENCE_LENGTH_IDLE = 2
    PLAYER_SEQUENCE_LENGTH_WALK = 2

    PLAYER_TILES_CHANGE_SPEED = 0.005

    player_textures = {
        PLAYER_IDLE_LEFT: [
            pygame.image.load('./images/character/idleA1.png'),
            pygame.image.load('./images/character/idleA2.png')
        ],

        PLAYER_IDLE_RIGHT: [
            pygame.transform.flip(pygame.image.load('./images/character/idleA1.png'), True, False),
            pygame.transform.flip(pygame.image.load('./images/character/idleA2.png'), True, False)
        ],

        PLAYER_WALK_LEFT: [
            pygame.image.load('./images/character/walkA1.png'),
            pygame.image.load('./images/character/walkA2.png')
        ],

        PLAYER_WALK_RIGHT: [
            pygame.transform.flip(pygame.image.load('./images/character/walkA1.png'), True, False),
            pygame.transform.flip(pygame.image.load('./images/character/walkA2.png'), True, False)
        ]

    }

    # TODO: player class
    player_position = (0,0)
    player_facing = 1
    player_is_walking = False
    player_speed = 5

    def __init__(self, level):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.level = level
        self.player_position = level.initial_player_position
        self.player_facing = level.initial_player_facing

    def getPlayerTile(self, dt):
        # defaults
        sequence_frame = 0
        tile_group = tile_group = self.PLAYER_IDLE_RIGHT

        if self.player_is_walking:
            sequence_frame = int((math.floor(pygame.time.get_ticks() * self.PLAYER_TILES_CHANGE_SPEED) % self.PLAYER_SEQUENCE_LENGTH_WALK))
            if self.player_facing >= 0:
                tile_group = self.PLAYER_WALK_RIGHT
            else:
                tile_group = self.PLAYER_WALK_LEFT
        else: # Idle
            sequence_frame = int((math.floor(pygame.time.get_ticks() * self.PLAYER_TILES_CHANGE_SPEED) % self.PLAYER_SEQUENCE_LENGTH_IDLE))

            if self.player_facing >= 0:
                tile_group = self.PLAYER_IDLE_RIGHT
            else:
                tile_group = self.PLAYER_IDLE_LEFT

        return self.player_textures[tile_group][sequence_frame]

    def drawBackground(self):
        if self.level.background_color != None:
            self.screen.fill(self.level.background_color)

        if self.level.background_image != None:
            self.screen.blit(self.level.background_image, (0,0))

    def drawForeground(self):
        if self.level.foreground_image != None:
            self.screen.blit(self.level.foreground_image, (0,0))

    def drawObjects(self, dt):
        for row in range(self.level.MAPHEIGHT):
            for column in range(self.level.MAPWIDTH):
                textureIndex = self.level.tilemap[row][column]
                if textureIndex != None:
                    self.screen.blit(self.level.textures[textureIndex], (column * self.level.TILESIZE, row * self.level.TILESIZE))

    def drawPlayer(self, dt):
        self.screen.blit(self.getPlayerTile(dt), self.player_position)

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.done = True

    def update(self, dt):
        self.player_is_walking = False

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.player_facing = -1;
            self.player_is_walking = True

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.player_facing = 1;
            self.player_is_walking = True

        #if pygame.mouse.get_pressed()[0]:
        #    print(pygame.mouse.get_pos()) #debug

        if (self.player_is_walking):
            self.player_position = (self.player_position[0] + (self.player_speed * self.player_facing), self.player_position[1])

    def draw(self, dt):
        self.drawBackground()
        self.drawObjects(dt)
        self.drawPlayer(dt)
        self.drawForeground()
        pygame.display.flip()

    def main_loop(self):
        dt = 0
        while not self.done:
            self.eventLoop()
            self.update(dt)
            self.draw(dt)
            dt = self.clock.tick(self.fps) / 1000.0

    def run(self):
        self.main_loop()
