#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from gui import menu_button

class Menu(object):
    done = False
    screen = None
    level = None
    buttons = []

    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.get_surface()

        screen_width = pygame.display.Info().current_w
        self.buttons = [
            #menu_button.MenuButton('Level Test', screen_width / 2, 70,  lambda: self.openLevel('level_test')),
            menu_button.MenuButton('Start',    screen_width / 2, 210, lambda: self.openLevel('level1')),
            menu_button.MenuButton('Exit',     screen_width / 2, 350, lambda: pygame.quit())
        ]

    def openLevel(self, level):
        self.done = True
        self.level = level

    def eventLoop(self):
        self.mouse_released = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    if button.checkMouseOver(pygame.mouse.get_pos()):
                        button.click_callback()

    def update(self):
        None

    def drawBackground(self):
        self.screen.fill((0,0,0))

    def drawButtons(self):
        i = 0
        for button in self.buttons:
            button.draw(self.screen, pygame.mouse.get_pos())

    def draw(self):
        self.drawBackground()
        self.drawButtons()
        pygame.display.flip()

    def clear(self):
        self.screen.fill((0,0,0))

    def main_loop(self):
        while not self.done:
            self.eventLoop()
            self.update()
            self.draw()

    def run(self):
        self.main_loop()
        self.clear()
        return self.level
