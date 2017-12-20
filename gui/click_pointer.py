#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import time

class ClickPointer(object):
    DISPLAY_DURATION = 2
    CIRCLE_RADIUS = 8
    position = None
    click_time = None

    def click(self, position):
        self.position = position
        self.click_time = time.time()

    def draw(self, screen):
        if self.position != None and time.time() - self.click_time < self.DISPLAY_DURATION:
            pygame.draw.circle(screen, (255, 0, 0), self.position, self.CIRCLE_RADIUS)
