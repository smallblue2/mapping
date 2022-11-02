#!/usr/bin/env python3

# Author: Niall Ryan
# Map object for project, handles map generation through drawing values in matrix

# Imports
import pygame as pg
from settings import HEIGHT, WIDTH

# Using the underscore here instead of inputting false in array to get a better
# outlook of the map created.
_ = False
# Sample hard-coded map, eventually will be modular and swappable
mini_map= [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, 1, 1, 1, _, _, 1, 1, 1, 1, 1, _, _, 1, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1],
        [1, _, _, 1, 1, 1, _, _, 1, _, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, 1],
        [1, _, _, 1, _, _, _, _, 1, 1, 1, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, 1, _, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, 1, 1, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
        [1, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

# Map object to handle map generation
class Map:
    # Creator method handles setup and takes in game object as parameter.
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map # Take in hard-coded mini-map for now to visualise
        self.world_map = {} # World_map is a dictionary that stores tile position and value
        self.get_map() # called get_map method to manipulate our matrix as key-value pairs in world_map
        rows = len(self.mini_map)
        columns = len(self.mini_map[0])
        self.ver_split = HEIGHT/rows  # ver_split and hor_split are calculated to ensure drawn tiles
        self.hor_split = WIDTH/columns # always fit in screen.

    # get_map method manipulated given matrix as key-value pairs
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                self.world_map[(i, j)] = value

    # draw method uses list comprehension to iterate through
    # world-map dictionary key-value pairs, drawing them if
    # their value isn't false. Position and size of tiles
    # depends on screen size.
    def draw(self):
       [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * self.hor_split, pos[1] * self.ver_split, self.hor_split, self.ver_split), 2)
        for pos in self.world_map if self.world_map[pos]]
