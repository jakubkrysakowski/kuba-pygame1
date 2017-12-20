#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class ClickPointer(object):
    target_position = None,
    click_time = None

    def click(self, position):
        print position
        self.target_position = position
        self.click_time = pygame.time.Clock()

    def draw(self):
        None
        # todo
