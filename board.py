import pygame
from constants import BLACK, RED, SQUARE_SIZE, ROWS, COLUMBS

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_remaining = 12
        self.white_remaining = 12
        self.red_kings = 0
        self.white_kings = 0

    def draw_squares(self, win):
        #win.fill(BLACK)

        for row in range(ROWS):
             # Draws chekcerboard pattern by stepping by 2 so that the cubes are spaced out
            for columb in range(row % 2, ROWS, 2):
                 # Draws a shape in window that is red and of dimension "SQUARE_SIZE"
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, columb * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))