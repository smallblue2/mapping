#!/usr/bin/env python3

# Imports
import pygame as pg
import sys
from settings import *
from map import *

# Game object
class Game:
    # Game creator method initialises pygame and performs setup.
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

    # new_game method handles all processes to be performed when
    # a new_game is created
    def new_game(self):
        self.map = Map(self)

    # update method handles all continuous processes throughout
    # the game
    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.2f}')

    # draw method ensures all elements are continuously drawn
    # to the screen
    def draw(self):
        self.screen.fill('black')
        self.map.draw()

    # check_events method checks any input from user for use
    # in-game
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    # run method carries the main game loop and calls other
    # methods such as draw and check_events
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

# Run's the game if the script is being ran as main
if __name__ == "__main__":
    game = Game()  # creates an instance of game
    game.run()     # calls the game's loop
