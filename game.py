#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math
import player
from gui import click_pointer

class Game(object):
    level = None
    click_pointer = None

    def __init__(self, level):
        self.screen = pygame.display.get_surface()
        self.player = player.Player()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.level = level
        self.player.position = level.initial_player_position
        self.player.facing = level.initial_player_facing
        self.click_pointer = click_pointer.ClickPointer()

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
        self.screen.blit(self.player.getTile(), self.player.position)

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.click_pointer.click(pygame.mouse.get_pos())

    def update(self, dt):
        self.player.is_walking = False

        if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
            self.player.facing = -1;
            self.player.is_walking = True

        if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
            self.player.facing = 1;
            self.player.is_walking = True

        if (self.player.is_walking):
            self.player.position = (self.player.position[0] + (self.player.speed * self.player.facing), self.player.position[1])

    def draw(self, dt):
        self.drawBackground()
        self.drawObjects(dt)
        self.drawPlayer(dt)
        self.drawForeground()
        self.click_pointer.draw(self.screen)
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
