#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import player
import math
from gui import click_pointer

class Game(object):
    level = None
    click_pointer = None
    guiFont = None
    currentRoomName = ''

    def __init__(self, level):
        self.screen = pygame.display.get_surface()
        self.player = player.Player()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.level = level
        self.player.position_x = level.initial_player_position_x
        self.player.current_floor = level.initial_floor
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

    def drawObjects(self, dt, time):
        for worldObject in self.level.getObjects(dt, time):
            image = pygame.transform.rotate(worldObject.image, worldObject.rotation)
            imageRectangle = image.get_rect()
            imageRectangle.center = worldObject.image.get_rect().center
            imageRectangle = imageRectangle.move(worldObject.x, worldObject.y)

            self.screen.blit(
                image,
                imageRectangle
            )

    def drawPlayer(self, dt):
        self.screen.blit(self.player.getTile(), (self.player.position_x, self.level.getFloorY(self.player.current_floor) - self.player.HEIGHT))

    def drawGui(self, dt):
        label = self.guiFont.render(self.currentRoomName, 1, (255,255,0))
        self.screen.blit(label, (30, self.screen.get_height() - 30))

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                self.done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                floorIndex = self.level.getFloorIndex(pygame.mouse.get_pos()[1])
                floorY = self.level.getFloorY(floorIndex)
                self.click_pointer.click(pygame.mouse.get_pos(), floorIndex, floorY)

    def update(self, dt):
        if self.click_pointer.position != None:
            if self.click_pointer.floor != self.player.current_floor:
                # player is on different floor - go to lift (hidden staircase)
                if math.fabs(self.level.LIFT_X - self.player.position_x) > self.level.LIFT_MARGIN:
                    # go to lift
                    self.player.goToLift(self.level.LIFT_X, dt)
                else:
                    # player is inside the lift, change floor
                    self.player.position_x = self.level.LIFT_X
                    self.player.current_floor = self.click_pointer.floor
            else:
                # player is on target floor - go to point
                self.player.goTo(self.click_pointer, dt)

            self.updateCurrentRoom()

    def updateCurrentRoom(self):
        self.currentRoomName = self.level.getRoomName(self.player.position_x, self.player.current_floor)

    def draw(self, dt):
        time = pygame.time.get_ticks()

        self.drawBackground()
        self.drawPlayer(dt)
        self.drawForeground()
        self.drawObjects(dt, time)
        self.drawGui(dt)
        self.click_pointer.draw(self.screen)
        pygame.display.flip()

    def main_loop(self):
        dt = 0
        while not self.done:
            self.eventLoop()
            self.update(dt)
            self.draw(dt)
            dt = self.clock.tick(self.fps) / 1000.0

    def init(self):
        self.guiFont = pygame.font.SysFont("monospace", 18)
        self.updateCurrentRoom()

    def run(self):
        self.init()
        self.main_loop()
