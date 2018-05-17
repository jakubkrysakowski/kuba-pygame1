#!/usr/bin/env python
# -*- coding: utf-8 -*-

from roomData import roomData
from worldObject import worldObject

class Level(object):
    NAME = 'House'
    FLOOR_Y = [
        344,
        466,
        588,
        744
    ]

    ROOMS = [
        roomData(0, 240, 438, 'Office'),
        roomData(0, 455, 653, 'Playroom'),
        roomData(1, 240, 438, 'Bedroom'),
        roomData(1, 455, 653, 'Bathroom'),
        roomData(1, 679, 865, 'Laundry'),
        roomData(2, 240, 438, 'TV room'),
        roomData(2, 455, 653, 'Kitchen'),
        roomData(2, 679, 912, 'Garage'),
        roomData(3, 679, 912, 'Boiler room')
    ]

    LIFT_X = 660
    LIFT_MARGIN = 12

    initial_player_position_x = 310
    initial_floor = 0
    initial_player_facing = 1

    background_color = None
    background_image = None
    foreground_image = None
    fan_image = None

    def __init__(self, pygame):
        self.background_image = pygame.image.load('./images/levels/home/home_background.png')
        self.foreground_image = pygame.image.load('./images/levels/home/home_foreground.png')
        self.fan_image = pygame.image.load('./images/levels/home/fan.png')

    def getFloorY(self, floor_index):
        return self.FLOOR_Y[floor_index]

    def getFloorIndex(self, y):
        key = 0
        for floor_y in self.FLOOR_Y:
            if y < floor_y:
                return key
            key = key + 1
        return 0

    def getRoomName(self, x, floor):
        for roomData in self.ROOMS:
            if (roomData.floor == floor and x >= roomData.minX and x <= roomData.maxX):
                return roomData.name

        return ''

    def getObjects(self, dt, time):
        return [
            #worldObject(self.fan_image, 830, 140, time * 0.02) #TODO: uncoment and finish it
        ]
